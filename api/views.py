from django.shortcuts import get_object_or_404
from watchlist_app.models import WatchList,StreamPlatform,Review
from .serializers import WatchlistSerializer,StreamPlatformSerializer,ReviewSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.decorators import api_vie
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.permissions import AdminOrReadyOnly,ReviewUserOrReadyOnly
#from rest_framework import mixins
# Create your views here.



############# WATCHLIST CRUD API ####################

class WatchListAV(APIView):
    
    def get(self,request):
        movies=WatchList.objects.all()
        serializer=WatchlistSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class WatchMovieDetailAV(APIView):
    
    def get(self,request,pk):
        try:
            movie=WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error':'Movie Does Not Exit'}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer=WatchlistSerializer(movie)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        serializer=WatchlistSerializer(movie, data=request.data)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        movie=WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.http_204)
        
            
################## STREAMPLATFORM CRUD API #############

class StreamPlatformListAV(APIView):
    
    def get(self,request):
        streamlines=StreamPlatform.objects.all()
        serializer= StreamPlatformSerializer(streamlines, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailAV(APIView):
    
    def get(self,request,pk):
        try:
            streamline=StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'error':'Streamline doesnot exist'}, status.HTTP_400_BAD_REQUEST)
        serializer=StreamPlatformSerializer(streamline)
        return Response(serializer.data)
    
    def put(self,request,pk):
        serializer=StreamPlatformSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
    
    def delete(self,request,pk):
        streamline=StreamPlatform.objects.get(pk=pk)
        streamline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
            

############ REVIEW APIS #####################

class ReviewList(generics.ListAPIView):

    serializer_class=ReviewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return  Review.object.filter(watchlist=pk)


class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class=ReviewSerializer
    
    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        movie=WatchList.objects.get(pk=pk)
        review_user=self.request.user
        queryset=Review.objects.filter(review_user=review_user,watchlist=movie)
        
        if queryset.exists():
            raise ValidationError('You have reviewed this movie')
        
        if WatchList.number_rating==0:
            WatchList.avg_rating=serializer.validated_data['rating']
        
        else:
            WatchList.avg_rating=(WatchList.avg_rating + serializer.validate_data['rating'])/2
        WatchList.number_rating = WatchList.number_rating +1
        
        WatchList.save()
        
        serializer.save(watchlist=movie,review_user=review_user)
 
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[ReviewUserOrReadyOnly]
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    
       
class StreamPlatformVS(viewsets.ModelViewSet):
    
    queryset=StreamPlatform.objects.all()
    serializer_class=StreamPlatformSerializer


"""
class StreamPlatformTest(viewsets.ViewSet):
    
    def list(self,request):
        queryset=StreamPlatform.object.all()
        serializer=StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrive(self,request,pk):
<<<<<<< HEAD
=======
        
>>>>>>> 7f8a07826bb2de6e8d98c0272d59484f74cbe5c8
        queryset=StreamPlatform.object.all()
        stream=get_object_or_404(queryset,pk=pk)
        serializer=StreamPlatformSerializer(stream)
        return Response(serializer.data)
    
    def create(self,request):
    
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
<<<<<<< HEAD
=======

"""


"""
>>>>>>> 7f8a07826bb2de6e8d98c0272d59484f74cbe5c8
class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    def post (self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


"""


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