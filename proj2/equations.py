import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from math import log10, sqrt
import cv2


def calculate_snr(image):
    # Load the image
    img = np.array(image)

    # Calculate the signal power as the average pixel value
    signal_power = np.mean(img)

    # Calculate the noise power as the standard deviation of the pixel values
    noise_power = np.std(img)

    # Calculate the SNR in decibels (dB)
    snr = 10 * np.log10(signal_power / noise_power)

    return snr



def calculate_msc(image):
    # Load the image
    img = np.array(image)

    # Calculate the mean pixel value
    mean = np.mean(img)

    # Calculate the difference between the pixel values and the mean
    diff = img - mean

    # Calculate the mean square contrast (MSC)
    msc = np.mean(diff*diff)

    return msc



def calculate_psnr(img1_path, image):
   
    # Load the images
    img1 = np.array(Image.open(img1_path))
    img2 = np.array(image)
  

    mse = np.mean((img1 - img2) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
  



def calculate_similarity(img1_path, image):
    # Load the images
    img1 = np.array(Image.open(img1_path))
    img2 = np.array(image)

    # Calculate the SSIM between the images
    similarity = ssim(img1, img2, multichannel=True)

    return similarity