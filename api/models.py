from django.db import models

from accounts.models import CustomUser
# Create your models here.


class Task(models.Model):
    STATUS_CHOICES = [
        ('D', 'Done'),
        ('P', 'In progress'),
        ('TBD', 'Not done'),
    ]

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=500, blank=True)
    status = models.CharField(
        max_length=3,
        choices=STATUS_CHOICES,
        default='TBD'
    )
    created_at = models.DateTimeField(auto_now_add=...)
    due_date = models.DateTimeField()
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return "<Task: %s>" % self.name[:20]+'...' if len(self.name) > 21 else self.name

