# MCPIL texturepack code
# Coded by NikZapp for the MCPIL project by Alvarito050506
# This program is sadly not protected in any way.
import os
import shutil
import zipfile
from pathlib import Path


def loadTextures(filename):
    print("Loading the following textures into the game files:")
    global foundInTexturepack
    zipObj = zipfile.ZipFile(filename, "r")
    zipObj.extractall()
    for i in foundInTexturepack:
        # i = i[:-2]
        print(i[:-2])
        tempFiles = zipObj.namelist()
        for t in tempFiles:
            if t == i[-int(i[-2:]) - 2 : -2]:
                if True:
                    Path(t).rename(i[:-2])
                    print("from", t)
                    print("to  ", i[:-2])

                    # print('Permission error. Run this in a terminal using sudo.')
    zipObj.close()
    for t in tempFiles:
        try:
            Path(t).unlink()
        except:
            pass  # print('Permission error. Run this in a terminal using sudo.')


print(
    """
Input texturepack file path (.zip)
Leave blank to recover textures:"""
)
filePath = input()
if filePath == "":
    filePath = "recoveryPack.zip"
    archive = zipfile.ZipFile("recoveryPack.zip", "r")
    print("Recovering textures to an old state")
else:
    try:
        archive = zipfile.ZipFile(filePath, "r")
    except:
        print("Error while accessing texturepack file")

texturePaths = [
    "~/.minecraft-pi/overrides/images/armor/chain_1.png11",
    "~/.minecraft-pi/overrides/images/armor/chain_2.png11",
    "~/.minecraft-pi/overrides/images/armor/cloth_1.png11",
    "~/.minecraft-pi/overrides/images/armor/cloth_2.png11",
    "~/.minecraft-pi/overrides/images/armor/diamond_1.png13",
    "~/.minecraft-pi/overrides/images/armor/diamond_2.png13",
    "~/.minecraft-pi/overrides/images/armor/gold_1.png10",
    "~/.minecraft-pi/overrides/images/armor/gold_2.png10",
    "~/.minecraft-pi/overrides/images/armor/iron_1.png10",
    "~/.minecraft-pi/overrides/images/armor/iron_2.png10",
    "~/.minecraft-pi/overrides/images/art/kz.png06",
    "~/.minecraft-pi/overrides/images/environment/clouds.png10",
    "~/.minecraft-pi/overrides/images/font/default8.png12",
    "~/.minecraft-pi/overrides/images/gui/background.png14",
    "~/.minecraft-pi/overrides/images/gui/bg32.png08",
    "~/.minecraft-pi/overrides/images/gui/cursor.png10",
    "~/.minecraft-pi/overrides/images/gui/default_world.png17",
    "~/.minecraft-pi/overrides/images/gui/gui.png07",
    "~/.minecraft-pi/overrides/images/gui/gui2.png08",
    "~/.minecraft-pi/overrides/images/gui/gui_blocks.png14",
    "~/.minecraft-pi/overrides/images/gui/icons.png09",
    "~/.minecraft-pi/overrides/images/gui/itemframe.png13",
    "~/.minecraft-pi/overrides/images/gui/items.png09",
    "~/.minecraft-pi/overrides/images/gui/pi_title.png12",
    "~/.minecraft-pi/overrides/images/gui/spritesheet.png15",
    "~/.minecraft-pi/overrides/images/gui/title.png09",
    "~/.minecraft-pi/overrides/images/gui/touchgui.png12",
    "~/.minecraft-pi/overrides/images/gui/badge/minecon140.png14",
    "~/.minecraft-pi/overrides/images/gui/logo/raknet_high_72.png18",
    "~/.minecraft-pi/overrides/images/gui/logo/raknet_low_18.png17",
    "~/.minecraft-pi/overrides/images/item/arrows.png10",
    "~/.minecraft-pi/overrides/images/item/camera.png10",
    "~/.minecraft-pi/overrides/images/item/sign.png08",
    "~/.minecraft-pi/overrides/images/mob/char.png08",
    "~/.minecraft-pi/overrides/images/mob/chicken.png11",
    "~/.minecraft-pi/overrides/images/mob/cow.png07",
    "~/.minecraft-pi/overrides/images/mob/creeper.png11",
    "~/.minecraft-pi/overrides/images/mob/pig.png07",
    "~/.minecraft-pi/overrides/images/mob/pigzombie.png13",
    "~/.minecraft-pi/overrides/images/mob/sheep.png09",
    "~/.minecraft-pi/overrides/images/mob/sheep_fur.png13",
    "~/.minecraft-pi/overrides/images/mob/skeleton.png12",
    "~/.minecraft-pi/overrides/images/mob/spider.png10",
    "~/.minecraft-pi/overrides/images/mob/zombie.png10",
    "~/.minecraft-pi/overrides/images/particles.png13",
    "~/.minecraft-pi/overrides/images/terrain.png11",
]

foundInSystem = []
notFoundInSystem = []
foundInTexturepack = []
notFoundInTexturepack = []

for fn in texturePaths:
    if Path(fn[:-2]).is_file():
        foundInSystem.append(fn)
    else:
        notFoundInSystem.append(fn)

    try:
        imgdata = archive.read(fn[-int(fn[-2:]) - 2 : -2])
        print("Found", fn[-int(fn[-2:]) - 2 : -2], "in tp")
        foundInTexturepack.append(fn)
    except:
        notFoundInTexturepack.append(fn)

print("MCPI Texture check:", str(len(foundInSystem)), "out of", str(len(texturePaths)))
if len(foundInSystem) < len(texturePaths):
    print("The following textures were not found:")
    for i in notFoundInSystem:
        print(i[-int(i[-2:]) - 2 : -2])
loadTextures(filePath)
