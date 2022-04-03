#!/bin/bash

rm -r planet/__pycache__

mkdir build
mkdir build/planet
mkdir build/planet/usr
mkdir build/planet/usr/lib

cp -r ./planet/ ./build/planet/usr/lib/planet-launcher

mkdir build/planet/DEBIAN
cp ./scripts/package/deb/control ./build/planet/DEBIAN/control
cp ./scripts/package/deb/postinst ./build/planet/DEBIAN/postinst
cp ./scripts/package/deb/postrm ./build/planet/DEBIAN/postrm
wget https://github.com/MCPI-Revival/MCPIedit/raw/master/pi-nbt.c -O ./build/planet/usr/lib/planet-launcher/pi-nbt.c -q

dpkg-deb --build ./build/planet
mkdir dist
cp ./build/planet.deb ./dist/planet.deb
rm -r build
