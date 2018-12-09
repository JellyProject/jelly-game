# Generated by Django 2.1.2 on 2018-12-09 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='a', max_length=20)),
                ('current_index_pile', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HydrocarbonSupplyPile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_amount', models.FloatField(default=0)),
                ('multiplier', models.IntegerField(default=0)),
                ('index', models.IntegerField(editable=False, unique=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hydrocarbon_piles', to='game.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technologies', models.IntegerField(default=0)),
                ('builded', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='game.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('um', models.IntegerField(default=0)),
                ('hydrocarbons', models.IntegerField(default=1)),
                ('food', models.IntegerField(default=0)),
                ('electricity', models.IntegerField(default=0)),
                ('pollution', models.IntegerField(default=1)),
                ('waste', models.IntegerField(default=0)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('um', models.IntegerField(default=10)),
                ('hydrocarbons', models.IntegerField(default=0)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Player')),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('economical', models.IntegerField(default=50)),
                ('social', models.IntegerField(default=50)),
                ('environmental', models.IntegerField(default=100)),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='game.Player')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='MiguelDePatatas', max_length=30)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='game.User'),
        ),
    ]
