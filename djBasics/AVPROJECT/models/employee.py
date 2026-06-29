from django.db import models
from typing import Dict, Any, Optional,List
from avapp.models.branch import branch

class employee(models.Model):
    empname = models.TextField()
    empaddr = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    worksat = models.ForeignKey(branch,on_delete=models.CASCADE,null=True)