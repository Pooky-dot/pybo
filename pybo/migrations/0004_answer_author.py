# Generated by Django 4.0.3 on 2024-10-25 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybo', '0003_question_author_alter_answer_content_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
