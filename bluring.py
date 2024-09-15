import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#bluring (decrease the noise and decrease the sharpness)
img=cv2.imread("nyc.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Original Image")
plt.show()

#mean blur
blur_img=cv2.blur(img,ksize=(5,5))
plt.figure()
plt.imshow(blur_img)
plt.axis("off")
plt.title("Mean Blur")
plt.show()

#gaussian blur
gaussian_img=cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7)
plt.figure()
plt.imshow(gaussian_img)
plt.axis("off")
plt.title("Gaussian Blur")
plt.show()

#median blur
median_img=cv2.medianBlur(img,ksize=3)
plt.figure()
plt.imshow(median_img)
plt.axis("off")
plt.title("Median Blur")
plt.show()

def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    return noisy

#adding gaussian noise
img_normal=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255
noisy_img=gaussianNoise(img_normal)
plt.figure()
plt.imshow(noisy_img)
plt.axis("off")
plt.title("Noisy Image")
plt.show()

#applying gaussian blur to noisy image
gaussian_noisy_img=cv2.GaussianBlur(noisy_img,ksize=(3,3),sigmaX=7)
plt.figure()
plt.imshow(gaussian_noisy_img)
plt.axis("off")
plt.title("Noisy Image Blurred")
plt.show()




def saltAndPepperNoise(image, prob):
    output = np.copy(image)
    # Randomly select pixels for salt noise
    num_salt = np.ceil(prob * image.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]

    # Ensure coordinates are within bounds
    coords = tuple(np.clip(c, 0, dim_size - 1) for c, dim_size in zip(coords, image.shape))

    output[coords] = 1

    # Randomly select pixels for pepper noise
    num_pepper = np.ceil(prob * image.size * 0.5)
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]

    # Ensure coordinates are within bounds
    coords = tuple(np.clip(c, 0, dim_size - 1) for c, dim_size in zip(coords, image.shape))

    output[coords] = 0
    return output


# Apply salt and pepper noise
spImage = saltAndPepperNoise(img, 0.05)

# Display or save the noisy image
cv2.imshow('Noisy Image', spImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

spImage =saltAndPepperNoise(img,0.05)
plt.figure()
plt.imshow(spImage)
plt.axis("off")
plt.title("Salt and Pepper Image")
plt.show()
