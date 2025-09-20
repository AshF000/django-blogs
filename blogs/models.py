from django.db import models


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        max_title_length = 10
        truncated_title = self.title if len(self.title) <= max_title_length else self.title[:max_title_length] + "..."
        return f"{self.name} : {truncated_title}"
