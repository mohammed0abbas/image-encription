# import required libraries
import cv2
import matplotlib.pyplot as plt
from PIL import Image

def histogram(img1, img2):

  
    


    # Calculate the histograms, and normalize them
    hist_img1 = cv2.calcHist([img1], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist_img1, hist_img1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
    hist_img2 = cv2.calcHist([img2], [0, 1, 2], None, [256, 256, 256], [0, 256, 0, 256, 0, 256])
    cv2.normalize(hist_img2, hist_img2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

    # Find the metric value
    metric_val = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
    print("Metric Value:", metric_val)

    # plot the histograms of two images
    plt.subplot(121), plt.hist(img1.ravel(),256,[0,256]),
    plt.title('horizon.jpg')
    plt.subplot(122), plt.hist(img2.ravel(),256,[0,256]),
    plt.title('coins.jpg')
    plt.show()