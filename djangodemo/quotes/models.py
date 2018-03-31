from django.db import models


class Quote(models.Model):
    text = models.TextField(max_length=1024, blank=False, null=False)