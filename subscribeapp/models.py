from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import UniqueConstraint

from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        # unique_together = ('user', 'project')
        constraints = [models.UniqueConstraint(fields=['user', 'project'], name='user_project_constraint')]
