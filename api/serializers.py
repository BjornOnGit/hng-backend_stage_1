from rest_framework import serializers

class VisitorSerializer(serializers.Serializer):
    client_ip = serializers.CharField(max_length=45)
    location = serializers.CharField(max_length=100)
    greeting = serializers.CharField(max_length=1000)
