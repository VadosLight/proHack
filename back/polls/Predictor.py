from rest_framework.response import Response
from rest_framework.decorators import action    
# from keras.applications import ResNet152
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from django.conf import settings
from tensorflow.keras.preprocessing import image
from sklearn.metrics import classification_report, confusion_matrix
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.python.keras.backend import set_session
import tensorflow
from PIL import Image
from tensorflow.python.keras.models import load_model
from back.settings import  graph
import os
import numpy as np
import PIL
class Predictor:
    def __init__(self):
        pass
   
    def predict():
        tensorflow.keras.backend.clear_session()
        classes = ['Class0','Class1','Class10','Class11','Class12','Class2','Class3','Class4',
        'Class5','Class6','Class7','Class8',
        'Class9']
        target_names = ['Хороший класс', 'Волосяные трещины', 'Сломанный и раздавленный', "Тонкий слой",
          'Хвостики', 'Затертая поверхность', 'Значительное искажение',
          'Отверстия в шоколаде', 'Открытый центр', 'Плохая декорация', 'Плохое донышко','Повреждение упаковочной машины']
        model = tensorflow.keras.models.load_model("keras_restnet152_TF_06.h5")
        # with graph.as_default():          
        
            
        validation_img_paths = [os.path.join(os.getcwd(),"test",'test.JPG')]
        img_list = [Image.open(img_path) for img_path in validation_img_paths]
        validation_batch = np.stack([preprocess_input(np.array(img.resize((224,224))))
            for img in img_list])
        # print(validation_batch)    
        model._make_predict_function()
        pred_probs = model.predict(validation_batch)
        print("\r\n")
        # print(pred_probs)
        # top_values= [pred_probs[0][i] for i in np.argsort(class_prob)[-3:]]
        top_values= [pred_probs[0][i] for i in np.argsort(pred_probs[0])[-3:]]
        top = pred_probs.argsort()[0][-3:][::-1]
        resp = [{
                    "Name":target_names[top[0]],
                    "Accuracy":pred_probs[0][top[0]],
                },
                {
                    "Name":target_names[top[1]],
                    "Accuracy":pred_probs[0][top[1]],
                },
                {
                    "Name":target_names[top[2]],
                    "Accuracy":pred_probs[0][top[2]],
                }]
            # y_pred = np.argmax(pred_probs, axis=1)
        print(resp)
            # img_list = [Image.open(input_path + img_path) for img_path in validation_img_paths]
            # print(os.path.join(os.getcwd(),"test"))
            # test_generator = test_datagen.flow_from_directory(
            #     os.path.join(os.getcwd(), "test"),
            #     target_size=(224, 224),
            #     color_mode="rgb",
            #     shuffle = False,
            #     class_mode='binary',
            #     batch_size=1)
            # Y_pred=model.predict(test_generator)
            # y_pred = np.argmax(Y_pred, axis=1)
            # print( Y_pred)
            # print(classification_report(classes, y_pred, target_names=target_names))
        return resp