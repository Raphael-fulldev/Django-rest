# Generated by Django 3.1.1 on 2021-04-10 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0002_auto_20210410_0104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org_Account',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('account_name', models.CharField(max_length=32)),
                ('number_of_users', models.IntegerField()),
                ('org_entity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.org_entity')),
            ],
            options={
                'verbose_name_plural': 'Org_Account',
            },
        ),
        migrations.CreateModel(
            name='Plan_Info',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('plan_type', models.CharField(max_length=32)),
                ('plan_cost', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Plan_Info',
            },
        ),
        migrations.CreateModel(
            name='User_Permission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('create_super_user', models.BooleanField()),
                ('change_plan', models.BooleanField()),
                ('create_account_admin', models.BooleanField()),
                ('create_account', models.BooleanField()),
                ('manage_user', models.BooleanField()),
                ('manage_project', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'User_Permission',
            },
        ),
        migrations.CreateModel(
            name='User_Personal_Info',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=32)),
                ('middle_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('suffix', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=32)),
                ('street', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=32)),
                ('zipcode', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32)),
                ('company_name', models.CharField(max_length=32)),
                ('department', models.CharField(max_length=32)),
                ('division', models.CharField(max_length=32)),
                ('employee_number', models.CharField(max_length=32)),
                ('user_entity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.user_entity')),
            ],
            options={
                'verbose_name_plural': 'User_Personal_Info',
            },
        ),
        migrations.CreateModel(
            name='User_Language_Timezone',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('time_zone', models.CharField(default='UTC', max_length=32)),
                ('locale', models.CharField(max_length=32)),
                ('language', models.CharField(max_length=32)),
                ('user_entity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.user_entity')),
            ],
            options={
                'verbose_name_plural': 'User_Language_Timezone',
            },
        ),
        migrations.CreateModel(
            name='User_Account',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('org_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_setting.org_account')),
            ],
            options={
                'verbose_name_plural': 'User_Account',
            },
        ),
        migrations.CreateModel(
            name='Org_Plan_Entity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('org_entity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.org_entity')),
                ('plan_info_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_setting.plan_info')),
            ],
            options={
                'verbose_name_plural': 'Org_Plan_Entity',
            },
        ),
        migrations.CreateModel(
            name='Org_Info',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('org_name', models.CharField(max_length=32)),
                ('contact_number', models.CharField(max_length=32)),
                ('street', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=32)),
                ('zipcode', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32)),
                ('org_entity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.org_entity')),
            ],
            options={
                'verbose_name_plural': 'Org_Info',
            },
        ),
        migrations.CreateModel(
            name='Billing_Info',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=32)),
                ('state', models.CharField(max_length=32)),
                ('zipcode', models.CharField(max_length=32)),
                ('country', models.CharField(max_length=32)),
                ('org_entity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.org_entity')),
            ],
            options={
                'verbose_name_plural': 'Billing_Info',
            },
        ),
    ]