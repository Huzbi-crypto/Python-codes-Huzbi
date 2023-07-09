# Cursor Control by Vision

## Introduction

This is my very first project in Computer-Vision. It's a really simple program that uses the positions of your eyes to move 'n drag the mouse cursor and click (left-click) on things, such as links, etc.

### Details

These are libraries that made it possible:

  - Mediapipe,
  - PyAutoGUI,
  - Requests.

How it works is that it uses your right eye's 4 positions through the camera and takes one of them to move the mouse over the screen. The clicking functionality is achieved through the blink of your left eye. The blink is nothing but the difference between your left eye's center-top and center-bottom location. When you close your eyes, the y values between them change, and a difference is calculated. Lastly, it compares with a defined value and if it's true, the click happens thanks to PyAutoGUI.

### Instructions

How to make it run:

  1. Install all libraries mentioned above.
  2. Run the `main.py` file.

That's it. I hope you like this project. If there are any problems, pull it!

Date: 09/07/2023
Updated: 09/07/2023
