from django.db import models
from django.utils import timezone


JOB_NATURE_CHOICES = (
        ('Full Time', 'Full-Time'),
        ('Part Time', 'Part-Time'),
        ('Remote', 'Remote'),
        ('Freelance', 'Freelance'),
    )


SERVICE_CHOICES = (
        ('Design & Creative', 'Design & Creative'),
        ('Design & Development', 'Design & Development'),
        ('Sales & Marketing', 'Sales & Marketing'),
        ('Mobile Application', 'Mobile Application'),
        ('Construction', 'Construction'),
        ('Information Technology', 'Information Technology'),
        ('Real Estate', 'Real Estate'),
        ('Content Writer', 'Content Writer'),
    )

# Create your models here.
class Jobs(models.Model):
    title = models.CharField(max_length=255)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    company = models.ForeignKey('Company', related_name='jobs_company', on_delete=models.CASCADE)
    hours = models.IntegerField()
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=50)
    job_description = models.TextField(max_length=2500)
    required_skills = models.TextField(max_length=2500)
    education = models.TextField(max_length=2500)
    experience = models.IntegerField()
    create_date = models.DateTimeField(default=timezone.now)
    application_date = models.DateField()
    number_of_vacancies = models.PositiveIntegerField()
    job_nature = models.CharField(choices=JOB_NATURE_CHOICES, max_length=50)


    def __str__(self):
        return self.title
    

class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    website = models.URLField(max_length=200)
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=2500)

    def __str__(self):
        return self.name