# Generated by Django 4.1.4 on 2023-01-31 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cam_main', '0004_custamer_prudect_rating_sociallink_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='prudect',
            name='price',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
