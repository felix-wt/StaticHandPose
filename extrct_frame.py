import numpy as np
import cv2
import os


import tensorflow as tf

#
# vid = cv2.VideoCapture('handpose_light.mp4')
# currentPath = 'n/'
# # Check if the video
#
#
# print('>> loading frozen model..')
# detection_graph, sess = detector_utils.load_inference_graph()
# sess = tf.Session(graph=detection_graph)
# print('>> model loaded!')
#
# _iter = 1
# # Read until video is completed
# while (vid.isOpened()):
#     # Capture frame-by-frame
#     ret, frame = vid.read()
#     if ret:
#         print('   Processing frame: ' + str(_iter))
#         # Resize and convert to RGB for NN to work with
#         frame = cv2.resize(frame, (320, 180), interpolation=cv2.INTER_AREA)
#
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#         # Detect object
#         boxes, scores = detector_utils.detect_objects(frame, detection_graph, sess)
#
#         # get region of interest
#         res = detector_utils.get_box_image(1, 0.2, scores, boxes, 320, 180, frame)
#
#         # Save cropped image
#         if (res is not None):
#             cv2.imwrite(currentPath  + str(_iter) + '.png', cv2.cvtColor(res, cv2.COLOR_RGB2BGR))
#
#         _iter += 1
#     # Break the loop
#     else:
#         break
files = os.listdir('./')
# for file in files:
#     print(file)
#     if (file.endswith(".png")):
#         path = './'  + file
#         # Read image
#         im = cv2.imread('100 - 副本 (2).png')
#         print(im)
#         height, width, channels = im.shape
#         if not height == width == 28:
#             # Resize image
#             im = cv2.resize(im, (28, 28), interpolation=cv2.INTER_AREA)
#             # Write image
#             cv2.imwrite(path, im)

path = "Poses/slide/slide_3"    # 目标路径

"""os.listdir(path) 操作效果为 返回指定路径(path)文件夹中所有文件名"""
filename_list = os.listdir(path)  # 扫描目标路径的文件,将文件名存入列表

a = 0
j = 0
for i in filename_list:
    j = j + 1
    used_name = path + '\\'+filename_list[a]
    new_name = path  + '\\' + 'slide_3_'+ str(j) + '.png'
    os.rename(used_name,new_name)
    print("文件%s重命名成功,新的文件名为%s" %(used_name,new_name))
    a += 1