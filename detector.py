from image import detect_image
from video import detect_video
import getopt
import sys

video_path = ''
image_path = ''

try:
    options, remainder = getopt.getopt(
        sys.argv[1:],
        'i:v:c',
        ['image=',
         'verbose',
         'video=',
         'camera'
         ])
except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)

print('OPTIONS   :', options)

for opt, arg in options:
    if opt in ('-i', '--image'):
        image_path= arg
    elif opt in ('-v', '--video'):
        video_path= arg
    elif opt in ('-c', '--camera'):
        video_path= 'camera'
        
print('IMAGE_PATH   :', image_path)
print('VIDEO_PATH   :', video_path)
print('REMAINING :', remainder)

if(image_path != ''):
    detect_image(image_path)

if(video_path != ''):
    detect_video(video_path)