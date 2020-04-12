""" ImageNet: VGGNet, ResNet, Inception, and Xception with Keras """

import os
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.applications import imagenet_utils
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
MODEL = InceptionV3(weights="imagenet")


def classify_image(image_file):
    """ Classify image using Inception_V3"""

    input_shape = (299, 299)
    img = image.load_img(image_file, target_size=input_shape)
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    preds = MODEL.predict(img)
    p_from_im = imagenet_utils.decode_predictions(preds)

    (_, label, prob) = p_from_im[0][0]
    return [label, prob]
