

import qrcode

name_user = input("please enter your name:\n")
num_user = input("please enter your number phone:\n")

qr = qrcode.QRCode(version = 1,
                   box_size = 10,
                   border = 5)

qr.add_data(name_user + num_user)

qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
                    back_color = 'white')
img.save("user_qrcode.png")


