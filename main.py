#!/bin/env python
# -*- coding:utf-8 -*-
# -------------------------------
import pygame
import cv
 
pygame.init()
size = width, height = 640, 480
speed = [1, 1]  
black = 0, 0, 0 
   
pygame.display.set_caption('cncore.com')
screen = pygame.display.set_mode(size)
 
cam = cv.CreateCameraCapture(0)
cv.SetCaptureProperty(cam,cv.CV_CAP_PROP_FRAME_WIDTH, 640)
cv.SetCaptureProperty(cam,cv.CV_CAP_PROP_FRAME_HEIGHT, 480);
 
while 1:
    try:
        cv.GrabFrame(cam)
        img = cv.RetrieveFrame(cam)
        cv.SaveImage('/tmp/test.jpg', img)
    except:
        pass
    cv.WaitKey(1500)
    image = pygame.image.load('/tmp/test.jpg')
    screen.blit(image, speed)
    pygame.display.flip()
