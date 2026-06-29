from django.db import models
from ninja import Schema
from typing import Dict, Any, Optional,List

class branch (models.Model):
    branchname  = models.TextField()
    branchlocation  = models.TextField()
    allowedemps = models.IntegerField(default=10)
    def __str__(self):
        return self.branchname

#schema for representing data in terms of request and response.
#also good for validating and auto conversion.
class branchinSchema(Schema):
    branchname: str
    branchlocation: str
    allowedemps: int

class empBriefSchema(Schema):
    id: int
    empname: str
    email: str

class branchoutSchema(Schema):
    id: int
    branchname: str
    branchlocation: str
    allowedemps: int
    employees: List[empBriefSchema]

class branchesListSchema(Schema):
    id: int
    branchname: str
    branchlocation: str    
    
