from rest_framework import serializers
from .models import Customer

#serializer to handle the customer catalog
class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('id','name','email')
        
