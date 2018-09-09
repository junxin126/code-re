# coding:utf-8
import re

# 在“*”或者“+”后面加“？”即可关闭贪婪模式
result = re.match(r"(.*?)(\d*?)(yes)","thisnumber234yes")
gr_re=result.groups()
print (result)
print (gr_re)


