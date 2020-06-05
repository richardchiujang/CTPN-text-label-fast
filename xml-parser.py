from libs.pascal_voc_io import PascalVocReader
from libs.pascal_voc_io import PascalVocWriter
from libs.pascal_voc_io import XML_EXT
from libs.labelFile import LabelFile, LabelFileError

from os import walk
import os.path
import sys

try:
    from PyQt5.QtGui import QImage
except ImportError:
    from PyQt4.QtGui import QImage

def readPascalVocFormat(filename):
    tVocParseReader = PascalVocReader(filename)
    shapes = tVocParseReader.getShapes()
    # print(shapes, '\n')

    newtext = []
    for shape in shapes:
        # newtext = []
        if shape[0]=='text':
            # {'label': 'text', 'line_color': (160, 67, 78, 100), 'fill_color': (160, 67, 78, 100), 'points': [(84.0, 305.0), (99.0, 305.0), (99.0, 321.0), (84.0, 321.0)], 'difficult': False}
            # ('text', [(52, 305), (67, 305), (67, 321), (52, 321)], None, None, False)
            # {'label': 'text', 'line_color': (160, 67, 78, 100), 'fill_color': (160, 67, 78, 100), 'points': shape[1], 'difficult': False}
            newtext.append({'label': 'text', 'line_color': (160, 67, 78, 100), 'fill_color': (160, 67, 78, 100), 'points': shape[1], 'difficult': False})
            # print(newtext, '\n')
            pass
        elif shape[0]=='textbox':    
            # ('textbox', [(224, 273), (313, 273), (313, 298), (224, 298)], None, None, False)   
            #           # [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
            # newtext = []
            xmin = shape[1][0][0] # 左邊點
            xmax = shape[1][1][0] 
            ymin = shape[1][0][1]
            ymax = shape[1][2][1]        
            xlen = xmax - xmin  # 計算寬度 
            leftx = xmin # 小框的左邊點
            rightx = xmin + 15  # 往右邊15點(小框的右邊點)
            while rightx < xmax: # 小框右邊點 < 大框的右邊界
                # newtext.append(('text', [(leftx, ymin), (rightx, ymin), (rightx, ymax), (leftx, ymax)], None, None, False))
                newtext.append({'label': 'text', 'line_color': (160, 67, 78, 100), 'fill_color': (160, 67, 78, 100), 'points': [(leftx, ymin), (rightx, ymin), (rightx, ymax), (leftx, ymax)], 'difficult': False})
                leftx = rightx + 1  # 小框右邊界 右移 1點
                rightx = leftx + 15 # 小框左邊界 往右15點
            else: # 小框右邊點 >= 大框的右邊界 ，就畫上最後一格
                # pass
                # 如果 rightx > xmax ( 超過 )  OR   rightx = xmax (相同) 為避免框框寬為0而出錯，所以一律 xmax+1 處理
                # newtext.append(('text', [(leftx, ymin), (xmax+1, ymin), (xmax+1, ymax), (leftx, ymax)], None, None, False))
                newtext.append({'label': 'text', 'line_color': (160, 67, 78, 100), 'fill_color': (160, 67, 78, 100), 'points': [(leftx, ymin), (rightx, ymin), (rightx, ymax), (leftx, ymax)], 'difficult': False})

    # for ntext in newtext:
    #     print(ntext, '\n')
    shapes =  newtext
    return shapes

def savePascalVocFormat(filename, shapes, imagePath, lineColor=None, fillColor=None, databaseSrc=None):
    imgFolderPath = os.path.dirname(imagePath)
    imgFolderName = os.path.split(imgFolderPath)[-1]
    imgFileName = os.path.basename(imagePath)
    #imgFileNameWithoutExt = os.path.splitext(imgFileName)[0]
    # Read from file path because self.imageData might be empty if saving to
    # Pascal format
    image = QImage()
    image.load(imagePath)
    imageShape = [image.height(), image.width(),
                    1 if image.isGrayscale() else 3]
    writer = PascalVocWriter(imgFolderName, imgFileName,
                                imageShape, localImgPath=imagePath)
    # writer.verified = verified

    for shape in shapes:
        # print('shape:\n', shape)
        points = shape['points']
        label = shape['label']
        # Add Chris
        difficult = int(shape['difficult'])
        bndbox = LabelFile.convertPoints2BndBox(points)
        writer.addBndBox(bndbox[0], bndbox[1], bndbox[2], bndbox[3], label, difficult)

    writer.save(targetFile=filename)
    return


# spath = 'C:\\Application\\Develop\\text-detection-ocr\\data\\id_data\\IX0090\\'
# spath = 'C:\\Application\\Develop\\text-detection-ocr\\data\\id_data\\IA0021\\'
# spath = 'C:\\Application\\Develop\\text-detection-ocr\\data\\id_data\\IB0011\\'
# spath = 'C:\\Application\\Develop\\text-detection-ocr\\data\\id_data\\IC0010\\'
# spath = 'C:\\Application\\Develop\\text-detection-ocr\\data\\id_data\\IB0010\\'
spath = 'C:\\Application\\Develop\\text-detection-ocr\\data\\id_data\\try0091\\'

for (dirpath, dirnames, filenames) in walk(spath):
    all_files = filenames
    break # 就是只抓一層

for nfile in all_files[:]:
    if nfile.split('.')[-1] != 'xml':
        pass
    else:
        imagePath = spath + nfile.split('.')[0] + '.jpg'
        filename = spath + nfile
        shapes = readPascalVocFormat(filename)
        savePascalVocFormat(filename=filename, imagePath=imagePath, shapes=shapes)
        print('process image file {}.'.format(nfile))




