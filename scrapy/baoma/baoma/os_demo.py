import os



print(os.path.join(os.path.dirname(os.path.dirname(__file__)),'images'))

images_path =  os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
if not os.path.exists(images_path):

    os.mkdir(images_path)
else:
    print("images文件夹存在")