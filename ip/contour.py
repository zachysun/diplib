import cv2
from .thresh import *
import numpy as np

def contour(img,colour=(0,255,0),linewidth=1):
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    init = np.mean(img_gray)
    thresh = iter_thresh(img_gray,init)
    re,th = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)
    #直接寻找轮廓
    contours, hierarchy = cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    img_copy = img.copy()
    #绘制轮廓
    cv2.drawContours(img_copy,contours,-1,colour,linewidth)
    return img_copy