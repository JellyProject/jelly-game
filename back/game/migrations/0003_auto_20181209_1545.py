# Generated by Django 2.1.2 on 2018-12-09 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20181209_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BuildingPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(unique=True)),
                ('unlockable', models.BooleanField(default=False)),
                ('unlocked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='game.Game')),
            ],
        ),
        migrations.CreateModel(
            name='TechnologyGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technologies', to='game.Game')),
            ],
        ),
        migrations.CreateModel(
            name='TechnologyPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(unique=True)),
                ('unlockable', models.BooleanField(default=False)),
                ('unlocked', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='builded',
        ),
        migrations.RemoveField(
            model_name='player',
            name='technologies',
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('buildinggame_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='game.BuildingGame')),
            ],
            bases=('game.buildinggame',),
        ),
        migrations.AddField(
            model_name='technologyplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technologies', to='game.Player'),
        ),
        migrations.AddField(
            model_name='buildingplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='game.Player'),
        ),
        migrations.AddField(
            model_name='buildinggame',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buildings', to='game.Game'),
        ),
    ]
