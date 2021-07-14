import numpy as np
import matplotlib.pyplot as plt

width = 300
height = 200

camera = np.array([0,0,1])

def normalize(vector):
    return vector/np.linalg.norm(vector)

ratio = float(width)/height

screen = [-1, 1/ratio, 1, -1/ratio]

image = np.zeros((height, width, 3))

for i, x in enumerate(np.linspace(screen[0], screen[2], width)):
    for j, y in enumerate(np.linspace(screen[1], screen[3], height)):
        pixel = np.array([i/width, j/height, 0])
        image[j, i] = pixel
    print(f"{i}/{width}")

plt.imsave("image.png", image)