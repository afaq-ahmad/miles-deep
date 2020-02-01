## Translation
This is a translation of [ryanjay0/miles-deep](https://github.com/ryanjay0/miles-deep) in tf.keras.

This is just a model translation without any feature. The model is translated using [microsoft/MMdnn.](https://github.com/microsoft/MMdnn)

The accuracy has not been verified since the data used to train the model is not available.

The description below is slightly modified from the original repository.

## Miles Deep - AI Porn Video Classifier
Using a deep convolutional neural network with residual connections, Miles Deep quickly classifies each second of a pornographic video into 6 categories based on sexual act with 95% accuracy.
* blowjob_handjob
* cunnilingus
* other
* sex_back
* sex_front
* titfuck

## Dependencies
* apt install ffmpeg
* pip install tensorflow
* pip install opencv-python

## Test
* Put a short video with file name vid.mp4
* Run python test.py

It will convert the video into 1 image/second and print out only the labels (>0.7) ignoring "other" label.