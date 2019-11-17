from rest_framework import viewsets
from polls.serializers import UserSerializer, GroupSerializer,PredictSerializer

from rest_framework.response import Response
from rest_framework.decorators import action
from .Predictor import Predictor
import os
import json
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class PredictViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    # serializer_class = PredictSerializer
    @action(detail=True, methods=['post'])
    def predict(self, request):
        print("hello")
        # data = request.data
        # if data['algos'] == 'Linear Reg':
        #     ret = Calculations.LinearReg(data['params'])
        #     return Response(ret)
        return Response(request,200)
class CalculateViewset(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def predict(self, request):
        print(request.FILES)
        my_file = request.FILES['file']
        filename = os.path.join(os.getcwd(),"test.JPG")
        with open(filename, 'wb+') as temp_file:
            for chunk in my_file.chunks():
                temp_file.write(chunk)
        # data = request.file
        resp = Predictor.predict()
        return Response(resp,200)