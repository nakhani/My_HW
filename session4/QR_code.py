

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

# name_user = input("please enter your name:\n")
# num_user = input("please enter your number phone:\n")

qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)

qr.add_data("najmeh")

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask(back_color=(42,42,42), center_color=(247,239,137), edge_color=(210,172,71)))
# img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="H:/python_class/My_HW/user_image.png")
# qr.make(fit = True)
# img = qr.make_image(fill_color = 'gold')
img_2.save("user_qrcode.png")


