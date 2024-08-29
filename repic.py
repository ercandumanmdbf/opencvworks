#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:11:55 2024

@author: ercanduman
"""

import cv2

#import funct of a pic on img object

img=cv2.imread("kule.jpg")
print ("press 'q' to quit")
while(1):
    cv2.imshow("photo maiden tower",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cv2.destroyAllWindows()

