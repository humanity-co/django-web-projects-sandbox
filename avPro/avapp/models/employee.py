from django.db import models
from typing import Dict, Any, Optional,List
from avapp.models.branch import branch



class employee(models.Model):
    empname = models.CharField(max_length=255)
    empaddr = models.TextField()
    email = models.EmailField(unique=True)
    worksat = models.IntegerField()

    def _str_(self):
        return self.empname


from pydantic import BaseModel

class employeeinschema(BaseModel):
    empname: str
    empaddr: str
    email: str
    worksat: Optional[int]=0

    class Config:
        arbitrary_types_allowed = True  # ✅ Allow unknown types


from pydantic import BaseModel

class EmployeeOutSchema(BaseModel):
    id: int
    empnamename: str
    email: str

    class Config:
        arbitrary_types_allowed = True  # Add this if it's missing