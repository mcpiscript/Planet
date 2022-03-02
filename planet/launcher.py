import os

FEATURES = [
    "Touch GUI",
    "Fix Bow & Arrow",
    "Fix Attacking",
    "Force Mob Spawning",
    "Fancy Graphics",
    "Disable Autojump By Default",
    "Display Nametags By Default",
    "Fix Sign Placement",
    "Show Block Outlines",
    "Expand Creative Inventory",
    "Remove Creative Mode Restrictions",
    "Peaceful Mode",
    "Animated Water",
    "Remove Invalid Item Background",
    'Disable "gui_blocks" Atlas',
    "Smooth Lighting",
    "3D Anaglyph",
    "Fix Camera Rendering",
    "Implement Chat",
    "Hide Chat Messages",
    "Implement Death Messages",
    "Implement Game-Mode Switching",
    "Allow Joining Survival Servers",
    "Miscellaneous Input Fixes",
    'Bind "Q" Key To Item Dropping',
    "Bind Common Toggleable Options To Function Keys",
    "Render Selected Item Text",
    "External Server Support",
    "Load Language Files",
    "Implement Sound Engine",
    "Close Current Screen On Death",
]

DEFAULT_FEATURES = {
    "Touch GUI": True,
    "Fix Bow & Arrow": True,
    "Fix Attacking": True,
    "Force Mob Spawning": False,
    "Fancy Graphics": True,
    "Disable Autojump By Default": True,
    "Display Nametags By Default": True,
    "Fix Sign Placement": True,
    "Show Block Outlines": True,
    "Expand Creative Inventory": True,
    "Remove Creative Mode Restrictions": True,
    "Peaceful Mode": False,
    "Animated Water": True,
    "Remove Invalid Item Background": True,
    'Disable "gui_blocks" Atlas': True,
    "Smooth Lighting": True,
    "3D Anaglyph": False,
    "Fix Camera Rendering": True,
    "Implement Chat": True,
    "Hide Chat Messages": False,
    "Implement Death Messages": True,
    "Implement Game-Mode Switching": True,
    "Allow Joining Survival Servers": True,
    "Miscellaneous Input Fixes": True,
    'Bind "Q" Key To Item Dropping': True,
    "Bind Common Toggleable Options To Function Keys": True,
    "Render Selected Item Text": True,
    "External Server Support": True,
    "Load Language Files": True,
    "Implement Sound Engine": True,
    "Close Current Screen On Death": True,
}


def set_username(username: str):
    os.environ["MCPI_USERNAME"] = username


def set_render_distance(distance: str):
    if distance.upper() not in ["TINY", "SHORT", "NORMAL", "FAR"]:
        raise Exception("Invalid render distance")
    else:
        os.environ["MCPI_RENDER_DISTANCE"] = distance.upper()


def set_hud(options: str):
    os.environ["GALLIUM_HUD"] = options


def set_options(options: dict = DEFAULT_FEATURES):
    output = str()
    for option in options:
        output += f"{str(options[option]).upper()} {option}\n"

    os.environ["MCPI_FEATURE_FLAGS"] = output
