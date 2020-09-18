"""
正则表达式练习：
"""
# number=int(input("请输入手机号码"))
import re
# if len(str(number))==11:
#     re.findall("1[3578]{10}", "number")

# mes="Thu Sep  7 15:17:18.514 UTC"
# mes01="  "
# print(len(mes01))

print(re.search(r'(?P<pig>ab)+', "ababababab").group('pig'))

print(re.search("(?P<ha>op)+", "opopopop").group('ha'))

print(re.search("(?P<ha>op)+", "opopopop").group())


# 正则表达式中有子组，则只能返回子组对应部分
print(re.findall("(opo)+", "opoopopop"))
# ['opo']  (实际找到了 opoopo , 但是因为有子组，所以只返回子组里的opo)
print(re.findall("(opo)+", "opopopop"))
# ['opo', 'opo']
# (实际找到了 opo opo , 但是因为有子组，所以只返回子组里的opo)