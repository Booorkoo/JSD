from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

	initial = True

	dependencies = [
	]

	operations = [
		migrations.CreateModel(
			name='test',
			fields=[
				('id',models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('el1',models.CharField(max_length=5, null=True, default=1)),
				('el2',models.TextField(max_length=6, null=True)),
				('el3',models.TextField(default=1, max_length=6)),
				('el4',models.TextField(max_length=6)),
				('el4',models.CharField(default=0)),
				('el5',models.CharField()),
			],
		),
		migrations.CreateModel(
			name='novi_test',
			fields=[
				('id',models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('el11',models.TextField(max_length=5, null=True)),
				('el12',models.TextField(max_length=5)),
				('el13',models.CharField(max_length=5, null=True, default=1)),
				('el14',models.CharField()),
			],
		),
	]