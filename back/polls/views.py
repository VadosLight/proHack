from rest_framework import viewsets
from polls.serializers import UserSerializer, GroupSerializer,PredictSerializer

from rest_framework.response import Response
from rest_framework.decorators import action
from .Predictor import Predictor
import numpy as np
import os
import json
from keras.applications.resnet import preprocess_input
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
        my_file = request.FILES['file'].read()
        # validation_batch = np.stack([preprocess_input(np.array(my_file.resize((224,224))))])
        filename = os.path.join(os.getcwd(),"test","test.JPG")
        os.remove(filename)
        with open(filename, 'wb+') as temp_file:
            # for chunk in my_file.chunks():
            temp_file.write(my_file)
        # data = request.file
        resp = Predictor.predict()
        return Response(resp,200)