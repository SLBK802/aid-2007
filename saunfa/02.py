"""
暂停一秒输出，并格式化当前时间。
"""
import time

print(time.ctime())
# 格式化当前时间
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))