
from PIL import Image

POSITIONS = {
    "grass_top" : (0, 0, 16, 16), 
    "stone": (16, 0, 32, 16), 
    "dirt": (32, 0, 48, 16),
    "grass_side_carried": (48, 0, 64, 16), 
    "planks_oak": (64,  0,  80,  16), 
    "stone_slab_side" : (80,  0,  96,  16), 
    "stone_slab_top":(96,  0,  112,  16), 
    "brick":(112,  0,  128,  16), 
    "tnt_side":(128,  0,  144,  16), 
    "tnt_top":(144,  0,  160,  16), 
    "tnt_bottom":(160,  0,  176,  16), 
    "web": (176,  0,  192,  16), 
    "flower_rose":(192,  0,  208,  16), 
    "flower_dandelion":(208,  0,  224,  16), 
    "sapling_oak": (240,  0,  256,  16), 
    "cobblestone": (0,  16,  16,  32), 
    "bedrock": (16,  16,  32,  32), 
    "sand":(32, 16,  48,  32), # I love these blocks
    "gravel":(48, 16,  64,  32), 
    "log_oak":(64, 16,  80, 32), 
    "log_oak_top":(80,  16,  96,  32), 
    


}

if __name__ == "__main__":
    with Image.open("/home/leha2/.minecraft-pi/overrides/images/terrain.png") as img:
        region=img.crop(POSITIONS["gravel"])
        region.show()
