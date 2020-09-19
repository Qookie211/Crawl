# 通过httpbin.org/cookies，模拟设置一个cookie的值： 比如， number=123456789

# 再次访问httpbin.org/cookies， 查看响应中是否有刚刚设定的cookie值。
import requests
requests.get('http://httpbin.org/cookies/set/number/123456789')
resp = requests.get('http://httpbin.org/cookies')
print(resp.text)


# 通过session来设定cookies，访问cookies. 维持session，保证cookie有效
session = requests.Session()
session.get('http://httpbin.org/cookies/set/number/123456789')
resp = session.get('http://httpbin.org/cookies')
print(resp.text)