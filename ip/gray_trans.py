import numpy as np
import cv2


def gray_trans(img,g_type,line_para=None,ln_para=None,e_para=None):
    
    img_copy = img.copy()

    if (g_type == 'linear'):
        a = img.min()
        b = img.max()
        c = line_para[0]
        d = line_para[1]
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                img_copy[i,j] = ((d-c)/(b-a))*(img[i,j]-a)+c
        return img_copy
    
    elif (g_type == 'ln'):
        p = ln_para[0]
        q = ln_para[1]
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                img_copy[i,j] = p+q*(np.log(img[i,j]+1.0))
        return img_copy
        
    elif (g_type == 'e'):
        img = np.float32(img)/255.0
        
        a = e_para[0]
        b = e_para[1]
        c = e_para[2]
        img_copy = np.uint8(255*(b**(c*(img-a))-1))
        return img_copy