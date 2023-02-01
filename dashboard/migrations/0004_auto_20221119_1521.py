# Generated by Django 2.2.12 on 2022-11-19 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_transaksi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sosmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_depan', models.CharField(max_length=100)),
                ('nama_belakang', models.CharField(max_length=100)),
                ('usernamae', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaksi',
            name='uaraian',
        ),
        migrations.AddField(
            model_name='transaksi',
            name='phone',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='tanggal',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]