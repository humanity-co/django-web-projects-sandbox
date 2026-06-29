from ninja import Router
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from avapp.models.customer import customer,customerinSchema,customeroutSchema

customerRouter = Router()
@customerRouter.post("/add",response=customeroutSchema)
def addcustomer(request:HttpRequest,payload: customerinSchema):
    newcust= customer.objects.create(**payload.dict())
    return newcust

@customerRouter.get("/List",response=list[customeroutSchema])
def listCustomers(request: HttpRequest):
    return customer.objects.all()

@customerRouter.get("single{branch_id}",response=customerinSchema)
def singlecustomer(request: HttpRequest,branch_id: int):
    customerRecord= get_object_or_404(customer, id=branch_id)
    return customerRecord