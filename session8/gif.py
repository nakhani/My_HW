import os
import imageio
#import numpy as np

file_list = sorted(os.listdir("session8/images"))


images = []
 
for file_name in file_list:
    file_path = "session8/images/" + file_name
    image = imageio.imread(file_path)
    #image = np.resize(image,(280,240))
    images.append(image) 



imageio.mimsave("session8/out_put.gif", images)