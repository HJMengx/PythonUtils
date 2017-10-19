# encoding:utf-8
"""
  封装相关的工具方法,方便使用
"""

import PIL.Image as pil
import numpy as np
import pickle as pke
import matplotlib.pyplot as pyplot

########################################################################
class MXUtils:
    """"""
    imagesPath = ""
    imageSize = []
    #----------------------------------------------------------------------
    def __init__(self,path,imageSize):
        """Constructor"""
        self.imagesPath = path
        self.imageSize = imageSize
    
    def imageToArray(self,imageNames):
        print("--------------------------------------")
        if (not type(imageNames) == type(np.array([]))) and (not isinstance(imageNames,list)):
            raise TypeError("the imageNames must to be np.array or list")
        # 得到总共的图片数
        image_count = len(imageNames)
        # 初始化结果数组
        result = np.array([])
        print("开始转化")
        size = self.imageSize[0] * self.imageSize[1]
        for index in range(0,image_count):
            # 打开文件
            image = pil.open(self.imagesPath + imageNames[index])
            print(image)
            # 分离像素值
            r,g,b = image.split()
            # 一定要reshpae(1024)使其变为一维数组，否则拼接的数据会出现错误，导致无法恢复图片,根据图片大小来
            arr_red = np.array(r).reshape(size)
            arr_green = np.array(g).reshape(size)
            arr_blue = np.array(b).reshape(size)
            #n行，一行3072列，为一张图片的rgb值
            image_arr = np.concatenate((arr_red, arr_green, arr_blue))
            result = np.concatenate((result, image_arr)) 
            print(result)
        # 将一维数组转化为count行3072列的二维数组
        result = result.reshape((image_count, 3072))  
        print("转为数组成功，开始保存到文件") 
        """file_path = self.data_base_path + "data2.bin"
           with open(file_path, mode='wb') as f:
           p.dump(result, f)        
        """
        # 返回结果数组
        return result
    
    def arrayToImage(self,array,imageNames):
        # 接收数据数组,文件名称数组
        """with open(self.data_base_path + filename, mode='rb') as f:
               arr = p.load(f)  # 加载并反序列化数据
        """
        
                




        rows =  array.shpae[0]
        width = self.imageSize[1]
        height = self.imagesPath[0]
        # 也是还原图片大小
        imageData = array.reshape(rows,3,width,height)
        for index in range(0,rows):
            a = imageData[index]
            # 得到RGB通道
            r = pil.fromarray(a[0]).convert('L')
            g = pil.fromarray(a[1]).convert('L')
            b = pil.fromarray(a[2]).convert('L')
            image = pil.merge("RGB", (r, g, b))            
            # 显示图片,通过pyplot
            pyplot.imshow(image)
            pyplot.show()  
            image.save(self.imagesPath + imageNames[index] + ".png")
        

if __name__  == "__main__":
    utils = MXUtils("images/",[32,32])
    utils.imageToArray(np.array(["0.png","1.png","2.png"]))