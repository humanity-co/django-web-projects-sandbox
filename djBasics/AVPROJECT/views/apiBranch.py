from ninja import Router
from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from avapp.models.branch import branch, branchinSchema, branchoutSchema 
branchRouter = Router()
@branchRouter.post("/add",response=branchoutSchema)
def addBranch(request: HttpRequest, payload: branchoutSchema):
    print("inside post")
    newbranch = branch.objects.create(**payload.dict())
    return {"id": newbranch.id, "branchname": newbranch.branchname,"branchlocation": newbranch.branchlocation}


@branchRouter.get("/list",response=list[branchoutSchema] )
def listBranches(request: HttpRequest):
    return branch.objects.all()
@branchRouter.get("single{branch_id}",response=branchinSchema)
def singleBranch(request: HttpRequest,branch_id: int):
    branchRecord= get_object_or_404(branch, id=branch_id)
    return branchRecord