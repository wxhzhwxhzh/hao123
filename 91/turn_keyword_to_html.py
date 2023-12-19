#!/usr/bin/env python
# -*- coding:utf-8 -*-
# pip install DrissionPage==4.0.0b16
# http://g1879.gitee.io/drissionpagedocs/

from DrissionPage import ChromiumPage, SessionPage
import json
import random
import os, time
import sys

# 定义常量
URL = "https://heiliao385.pro/archives/3259.html"

UA_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1"
UA_anzhuo = "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.99 Mobile Safari/537.36"


def save_text_to_file(text, filename):
    """将文本保存到文件中"""
    with open(filename, "w") as f:
        f.write(text)


def random_num():
    """生成随机数"""
    return random.randint(1000, 9999)


def to_dict(string):
    """将字符串转换为字典"""
    return json.loads(string)


def show(dictionary):
    """展示字典内容"""
    for key, value in dictionary.items():
        kk = str(key).ljust(15)
        print(f" {kk}:{value}")


def new_folder(folder_name):
    """创建新文件夹"""
    current_dir = os.getcwd()  # 获取当前文件夹路径
    folder_path = os.path.join(current_dir, folder_name)  # 拼接文件夹路径

    if os.path.exists(folder_path):
        return folder_path

    os.makedirs(folder_path)  # 创建文件夹
    return folder_path


def write_dict_to_file(input_dict, folder_path):
    """将字典以JSON格式写入文件"""
    file_path = os.path.join(folder_path, f"a.txt")  # 拼接文件路径

    with open(file_path, "w", encoding="gb2312") as file:
        json.dump(
            input_dict, file, ensure_ascii=False
        )  # 指定ensure_ascii参数为False，确保输出非ASCII字符








def generate_html(link_list):
    huiche='\n'
    html_content = fr'<html><head> <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">  <title>{key}</title></head><body>'

    for link in link_list:
        parts = link.split("    ")
        if len(parts) == 2:
            url = parts[0]
            title = parts[1]
            html_content += huiche+f'<a href="{url}">{title}</a><br>'+huiche

    html_content += "</body></html>"

    # 将生成的HTML保存到文件
    with open(f"{key}.html", "w",encoding="utf-8") as file:
        file.write(html_content)



def main():

    global key 
    key = "酒吧"

    #接受命令行参数ll
    args = sys.argv[1]  
    if len(args)>=1:
        key=args

    page = SessionPage()

    URL2 = r"https://cn1.91-short.com/search?wd=" + key

    # 访问网页
    page.set.user_agent(UA_iphone)
    page.get(URL2)


    # pic_info_s = page.eles("tag:div@@class=module-item-pic")
    pic_info_s = page.eles("xpath://div[@class='module-item-pic']")


    links = [
        pic_info.ele("tag:a").attr("href") + "    " + pic_info.ele("tag:a").attr("title")
        for pic_info in pic_info_s
    ]

    for i in links:
        print(i)

    generate_html(links)

if __name__ == "__main__":
    main()
