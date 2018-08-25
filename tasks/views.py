from django.shortcuts import render
from .models import tasks
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import taskSerializers
from . import serializers
from rest_framework.response import Response


# Create your views here.
class create(APIView):
    serializer_class = taskSerializers
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)




class list(generics.ListCreateAPIView):
    queryset = tasks.objects.all()
    serializer_class = serializers.taskSerializers

class individual(generics.RetrieveUpdateDestroyAPIView):
    queryset = tasks.objects.all()
    serializer_class = serializers.taskSerializers
