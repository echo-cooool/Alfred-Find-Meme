# -*- coding:utf-8 -*-
import json
import sys
from datetime import datetime
from workflow import Workflow, web
import random
from threading import Thread

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
api_url = "https://leancloud.cn:443/1.1/classes/alldata2"
header = {
    "X-LC-Id": "B31gHGxVh5go1JPV6OpeRgtq-gzGzoHsz",
    "X-LC-Key": "0YVx0en5m7TpDJF0wY0D1W03",
    "Content-Type": "application/json"
}


def get_keyword(keyword):
    global api_url
    data = "where=%7B%22keyword%22%3A%7B%22%24regex%22%3A%22%5E.*"+keyword + \
        ".*%22%7D%7D&limit=20&&order=-updatedAt"
    api_url += "?" + data
    res = web.get(api_url, headers=header)
    return res.json()['results']


def downloader(url):
    if url == "":
        return 0
    name = url.split('/')[-1]
    r = web.get(url)
    with open(name, "wb") as file:
        file.write(r.content)


def main(wf):
    args = wf.args
    input_data = args[0]
    # 自定义的程序
    # 向结果中添加显示内容
    tmp = get_keyword(input_data)
    for i in tmp:
        url = i['url']
        Thread(target=downloader, args=(url,)).start()
        wf.add_item(i['name'], i['url'],
                    icon=i['url'].split('/')[-1], valid=True, arg=i['url'].split('/')[-1])

    wf.send_feedback()

    # 让 Alfred 显示结果


if __name__ == '__main__':
    wf = Workflow()  # 创建针对 Alfred2 的 Workflow 对象
    # 如果针对的是 Alfred3，那么应该使用 wf = Workflow3()
    # 设置日志对象
    log = wf.logger

    wf.run(main)  # 调用主函数
