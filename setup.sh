#!/bin/sh

cat ./mararigidity.desktop | sed "s|THEPATH|$(pwd)|g" > $HOME/.applications/mararigidity.desktop


