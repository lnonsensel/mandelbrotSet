import numpy as np
import cv2
from tqdm import tqdm

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    mset = np.zeros((height, width, 3), np.uint8)
    for i in range(height):
        for j in range(width):
            c = complex(x[j], y[i])
            value = mandelbrot(c, max_iter)
            mset[i][j][0], mset[i][j][1], mset[i][j][2] = value, value, value
    return mset

x = 0.3001301496
y = -0.025500022629245
def generate_xmin_xmax(x, y, counter):
    mas = []
    xmin, xmax, ymin, ymax = -2., 1., -1.5, 1.5
    xminmas = np.linspace(xmin, x, counter)
    xmaxmas = np.linspace(xmax, x, counter)
    yminmas = np.linspace(ymin, y, counter)
    ymaxmas = np.linspace(ymax, y, counter)
    for x1,x2,y1,y2 in zip(xminmas, xmaxmas, yminmas, ymaxmas):
        mas.append([x1,x2,y1,y2])
    return mas

xmin, xmax, ymin, ymax = -2., 1., -1.5, 1.5
frames = 10000
minmaxmas = generate_xmin_xmax(x,y,frames)
width, height = 500, 500
max_iter = 250

# size = width, height
# video = []

# fps = 25
# duration = frames // fps
# out = cv2.VideoWriter('./output1.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (size[1], size[0]), True)
# for xmin, xmax, ymin, ymax in tqdm(minmaxmas):
#     image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)
#     video.append(image)
#     out.write(image)

# out.release()

xmin, xmax, ymin, ymax = minmaxmas[-2]
image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

cv2.imshow('Mandelbrot',image)
cv2.waitKey(0)
cv2.destroyAllWindows()