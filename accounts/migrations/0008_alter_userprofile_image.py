# Generated by Django 5.0.6 on 2024-08-20 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='media/images/go9xwcxemxj7sajmn1zf', null=True, upload_to='images/'),
        ),
    ]
