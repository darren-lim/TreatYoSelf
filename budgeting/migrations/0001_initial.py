# Generated by Django 2.2.12 on 2020-08-06 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_type', models.CharField(max_length=15, null=True, verbose_name='Income/Expense')),
                ('category', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=30, verbose_name='Title')),
                ('amount', models.CharField(default='0', max_length=100)),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Additional Information')),
                ('date_posted', models.DateField(null=True, verbose_name='Transaction Date (mm/dd/yyyy)')),
                ('year', models.IntegerField(null=True)),
                ('month', models.IntegerField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_categories', jsonfield.fields.JSONField()),
                ('expense_categories_budget', jsonfield.fields.JSONField()),
                ('expense_categories_monthly', jsonfield.fields.JSONField()),
                ('income_categories', jsonfield.fields.JSONField()),
                ('income_categories_monthly', jsonfield.fields.JSONField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
