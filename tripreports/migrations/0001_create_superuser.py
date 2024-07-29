# Generated by Django 5.0.7 on 2024-07-29 19:28

import os

from django.contrib.auth.models import User
from django.db import migrations
from django.db.backends.postgresql.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps

import google.auth
from google.cloud import secretmanager


def createsuperuser(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    client = secretmanager.SecretManagerServiceClient()

    _, project = google.auth.default()

    PASSWORD_NAME = os.environ.get("PASSWORD_NAME", "superuser_password")
    name = f"projects/{project}/secrets/{PASSWORD_NAME}/versions/latest"
    admin_password = client.access_secret_version(name=name).payload.data.decode("UTF-8")

    User.objects.create_superuser("admin", password=admin_password.strip())


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.RunPython(createsuperuser)]