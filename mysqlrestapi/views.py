from django.http import response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from mysqlrestapi.models import Department,Employees
from mysqlrestapi.serializers import DepartmentSerializer,EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
# API Method - Function that contains tasks to be done when department table is queried
def departmentApi(request, id=0):
    #if GET, get all objects in the department table and serialize it
    if request.method=='GET': 
        department = Department.objects.all()
        department_serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(department_serializer.data,safe=False)
    # if POST, get data in the request, serialize it and if valid, add to the DB
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer=DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Data Added Successfully",safe=False)
        return JsonResponse("Data is invalid. Failed to Add",safe=False)
    # if PUT, get the change from requests using id, serialize the change and if valid, add to DB
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentId'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse('Update Successful',safe=False)
        return JsonResponse("Data is invalid. Failed to Update",safe=False)
    # If DELETE, get the ID to be deleted then delete
    elif request.method=='DELETE':
        department=Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Successfully",safe=False)


@csrf_exempt
# API Method - Function that contains tasks to be done when department table is queried
def employeeApi(request, id=0):
    #if GET, get all objects in the department table and serialize it
    if request.method=='GET': 
        employee = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data,safe=False)
    # if POST, get data in the request, serialize it and if valid, add to the DB
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer=EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Data Added Successfully",safe=False)
        return JsonResponse("Data is invalid. Failed to Add",safe=False)
    # if PUT, get the change from requests using id, serialize the change and if valid, add to DB
    elif request.method=='PUT':
        employee_data=JSONParser().parse(request)
        employee=Employees.objects.get(EmployeesId=employee_data['EmployeesId'])
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Update Successful',safe=False)
        return JsonResponse("Data is invalid. Failed to Update",safe=False)
    # If DELETE, get the ID to be deleted then delete
    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeesId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully",safe=False)

# API method for files upload
@csrf_exempt
def savefile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)