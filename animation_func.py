import cv2
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def grab_frame():
    image = io.imread("http://[ip-address]/cam_pic.php")
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    faces = detect(image_gray)
    return faces_draw(image, faces)


# create axes
ax1 = plt.subplot(111)

# create axes
im1 = ax1.imshow(grab_frame())


def update(i):
    im1.set_data(grab_frame())


ani = FuncAnimation(plt.gcf(), update, interval=200)
plt.show()
