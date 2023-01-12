from django.db import models

class JobPortal(models.Model):
    job = models.charField(max_length=100, null=False,  blank=False)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    job_type = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    salary_range = models.IntegerField(max_digits=20, decimal_places=2, default=99.99)
    slug = models.SlugField(unique=True,  blank=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="date created")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="date updated")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)