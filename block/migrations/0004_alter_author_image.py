# Generated by Django 4.2.4 on 2023-09-08 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0003_author_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Author/'),
        ),
    ]
