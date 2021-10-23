# _*_ encoding: utf-8 _*_
# 弹幕爬虫新接口
import os
import re
import csv
import requests
import config as cfg

class BulletChatSpider(object):
    '''B站弹幕爬虫'''
    api = "https://api.bilibili.com/x/v2/dm/web/seg.so"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
    }
    def __init__(self, bvid):
        self.bvid = bvid
        self.oid = None
        self.pid = None
        self.datas = None


    def getOidAndPid(self) -> tuple:
        '''获得OID和PID'''
        _url = f"https://www.bilibili.com/video/{self.bvid}"
        _response = requests.get(_url, headers=self.headers)
        pat = re.compile('''"cids":{"1":(.*?)}},"%s":{"aid":(.*?),''' % self.bvid)
        return re.findall(pat, _response.text)[0]


    def bulletChat(self) -> list:
        '''发起弹幕请求'''
        params = {
            "type": 1,
            "oid": self.oid,
            "pid": self.pid,
            "segment_index": 1
        }
        response = requests.get(self.api, headers=self.headers, params=params)
        # 正则匹配
        pat = re.compile(".*?([\u4E00-\u9FA5]+).*?")
        return re.findall(pat, response.text)


    def save(self) -> None:
        '''存储'''
        with open(os.path.join(cfg.SAVE_TO_PATH, f"{self.bvid}.csv"), "w") as fp:
            writer = csv.writer(fp)
            for line in self.datas:
                writer.writerow((line,))
        return


    def loop(self) -> None:
        '''运行'''
        self.oid, self.pid = self.getOidAndPid()
        self.datas = self.bulletChat()
        self.save()
        return


if __name__ == "__main__":
    BulletChatSpider("BV19v411M7Rs").loop()
