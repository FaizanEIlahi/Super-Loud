# Generated by Django 3.2 on 2023-02-07 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_auto_20220325_0351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription_details',
            name='stripeCustomerId',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subscription_details',
            name='stripeSubscriptionId',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
