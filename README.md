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




# Miles DEEP Upgradation 
### Requirements Installations:
	
	- intel-tensorflow
	- opencv-python
	- numpy
	
	>pip install -r requirements.txt

### optional arguments:
  -h, --help            show this help message and exit
  -vp VIDEO_PATH, --video_path VIDEO_PATH
                        Input video path
  -ovp OUTVIDEO_PATH, --outvideo_path OUTVIDEO_PATH
                        output video path
  -c CTG_IN, --ctg_in CTG_IN
                        Categories you want to
                        save,categories:['blowjob_handjob', 'cunnilingus',
                        'other', 'sex_back', 'sex_front', 'titfuck'], if you
                        want to use multiple then add with comma like
                        sex_back,sex_front
  -x, --sexual          This edits out all the non-sexual scenes from input
                        video
  -ss SKIP_S, --skip_s SKIP_S
                        Skip seconds to remove the small flickering in
                        categories if appear do to false classification,
                        (default:3)
						
						
#Usage

* This finds the scenes that have no sex inside them from input.mp4 video and outputs the result in output.mp4
	> python miles_deep.py -vp input.mp4 -c other -ovp output.mp4

* This finds the scenes sex from input.mp4 video related to sex back or front and outputs the result in output.mp4
	> python miles_deep.py -vp input.mp4 -c sex_back,sex_front -ovp output.mp4


* This edits out all the non-sexual scenes from input.mp4 and outputs the result in output.mp4.
	
	> python miles_deep.py -vp input.mp4 -x -ovp output.mp4
