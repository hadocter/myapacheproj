#!/usr/bin/python3
print("content-type:text/html;charset=UTF-8\n")

from flask import Flask, render_template
import os

app=Flask(__name__)

app.route('/hi')
def hi():
    print("<h1>hi</h1>")
