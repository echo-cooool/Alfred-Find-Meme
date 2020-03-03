import json
import sys
from datetime import datetime
from workflow import Workflow, web
import random
from threading import Thread
reload(sys)
sys.setdefaultencoding('utf-8')
api_url = "https://leancloud.cn:443/1.1/classes/alldata2"
header = {
    "X-LC-Id": "B31gHGxVh5go1JPV6OpeRgtq-gzGzoHsz",
    "X-LC-Key": "0YVx0en5m7TpDJF0wY0D1W03",
    "Content-Type": "application/json"
}


def get_keyword(keyword):
    global api_url
    data = "where=%7B%22keyword%22%3A%7B%22%24regex%22%3A%22%5E"+keyword + \
        ".*%22%7D%7D&limit=20&&order=-updatedAt"
    api_url += "?" + data
    res = web.get(api_url, headers=header)
    return res.json()['results']


res = get_keyword("niu")
print json.dumps(res, ensure_ascii=False)
