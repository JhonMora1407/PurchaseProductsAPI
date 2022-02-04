import csv

from .models import Client
from .serializers import ClientSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.http import HttpResponse, Http404
from django.db import connection
from django.contrib.auth.hashers import make_password


class LoginClientView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        client = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=client)
        return Response({
            'token': token.key,
            'client_id': client.pk,
            'email': client.email
        })


class RetrieveClientView(APIView):

    def get(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404
        serializer = ClientSerializer(client)

        return Response(serializer.data)


class ListClientView(APIView):

    def get(self, request):
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)

        return Response(serializer.data)


class CreateClientView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        client = request.data
        serializer = ClientSerializer(data=client)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class UpdateClientView(APIView):

    def patch(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

        serializer = ClientSerializer(client, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DestroyClientView(APIView):

    def delete(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404

        client.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ImportClientView(APIView):

    def post(self, request):
    
        file = request.FILES['file']    
        clients = []

        decoded_file = file.read().decode('utf-8').splitlines()
        data = list(csv.reader(decoded_file, delimiter=","))

        for row in data[1:]:
            clients.append(
                Client(
                    first_name=row[0],
                    last_name=row[1],
                    document=row[2],
                    email=row[3],
                    password=make_password(row[4])
                )
            )
            
        if len(clients) > 0:
            Client.objects.bulk_create(clients)
    
        return Response('Successfully Import')


class ExportClientView(APIView):

    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=clients.csv'

        writer = csv.writer(response)
        fields_names, rows = self.get_queryset()
        writer.writerow(fields_names)

        for row in rows:
            writer.writerow(row)

        return response

    def get_queryset(self):

        with connection.cursor() as cursor:
            cursor.execute('''SELECT clients.document, (clients.first_name || ' ' || clients.last_name) as full_name, 
                               COUNT(bills.client_id_id) as number_of_bills 
                               FROM clients_client as clients LEFT JOIN bills_bill as bills 
                               ON clients.id=bills.client_id_id GROUP BY clients.email''')

            rows = cursor.fetchall()
            fields_names = [col[0] for col in cursor.description]

        return fields_names, rows
