#!/usr/bin/python
#-*- coding: utf8 -*-

print("content-type: text/html")
print("")
f = open("status.txt", "r")
arquivo=f.read()
f.close
print(arquivo)
