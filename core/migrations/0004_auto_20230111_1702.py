# Generated by Django 3.2.16 on 2023-01-11 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20230111_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_patient',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_physician',
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('Email', models.EmailField(default='none@email.com', max_length=254)),
                ('Stomach_ach', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Diarrheal', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Injuries', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Head_ache', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('Cough', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
