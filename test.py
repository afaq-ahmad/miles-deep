import glob
import tensorflow as tf
import cv2
import numpy as np
import os

def process(file):
	img = cv2.imread(file)
	img = cv2.resize(img, (224, 224))
	img = img.astype("float32")
	img -= mean_image
	return img

for f in glob.glob("images/*"): os.remove(f)
os.system("ffmpeg -i vid.mp4 -vf fps=1 images/%d.jpg")
mean_image = np.load("model/mean.npy")
x = []
print("Preprocessing")
for f in glob.glob("images/*"):
	x.append(process(f))
x = np.array(x)
print("Loading model")
model = tf.keras.models.load_model('model/weights.h5')
print("predicting")
preds = model.predict(x)
y = preds.argmax(axis=-1)
categories = ["blowjob_handjob", "cunnilingus", "other", "sex_back", "sex_front", "titfuck"]
labels = [categories[i] for i in y]
for i, l in enumerate(labels):
	if l != "other" and preds[i][y[i]]>0.7: print(i, l)
