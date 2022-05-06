from django.db import models

# Create your models here.

class login_credentials(models.Model):
    user_name = models.CharField(max_length=20, unique=True)
    pass_word = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.id

    class Meta:
        ordering = ['pk']
