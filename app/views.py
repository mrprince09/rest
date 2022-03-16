from django.shortcuts import render
from . models import Musician
from .serializers import StudentSerialized 
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# Create your views here.

class Generic:
	serailizer_class=None
	model=None

	@classmethod
	def get(cls,*args):

		data=cls.model.objects.all()
		data=cls.serailizer_class(data,many=True)
		return JsonResponse(data.data,safe=False)

	@classmethod
	def post(cls,*args):
		obj=cls.serailizer_class(request.data)
		obj.save()

	@classmethod
	def as_view(cls,*args):
		request=args[0]
		if request.method=="GET":
			return cls.get(*args)
		if request.method=="POST":
			return cls.post(*args) 





class Student(Generic):
	serailizer_class=StudentSerialized
	model=Musician


	def post(self):
		return {"not authorized":"False"}












def student(request):

	if request.method=='GET':
		id=request.GET.get('id',None)
		if id is not None:
			stu= Musician.objects.get(id=id)
			serializer= StudentSerialized(stu)
			return JsonResponse(serializer.data)
		stu= Musician.objects.all()
		serializer= StudentSerialized(stu, many=True)
		return JsonResponse(serializer.data, safe=False)   


def student1(request):
	stu= Musician.objects.all()
	serializer= StudentSerialized(stu, many=True)
	return JsonResponse(serializer.data, safe=False)


class zeneric1 :
	model=None
	serializer= None
	@classmethod
	def get(cls, *args):
		data=cls.model.objects.all()
		data=cls.serializer(data, many= True)
		return JsonResponse(data.data, safe=False)
	@classmethod
	def post(cls,*args):
		data=cls.serializer(request.data)
		data.save()

	@classmethod
	def put(cls, *args):
		pass
from django.views.decorators.csrf import csrf_exempt

class Api():
	def __init__(self,model,serializer,*arge):
		self.model=model
		self.serializer=serializer

	def get(self, *args):
		request=args[0]
		id=request.GET.get("id",None)
		if id is not None:
			data=self.model.objects.get(id=id)
			sdata=self.serializer(data)
			return JsonResponse(sdata.data)
		data=self.model.objects.all()
		sdata=self.serializer(data, many=True)
		return JsonResponse(sdata.data, safe=False)


	
	def post(self,*args):
		
		request=args[0]
		import json
		data=dict(json.loads(request.body.decode('utf-8')))
		sdata=self.serializer(data=data)

		if sdata.is_valid():
			sdata.save()
			return JsonResponse({"msg":"data created"})

   
	def view(self,*args):
		request=args[0]
		if request.method=="GET":
			return self.get(*args)
		if request.method=="POST":
			return self.post(*args)




