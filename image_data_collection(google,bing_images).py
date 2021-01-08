# -*- coding: utf-8 -*-
"""Image data collection(google,bing images).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jGIiDWgZLPImF2aJy9ufNVBKEwWogoAF

# @copyrights limited.

#How to collect data for image classification *task*

# custom data set for image classification

# installing this package from github repo. Actually !pip install google iamge download package available but it is not available now, so this is a modified version of that.
"""

!pip install git+https://github.com/Joeclinton1/google-images-download.git

"""calling the below command to import the package"""

from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()

"""https://google-images-download.readthedocs.io/en/latest/arguments.html.

We cn go here for complete documentation of arguments that might be useful for the google images download

i want the the images of polar bear in arctic,penguin in antarctica, donald trump ad some of my most liked people of 6 images each and the format is jpg and also the urls.
"""

arguments = {"keywords":"polar bear in arctic,penguin in antarctica, Ys Jagan Mohan Reddy, Ayn Rand,brand logos, traffic in new york city", "limit":6, "format": "jpg", "print_urls":True}
paths = response.download(arguments)

!ls downloads/

"""We can see 3 folders here as we have given 3 searches criteria"""

!ls downloads/'polar bear in arctic'

!ls downloads/'penguin in antarctica'

!ls downloads/' Ayn Rand'

"""# visualise and see how the images looks like. to check wheteher the downloaded image is valid or not."""

from six import BytesIO
from PIL import Image
import numpy as np
import glob
import os

import matplotlib
import matplotlib.pyplot as plt

# craeted a function which loads image into numpy array.
# read the image and open it and finding the height and width f the image and then it is going to convert into a numpy array and return it back
def load_image_into_numpy_array(path):
  img_data = open(path,'rb').read()
  image = Image.open(BytesIO(img_data))
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)

polar_image_path = "/content/downloads/polar bear in arctic/*"
polar_images_np = []
for iname in glob.glob(polar_image_path):
  polar_images_np.append(load_image_into_numpy_array(iname))

plt.rcParams['figure.figsize'] = [14, 7]

for idx, polar_image_np in enumerate(polar_images_np):
  plt.subplot(2, 3, idx+1)
  plt.imshow(polar_image_np)
plt.show()

penguin_image_path = "/content/downloads/penguin in antarctica/*"
penguin_images_np = []
for iname in glob.glob(penguin_image_path):
  penguin_images_np.append(load_image_into_numpy_array(iname))

plt.rcParams['figure.figsize'] = [14, 7]

for idx, penguin_image_np in enumerate(penguin_images_np):
  plt.subplot(2, 3, idx+1)
  plt.imshow(penguin_image_np)
plt.show()

andhra_cm_image_path = "/content/downloads/ Ys Jagan Mohan Reddy/*"
andhra_cm_images_np = []
for iname in glob.glob(andhra_cm_image_path):
  andhra_cm_images_np.append(load_image_into_numpy_array(iname))

plt.rcParams['figure.figsize'] = [14, 7]

for idx, andhra_cm_image_np in enumerate(andhra_cm_images_np):
  plt.subplot(2, 3, idx+1)
  plt.imshow(andhra_cm_image_np)
plt.show()

"""# sometimes google wont allow the images to be downloaded, then we have an alternative which is microsoft bing. so lets see how we can extract the images from bing.

# download images from bing image search
"""

!pip install bing-image-downloader

"""# make a directory in current folder"""

!mkdir images

from bing_image_downloader import downloader
downloader.download("elephant in africa", limit = 5, output_dir ="images", adult_filter_off = True, force_replace = False)

downloader.download("tigers in india", limit = 10, output_dir="images", force_replace = False)

!ls images/ - alrt

!ls "images"/"tigers in india"

!ls "images"/"elephant in africa"

from IPython.display import Image
Image('images/elephant in africa/Image_1.jpg')

Image('images/tigers in india/Image_1.jpg')

# convert into numpy so that i can feed it into any model
from six import BytesIO
from PIL import Image
import numpy as np
import glob
import os

import matplotlib
import matplotlib.pyplot as plt

# craeted a function which loads image into numpy array.
# read the image and open it and finding the height and width f the image and then it is going to convert into a numpy array and return it back
def load_image_into_numpy_array(path):
  img_data = open(path,'rb').read()
  image = Image.open(BytesIO(img_data))
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)

tiger_image_path = "/content/images/tigers in india/*"
tiger_images_np = []
for iname in glob.glob(tiger_image_path):
  tiger_images_np.append(load_image_into_numpy_array(iname))

plt.rcParams['figure.figsize'] = [14, 7]

for idx, tiger_image_np in enumerate(tiger_images_np):
  plt.subplot(2, 5, idx+1)
  plt.imshow(tiger_image_np)
plt.show()

elephant_image_path = "/content/images/elephant in africa/*"
elephant_images_np = []
for iname in glob.glob(elephant_image_path):
  elephant_images_np.append(load_image_into_numpy_array(iname))

plt.rcParams['figure.figsize'] = [14, 7]

for idx, elephant_image_np in enumerate(elephant_images_np):
  plt.subplot(1, 5, idx+1)
  plt.imshow(elephant_image_np)
plt.show()