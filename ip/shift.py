from .thresh import *
import cv2

def shift(img,s_type,angle=45,size=2,direct='lr'):
    if (s_type == 'rotate'):
        height = img.shape[0]
        width = img.shape[1]
        pad = np.sqrt((height/2)**2+(width/2)**2)
        img_pad = cv2.copyMakeBorder(img
                              ,int(1.1*(pad-height/2))
                              ,int(1.1*(pad-height/2))
                              ,int(1.1*(pad-width/2))
                              ,int(1.1*(pad-width/2))
                              ,cv2.BORDER_CONSTANT
                              ,value=[0])
        m = img_pad.shape[0]
        n = img_pad.shape[1]
        
        matRotate = cv2.getRotationMatrix2D((n*0.5, m*0.5), 
                                             angle, 1) 
        img_rot = cv2.warpAffine(img_pad, matRotate, (n, m))
        _,img_rot = thresh(img_rot,'iter')
        
        return img_rot
    
    if (s_type == 'scale'):
        height = img.shape[0]
        width = img.shape[1]
        img_sca = cv2.resize(img, (int(size*width),
                               int(size*height)))
        _,img_sca = thresh(img_sca,'iter')
        return img_sca
                             
    if (s_type == 'mirror'):
        height = img.shape[0]
        width = img.shape[1]
        if(direct == 'ud'):
            img_mir = np.zeros([height,width], np.uint8)
            for i in range(height):
                for j in range(width):
                    img_mir[height-i-1,j] = img[i,j]
            return img_mir
        if(direct == 'lr'):
            img_mir = np.zeros([height,width], np.uint8)
            for i in range(height):
                for j in range(width):
                    img_mir[i,width-j-1] = img[i,j]
            return img_mir