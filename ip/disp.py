import matplotlib.pyplot as plt

def disp(img_list,title_list,size,figsize=(16,8)
         ,method='gray'
         ,path=None):
    fig = plt.figure(figsize=figsize)
    m = size[0]
    n = size[1]
    N = len(img_list)
    for i in range(1,N+1):
        plt.subplot(m,n,i)
        plt.imshow(img_list[i-1],method)
        plt.title(title_list[i-1],fontsize=8)
    if (path != None):
        plt.savefig(path)
    plt.show()   