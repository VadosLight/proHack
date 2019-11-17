from rest_framework.response import Response
from rest_framework.decorators import action    
# from keras.applications import ResNet152
from keras.preprocessing.image import ImageDataGenerator
from django.conf import settings
from keras.preprocessing import image
from back.settings import graph
from back.settings import model
from back.settings import sess
from back.settings import tf
from sklearn.metrics import classification_report, confusion_matrix


from keras.backend import set_session

import os
import numpy as np
import PIL
class Predictor:
    def __init__(self):
        pass
   
    def predict():
        classes = ['Class0','Class1','Class2','Class3','Class4',
        'Class5','Class6','Class7','Class8',
        'Class9','Class10','Class11','Class12']
        target_names = ['Хороший класс', 'Волосяные трещины', 'Затертая поверхность', 'Значительное искажение', 'Отверстия в шоколаде', 'Открытый центр', 'Плохая декорация', 'Плохое донышко',
               'Повреждение упаковочной машины', 'Сломанный и раздавленный', 'Тонкий слой шоколада', 'Хвостики']
        global sess
        global graph
        with graph.as_default():
            set_session(sess)
            sess.run(tf.global_variables_initializer())
            img = image.load_img(os.path.join(os.getcwd(),"test.JPG"), target_size=(224, 224))
            img_tensor = image.img_to_array(img)                    # (height, width, channels)
            img_tensor = np.expand_dims(img_tensor, axis=0)
            Y_pred=model.predict(img_tensor)
            y_pred = np.argmax(Y_pred, axis=1)
            # print(classification_report(classes, y_pred, target_names=target_names))
        return y_pred