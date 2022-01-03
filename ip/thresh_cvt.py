import cv2

def thresh_cvt(img,res=None):
    num,_,stats,_ = cv2.connectedComponentsWithStats(img, connectivity=4, ltype=None)
    stats_cvt = stats[1:,:]
    start = []
    end = []
    img_list = []
    title_list = []
    
    for i in range(0,num-1):
        start.append([stats_cvt[i][1],stats_cvt[i][0]])
        end.append([stats_cvt[i][1]+stats_cvt[i][3]+1,stats_cvt[i][0]+stats_cvt[i][2]+1])
        
    for i in range(num-1):
        img_list.append(img[start[i][0]:end[i][0],start[i][1]:end[i][1]])
        title_list.append('area_%i'%i)
        
    return start,end,img_list,title_list,num
        
    