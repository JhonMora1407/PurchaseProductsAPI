import datetime

import pytz
from django.conf import settings
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from rest_framework.authtoken.models import Token


class ExpiringTokenAuthentication(TokenAuthentication):
    
    def authenticate_credentials(self, key, request=None):

        try:
            token = Token.objects.select_related("user").get(key=key)
        except Token.DoesNotExist:
            raise AuthenticationFailed(
                {"error": "Invalid or Inactive Token", "is_authenticated": False}
            )

        if not token.user.is_active:
            raise AuthenticationFailed(
                {"error": "Invalid user", "is_authenticated": False}
            )

        utc_now = timezone.now().replace(tzinfo=pytz.utc)

        if token.created < utc_now - settings.TOKEN_TTL:
            token.delete()
            raise AuthenticationFailed(
                {"error": "Token has expired", "is_authenticated": False}
            )
        return token.user, token