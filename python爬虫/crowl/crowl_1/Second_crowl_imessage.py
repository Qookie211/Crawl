from urllib import request,parse
import http.cookiejar
url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
resp = request.urlopen(url)
headers = {
    'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_/p-city_2?px=new&gx=&hy=%E7%A7%BB%E5%8A%A8%E4%BA%92%E8%81%94%E7%BD%91&isSchoolJob=1',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'x-anit-forge-code': 0,
    'x-anit-forge-token': 'None',
    'x-requested-with': 'XMLHttpRequest'
}

cookiefile = 'cookie_lagou_2'
cookies = http.cookiejar.MozillaCookieJar(cookiefile)
handerler = request.HTTPCookieProcessor(cookies)
opener = request.build_opener(handerler)
resq = request.Request(url,headers=headers)
resp = opener.open(resq)
cookies.save(ignore_discard=True,ignore_expires=True)

ajax_url = 'https://www.lagou.com/jobs/positionAjax.json'
params = {
    'hy':'移动互联网',
    'px':'new',
    'city':'北京',
    'needAddtionalResult':'false',
    'sSchoolJob':'1'
}
params = parse.urlencode(params)
# print(params)
ajax_url = ajax_url+"?"+params
print(ajax_url)

cookie = http.cookiejar.MozillaCookieJar()
cookie.load(cookiefile,ignore_discard=True,ignore_expires=True)
handerler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handerler)

data = {
    'first': 'true',
    'pn': '1',
    'kd': ''

}

data = parse .urlencode(data).encode("utf8")
resq = request.Request(ajax_url,headers=headers,data=data,method='POST')
resp = opener.open(resq,timeout=10)
print(resp.read().decode("utf8"))







