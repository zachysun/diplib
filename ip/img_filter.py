import cv2
import numpy as np

def img_filter(img,type1=None,type2=None,type3='lp',
               D0=60,N=2,W=30,size=5):
    '''
    type1:'time'--时域滤波;'fre'--频域滤波
    type2:当'type1'的选择为'time'时，type2有
            'blur'--均值滤波;'median'--中值滤波;
          当'type1'的选择为'fre'时，type2有
            'ideal'--理想滤波器;
            'gauss'--高斯滤波器;
            'butter'--巴特沃斯滤波器
    type3:当选择频域滤波器时，type3有
            'lp'--低通;'hp'--高通;
            'bp'--带通;'bs'--带阻
    D0:截止频率
    W:带宽
    size:时域滤波器的模板大小
    '''
    if (type1 == 'time'):  
        if (type2 == 'blur'):
            img_mean = cv2.blur(img,(size,size))  #均值滤波
            return img_mean
        elif (type2 == 'median'):
            img_median = cv2.medianBlur(img,size)  #中值滤波
            return img_median
    elif (type1 == 'fre'):
        f=cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)  #图像快速傅里叶变换
        f_shift = np.fft.fftshift(f)  #中心化
        rows = img.shape[0] 
        cols = img.shape[1]
        crow,ccol = int(rows/2),int(cols/2)  #得到频谱中心坐标
        mask = np.zeros((rows,cols,2))  #全0矩阵
        for i in range(rows):
            for j in range(cols):
                D = np.sqrt((i-crow)**2+(j-ccol)**2) #计算距离
                if (type2 == 'ideal'):    #理想滤波器
                    if (type3 == 'lp'):
                        if(D<D0):
                            mask[i,j] = 1
                    elif (type3 == 'hp'):
                        if(D>D0):
                            mask[i,j] = 1
                    elif (type3 == 'bp'):
                        if(D > D0 and D < D0+W):
                            mask[i,j] = 1
                    elif (type3 == 'bs'):
                        if(D < D0 and D > D0+W):
                            mask[i,j] = 1
                elif (type2 == 'gauss'):   #高斯滤波器(N=2)
                    if (type3 == 'lp'):
                        mask[i, j] = np.exp(-(D/D0)**(2*N))
                    elif (type3 == 'hp'):
                        mask[i, j] = np.exp(-(D0/D)**(2*N))
                    elif (type3 == 'bp'):
                        mask[i, j] = np.exp(-((D**2 - D0**2)/D*W)**(2*N))
                    elif (type3 == 'bs'):
                        mask[i, j] = np.exp(-(D*W/(D**2 - D0**2))**(2*N))
                elif (type2 == 'butter'):   #巴特沃斯滤波器
                    if(type3 == 'lp'):
                        mask[i, j] = 1/(1+(D/D0)**(2*N))
                    elif(type3 == 'hp'):
                        mask[i, j] = 1/(1+(D0/D)**(2*N))
                    elif(type3 == 'bp'):
                        mask[i, j] = 1/(1+((D**2-D0**2)/D*W)**(2*N))
                    elif(type3 == 'bs'):
                        mask[i, j] = 1/(1+(D*W/(D**2-D0**2))**(2*N))
        
        f_mask = f_shift*mask
        f_imask=np.fft.ifftshift(f_mask) 
        
        img_fil=cv2.idft(f_imask) 
        img_fil=cv2.magnitude(img_fil[:,:,0],img_fil[:,:,1])
        img_fil=np.abs(img_fil)
        img_fil=(img_fil-np.amin(img_fil))/(np.amax(img_fil)-np.amin(img_fil))

        return img_fil                                