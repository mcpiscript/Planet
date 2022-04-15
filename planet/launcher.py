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
import subprocess
import os


def get_features_list(path_: str) -> list:
    features = subprocess.run(
        [path_, "--print-available-feature-flags"], stdout=subprocess.PIPE
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


def get_features_dict(path_: str) -> dict:
    features = subprocess.run(
        [path_, "--print-available-feature-flags"], stdout=subprocess.PIPE
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


def run(env, path_: str):
    return subprocess.Popen([path_], env=env, preexec_fn=os.setsid)
