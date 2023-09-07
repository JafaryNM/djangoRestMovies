from django.shortcuts import render
from watchlist_app.models import Movie
from .serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

# Retrive all data
# 

class MovieListAV(APIView):
    
    def get(self,request):
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class MovieDetailAV(APIView):
    
    def get(self,request,pk):
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error':'Movie Does Not Exit'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie, data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.http_204)
        
            


"""
@api_view(['GET', 'POST'])

def movies_list(request):
    if request.method=='GET':
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    if request.method=='POST':
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
    


# Retrive individual data 

@api_view(['GET', 'PUT','DELETE'])

def movies_detail(request,pk):
    if request.method=='GET':
        try:
            movie=Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error':'Error doesnot exit'}, status=status.HTTP_400_BAD_REQUEST)
        
        
        serializer=MovieSerializer(movie)
        return Response(serializer.data)
    
    if request.method=='PUT':
        movie=Movie.objects.get(pk=pk)
        serializer=MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method=='DELETE':
        movie=Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    """