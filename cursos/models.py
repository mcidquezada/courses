from django.db import models


class LeManager(models.Manager):
    def validator(self, data):
        errors = {}
        if len(data['name']) < 5:
            errors['name'] = 'Course name must be at least 5 characters'
        if len(data['desc']) < 15:
            errors['desc'] = 'Description must be at least 15 characters'
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LeManager()