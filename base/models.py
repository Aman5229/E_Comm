from django.db import models

class BaseModel(models.Model):

  uid = models.UUIDField(primary_key=True, editable=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_add=True)
   
  class Meta:
    abstract = True