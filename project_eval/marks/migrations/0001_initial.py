# Generated by Django 3.0.3 on 2020-02-28 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.PositiveIntegerField()),
                ('max_marks', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Rubrics',
            },
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField()),
                ('date_entered', models.DateTimeField(auto_now_add=True, null=True)),
                ('panel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Panel')),
                ('rubric_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marks.Rubrics')),
                ('usn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='accounts.Student')),
            ],
            options={
                'verbose_name_plural': 'Marks',
            },
        ),
    ]
