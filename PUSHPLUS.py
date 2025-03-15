import requests
import os
token = '51128351c4004a8288c26a6a4a489153'
title= 'Epic-FreeGamer'
content ='Epic-FreeGamer任务已执行'
url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content
requests.get(url)
