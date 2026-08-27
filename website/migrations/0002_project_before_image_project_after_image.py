from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='before_image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/before/'),
        ),
        migrations.AddField(
            model_name='project',
            name='after_image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/after/'),
        ),
    ]