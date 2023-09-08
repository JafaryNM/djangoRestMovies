from rest_framework import serializers
from watchlist_app.models import Movie

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
    
    
        """
         def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError('Name is too short!')
        return value
        """
    
    def validate(self,data):
        if data['name']==data['description']:
            raise serializers.ValidationError('Name should not equal to Description')
        return data