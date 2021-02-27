
from ssd_predict import detector
from PIL import Image
import cv2
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

###########################
NETWORK = "mobilenetv1" # Choose an option in `mobilenetv1`, `mobilenetv2` or `mobilenetv3`
WEIGHT_FILE = "./weights/ssdlite_mobilenetv1.h5" # The network weigth file path.
###########################

tf.config.set_visible_devices([], 'GPU')
visible_devices = tf.config.get_visible_devices()
for device in visible_devices:
    assert device.device_type != "GPU"

det = detector(weight_path="./ssd_vgg/ssd_vgg-148.h5", network="vgg")
image = Image.open("./image/06694.jpg")
predicts = []

det = detector(weight_path=WEIGHT_FILE, network=NETWORK)
image = det.detect_image(image)
plt.imshow(image)
plt.show()