from django.db import models
from ninja import Schema
from typing import Dict, Any, Optional,List
from avapp.models.branch import branch

class customer(models.Model):
    cstname = models.TextField()
    custaddress = models.TextField()
    clientof = models.ForeignKey(branch,on_delete=models.CASCADE,null=True)
    firsttime = models.BooleanField(default=True)