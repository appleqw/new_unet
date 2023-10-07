import torch

from net import *
import os
from data import *

net=UNet().cuda()

weights='params/unet.path'
if os.path.exists(weights):
    net.load_state_dict(torch.load(weights))
    print('successfully')
else:
    print('no loading')

_input=input('please input image path:')
img=keep_image_size_open(_input)
img_date=transform(img)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
img_date = img_date.to(device)
img_date = img_date.unsqueeze(0)

out=net(img_date)
print(out)

