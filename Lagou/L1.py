import requests
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=1'
data = {
        'first': 'true',
        'pn': '1',
        'kd': 'python'
}

headers = {

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',

    'Referer': 'https://www.lagou.com/jobs/list_python/p-city_2?&cl=false&fromSearch=true&labelWords=&suginput=&isSchoolJob=1',

    'Accept': 'application/json, text/javascript, */*; q=0.01'

}
urls = 'https://www.lagou.com/jobs/list_python/p-city_2?&cl=false&fromSearch=true&labelWords=&suginput=&isSchoolJob=1'
session = requests.Session()
def get_cookie(url):
    session.get(url, headers=headers, timeout=3)
    cookie = session.cookies
    return cookie
def get_one_page(cookie):
    try:
        resp = session.post(url, cookies=cookie, data=data, headers=headers, timeout=5)
        return resp.json() if resp.status_code == 200 else None
    except Exception as e:
        print(e)
        return None
def main():
    cookie = get_cookie(urls)
    datas = get_one_page(cookie)
    print(datas)
if __name__ == '__main__':
    main()
