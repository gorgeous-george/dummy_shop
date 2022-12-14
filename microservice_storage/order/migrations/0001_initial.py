# Generated by Django 4.1.1 on 2022-09-18 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_email', models.EmailField(max_length=255)),
                ('status', models.CharField(choices=[('IN_WORK', 'In work'), ('SUCCESS', 'Success'), ('FAIL', 'Fail')], default='IN_WORK', max_length=7)),
                ('delivery_address', models.CharField(max_length=255)),
                ('shop_order_id', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['client_email', 'id', 'status'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('book_item', models.ManyToManyField(related_name='order_items', related_query_name='order_item', to='book.bookitem')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
            options={
                'ordering': ['order_id', 'book_id', 'quantity'],
            },
        ),
    ]
