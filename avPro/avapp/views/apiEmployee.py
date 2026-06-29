from ninja import Router
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from avapp.models.employee import employee, employeeinschema
from avapp.models.employee import EmployeeOutSchema

employeeRouter = Router()

@employeeRouter.post("/add", response=EmployeeOutSchema)
def addEmployee(request: HttpRequest, payload: employeeinschema):
    print("inside details")
    newemployee = employee.objects.create(**payload.model_dump())
    return {
        "id": newemployee.id,
        "empname": newemployee.empname,  
        "empaddr": newemployee.empaddr,  
        "email": newemployee.email,      
        "worksat": newemployee.worksat }  


@employeeRouter.get("/list", response=list[EmployeeOutSchema])
def listEmployees(request: HttpRequest):
    return list(employee.objects.all())  # Convert QuerySet to a list

@employeeRouter.get("/single/{employee_id}", response=EmployeeOutSchema)
def singleemployee(request: HttpRequest, employee_id: int):
    employeeRecord = get_object_or_404(employee, id=employee_id)
    return employeeRecord