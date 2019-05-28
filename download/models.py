from django.db import models


class Download(models.Model):
    upload = models.URLField()
    download_date = models.DateTimeField(auto_now_add=True)


