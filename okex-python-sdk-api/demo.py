import talib
import time
import datetime

print("hello python.")

print(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1546007760000/1000)))

print(time.strftime("%Y-%m-%dT%H:%M:%SZ", time.localtime(1546007760000/1000)))

print((datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))

# for x in range(1, 13):
#   dt_start = (datetime.datetime(2016, x, 1)).strftime("%Y%m%d")
#   if 12 == x:
#     dt_end = (datetime.datetime(2016, 12, 31)).strftime("%Y%m%d")
#   else:
#     dt_end = (datetime.datetime(2016, x+1, 1) - datetime.timedelta(days = 1)).strftime("%Y%m%d")
#     pass
#   print (dt_start, dt_end)
        
#   print((datetime.datetime.strptime(dt_start, "%Y%m%d") + datetime.timedelta(days=1)).strftime("%Y%m%d"))


for x in range(1, 13):
  dt_start = (datetime.datetime(2016, x, 1))
  if 12 == x:
    dt_end = (datetime.datetime(2016, 12, 31))
  else:
    dt_end = (datetime.datetime(2016, x+1, 1) - datetime.timedelta(days = 1))
    pass
  print (dt_start, dt_end)

  while dt_start != dt_end:
      str_start = (dt_start.strftime("%Y-%m-%dT%H:%M:%SZ"))
      dt_start = dt_start + datetime.timedelta(days=1)
      str_end = (dt_start.strftime("%Y-%m-%dT%H:%M:%SZ"))

      print(str_start, str_end)
      time.sleep(0.2)
      pass

  str_start = (dt_start.strftime("%Y-%m-%dT%H:%M:%SZ"))
  dt_start = dt_start + datetime.timedelta(days=1)
  str_end = (dt_start.strftime("%Y-%m-%dT%H:%M:%SZ"))
  print(str_start, str_end)


#   print((datetime.datetime.strptime(dt_start, "%Y%m%d") + datetime.timedelta(days=1)).strftime("%Y%m%d"))



# 1546180726.9398546
# 1546007760000

# @File    : 4.10.hash加密算法.py
# @Software: PyCharm

import hashlib

# 1.将字符串，通过加密算法，变成固定长度的输出
s = 'abc'
print(len(str(hash(s)))*4, hash(s))

# 2.生成md5数字指纹。
# 第1种写法：
s2 = b'!@abc'  # 定义字节型字符串
md = hashlib.md5()  # 导入md5算法
md.update(s2)  # 把值传给md5算法

print(md.digest())  # 生成一个128位的2进制数
print('MD5', '长度:', len(md.hexdigest())*4, md.hexdigest())
# 第2种写法：
print(hashlib.md5("!@abc".encode("utf-8")).hexdigest())

print(hashlib.md5(str(time.time()).encode("utf-8")).hexdigest())

# 3.SHA-1

hash = hashlib.sha1()
hash.update('admin'.encode('utf-8'))
print('SHA-1', '长度:', len(hash.hexdigest())*4, hash.hexdigest())

# 4.SHA-256

hash = hashlib.sha256()
hash.update('admin'.encode('utf-8'))
print('SHA-256', '长度:', len(hash.hexdigest())*4, hash.hexdigest())

# 5.SHA-384

hash = hashlib.sha384()
hash.update('admin'.encode('utf-8'))
print('SHA-384', '长度:', len(hash.hexdigest())*4, hash.hexdigest())

# 5.SHA-512

hash = hashlib.sha512()
hash.update('admin'.encode('utf-8'))
print('SHA-384', '长度:', len(hash.hexdigest())*4, hash.hexdigest())