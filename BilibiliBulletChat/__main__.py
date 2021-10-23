# _*_ encoding: utf-8 _*_
# B站弹幕爬虫
from utils.bilibliApp import BilibiliApp
if __name__ == "__main__":
    BVID = "BV19v411M7Rs"
    BilibiliApp(BVID).bulletChat()