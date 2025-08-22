from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    active_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']  # Order by id in descending order
    def __str__(self):
        # Return the string representation of the Task instance.
        return self.title + " - Completed" if self.completed else self.title + " - Incomplete"
