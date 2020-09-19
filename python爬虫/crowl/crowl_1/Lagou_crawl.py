import requests
url = 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB/p-city_2?px=default&gx=&isSchoolJob=1#filterBox'
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
params = {
    'px': 'default',
    'city': '北京',
    'needAddtionalResult': 'false',
    'isSchoolJob': 1,
}
data = {
    'first': 'true',
    'pn': 1,
    'kd': '爬虫'
}
resp =requests.post(url,data=data,params=params,headers=headers)
print(resp.text)
