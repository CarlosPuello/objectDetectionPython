from utils import load_class_names, output_boxes, draw_outputs, resize_image
from yolov3 import YOLOv3Net
import tensorflow as tf
from cfg import cfg
import time
import cv2

''' To use a dedicated  CUDA GPU
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
tf.config.experimental.set_memory_growth(physical_devices[0], True)
'''
max_output_size = 100
max_output_size_per_class= 20

def returnCameraIndexes(path):
    if path == 'camera':
        index = 0
        arr = []
        i = 10
        while i > 0:
            cap = cv2.VideoCapture(index)
            if cap.read()[0]:
                arr.append(index)
                cap.release()
            index += 1
            i -= 1
        return arr[0]
    else:
        return path

def detect_video(video_path):
    model = YOLOv3Net(cfg.CFGFILE,cfg.MODEL_SIZE,cfg.NUM_CLASSES)
    model.load_weights(cfg.WEIGHTFILE)
    class_names = load_class_names(cfg.CLASS_NAME)
    win_name = 'Detection'
    cv2.namedWindow(win_name)
    #Change returnCameraIndexes()[0] for file path
    cap = cv2.VideoCapture(returnCameraIndexes(video_path))
    frame_size = (cap.get(cv2.CAP_PROP_FRAME_WIDTH),
                  cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    try:
        while True:
            start = time.time()
            ret, frame = cap.read()
            if not ret:
                break
            resized_frame = tf.expand_dims(frame, 0)
            resized_frame = resize_image(resized_frame, (cfg.MODEL_SIZE[0],cfg.MODEL_SIZE[1]))
            pred = model.predict(resized_frame)
            boxes, scores, classes, nums = output_boxes( \
                pred, cfg.MODEL_SIZE,
                max_output_size=max_output_size,
                max_output_size_per_class=max_output_size_per_class,
                iou_threshold=cfg.IOU_THRESHOLD,
                confidence_threshold=cfg.CONFIDENCE_THRESHOLD)
            img = draw_outputs(frame, boxes, scores, classes, nums, class_names)
            cv2.imshow(win_name, img)
            stop = time.time()
            seconds = stop - start
            # Calculate frames per second
            fps = 1 / seconds
            print("Frames per second : {0}".format(fps))
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
    finally:
        cv2.destroyAllWindows()
        cap.release()
        print('Detections performed successfully.')

if __name__ == '__main__':
    print("Please execute from Detector.py")
    detect_video('camera')