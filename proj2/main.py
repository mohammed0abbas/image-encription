import numpy as np ##import numpy library
import matplotlib.pyplot as plt ##import matplotlib library



# Load the input image    imread = image read
x = input("Enter the name of the image file: ")
image = plt.imread(x)



# Define the Henon map
def henon_map(x, y, a, b):
  x_new = 1 - a * x**2 + y
  y_new = b * x
  return x_new, y_new

# Define the skew tent map
def skew_tent_map(x, r):
  return r * abs(x)

  
# Define the bernulli map
def bernulli_map(x):
    if x < 0.5:
        return x*2
    else:
        return 2 * (1-x)
 





transformed_image = np.copy(image)

## image.shape[0] = width of image
## image.shape[1] = height of image

width = image.shape[0]
height = image.shape[1]

for i in range(width):
  for j in range(height):
    ## pixel = {r,g,b}
    ## red
    transformed_image[i, j, 0] , y = henon_map(image[i, j, 0], 0.0, 3.4, 0.6)
    ## green
    transformed_image[i, j, 1] = skew_tent_map(image[i, j, 1], 5.0)
    ## blue 
    transformed_image[i, j, 2] = skew_tent_map(bernulli_map(image[i, j, 2]),5.5)




# Display the original and transformed images

plt.imshow(image)
plt.show()


plt.imshow(transformed_image)
plt.show()
