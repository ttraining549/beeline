# Generated by Django 5.0.6 on 2024-05-31 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vacancy", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="vacancy",
            options={"ordering": ("-pk",), "verbose_name_plural": "vacancies"},
        ),
    ]
