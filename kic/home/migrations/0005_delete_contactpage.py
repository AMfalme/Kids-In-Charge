# Generated by Django 3.0.9 on 2020-08-20 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('home', '0004_contactpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactPage',
        ),
    ]