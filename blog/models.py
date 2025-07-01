from django.db import models

class Post(models.Model):
    STATUS_CHOICES = (
        (0, "Rascunho"),
        (1, "Publicado")
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
