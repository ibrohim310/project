from django.db import models

class Courses(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()


class Speciality(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    icon = models.ImageField()


class Blog(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"murojat {self.first_name}dan"
    
    class Meta:
        verbose_name = "Murojatlar royhati"
        verbose_name_plural = "Murojatlar"
        ordering = ("is_active",)