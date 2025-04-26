from PIL import Image

image_paths = [
    "files/images/dog1.png",
    "files/images/dog2.png",
    "files/images/dog3.png"
]

images = [Image.open(path) for path in image_paths]

images[0].save(
    "files/costumes.gif", 
    save_all=True, 
    append_images=images[1:], 
    duration=200, 
    loop=0
)