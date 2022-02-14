# Generated by Django 4.0.2 on 2022-02-14 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CircleShape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Cube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RectangleShape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField()),
                ('b', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Square',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rhombus',
            fields=[
                ('rectangleshape_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cal_app.rectangleshape')),
            ],
            options={
                'abstract': False,
            },
            bases=('cal_app.rectangleshape',),
        ),
        migrations.CreateModel(
            name='Sphere',
            fields=[
                ('circleshape_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cal_app.circleshape')),
            ],
            options={
                'abstract': False,
            },
            bases=('cal_app.circleshape',),
        ),
        migrations.CreateModel(
            name='Triangle',
            fields=[
                ('rectangleshape_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cal_app.rectangleshape')),
                ('c', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cal_app.rectangleshape',),
        ),
        migrations.CreateModel(
            name='Cylinder',
            fields=[
                ('sphere_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cal_app.sphere')),
                ('b', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cal_app.sphere',),
        ),
        migrations.CreateModel(
            name='Trapezoid',
            fields=[
                ('triangle_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cal_app.triangle')),
                ('d', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cal_app.triangle',),
        ),
        migrations.CreateModel(
            name='Cone',
            fields=[
                ('cylinder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cal_app.cylinder')),
            ],
            options={
                'abstract': False,
            },
            bases=('cal_app.cylinder',),
        ),
        migrations.CreateModel(
            name='Parallelepiped',
            fields=[
                ('cylinder_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cal_app.cylinder')),
                ('c', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
            bases=('cal_app.cylinder',),
        ),
        migrations.CreateModel(
            name='Pyramid',
            fields=[
                ('parallelepiped_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cal_app.parallelepiped')),
            ],
            options={
                'abstract': False,
            },
            bases=('cal_app.parallelepiped',),
        ),
    ]