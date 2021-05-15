# Object Detector

## Structure

![](https://i.imgur.com/TgevKPc.png)
Note: YOLOv3 is not directly contained in this repo, check sources for YOLOv3's website.

## Requirements

- [TensorFlow](https://www.tensorflow.org/install/pip?hl=es-419)
- [numpy](https://pypi.org/project/numpy/)
- [OpenCV](https://pypi.org/project/opencv-python/)

## Usage

You can execute this project with

`python detect.py <args> <path to file>`

**Arguments:**

`-i <path to image> (or --image)`
`-v <path to video> (or --video)`
`-c (or --camera)`

Execution is limited to **_one_** argument, if you try `-i image -v video` it will only process the first argument, in this case the image.

## Download Examanager weights

Execute the command

`wget link -P weights/`

_or_

[download from google drive.](https://drive.google.com/drive/folders/1DiVZc7tjy-C0CJXh1aPl3OakzJfMI5HP?usp=sharing)

Just be sure to leave the file in

## Training

To train a model for this project, you need to download and label images (I suggest using [AIGuysCode's OIDv4 ToolKit fork](https://github.com/theAIGuysCode/OIDv4_ToolKit/blob/master/convert_annotations.py)) and then train it in Darknet.

After that, convert the weights file.

**Note:**
Be sure to update [examanager.names](https://github.com/CarlosPuello/objectDetectionPython/data/examanager.names) if the classes used for training were different.

## Converting weights file

The resulting .weights file should be placed in [the weights folder](https://github.com/CarlosPuello/objectDetectionPython/weights) and then converted to a tensorflow model using [convert_weights.py](https://github.com/CarlosPuello/objectDetectionPython/convert_weights.py).

## Sources:

[Darknet53](https://www.researchgate.net/figure/Structure-of-the-Darknet53-convolutional-network_fig4_338121987)
[YOLOv3](https://pjreddie.com/darknet/yolo/)
