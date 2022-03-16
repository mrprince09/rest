from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Musician

class StudentSerialized(serializers.ModelSerializer):
	class Meta:
		model=Musician
		fields='__all__'

	

