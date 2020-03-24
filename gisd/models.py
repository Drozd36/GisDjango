from django.contrib.auth.models import User
from django.db import models

TEXT_LEN = 600

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.title
    def short_text(self):
        if len(self.text) > TEXT_LEN:
            return self.text[:TEXT_LEN]
        return self.text