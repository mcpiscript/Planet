#!/usr/bin/env python3
"""

Copyright (C) 2022  Alexey Pavlov

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""


import click

INDEX = [
    # Armor
    "armor/chain_1.png",
    "armor/chain_2.png",
    "armor/cloth_1.png",
    "armor/cloth_2.png",
    "armor/diamond_1.png",
    "armor/diamond_2.png",
    "armor/gold_1.png",
    "armor/gold_2.png",
    "armor/iron_1.png",
    "armor/iron_2.png",
    # Miscelannous
    "art/kz.png",
    "environment/clouds.png",
    # Font and GUI
    "font/default8.png",
    "gui/background.png",
    "gui/bg32.png",
    "gui/cursor.png",
    "gui/default_world.png",
    "gui/gui.png",
    "gui/gui2.png",
    "gui/gui_blocks.png",
    "gui/icons.png",
    "gui/itemframe.png",
    "gui/items.png",  # Items
    "gui/pi_title.png",
    "gui/spritesheet.png",
    "gui/title.png",
    "gui/touchgui.png",
    "gui/badge/minecon140.png",
    "gui/logo/raknet_high_72.png",
    "gui/logo/raknet_low_18.png",
    # Item entitites
    "item/arrows.png",
    "item/camera.png",
    "item/sign.png",
    # Mobs
    "mob/char.png",
    "mob/chicken.png",
    "mob/cow.png",
    "mob/creeper.png",
    "mob/pig.png",
    "mob/pigzombie.png",
    "mob/sheep.png",
    "mob/sheep_fur.png",
    "mob/skeleton.png",
    "mob/spider.png",
    "mob/zombie.png",
    # Misc entities
    "particles.png",
    # Blocks
    "terrain.png",
]

INDEX = [
    # Armor
    "chain_1.png",
    "chain_2.png",
    "cloth_1.png",
    "cloth_2.png",
    "diamond_1.png",
    "diamond_2.png",
    "gold_1.png",
    "gold_2.png",
    "iron_1.png",
    "iron_2.png",
    # Miscelannous
    "kz.png",
    "clouds.png",
    # Font and GUI
    "default8.png",
    "background.png",
    "bg32.png",
    "cursor.png",
    "default_world.png",
    "gui.png",
    "gui2.png",
    "gui_blocks.png",
    "icons.png",
    "itemframe.png",
    "items.png",  # Items
    "pi_title.png",
    "spritesheet.png",
    "title.png",
    "touchgui.png",
    "minecon140.png",
    "raknet_high_72.png",
    "raknet_low_18.png",
    # Item entitites
    "arrows.png",
    "camera.png",
    "sign.png",
    # Mobs
    "char.png",
    "chicken.png",
    "cow.png",
    "creeper.png",
    "pig.png",
    "pigzombie.png",
    "sheep.png",
    "sheep_fur.png",
    "skeleton.png",
    "spider.png",
    "zombie.png",
    # Misc entities
    "particles.png",
    # Blocks
    "terrain.png",
]

def install_pack():
    pass



@click.group()
def main():
    pass
    
@main.command(help="Install a texture pack")
@click.option("--file", "--zipfile",  "-f",  "texture_path",  help="Texture pack path.", type=click.Path(exists=True))
#@click.option("--mcpit",  is_flag=True, default=True)
def install(texture_path,  mcpit):
    if texture_path == None:
        click.echo("Please supply a path")
        return
    click.echo("Path is "+click.format_filename(texture_path))
    
if __name__ == "__main__":
    main()
