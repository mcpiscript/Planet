import subprocess
import os


def get_features_list() -> list:
    features = subprocess.run(
        ["minecraft-pi-reborn-client", "--print-available-feature-flags"],
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8")
    features = features.split("\n")
    returnlist = list()
    for feature in features:
        if feature.startswith("TRUE"):
            feature = feature[5:]
        if feature.startswith("FALSE"):
            feature = feature[6:]
        returnlist.append(feature)

    return returnlist


def get_features_dict() -> dict:
    features = subprocess.run(
        ["minecraft-pi-reborn-client", "--print-available-feature-flags"],
        stdout=subprocess.PIPE,
    ).stdout.decode("utf-8")
    features = features.split("\n")
    returndict = dict()
    for feature in features:
        if feature.startswith("TRUE"):
            feature = feature[5:]
            returndict[feature] = True
        if feature.startswith("FALSE"):
            feature = feature[6:]
            returndict[feature] = False
    return returndict


def set_username(env, username: str = "StevePi"):
    env["MCPI_USERNAME"] = username
    return env


def set_render_distance(env, distance: str = "SHORT"):
    if distance.upper() not in ["TINY", "SHORT", "NORMAL", "FAR"]:
        raise Exception("Invalid render distance")
    else:
        env["MCPI_RENDER_DISTANCE"] = distance
        return env


def set_hud(env, options: str = "fps,simple"):
    env["GALLIUM_HUD"] = options
    return env


def set_options(env, options: dict):
    output = str()
    for option in options:
        if options[option]:
            output += f"{option}|"

    env["MCPI_FEATURE_FLAGS"] = output
    return env


def run(env):
    return subprocess.Popen(
        ["/usr/bin/minecraft-pi-reborn-client"], env=env, preexec_fn=os.setsid
    ).wait()
