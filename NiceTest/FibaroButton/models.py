from django.db import models

# Create your models here.
class Buttonlog(models.Model) :
    button = models.CharField(max_length=200,null=True)
    value = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)