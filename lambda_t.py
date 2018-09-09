# coding:utf-8

import re


# 将https://github.com/junxin126/code-re中的https://github.com/提取出来
text = "https://github.com/junxin126/code-re"
result = re.sub(r"(http.*?m/).*", lambda x: x.group(1), text)
print(result)
