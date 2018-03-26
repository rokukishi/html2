#!/bin/bash
read -p "" var
echo "$var" > status.txt
var=$(cut -c5- status.txt)
systemctl status $var > status.txt
./status.py
