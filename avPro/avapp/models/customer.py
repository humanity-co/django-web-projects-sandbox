from django.db import models
from ninja import Schema
from typing import Dict, Any, Optional,List
from avapp.models.branch import branch


class customer(models.Model):
    custname = models.TextField()
    custaddr = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    worksat = models.ForeignKey(branch,on_delete=models.CASCADE,null=True)

    def str(self):
        return self.custname
    
class customerinSchema(Schema):
    custname: str
    custaddr: str
    email: str
    password: str
    worksat: Optional[int] = None

class customeroutSchema(Schema):
    id: int
    custname: str
    custaddr: str
    email: str
    worksat: str