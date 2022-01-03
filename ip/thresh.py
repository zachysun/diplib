import cv2 
import numpy as np

def iter_thresh(img,init,maxiter=30,thr=1):    
    
    T0 = img[img < init].mean()
    T1 = img[img >= init].mean()
    T  = (T0 + T1) / 2
    if abs(T - init) < thr or maxiter == 0:
        return T
    return iter_thresh(img, T, maxiter - 1)

def thresh(img,method,size=15,C=1):
    if len(img.shape) == 3:                      #灰度图转化
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if (method == 'OTSU'):                       # OTSU阈值分割
        re1,th1 = cv2.threshold(img,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return re1,th1
    elif (method == 'iter'):                    # 迭代阈值分割
        init = np.mean(img)
        thresh = iter_thresh(img,init)
        re2,th2 = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
        return re2,th2
    elif (method == 'adapt'):                   # 动态阈值分割
        th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=size,C=C)
        return th3
        