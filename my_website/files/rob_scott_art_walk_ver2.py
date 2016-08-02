import matplotlib.pyplot as plt
import os.path
import numpy as np
import PIL
import PIL.ImageDraw

#Open Jack Nicholson's picture in numpy
directory = os.path.dirname(os.path.abspath(__file__))  
filepath_jack = os.path.join(directory, 'jack_nicholson.jpg')
jack_nicholson_numpy = plt.imread(filepath_jack)

#Open Rob in numpy
filepath_rob = os.path.join(directory, 'rob.JPG')
rob_numpy = plt.imread(filepath_rob)

# Open Scott's picture in numpy.
filepath_scott = os.path.join(directory, 'scottlockhart.JPG')
scott_numpy = plt.imread(filepath_scott)

# Opens the grill in numpy.
filepath_teeth = os.path.join(directory, 'diamond_tooth_grill.jpg')
grill_numpy = plt.imread(filepath_teeth)

# Converts Rob's, Scott's, and Jack's numpy picture to PIL
rob_image_pil = PIL.Image.fromarray(rob_numpy)
scott_image_pil = PIL.Image.fromarray(scott_numpy)
jack_image_pil = PIL.Image.fromarray(jack_nicholson_numpy)
teeth_image_pil = PIL.Image.fromarray(grill_numpy)

# Cuts out all the extra stuff on Rob's and Scott's picture.
rob_crop = rob_image_pil.crop( (5, 4, 84, 123) )
scott_crop = scott_image_pil.crop( (5, 4, 84, 123) )

# Makes sure images of Rob and Scott are small enough to paste on Jack's picture
rob_img_small = rob_crop.resize((348,646))
scott_img_small = scott_crop.resize((348,646))
teeth_resize = teeth_image_pil.resize((1240-884,701-568))

# Places Rob's and Scott's picture on either side of Jack
jack_image_pil.paste(rob_img_small,(1478,164))
jack_image_pil.paste(scott_img_small,(192,164))

# Places a grill on Jack.
jack_image_pil.paste(teeth_resize,(884,568))

jack_numpy = np.array(jack_image_pil)

# Makes the picture grayscale
#gray_jack_pil = jack_image_pil.convert('LA')

# Converts Jack's picture back to numpy.
#gray_jack_numpy = np.array(gray_jack_pil)

# Makes Jack's eyes red
for r in range(308,354):
    for c in range(812,968):
        if sum(jack_numpy[r][c])>400:
            jack_numpy[r][c] = [255,0,0]
for r in range(290,351):
    for c in range(1133,1255):
        if sum(jack_numpy[r][c])>450:
            jack_numpy[r][c] = [255,0,0]

fig, ax = plt.subplots(1, 1)
ax.imshow(jack_numpy, interpolation='none')
fig.show()