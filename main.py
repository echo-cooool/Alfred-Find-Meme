# -*- coding:utf-8 -*-
import json
import sys
from datetime import datetime
from workflow import Workflow, web
import random
from threading import Thread
reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')
with open("data2.json") as file:
    data = json.load(file)


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
    number = 0
    tmp = []
    tmp += wf.filter(input_data, data.keys(), key=lambda x: x,
                     max_results=20, match_on=17)
    for i in tmp:
        number += 1
        url = data[i]['url']
        Thread(target=downloader, args=(url,)).start()
        wf.add_item(data[i]['name'], data[i]['url'],
                    icon=data[i]['url'].split('/')[-1], valid=True, arg=data[i]['url'].split('/')[-1])

    wf.send_feedback()

    # 让 Alfred 显示结果


if __name__ == '__main__':
    wf = Workflow()  # 创建针对 Alfred2 的 Workflow 对象
    # 如果针对的是 Alfred3，那么应该使用 wf = Workflow3()
    # 设置日志对象
    log = wf.logger
    wf.run(main)  # 调用主函数
