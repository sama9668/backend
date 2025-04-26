from django.db import models

# Create your models here.
class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} from {self.institution}"
    
class Work(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company}"
    
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/')
    url = models.URLField()
    def __str__(self):
        return self.title