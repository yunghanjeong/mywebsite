# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 15:10:56 2021

@author: Yung Han Jeong Gtihub.com/yunghanjoeng

This code is to build a personal website based on Python Flask Library
"""
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home(): # home page
    return render_template("index.html", content="Testing")

@app.route("/about/")
def about(): # home page
    return redirect(url_for("about")) #render_template("base.html", content="Testing")

# @app.route("/<name>")
# def user(name): # home page
#     return f"hello {name}"

# @app.route("/admin/")
# def admin(): # home page
#     return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()