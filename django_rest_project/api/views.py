import re
from django.http import response
from django.shortcuts import render
from Employee.models import Departments, Employees
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import BlogPost
from .serializers import BlogPostSerializer
import datetime as time
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from Employee.serializers import DepartmentSerializer, EmployeeSerializer
from django.core.files.storage import default_storage

# Create your views here.
# @api_view(['GET', ])
# def api_blog_view(request):
#     try:
#         blog_post = BlogPost.objects.first()
#         # blog_post = {
#         #     'title': 'sodfg',
#         #     'body': 'Hi there!',
#         #     'image': 'image/url',
#         #     'date_updated': time.datetime.now()
#         # }
#     except BlogPost.DoesNotExists:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     serializer = BlogPostSerializer(blog_post)
#     return Response(serializer.data)

# @api_view(['POST', ])
# def api_save_blog_view(request):
#     serializer = BlogPostSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(status=status.HTTP_401_BAD_REQUEST)

class BlogApi(APIView):
    def get_blog(self, pk):
        try:
            blog_post = BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data)

    def get(self, req, pk=None):
        if pk:
            return self.get_blog(pk)
        else:
            blog_post = BlogPost.objects.all()
            serializer = BlogPostSerializer(blog_post, many=True)
        return Response(serializer.data)

    
    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_BAD_REQUEST)

@csrf_exempt
def departmentapi(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                department = Departments.objects.get(DepartmentId=id)
                dept_serializer = DepartmentSerializer(department)
                return JsonResponse(dept_serializer.data, status=status.HTTP_200_OK, safe=False)
            except Departments.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)   
        departments = Departments.objects.all()
        dept_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(dept_serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == 'POST':
        dept_payload = JSONParser().parse(request)
        dept_serializer = DepartmentSerializer(data=dept_payload)
        if dept_serializer.is_valid():
            dept_serializer.save()
            return JsonResponse(dept_serializer.data)
        return JsonResponse('Failed to Create', safe=False)
    elif request.method == 'PUT':
        dept_payload = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId=dept_payload['DepartmentId'])
        dept_serializer = DepartmentSerializer(department, data=dept_payload)
        if dept_serializer.is_valid():
            dept_serializer.save()
            return JsonResponse(dept_serializer.data)
        return JsonResponse('Failed to update', safe=False)
    elif request.method == 'DELETE':
        try:
            department = Departments.objects.get(DepartmentId=id)
            department.delete()
            return JsonResponse(f'Successfully Deleted the department id: {id}', safe=False)
        except Departments.DoesNotExist:
            return JsonResponse('Department Not Found to Delete', safe=False)

@csrf_exempt
def employeeapi(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                employee = Employees.objects.get(EmployeeId=id)
                employee_serializer = EmployeeSerializer(employee)
                return JsonResponse(employee_serializer.data, status=status.HTTP_200_OK, safe=False)
            except Employees.DoesNotExist:
                return JsonResponse(status=status.HTTP_404_NOT_FOUND)
        employees = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, status=status.HTTP_200_OK, safe=False)
    elif request.method == 'POST':
        emp_payload = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=emp_payload)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse(employee_serializer.data, status=status.HTTP_200_OK, safe=False)
        return JsonResponse('Failed to Create', safe=False)
    elif request.method == 'PUT':
        emp_payload = JSONParser().parse(request)
        try:
            employee = Employees.objects.get(EmployeeId=id)
            employee_serializer = EmployeeSerializer(employee, data=emp_payload)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return JsonResponse(employee_serializer.data, status=status.HTTP_200_OK, safe=False)
            return JsonResponse('Failed to update', safe=False)
        except Employees.DoesNotExist:
            JsonResponse('Employee Not Found to update', safe=False)
    elif request.method == 'DELETE':
        try:
            employee = Employees.objects.get(EmployeeId=id)
            employee.delete()
            return JsonResponse(f'Successfully Deleted the employee id: {id}', safe=False)
        except Employees.DoesNotExist:
            return JsonResponse('Employee Not Found to Delete', safe=False)


@csrf_exempt
def save_image(request):
    file = request.FILES['file']
    file_name=default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)