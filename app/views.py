from django.shortcuts import render
from app.models import *
from rest_framework.views import APIView
from app.serializers import *
from rest_framework.response import Response



# Create your views here.

class AllCategoryView(APIView):
    def get(self,request,*args, **kwargs):
        category = Category.objects.all()
        total_category = Category.objects.all().count()
        category_serializer =  CategorySerializer().data

        response_data = {
            category: category_serializer,
            total_category:total_category
        }
        return Response (response_data)
    def post (self, request, *args, **kwargs):
        category_serializer = CategorySerializer(data=request.data)

        if Category.objects.filter(**request.data).exists():
            raise serializers.ValidationError('This data already do exists')
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data)
        else:
            return Response('New Category canot be created')
class 