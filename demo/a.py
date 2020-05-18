import cv2

cap = cv2.VideoCapture('demo.avi')
flag,frame = cap.read()
i = 0
print(frame)
while flag:
    cv2.imwrite('pic/'+'frame_'+str(i),frame)
    flag, frame = cap.read()
    i = i + 1