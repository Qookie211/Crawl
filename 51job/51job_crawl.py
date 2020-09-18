import csv
import time
import requests
Begain_url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,'
project = '%25E7%2588%25AC%25E8%2599%25AB'
End_url= '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
def get_page(url):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Host': 'search.51job.com',
        'Referer': url,
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        resp = requests.get(url, headers=headers)
        return resp.json()if resp.status_code==200 else None
    except requests.exceptions.ConnectionError:
        print("error")
    except Exception as  e:
        print(e)
        print("error!")

def get_url(page,project_1):
    return Begain_url+project_1+","+"2"+","+str(page)+End_url

def get_total_page(page,pr):
    url = get_url(page,pr)
    data = get_page(url)
    return data.get('total_page')if 'total_page' in data.keys() else None

def get_from_imegge(url):
    data = get_page(url)
    current_page= data.get('curr_page') if 'curr_page' in data.keys() else None
    search_result = data.get('engine_search_result')if'engine_search_result' in data.keys() else None
    all_position = list()
    if current_page:
        print("处理完第"+current_page+"页信息")
        if search_result:
            for position in search_result:
                job_href = position.get('job_href')if 'job_href' in  position.keys() else None
                job_name = position.get('job_name')if 'job_name' in  position.keys() else None
                companytype_text = position.get('companytype_text') if 'companytype_text' in position.keys() else None
                company_href = position.get('company_href') if 'company_href' in position.keys() else None
                company_name = position.get('company_name') if 'company_name' in position.keys() else None
                providesalary_text = position.get('providesalary_text') if 'providesalary_text' in position.keys() else None
                workarea_text = position.get('workarea_text') if 'workarea_text' in position.keys() else None
                workyear = position.get('workyear') if 'workyear' in position.keys() else None
                issuedate = position.get('issuedate') if 'issuedate' in position.keys() else None
                jobwelf = position.get('jobwelf') if 'jobwelf' in position.keys() else None
                companysize_text = position.get('companysize_text') if 'companysize_text' in position.keys() else None
                companyind_text = position.get('companyind_text') if 'companyind_text' in position.keys() else None
                all_position.append((job_name,providesalary_text,job_href,company_name,
                                     company_href,workarea_text,
                                     companytype_text,companyind_text,companysize_text,jobwelf,workyear,issuedate))
    return all_position
def writeCsv(file,data,mode='a',encoding='utf-8'):
    with open(file,mode=mode,encoding=encoding,newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data) if'w'==mode else writer.writerows(data)
        f.close()
def write_csv_header(filename):
    datas = ("工作名称","工作薪资","工作网站","公司名称","公司网站","公司性质","公司地点","公司标签","公司人数","公司待遇","工作年限","招聘日期")
    writeCsv(filename,data=datas,mode='w',encoding='gbk')
def main(prj,page,filename):
    urls = get_url(page, prj)
    positions = get_from_imegge(urls)
    # print(positions)
    writeCsv(filename, data=positions, encoding='gbk')
if __name__ == '__main__':
    total_pages= get_total_page(1,project)
    total_pages= int(total_pages)
    fn = '51job' + project + "+" + time.strftime('%Y%m%d-%H%M%S', time.localtime()) + ".csv"
    write_csv_header(fn)
    for total_page in range(1,total_pages+1):
        main(project,total_page,fn)



