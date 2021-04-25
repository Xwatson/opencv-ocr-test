from aip import AipOcr
import pandas as pd

# 配置百度参数
config = {
    'appId': '',
    'apiKey': '',
    'secretKey': ''
}
client = AipOcr(**config)

def get_file_content(file):
    with open(file, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):
    image = get_file_content(image_path)
    """ 如果有可选参数 """
    options = {}
    # 是否检测图像朝向，默认不检测
    options["detect_direction"] = "true"
    # 是否返回识别结构中每一行的置信度
    options["probability"] = "true"
    # result = client.basicGeneral(image)
    result = client.basicAccurate(image, options)
    print(result.get("words_result"))
    df = pd.DataFrame(result.get("words_result"))
    return df

pictureContent = img_to_str('dxf1.png')
print(pictureContent)
print(list(pictureContent['words']))