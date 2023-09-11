from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform,Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'

class WatchlistSerializer(serializers.ModelSerializer):
    
    review=ReviewSerializer(many=True, read_only=True)
    class Meta:
        model=WatchList
        fields='__all__'

class StreamPlatformSerializer(serializers.ModelSerializer):
    
    watchlist= WatchlistSerializer(many=True, read_only=True)
    
    class Meta:
        model=StreamPlatform
        fields="__all__"











"""
    ########### VALIDATION ##################

    def get_len_name(self,object):
        return len(object.name)
        
########### VALIDATION ##################

    def validate(self,data):
        if data['name']==data['description']:
            raise serializers.ValidationError('Name should not equal to Description')
        return data
    
    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError('Name is too short!')
        return value
    
    
    def name_length(value):
    if len(value)<2:
        raise serializers.ValidationError('Name is too short!')
    return value
        

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField(validators=[name_length])
    description=serializers.CharField()
    active=serializers.BooleanField()
    
    def create(request,validate_data):
        return Movie.objects.create(**validate_data)
    
    def update(request,instance,validate_data):
        instance.name=validate_data.get('name',instance.name),
        instance.description=validate_data.get('description',instance.description),
        instance.active=validate_data.get('active',instance.active)
        instance.save()
        return instance
    
    

    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError('Name is too short!')
        return value
    
    
    def validate(self,data):
        if data['name']==data['description']:
            raise serializers.ValidationError('Name should not equal to Description')
        return data
"""