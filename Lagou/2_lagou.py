import csv
import time

import requests
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=1'
urls = 'https://www.lagou.com/jobs/list_python/p-city_2?&cl=false&fromSearch=true&labelWords=&suginput=&isSchoolJob=1'

headers = {

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',

    'Referer': 'https://www.lagou.com/jobs/list_python/p-city_2?&cl=false&fromSearch=true&labelWords=&suginput=&isSchoolJob=1',

    'Accept': 'application/json, text/javascript, */*; q=0.01'

}
data = {
        'first': 'true',
        'pn': '1',
        'kd': 'python'
}
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
def get_job(datas):
    results= datas.get('content').get('positionResult').get('result')
    all_position = list()
    for position in results:
        positionName = position.get('positionName')
        companyId = position.get('companyId')
        companyFullName = position.get('companyFullName')
        companyType = position.get('firstType')
        jobNature = position.get('jobNature')
        positionAdvantage = position.get('positionAdvantage')
        all_position.append((positionName,companyId,companyFullName,companyType,jobNature,positionAdvantage))
    return all_position
def main(filename,cookie):
    all_data = get_one_page(cookie)
    positions = get_job(all_data)
    writeCsv(filename,data=positions,encoding='gbk')
def writeCsv(file,data,mode='a',encoding='utf-8'):
    with open(file,mode=mode,encoding=encoding,newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data) if'w'==mode else writer.writerows(data)
        f.close()
def write_csv_header(filename):
    data = ("职位名称","公司id","公司名称","公司属性","职位性质","优点")
    writeCsv(filename,data=data,mode='w',encoding='gbk')
if __name__ == '__main__':
    cookie = get_cookie(urls)
    fn = 'lagou' + time.strftime('%Y%m%d-%H%M%S', time.localtime()) + ".csv"
    write_csv_header(fn)
    main(fn,cookie)
