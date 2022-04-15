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


@click.group()
def main():
    pass
    
@main.command()
@click.option("--path",  "-p",  "texture_path",  help="Texture pack path.")
@click.option("--mcpit",  is_flag=True)
def install(texture_path,  mcpit):
    click.echo("bruh")
    
if __name__ == "__main__":
    main()
