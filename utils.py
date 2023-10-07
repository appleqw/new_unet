from PIL import Image

def keep_image_size_open(path,size=(256,256)):
    img=Image.open(path)
    temp=max(img.size)
    mask=Image.new('RGB',(temp,temp),(0,0,0))   #新建一个mask，为原图的最大边长的正方形，
    mask.paste(img,(0,0))   #将原图粘贴上来，在左上角
    mask=mask.resize(size)
    return mask