# Generated by Django 4.1.7 on 2023-03-12 13:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pel', '0002_alter_encode_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encode',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]