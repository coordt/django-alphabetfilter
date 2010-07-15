from django.db import models

# Create your models here.

class TestName(models.Model):
    """A testing module"""
    name = models.CharField(max_length=255)
    sorted_name = models.CharField(max_length=255)

    class Meta:
        pass

    def __unicode__(self):
        return self.name
