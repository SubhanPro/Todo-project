from django.db import models
from django.contrib.auth.models import User

class ToDoModel(models.Model):
    name = models.CharField(max_length = 156, help_text = "Please, enter film name")
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    user = models.ForeignKey(User, related_name = "todo", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Todo"
    
    def __str__(self):
        return self.name