from .thresh import *
import cv2
import numpy as np

def obj_count(img):      #分水岭算法
    img = cv2.blur(img,(3,3))
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    init = np.mean(img_gray)
    
    thresh = iter_thresh(img_gray,init)
    _,thr = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)
    
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thr, cv2.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5) 
    ret, sure_fg = cv2.threshold(dist_transform, 0.25 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknow = cv2.subtract(sure_bg, sure_fg)
    
    _, markers = cv2.connectedComponents(sure_fg,connectivity=8) 
    markers = markers + 1   
    markers[unknow==255] = 0  
    markers = cv2.watershed(img, markers)
    img_copy = img.copy()
    img_copy[markers == -1] = [0, 0, 255]
    n = len(np.unique(markers))-2
    return n,img_copy