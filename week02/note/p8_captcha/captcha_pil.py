import requests
import os
from PIL import Image
import pytesseract

# 打开并显示文件
im = Image.open('cap.jpg')
im.show()

# 灰度图片
gray = im.convert('L')
gray.save('c_gray2.jpg')
im.close()

# 二值化:深色更深，浅色更浅
threshold = 100
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
# 将二值化后的图片保存
out = gray.point(table,'1')
out.save('c_th.jpg')
# 运用pytesseract识别，对图片进行切分
th = Image.open('c_th.jpg')
print(pytesseract.image_to_string(th,lang='chi_sim+eng'))

# 各种语言识别库 http://github.com/tesseract-ocr/tessdata
# 放到 /user/local/Cellar/tesseract/版本/share/tessdata
