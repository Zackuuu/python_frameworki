# Generated by Django 4.2.6 on 2023-10-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_blog_web', '0002_article_content_article_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='imgThumb',
            field=models.ImageField(blank=True, null=True, upload_to='media_img'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
