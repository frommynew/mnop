# Generated by Django 2.1 on 2018-08-12 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("templates", "0001_initial"),
        ("lists", "0001_initial"),
        ("campaigns", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="email",
            name="template",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="emails",
                to="templates.EmailTemplate",
                verbose_name="email template",
            ),
        ),
        migrations.AddField(
            model_name="campaign",
            name="mailing_list",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="campaigns",
                to="lists.MailingList",
                verbose_name="mailing list",
            ),
        ),
    ]