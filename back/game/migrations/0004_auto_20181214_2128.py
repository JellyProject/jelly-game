# Generated by Django 2.0 on 2018-12-14 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20181213_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='description',
            field=models.TextField(default='A rather plain building.'),
        ),
        migrations.AddField(
            model_name='building',
            name='electricity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='food',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='hydrocarbons',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='money',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='name',
            field=models.CharField(default='Building', max_length=40, unique=True),
        ),
        migrations.AddField(
            model_name='building',
            name='pollution',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='building',
            name='technology',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.Technology'),
        ),
        migrations.AddField(
            model_name='building',
            name='version',
            field=models.CharField(default='jelly', max_length=20),
        ),
        migrations.AddField(
            model_name='building',
            name='waste',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(default='Today will be a sunny day.'),
        ),
        migrations.AddField(
            model_name='event',
            name='name',
            field=models.CharField(default='Ragnarok', max_length=40, unique=True),
        ),
        migrations.AddField(
            model_name='event',
            name='version',
            field=models.CharField(default='jelly', max_length=20),
        ),
    ]
