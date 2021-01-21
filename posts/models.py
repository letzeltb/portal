from django.db import models
from datetime import datetime

class Posts(models.Model):
    Player_Name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.Player_Name
    class Meta:
        verbose_name_plural = "Posts"
