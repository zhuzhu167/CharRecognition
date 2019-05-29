# -*- coding: UTF-8 -*-
import os
import time
from aip import AipOcr  # pip3 install baidu-aip
from dataclasses import dataclass  # Python3.7及以上版本


def get_file_content(image_file):
    """生成原始图片的base64编码数据,得到image参数"""
    if not isinstance(image_file, str):
        return None
    if not os.path.isfile(image_file):
        print('图片文件有误，请传入正确的文件路径')
        return None
    with open(image_file, 'rb') as fp:
        return fp.read()


@dataclass
class BaiDuAPIMsg(object):
    app_id: str
    app_key: str
    secert_key: str
    image_file: str

    def __post_init__(self):
        self.image = get_file_content(self.image_file)
        self.options = {
            'detect_direction': 'true',
            'language_type': 'CHN_ENG',
            'probability': 'true', }

    def get_ocr_result(self):
        aipOcr = AipOcr(self.app_id, self.app_key, self.secert_key)
        # result = aipOcr.basicGeneral(self.image, self.options)    #通用版
        result = aipOcr.basicAccurate(image=self.image, options=self.options)  # 高精度版
        try:
            words = result['words_result']
            return '\n'.join([word['words'] for word in words])
        except:
            print('获取结果失败，请检查各参数是否配置正确。')
            return ''


if __name__ == '__main__':
    app_id = '16352414'  # 需要自己申请
    app_key = 'RQDWpy0Bw8Bmh1ZoXuOyIn0c'  # 需要自己申请
    secert_key = 'g4EMx16KsbRvHRSFvqCVLk5wNnrNBReL'  # 需要自己申请
    image = "/Users/liangzhu/Desktop/图片/2.jpeg"

    BaiDu = BaiDuAPIMsg(app_id, app_key, secert_key, image)
    result = BaiDu.get_ocr_result()
    print(result) # 123