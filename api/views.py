#from functools import partial
#from django.shortcuts import render
#from .serializers import StudentSerializer
#from rest_framework.decorators import api_view
#from rest_framework.response import Response
#from .models import Student
#from rest_framework import status
#from rest_framework import serializers


#from .serializers import StudentSerializer
#from .models import Student
#from rest_framework.mixins import ListModelMixin, CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
#from rest_framework.generics import GenericAPIView


#from .models import Student
#from .serializers import StudentSerializer
#from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


#from functools import partial
#from .models import Student
#from .serializers import StudentSerializer
#from rest_framework import viewsets
#from rest_framework.response import Response
#from rest_framework import status


from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_class = [BasicAuthentication]
    permission_class = [AllowAny]

#class StudentViewSet(viewsets.ViewSet):
#    def list(self,request):
#      stu = Student.objects.all()
#      serializer = StudentSerializer(stu,many=True)
#      return Response(serializer.data)

#    def create(self,request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response({'msg':'Data Created'}, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)


#    def retrieve(self,request,pk=None):
#        id=pk
#        if id is not None:
#            stu= Student.objects.get(id=id)
#            serializer = StudentSerializer(stu)
#            return Response(serializer.data)
#        stu = Student.objects.all()
#        serializer = StudentSerializer(stu,many=True)
#        return Response(serializer.data)


#    def update(self,request,pk):
#        id=pk
#        stu= Student.objects.get(pk=id)
#        serializer = StudentSerializer(stu,data=request.data)
#        if serializer.is_valid:
#            serializer.save()
#            return Response({'msg':'Data Updated'},status=status.HTTP_202_ACCEPTED)
#        return Response(serializer.errors,status= status.HTTP_304_NOT_MODIFIED)


#    def partial_update(self,request,pk):
#        id=pk
#        stu= Student.objects.get(pk=id)
#        serializer = StudentSerializer(stu,data=request.data,partial=True)
#        if serializer.is_valid:
#            serializer.save()
#            return Response({'msg':'Partial Data Updated'},status=status.HTTP_202_ACCEPTED)
#        return Response(serializer.errors,status= status.HTTP_304_NOT_MODIFIED)    


#    def destroy(self,request,pk):
#        id=pk
#        stu = Student.objects.get(pk = id)
#        stu.delete()
#        return Response({'msg':'Data Deleted'},status=status.HTTP_200_OK)


# GenericAPIView
# ListCreateAPIView

#class StudentListCreate(ListCreateAPIView):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer



#RetrieveUpdateDestroyAPIView

#class StudentRetUpdDes(RetrieveUpdateDestroyAPIView):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer

    


# ModelMixin
# List and Create(pk not required)

#class StudentLC(ListModelMixin,CreateModelMixin,GenericAPIView):

#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer
#    def get(self,request,*args, **kwargs):
#       return self.list(request,*args,**kwargs)

#    def post(self,request,*args, **kwargs):
#        return self.create(request,*args, **kwargs)


# Retrieve, Update, Delete(pk required)

#class StudentRUD(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):

#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer
#    def get(self,request,*args, **kwargs):
#       return self.retrieve(request,*args,**kwargs)             

#    def put(self,request,*args, **kwargs):
#       return self.update(request,*args,**kwargs)         

#    def delete(self,request,*args, **kwargs):
#       return self.destroy(request,*args,**kwargs)




# Function based class

#@api_view(['GET','POST','PUT','PATCH','DELETE'])

#def student_api(request,pk=None):
#    if request.method == 'GET':
#        id=pk
#        if id is not None:
#            stu= Student.objects.get(id=id)
#            serializer = StudentSerializer(stu)
#            return Response(serializer.data)
#        stu = Student.objects.all()
#        serializer = StudentSerializer(stu,many=True)
#        return Response(serializer.data) 



#    if request.method == 'POST':
#        serializer = StudentSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response({'msg':'Data Created'}, status = status.HTTP_201_CREATED)
#        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)    



#    if request.method == 'PUT':
#        id=pk
#        stu= Student.objects.get(pk=id)
#        serializer = StudentSerializer(stu,data=request.data)
#        if serializer.is_valid:
#            serializer.save()
#            return Response({'msg':'Data Updated'},status=status.HTTP_202_ACCEPTED)
#        return Response(serializer.errors,status= status.HTTP_304_NOT_MODIFIED)



#    if request.method == 'PATCH':
#        id=pk
#        stu=Student.objects.get(pk=id)
#        serializer = StudentSerializer(stu,data=request.data,partial=True)
#        if serializer.is_valid():
#            serializer.save()
#            return Response({'msg':'Partial Data Updated'},status= status.HTTP_202_ACCEPTED)
#        return Response(serializer.errors,status=status.HTTP_304_NOT_MODIFIED)




#    if request.method == 'DELETE':
#        id=pk
#        stu = Student.objects.get(pk = id)
#        stu.delete()
#        return Response({'msg':'Data Deleted'},status=status.HTTP_200_OK)           