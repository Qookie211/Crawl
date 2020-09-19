from urllib import  request,parse
url = 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB/p-city_2?px=default&gx=&isSchoolJob=1#filterBox'
resp = request.urlopen(url)
# print(resp.read().decode("utf-8"))
import http.cookiejar
headers = {
    'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB/p-city_2?px=default&gx=&isSchoolJob=1',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'x-anit-forge-code': 0,
    'x-anit-forge-token': 'None',
    'x-requested-with': 'XMLHttpRequest'
}
# 保存cookie
cookiefile = "lagou_cookie.txt"
cookies = http.cookiejar.MozillaCookieJar(cookiefile)
handler = request.HTTPCookieProcessor(cookies)
opener = request.build_opener(handler)
resq = request.Request(url,headers=headers)
resp = opener.open(resq)
cookies.save(ignore_discard=True,ignore_expires=True)

ajax_url = " https://www.lagou.com/jobs/positionAjax.json"
params = {
    'px': 'default',
    'city': '北京',
    'needAddtionalResult': 'false',
    'isSchoolJob': 1,
}
params = parse.urlencode(params)
ajax_url = (ajax_url+"?"+params)
# print(ajax_url)

# 获取cookie
cookie = http.cookiejar.MozillaCookieJar()
cookie.load(cookiefile,ignore_expires=True,ignore_discard=True)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)

data = {
    'first': 'true',
    'pn': 1,
    'kd': '爬虫'

}
data = parse.urlencode(data).encode('utf8')
resq = request.Request(ajax_url,headers=headers,data=data,method='POST')
resp = opener.open(resq)
print(resp.read().decode('utf8'))






