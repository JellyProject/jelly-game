# Generated by Django 2.0 on 2019-01-18 20:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('economic', models.IntegerField(default=50)),
                ('social', models.IntegerField(default=50)),
                ('environmental', models.IntegerField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(editable=False)),
                ('unlocked', models.BooleanField(default=False)),
                ('copies', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='A random game', editable=False, max_length=20, unique=True)),
                ('version', models.CharField(default='jelly', editable=False, max_length=20)),
                ('era', models.IntegerField(default=1)),
                ('current_index_pile', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HydrocarbonSupplyPile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_amount', models.FloatField(default=0)),
                ('multiplier', models.IntegerField(default=0)),
                ('index', models.IntegerField(editable=False)),
                ('game', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='hydrocarbon_piles', to='game.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='game.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=0)),
                ('hydrocarbon', models.IntegerField(default=1)),
                ('food', models.IntegerField(default=0)),
                ('electricity', models.IntegerField(default=0)),
                ('pollution', models.IntegerField(default=1)),
                ('waste', models.IntegerField(default=0)),
                ('player', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='game.Player')),
            ],
            options={
                'verbose_name': 'Production',
                'verbose_name_plural': 'Production',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(default=10)),
                ('hydrocarbon', models.IntegerField(default=0)),
                ('player', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='game.Player')),
            ],
            options={
                'verbose_name': 'Resources',
                'verbose_name_plural': 'Resources',
            },
        ),
        migrations.CreateModel(
            name='SourceBuilding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Old mansion', editable=False, max_length=40, unique=True)),
                ('slug', models.CharField(default='old-mansion', editable=False, max_length=40, unique=True)),
                ('version', models.CharField(default='jelly', editable=False, max_length=20)),
                ('era', models.IntegerField(default=1, editable=False)),
                ('description', models.TextField(default='A rather plain building.', editable=False)),
                ('cost', models.IntegerField(default=1, editable=False)),
                ('money_modifier', models.IntegerField(default=0, editable=False)),
                ('hydrocarbon_modifier', models.IntegerField(default=0, editable=False)),
                ('food_modifier', models.IntegerField(default=0, editable=False)),
                ('electricity_modifier', models.IntegerField(default=0, editable=False)),
                ('pollution_modifier', models.IntegerField(default=0, editable=False)),
                ('waste_modifier', models.IntegerField(default=0, editable=False)),
                ('economic_modifier', models.IntegerField(default=0, editable=False)),
                ('social_modifier', models.IntegerField(default=0, editable=False)),
                ('environmental_modifier', models.IntegerField(default=0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='SourceEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Sunny day', editable=False, max_length=40, unique=True)),
                ('slug', models.CharField(default='sunny-day', editable=False, max_length=40, unique=True)),
                ('version', models.CharField(default='jelly', editable=False, max_length=20)),
                ('era', models.IntegerField(default=1, editable=False)),
                ('description', models.TextField(default='There is nothing to report.', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='SourceTechnology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Fire discovery', editable=False, max_length=40, unique=True)),
                ('slug', models.CharField(default='fire-discovery', editable=False, max_length=40, unique=True)),
                ('version', models.CharField(default='jelly', editable=False, max_length=20)),
                ('era', models.IntegerField(default=1, editable=False)),
                ('description', models.TextField(default='Food may now be cooked.', editable=False)),
                ('cost', models.IntegerField(default=1, editable=False)),
                ('money_modifier', models.IntegerField(default=0, editable=False)),
                ('hydrocarbon_modifier', models.IntegerField(default=0, editable=False)),
                ('food_modifier', models.IntegerField(default=0, editable=False)),
                ('electricity_modifier', models.IntegerField(default=0, editable=False)),
                ('pollution_modifier', models.IntegerField(default=0, editable=False)),
                ('waste_modifier', models.IntegerField(default=0, editable=False)),
                ('economic_modifier', models.IntegerField(default=0, editable=False)),
                ('social_modifier', models.IntegerField(default=0, editable=False)),
                ('environmental_modifier', models.IntegerField(default=0, editable=False)),
                ('parent_technology', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_technology', to='game.SourceTechnology')),
            ],
            options={
                'verbose_name': 'Source technology',
                'verbose_name_plural': 'Source technologies',
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(editable=False, unique=True)),
                ('unlocked', models.BooleanField(default=False)),
                ('purchased', models.BooleanField(default=False)),
                ('player', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='technologies', to='game.Player')),
            ],
            options={
                'verbose_name': 'Technology',
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.AddField(
            model_name='sourcebuilding',
            name='parent_technology',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_building', to='game.SourceTechnology'),
        ),
        migrations.AddField(
            model_name='player',
            name='profile',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='game.Profile'),
        ),
        migrations.AddField(
            model_name='game',
            name='source_buildings',
            field=models.ManyToManyField(to='game.SourceBuilding'),
        ),
        migrations.AddField(
            model_name='game',
            name='source_technologies',
            field=models.ManyToManyField(to='game.SourceTechnology'),
        ),
        migrations.AddField(
            model_name='event',
            name='game',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='events', to='game.Game'),
        ),
        migrations.AddField(
            model_name='building',
            name='player',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='game.Player'),
        ),
        migrations.AddField(
            model_name='balance',
            name='player',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='game.Player'),
        ),
    ]
