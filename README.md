# PurchaseProductsAPI

> ### Django rest Framework

# Getting started

## Installation

Please check the official Django installation guide for server requirements before you start. [Official Documentation](https://docs.djangoproject.com/en/4.0/intro/install/)

> Please Refer to [Github and ssh keys help page](https://docs.github.com/es/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) before start.

Clone the repository with SSH

    git@github.com:JhonMora1407/PurchaseProductsAPI.git

Or clone the repository with HTTPS

    https://github.com/JhonMora1407/PurchaseProductsAPI.git

Switch to the repo folder

    cd PurchaseProductsAPI

Install all the dependencies using pip

    pip install -r requirements.txt

Install all the dependencies using pip

    pip install -r requirements.txt

Create the migrations based on the models

    python3 manage.py makemigrations

Run the database migrations (sqlite3 by default)

    python3 manage.py migrate

Start the local development server

    python3 manage.py runserver

You can now access the server at http://localhost:8000

## API Documentation

This is the documentation for consumption via Rest API.

> [Full API Spec](http://localhost:8000/swagger)

---

# Testing API

The api can now be accessed at

    http://localhost:8000/

Request headers

| **Required** | **Key**      | **Value**        |
| ------------ | ------------ | ---------------- |
| Optional     | Content-Type | application/json |
| Yes          | Auth-Token   | `token`          |

Refer the [api specification](#api-specification) for more info.

---
