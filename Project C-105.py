import os
import cv2

path = "C:/Users/Dell/Desktop/C-104/Project C-105/Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif','.webp']:
        file_name = path+"/"+file
        images.append(file_name)
        
count = len(images)
print(count)
frame = cv2.imread(images[0])
height, width, channels = frame.shape
print(height, width)
out = cv2.VideoWriter("friends.mp4",cv2.VideoWriter_fourcc(*'DIVX'), 0.8, (width, height))

for i in range(0, count-1, 1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print("Done !")