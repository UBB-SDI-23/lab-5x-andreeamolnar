# Generated by Django 4.2 on 2023-04-15 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_book_authors_alter_bookwithauthors_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AlterField(
            model_name='bookwithauthors',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='api.book'),
        ),
    ]
