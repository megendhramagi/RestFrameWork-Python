from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 
from .models import Students, Marks
# Create your views here.
from .serializers import StudentSerial,MarkSerial

class Student_Api(APIView):
    def get(self,request):
        stu_data = Students.objects.all()
        stu_li = []
        for stu in stu_data:
            stu_dict = {
                "name":stu.name,
                "age":stu.age
            }
            stu_li.append(stu_dict)
        return Response(stu_li)
    
    def post(self,request):
        print(request.data)
        student_data = Students(name = request.data['name'], age = request.data['age'])
        student_data.save()
        return Response('Data Saved')

    def patch(self, request, id):
        stu_data = Students.objects.filter(id = id) #try get instead of filter
        stu_data.update(name = request.data['name'], age = request.data['age'])
        print(request.data)
        return Response("Data updated")
class Student2Api(APIView):

    def get(self,request,id=None):
        if id==None:
            s_d = Students.objects.all()
            ss_d = StudentSerial(s_d, many=True).data
        else:
            s_d=Students.objects.get(id=id)
            ss_d = StudentSerial(s_d).data
        return Response(ss_d)
    def post(self,request):
        s_data = StudentSerial(data=request.data())
        if s_data.is_valid():
            s_data.save()
            return Response("Data saved")
        return Response("Data cannot be saved")
    def patch(self,request,id):
        s_d = Students.objects.get(id = id)
        ss_d = StudentSerial(s_d, data=request.data, partial=True)
        if ss_d.is_valid():
            ss_d.save()
            return Response("Data updated")
        return Response("Update failed")

class MarkApi(APIView):
    def get(self, request,id = None):
        if id == None:
            m_data = Marks.objects.all()
            mm_data=MarkSerial(m_data,many=True).data
        else:
            m_data = Marks.objects.get(id=id)
            mm_data=MarkSerial(m_data).data           
        return Response(mm_data)

    def post(self,request):
        total = request.data["tamil"]+request.data["english"]+request.data["maths"]
        average = total/3
        isPass = False
        if(request.data["tamil"]>=35 and request.data["english"]>=35 and request.data["maths"]>=35):
            isPass = True
        m_data = Marks(
            tamil = request.data["tamil"],
            english = request.data["english"],
            maths = request.data["maths"],
            total = total,
            average = average,
            isPass = isPass)
        m_data.save()
        return Response("Data saved")