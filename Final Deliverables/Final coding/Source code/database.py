#Import all Necessary Libraries import pandas as pd import numpy as np import matplotlib.pyplot as plt from tensorflow.keras.datasets import mnist (x_train,y_train),(x_test,y_test)=mnist.load_data() x_train

array([[[0, 0,	0,	..., 0,	0,	0],
[0, 0, 0, ...,	0,	0, 0],		
[0, 0,	0,	..., 0,	0,	0],
...,
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0]],
[[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
...,
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0]],
[[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
...,
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0]],
...,						
[[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
...,
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
 
[0,	0,	0,	...,	0,	0,	0]],
[[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
 
[0, 0, 0, ..., 0, 0, 0],
...,
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0]],
[[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
...,
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0],
[0,	0,	0,	...,	0,	0,	0]]], dtype=uint8)
x_train.shape (60000, 28, 28) one_img =
x_train[0] one_img.shape (28, 28) one_img array([[
0,

0,

[
0,

0,

[
0,

0,

[
0,

0,

[
0,

0,

[
3,
18, 18, 18, 126, 136, 175, 26, 166, 255, 247, 127,	0,
0,
0,	0],
 

170,

0,


253,

0,


253,

0,


253,

0,


253,

0,


253,

0,


190,

0,


35,

0,


0,

0,


0,
 
[ 0,	0,	0,

253, 253, 253,

0,	0],
[ 0,	0,	0,

253, 253, 253,

0,	0],
[ 0,	0,	0,

253, 198, 182,

0,	0],
[ 0,	0,	0,

205, 11,	0,

0,	0],
[ 0,	0,	0,

90,	0,	0,

0,	0],
[ 0,	0,	0,

190,	2,	0,

0,	0],
[ 0,	0,	0,

253, 70,	0,

0,	0],
[ 0,	0,	0,

241, 225, 160,

0,	0],
[ 0,	0,	0,

81, 240, 253,

0,	0],
[ 0,	0,	0,

0, 45, 186,
 

0],	
0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
0,	16,	93,	252,	253,	187,	0,	0,	0,	0,	0,
0],										
0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
0,	0,	0,	249,	253,	249,	64,	0,	0,	0,	0,
0],										
0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,

46, 130,	
183,	
253,	
253,	
207,	
2,	
0,	
0,	
0,	
0,

0],										
0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,

29, 253,	
253,	
253,	
250,	
182,	
0,	
0,	
0,	
0,	
0,

0],										
0,	0,	0,	0,	0,	0,	0,	0,	0,	24,	114,

53, 253,	
253,	
201,	
78,	
0,	
0,	
0,	
0,	
0,	
0,

0],										
0,	0,	0,	0,	0,	0,	0,	23,	66,	213,	253,

53, 198,	
81,	
2,	
0,	
0,	
0,	
0,	
0,	
0,	
0,

0],										
0,	0,	0,	0,	0,	18,	171,	219,	253,	253,	253,
80,	9,	0,	0,	0,	0,	0,	0,	0,	0,	0,
0],
0,	0,	
0,	
55,	
172,	
226,	
253,	
253,	
253,	
253,	
244,
0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
0],
0,	0,	
0,	
136,	
253,	
253,	
253,	
212,	
135,	
132,	
16,
0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,

0],
 
	[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
0,													
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
0,													
		0,	0],										
	[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
0,													
		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
0,													
		0,	0],										
	[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
0,													

0,		0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
0,	0]], dtype=uint8)
#plot the single image
plt.imshow(one_img,cmap='binary')
<matplotlib.image.AxesImage at 0x7f36882992d0>

y_train
array([5, 0, 4, ..., 5, 6, 8], dtype=uint8)
#categories the data
from tensorflow.keras.utils import to_categorical y_train.shape
(60000,)
 
y_example = to_categorical(y_train) print(y_example,y_example.shape)

[[0.	0.	0. ... 0.	0.	0.]
[1.	0.	0. ... 0.	0.	0.]
[0.	0.	0. ... 0.	0.	0.]
...				
[0.	0.	0. ... 0.	0.	0.]
[0.	0.	0. ... 0.	0.	0.]
[0.	0.	0. ... 0.	1.	0.]] (60000, 10)
y_example[0]
array([0., 0., 0., 0., 0., 1., 0., 0., 0., 0.], dtype=float32)
y_cat_test = to_categorical(y_test,num_classes=10) y_cat_train

= to_categorical(y_train,10)	one_img.max(),one_img.min()	
(255, 0)		
x_train = x_train/255 x_test = x_test/255		
scaled_img = x_train[0] scaled_img		
array([[0.	, 0.	, 0.	, 0.	, 0.	,
0.	, 0.	, 0.	, 0.	, 0.	,

0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
 
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	, 0.	, 0.01176471,	0.07058824,	0.07058824,
0.07058824, 0.49411765, 0.53333333,	0.68627451,	0.10196078,
0.65098039, 1.	, 0.96862745,	0.49803922,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	, 0.11764706, 0.14117647,
0.36862745,	0.60392157,	0.66666667, 0.99215686, 0.99215686,
0.99215686,	0.99215686,	0.99215686,	0.88235294,	0.6745098	,
0.99215686,	0.94901961,	0.76470588,	0.25098039,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	, 0.19215686, 0.93333333, 0.99215686,
0.99215686,	0.99215686,	0.99215686,	0.99215686,	0.99215686,
0.99215686,	0.99215686,	0.98431373,	0.36470588,	0.32156863,
0.32156863, 0.21960784, 0.15294118, 0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	, 0.	, 0.07058824,	0.85882353,	0.99215686,
0.99215686, 0.99215686, 0.99215686,	0.99215686,	0.77647059,
0.71372549, 0.96862745, 0.94509804, 0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	, 0.31372549, 0.61176471,
0.41960784,	0.99215686,	0.99215686,	0.8039	2157,	0.04313725	,
0.	,	0.16862745,	0.60392157,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	, 0.05490196,
0.00392157,	0.60392157,	0.99215686,	0.35294118,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.54509804,	0.99215686,	0.74509804,	0.00784314,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
 
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.04313725,	0.74509804,	0.99215686,	0.2745098	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.1372549	,	0.94509804,	0.88235294,
0.62745098,	0.42352941,	0.00392157,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.31764706,	0.94117647,
0.99215686,	0.99215686,	0.46666667,	0.09803922,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.17647059,
0.72941176,	0.99215686,	0.99215686,	0.58823529,	0.10588235,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.0627451	,	0.36470588,	0.98823529,	0.99215686,	0.73333333,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.97647059,	0.99215686,	0.97647059,
0.25098039,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.18039216,
0.50980392,	0.71764706,	0.99215686,	0.99215686,	0.81176471,
0.00784314,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.15294118,	0.58039216,	0.89803922,
0.99215686,	0.99215686,	0.99215686,	0.98039216,	0.71372549,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
 
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.09411765,	0.44705882,	0.86666667,	0.99215686,	0.99215686,
0.99215686,	0.99215686,	0.78823529,	0.30588235,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	, 0.	, 0.	, 0.09019608, 0.25882353,
0.83529412,	0.99215686,	0.99215686,	0.99215686,	0.99215686,
0.77647059,	0.31764706,	0.00784314,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	, 0.07058824, 0.67058824, 0.85882353, 0.99215686,
0.99215686, 0.99215686, 0.99215686, 0.76470588, 0.31372549,
0.03529412, 0.	, 0.	, 0.	, 0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	, 0.	, 0.	, 0.	, 0.21568627,
0.6745098 , 0.88627451, 0.99215686, 0.99215686, 0.99215686,
0.99215686, 0.95686275, 0.52156863, 0.04313725, 0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],			
[0.	, 0.	, 0.	, 0.	, 0.53333333,
0.99215686, 0.99215686, 0.99215686, 0.83137255, 0.52941176,
0.51764706, 0.0627451 , 0.	, 0.	, 0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],				
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],				
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	],				
[0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	,	0.	,	0.	,
0.	,	0.	,	0.	]]	)			
 
#reshape the scaled data
x_train = x_train.reshape(60000,28,28,1) x_test = x_test.reshape(10000,28,28,1) x_train.shape,x_test.shape
((60000, 28, 28, 1), (10000, 28, 28, 1))


 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras.utils import np_utils
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, Flatten
from tensorflow.keras.optimizers import Adam from tensorflow.keras.models import load_model from PIL import Image, ImageOps
import numpy




(X_train, y_train), (X_test, y_test) = mnist.load_data()
 









In [ ]:

In [2]:
 
Downloading data from https://storage.googleapis.com/tensorflow/tf-keras-data sets/mnist.npz
11490434/11490434 [==============================] - 0s 0us/step
 

print(X_train.shape) print(X_test.shape)
(60000, 28, 28)
(10000, 28, 28)

X_train[0]
 
In [3]:



In [4]:
 

	Out[4]:
array([[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	
	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	
	0,	0],												
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	
	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	
	0,	0],												
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	
	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	
	0,	0],												
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	
	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	
	0,	0],												
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	
	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	
	0,	0],												
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	3,	
 
18,	18, 18,	126,	136,	175,	26,	166,	255,	247,	127,	0,	0,
0,	0],										
[	0,	0,	0,	0,	0,	0,	0,	0,	30,	36,	94,	154,	170,
	253,	253,	253,	253,	253,	225,	172,	253,	242,	195,	64,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	49,	238,	253,	253,	253,	253,
	253,	253,	253,	253,	251,	93,	82,	82,	56,	39,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	18,	219,	253,	253,	253,	253,
	253,	198,	182,	247,	241,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	80,	156,	107,	253,	253,
	205,	11,	0,	43,	154,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	14,	1,	154,	253,
	90,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	139,	253,
	190,	2,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	11,	190,
253, 70,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	35,
	241,	225,	160,	108,	1,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	81,	240,	253,	253,	119,	25,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	45,	186,	253,	253,	150,	27,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0,	16,	93,	252,	253,	187,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0,	0,	0,	249,	253,	249,	64,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	46,	130,	183,	253,	253,	207,	2,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	39,
	148,	229,	253,	253,	253,	250,	182,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	24,	114,	221,
	253,	253,	253,	253,	201,	78,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	23,	66,	213,	253,	253,
	253,	253,	198,	81,	2,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	18,	171,	219,	253,	253,	253,	253,
	195,	80,	9,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
 
[	0,	0,	0,	0,	55,	172,	226,	253,	253,	253,	253,	244,	133,
	11,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	136,	253,	253,	253,	212,	135,	132,	16,	0,
	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0],											
[	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,
 
y_train[0] 5
 
0,	0]], dtype=uint8)
 
In [5]:

Out[5]:
In [11]:
 
plt.imshow(X_train[1])



X_train = X_train.reshape(60000, 28, 28, 1).astype('float32')
X_test = X_test.reshape(10000, 28, 28, 1).astype('float32')

number_of_classes = 10
Y_train = np_utils.to_categorical(y_train, number_of_classes) Y_test = np_utils.to_categorical(y_test, number_of_classes)
 

Out[11]:













In [12]:

In [13]:


In [14]:
 
Y_train[0]

array([0., 0., 0., 0., 0., 1., 0., 0., 0., 0.], dtype=float32)
Creating the model

model = Sequential()
 

Out[14]:

In [15]:
 
model.add(Conv2D(64, (3, 3), input_shape=(28, 28, 1), activation="relu"))
model.add(Conv2D(32, (3, 3), activation="relu")) model.add(Flatten())
model.add(Dense(number_of_classes, activation="softmax"))
Compiling the model
 

model.compile(loss='categorical_crossentropy', optimizer="Adam", metrics=["accuracy"])
Fitting the model

model.fit(X_train, Y_train, batch_size=32, epochs=5, validation_data=(X_test,Y_test))
Epoch 1/5
 
In [16]:


In [17]:
 
1875/1875 [==============================] - 205s 109ms/step - loss: 0.2844 -
accuracy: 0.9477 - val_loss: 0.0886 - val_accuracy: 0.9729 Epoch 2/5
1875/1875 [==============================] - 206s 110ms/step - loss: 0.0716 -
accuracy: 0.9776 - val_loss: 0.0771 - val_accuracy: 0.9769 Epoch 3/5
1875/1875 [==============================] - 204s 109ms/step - loss: 0.0513 -
accuracy: 0.9837 - val_loss: 0.1019 - val_accuracy: 0.9710 Epoch 4/5
1875/1875 [==============================] - 222s 119ms/step - loss: 0.0408 -
accuracy: 0.9873 - val_loss: 0.0890 - val_accuracy: 0.9767 Epoch 5/5
1875/1875 [==============================] - 209s 112ms/step - loss: 0.0302 -
accuracy: 0.9906 - val_loss: 0.0918 - val_accuracy: 0.9772
 

Observing the metrices

metrics = model.evaluate(X_test, Y_test, verbose=0) print("Metrics (Test Loss & Test Accuracy): ") print(metrics)
Metrics (Test Loss & Test Accuracy): [0.09176069498062134, 0.9771999716758728]
Predicting the output

prediction = model.predict(X_test[:4]) print(prediction)
1/1 [==============================] - 0s 86ms/step [[1.30325325e-11 1.95553570e-17 4.99655983e-10 2.01586161e-07
 
Out[17]:

In [18]:




In [19]:
 
2.20858217e-14	9.75999270e-14 9.15056906e-17	9.99999523e-01	
2.50245790e-07	5.38577793e-10]		
[1.79366751e-07	3.38282398e-08 9.99999285e-01	1.66379285e-10	
2.10076114e-14	9.13577841e-17 4.58118137e-07	5.16888727e-15	
2.91890595e-10	3.41794947e-16]		
[5.36327924e-08	9.99545157e-01 1.32159499e-07	6.90754225e-12	
2.88232812e-04	1.63993846e-07 1.19756329e-08	9.81503305e-08	
1.66109443e-04	2.50516774e-10]		
[1.00000000e+00	3.44754093e-19 1.12327614e-14	9.01947470e-16	
7.90818081e-15	2.17030373e-13 1.37855594e-09	8.90824635e-15	
7.06134152e-16	1.75300985e-12]]		In [20]:
print(numpy.argmax(prediction, axis=1)) print(Y_test[:4])
[7 2 1 0]
[[0.	0.	0.	0.	0.	0.	0.	1.	0.	0.]
[0.	0.	1.	0.	0.	0.	0.	0.	0.	0.]
[0.	1.	0.	0.	0.	0.	0.	0.	0.	0.]
[1.	0.	0.	0.	0.	0.	0.	0.	0.	0.]]
 
saving the model

model.save("model.h5")
Test with saved model

model=load_model("model.h5")

from keras.datasets import mnist
from matplotlib import pyplot (X_train,y_train),(X_test,y_test)=mnist.load_data() print('X_train:' +str(X_train.shape)) print('y_train:' +str(y_train.shape)) print('X_test:' +str(X_test.shape))
print('y_test:' +str(y_test.shape)) from matplotlib import pyplot
for i in range(9): pyplot.subplot(330+1+i)
pyplot.imshow(X_train[i],cmap=pyplot.get_cmap('gray')) pyplot.show()
X_train:(60000, 28, 28)
y_train:(60000,) X_test:(10000, 28, 28)
y_test:(10000,)
 

In [21]:


In [26]:

In [27]:
 
 
 
 

