#!/usr/bin/python3
# -*- coding: utf-8 -*- 
print("content-type:text/html; charset=UTF-8\n")
print("hi<br>")

import cgi
import sys
form = cgi.FieldStorage()
writer = form["writer"].value
title = form["title"].value
maintxt = form["maintxt"].value

print("writer:", writer, "<br>")
print("title:", title, "<br>")
print("maintxt:", maintxt, "<br>")
sys.stdout = open('1.txt', w)
file.write("writer:", writer, "<br>")
file.write("title:", title, "<br>")
file.write("maintxt:", maintxt, "<br>")
file.close()
print("saved")