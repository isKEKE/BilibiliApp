# _*_ encoding: utf-8 _*_
from spider import BulletChatSpider
from spider import BulletChatSpiderO

class BilibiliApp(object):
    def __init__(self,bvid,mode=False):
        '''
        :param bvid: 视频BVID
        :param mode: 使用爬取弹幕接口，默认`旧接口`
        '''
        self.bvid = bvid
        self.mode = mode

    def bulletChat(self) -> None:
        if self.mode == True:
            '''使用新接口'''
            BulletChatSpider(self.bvid).loop()
        else:
            '''使用旧接口'''
            BulletChatSpiderO(self.bvid).loop()
        return

    def run(self) -> None:
        '''运行'''
        self.bulletChat()
