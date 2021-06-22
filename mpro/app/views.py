from django.shortcuts import render

from rest_framework.response import Response
from .models import AdminProfile, TeacherProfile, Dep
from .serializers import ProfileSerializers,TeacherAccountSerializer, DepSerializer
from rest_framework import views, viewsets, generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



class TeacherAccountView(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin):
    queryset = TeacherProfile.objects.all().order_by("-id")
    serializer_class=TeacherAccountSerializer
    lookup_field = "pk"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)

            
class TeacherAccountView_detail(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
     queryset = TeacherProfile.objects.all()
     serializer_class=TeacherAccountSerializer
     lookup_field = "pk"

     def get(self,request, *args, **kwargs):
         return self.retrieve(request, *args, **kwargs)
     def put(self,request, *args, **kwargs):
         return self.update(request,*args, **kwargs)
     def delete(self,request, *args, **kwargs):
         return self.destroy(request,*args, **kwargs)


class ProfileView(views.APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        try:
            query = AdminProfile.objects.get(adminuser=request.user)
            serializer = ProfileSerializers(query)
            response_message = {"error": False, "data": serializer.data}
        except:
            response_message = {"error": True, "message": "Somthing is Wrong"}
        return Response(response_message)


class DepView(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.CreateModelMixin):
    queryset = Dep.objects.all().order_by("-id")
    serializer_class=DepSerializer
    lookup_field = "pk"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)

            
class DepView_detail(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
     queryset = Dep.objects.all()
     serializer_class=DepSerializer
     lookup_field = "pk"

     def get(self,request, *args, **kwargs):
         return self.retrieve(request, *args, **kwargs)
     def put(self,request, *args, **kwargs):
         return self.update(request,*args, **kwargs)
     def delete(self,request, *args, **kwargs):
         return self.destroy(request,*args, **kwargs)
