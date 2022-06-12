# Generated by Django 4.0.5 on 2022-06-12 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('job_posting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_posting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_application', to='job_posting.jobposting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_applications', to='user.user')),
            ],
        ),
    ]
