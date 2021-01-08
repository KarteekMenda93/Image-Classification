# -*- coding: utf-8 -*-
"""Datasets for Image Classification and Object Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WlM95C2cXzVfrfXphINNGE1hQV5o6BB7

# We can get some datasets directly from tensorflow datasets and openML datasets.

https://www.tensorflow.org/datasets/catalog/overview

https://www.openml.org/search?type=data
"""

import numpy as np
import tensorflow_datasets as tfds

import warnings
warnings.filterwarnings('ignore')

datasets, info = tfds.load('malaria', with_info=True, as_supervised=True, split=['train'])

info

train, info_train = tfds.load('malaria', with_info=True, split='train')
tfds.show_examples(info_train,train)

datasets, info = tfds.load(name = 'fashion_mnist', with_info=True, as_supervised=True, split = ['train','test'], batch_size=1)
train, test = tfds.as_numpy(datasets[0]), tfds.as_numpy(datasets[1])

"""# sklearn dataset fetch open ml"""

from sklearn.datasets import fetch_openml
faces= fetch_openml(name= 'UMIST_Faces_Cropped', version = 1)

faces.data.shape

faces.target

import matplotlib.pyplot as plt
import numpy as np

for i in range(6):
  idx = np.random.randint(1,500)
  face = faces.data[idx]
  face_pixels = face.reshape(112,92)
  plt.subplot(2,3,i+1)
  plt.imshow(face_pixels)
  plt.axis('off')

