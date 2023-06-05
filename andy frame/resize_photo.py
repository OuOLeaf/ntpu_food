#%%
from skimage.transform import resize
import matplotlib.image as mpimg
from glob import glob
#%%
for path in glob('foods/*'):
    photo = mpimg.imread(path)
    resized_pht = resize(photo, (400, 400))
    name = path.split('\\')[1][:-4]
    mpimg.imsave(f"resize_foods/{name}.jpg", resized_pht)
# %%
path.split('\\')