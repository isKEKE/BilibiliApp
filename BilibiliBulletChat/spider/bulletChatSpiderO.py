# _*_ encoding: utf-8 _*_
# 弹幕爬虫旧接口
import requests
import xml.dom.minidom as minidom
from spider.bulletChatSpider import BulletChatSpider

class BulletChatSpiderO(BulletChatSpider):
    api = "https://comment.bilibili.com/%s.xml"
    def __init__(self, bvid):
        super(BulletChatSpiderO, self).__init__(bvid)


    def bulletChat(self) -> map:
        '''方法重构'''
        self.api = self.api % self.oid
        response = requests.get(self.api, headers=self.headers)
        response.encoding = "utf-8"
        domobj = minidom.parseString(response.text)
        # element_i = domobj.getElementsByTagName('i')[0]
        # 获得根节点
        root = domobj.documentElement
        # 获得子节点 d
        elements_d = root.getElementsByTagName("d")
        # 获得内容
        # print(elements_d[0].getAttribute("p")) # p属性
        return map(lambda d: d.firstChild.nodeValue, elements_d)
    

if __name__ == "__main__":
    BulletChatSpiderO("BV19v411M7Rs").loop()
