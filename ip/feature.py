import skimage as ski
import numpy as np

def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 

def feature(img,f_type):
    S = len(img[img == 255])
    
    props = ski.measure.regionprops_table(img,properties=('euler_number','perimeter','moments_hu'))
    
    L = props['perimeter']
    euler_number = props['euler_number']
    
    dict2 = {'moments_hu-0':props['moments_hu-0'],
             'moments_hu-1':props['moments_hu-1'],
             'moments_hu-2':props['moments_hu-2'],
             'moments_hu-3':props['moments_hu-3'],
             'moments_hu-4':props['moments_hu-4'],
             'moments_hu-5':props['moments_hu-5'],
             'moments_hu-6':props['moments_hu-6']}

    if (f_type == 'euler'):
        return euler_num
    if (f_type == 'area'):
        return S
    if (f_type == 'perimeter'):
        return L
    if (f_type == 'roundness'):
        return 4*S*np.pi/L**2
    if (f_type == 'complexity'):
        return L**2/S
    if (f_type == 'moments_hu'):
        return dict2
    if (f_type == 'all'):
        dict1 = {'euler':euler_number,
                'area':S,
                'perimeter':L,
                'roundness':4*S*np.pi/L**2,
                'complexity':L**2/S}
        return Merge(dict1,dict2)