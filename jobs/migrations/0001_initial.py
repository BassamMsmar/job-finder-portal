# Generated by Django 4.2.2 on 2023-10-14 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company_logos/')),
                ('website', models.URLField()),
                ('email', models.EmailField(max_length=100)),
                ('description', models.TextField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('service', models.CharField(choices=[('Design & Creative', 'Design & Creative'), ('Design & Development', 'Design & Development'), ('Sales & Marketing', 'Sales & Marketing'), ('Mobile Application', 'Mobile Application'), ('Construction', 'Construction'), ('Information Technology', 'Information Technology'), ('Real Estate', 'Real Estate'), ('Content Writer', 'Content Writer')], max_length=50)),
                ('hours', models.IntegerField()),
                ('location', models.CharField(max_length=255)),
                ('salary_range', models.CharField(max_length=50)),
                ('job_description', models.TextField(max_length=2500)),
                ('required_skills', models.TextField(max_length=2500)),
                ('education', models.TextField(max_length=2500)),
                ('experience', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('application_date', models.DateField()),
                ('number_of_vacancies', models.PositiveIntegerField()),
                ('job_nature', models.CharField(choices=[('Full Time', 'Full-Time'), ('Part Time', 'Part-Time'), ('Remote', 'Remote'), ('Freelance', 'Freelance')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs_company', to='jobs.company')),
            ],
        ),
    ]
