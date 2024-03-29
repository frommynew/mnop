# Generated by Django 2.1 on 2018-08-12 20:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("campaigns", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailTemplate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="name")),
                ("content", models.TextField(blank=True)),
                (
                    "create_date",
                    models.DateTimeField(auto_now_add=True, verbose_name="create date"),
                ),
                (
                    "update_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="update date"
                    ),
                ),
                (
                    "last_used_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last used"
                    ),
                ),
                (
                    "last_used_campaign",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="campaigns.Campaign",
                        verbose_name="last used campaign",
                    ),
                ),
            ],
            options={
                "verbose_name": "email template",
                "verbose_name_plural": "email templates",
                "db_table": "colossus_email_templates",
            },
        ),
    ]
