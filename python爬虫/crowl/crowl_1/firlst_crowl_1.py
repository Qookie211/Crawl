# 引入requests
import requests
# # 使用get方式打开baidu
# url = 'http://www.baidu.com'
# resp = requests.get(url)
# # 显示响应的类型，响应的编码(status_code)，响应的文本内容类型
# print(type(resp))
# print(resp.status_code)
# print(type(resp.text))
# # 显示响应内容，响应的cookies
# print(resp.cookies)
# for cookie in  resp.cookies:
#     print(cookie.name,'->',cookie.value)
#
#
# # 使用requests模拟各种请求方式：get, post, put, delete, head, options, 请求网站 https://httpbin.org
# url_1 = 'http://httpbin.org/get'
# print(requests.get(url_1).text)
# print(requests.post(url_1).text)
# print(requests.put(url_1))
# print(requests.delete(url_1))
# print(requests.head(url_1))
# print(requests.options(url_1))

# requests基本get请求 -- http://httpbin.org/get
# url_2 = 'http://httpbin.org/get'
# print(requests.get(url_2))
# # 显示响应内容
# print(requests.get(url_2).text)

# 模拟带参数的get请求  http://httpbin.org/get?name=cliff&age=33
# url_3 = 'http://httpbin.org/get?name=cliff&age=33'
# resp = requests.get(url_3)
# # 显示响应内容
# print(resp.text)
#
# # 通过一个字典设置带的参数
# url_4 = 'http://httpbin.org/get'
# data = {
#     'name':'wby',
#     'age':21
# }
# resp = requests.get(url_4,params=data)
# # 显示响应内容
# print(resp.text)

# 访问 http://httpbin.org/get
# import json
# url_5 = 'http://httpbin.org/get'
# data = {
#     'name':'王斌印',
#     'age':21
# }
# resp = requests.get(url_5,params=data)
# resp_json = resp.json()
#
#
#
# # 获得的响应文本（json格式）转换为字典
# print(resp_json)
# print("-"*100)
# resp_dict =json.loads( resp.text)
# print(resp_dict)

# 获取二进制数据，如一张图片。 这里可以选择使用 https://github.com/favicon.ico github的图标
# url_6 = 'https://github.com/favicon.ico'
# resp = requests.get(url_6)
#
# # 获得相应的二进制方法 resp.content
#
# # 显示响应的文本内容和字节内容
# print(resp.text)
# print("--"*100)
# print(resp.content)
# # 把上例中获得的字节内容保存为一张本地的图片
# with open("favicon.ico",'wb') as  f:
#     f.write(resp.content)
#     f.close()

# 添加headers：
# 不添加任何headers信息，访问https://www.zhihu.com/explore
# url_7 = 'https://www.zhihu.com/explore'
# resp = requests.get(url_7)
# # 显示响应内容
# print(resp.text)
# print(resp.headers)
# # 上例中增加heards，传入User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}
# resp = requests.get(url_7,headers=headers)
# # 再次显示响应结果
# print(resp.text)

# 通过post方式访问http://httpbin.org/post，传入字典输出name和age
import json
# data = {
#     'name':'wby',
#     'age':21
# }
# url_8 = 'http://httpbin.org/post'
# resp = requests.post(url_8,data=data,headers=headers)
# print(resp.text)
# print(resp.json())

# get方式访问 http://www.jianshu.com， 获得响应
url_9 = 'http://www.jianshu.com'
resp = requests.get(url_9)

# 显示响应代码，响应头(headers)，响应cookies， 响应url，响应的history
print(resp.headers)
print(resp.cookies)
print(resp.url)
print(resp.history)
# 访问简书 http://www.chiwayedu.com/helloworld.html
url_10_html = 'http://www.chiwayedu.com/helloworld.html'
resp = requests.get(url_10_html)

# 如果返回响应码是404，则显示 '404 Not Fount'
print("404 Not Fount"if resp.status_code == 404 else "ok")

# 访问 http://www.jianshu.com, 如果返回值是200，则显示 Request Successfully
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}
url_11 = 'http://www.jianshu.com'
resp = requests.get(url_11,headers=headers)
print("Request Successfully" if resp.status_code == 200 else "Status_code is "+str(resp.status_code))
