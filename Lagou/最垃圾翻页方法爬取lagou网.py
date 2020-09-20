import csv
import time
import requests
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&needAddtionalResult=false&isSchoolJob=1'
urls = 'https://www.lagou.com/jobs/list_爬虫/p-city_0?px=default&gx=&isSchoolJob=1#filterBox'

headers = {

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',

    'Referer': 'https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB/p-city_0?px=default&gx=&isSchoolJob=1',

    'Accept': 'application/json, text/javascript, */*; q=0.01'

}

def get_page():
    all_position = list()
    for i in range(1,31):
        data = {
            'first':'false',
            'kd':'爬虫',
            'pn':i
        }
        session = requests.Session()
        session.get(urls, headers=headers, timeout=3)
        cookie = session.cookies
        resp = session.post(url, cookies=cookie, data=data, headers=headers, timeout=5)
        req_info= resp.json()
        results = req_info.get('content').get('positionResult').get('result')
        totalCount = int(req_info.get('content').get('positionResult').get('totalCount'))
        resultsize = int(req_info.get('content').get('pageSize'))
        totalCount = int(totalCount/resultsize)
        if i <= totalCount:
            print("正在爬取第"+str(i)+"页")
            for position in results:
                positionName = position.get('positionName')
                companyId = position.get('companyId')
                companyFullName = position.get('companyFullName')
                companyType = position.get('firstType')
                jobNature = position.get('jobNature')
                positionAdvantage = position.get('positionAdvantage')
                all_position.append((positionName, companyId, companyFullName, companyType, jobNature, positionAdvantage))
        else:
            return all_position
def main(filename):
    positions = get_page()
    writeCsv(filename,data=positions,encoding='gbk')
    print("crawl over")
def writeCsv(file,data,mode='a',encoding='utf-8'):
    with open(file,mode=mode,encoding=encoding,newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data) if'w'==mode else writer.writerows(data)
        f.close()
def write_csv_header(filename):
    data = ("职位名称","公司id","公司名称","公司属性","职位性质","优点")
    writeCsv(filename,data=data,mode='w',encoding='gbk')
if __name__ == '__main__':
    fn = 'lagou' + time.strftime('%Y%m%d-%H%M%S', time.localtime()) + ".csv"
    write_csv_header(fn)
    main(fn)

