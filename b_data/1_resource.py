import requests
from lxml import etree
import os
from urllib.parse import urljoin
import time
# 定义要下载的网页链接
urls = [
    "https://xxxb.bjut.edu.cn/rcpy/bks/kcjj.htm",
    "https://xxxb.bjut.edu.cn/rcpy/bks/pyfa.htm"
    "https://xxxb.bjut.edu.cn/rcpy/bks/pyfa/1.htm"
]
# 定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}
# 创建一个文件夹来存储下载的文件
output_folder = "class_data"
os.makedirs(output_folder, exist_ok=True)

# 遍历url
for url in urls:
    # 发送带有请求头的HTTP请求获取网页内容
    response = requests.get(url, headers=headers)
    # 检查响应状态码是否为200
    if response.status_code == 200:
        # 获取所有的HTML数据
        html_str = response.text
        # 使用lxml的etree来解析HTML
        xpath_html = etree.HTML(html_str)
        # 使用XPath操作提取数据
        data = xpath_html.xpath('//a[contains(@href,"../../dfiles")]/@href')
        print(data)
        # 下载文件并保存到output_folder
        for link in data:
            file_url = urljoin('https://xxxb.bjut.edu.cn', link)
            print(file_url)
