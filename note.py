# coding:utf-8
import re

# 在“*”或者“+”后面加“？”即可关闭贪婪模式，实际上“?"表示{0，1}，取0至1
result = re.match(r"(.+?)(\d+)", "this number is 234")
print result.groups()

# 匹配整数
result = re.match("-?\d+$", "8888")
print result.group()
