from PIL import Image as myImage
import pytesseract
# 指定tesseract路径
pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files\\Tesserect\\tesseract.exe'
# 读取图片
img = myImage.open('dxf1.png')
# 识别图片
text = pytesseract.image_to_string(img, lang='chi_sim')
print(text)