#!/bin/bash

rm -r planet/__pycache__

mkdir build
mkdir build/planet
mkdir build/planet/usr
mkdir build/planet/usr/lib

cp -r ./planet/ ./build/planet/usr/lib/planet-launcher

mkdir build/planet/DEBIAN
cp ./scripts/control ./build/planet/DEBIAN/control
cp ./scripts/postinst ./build/planet/DEBIAN/postinst
cp ./scripts/postrm ./build/planet/DEBIAN/postrm

dpkg-deb --build ./build/planet
mkdir dist
cp ./build/planet.deb ./dist/planet.deb
rm -r build
