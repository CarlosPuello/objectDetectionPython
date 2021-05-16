from utils import load_class_names, output_boxes, draw_outputs, resize_image
from yolov3 import YOLOv3Net
import tensorflow as tf
from cfg import cfg
import numpy as np
import cv2

''' To use a dedicated  CUDA GPU
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
tf.config.experimental.set_memory_growth(physical_devices[0], True)
'''
max_output_size = 40
max_output_size_per_class= 20

def detect_image(img_path):
    model = YOLOv3Net(cfg.CFGFILE,cfg.MODEL_SIZE,cfg.NUM_CLASSES)
    model.load_weights(cfg.WEIGHTFILE)
    class_names = load_class_names(cfg.CLASS_NAME)
    image = cv2.imread(img_path)
    image = np.array(image)
    image = tf.expand_dims(image, 0)
    resized_frame = resize_image(image, (cfg.MODEL_SIZE[0],cfg.MODEL_SIZE[1]))
    pred = model.predict(resized_frame)
    boxes, scores, classes, nums = output_boxes( \
        pred, cfg.MODEL_SIZE,
        max_output_size=max_output_size,
        max_output_size_per_class=max_output_size_per_class,
        iou_threshold=cfg.IOU_THRESHOLD,
        confidence_threshold=cfg.CONFIDENCE_THRESHOLD)
    image = np.squeeze(image)
    img = draw_outputs(image, boxes, scores, classes, nums, class_names)
    win_name = 'Detection'
    cv2.imshow(win_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cv2.imwrite('test.jpg', img) # To save image

if __name__ == '__main__':
    print("Please execute from Detector.py")
    detect_image("data/images/test.jpg")