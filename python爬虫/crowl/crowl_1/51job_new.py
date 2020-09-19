import  requests
import csv,time
import  django

BasUrl_1 ='https://search.51job.com/list/020000,000000,0000,00,9,99,'
EndUrl = '.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
project = 'python'
def get_one_page(url):
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
        resp = requests.get(url,headers=headers)
        return resp.json() if 200 == resp.status_code else None
    except requests.exceptions.ConnectionError:
        print("Connect Error")
    except Exception as e :
        print(e)
        print("Error Found")
        return None
def get_url(prj,page):
    return BasUrl_1+prj+',2,'+str(page)+EndUrl

def total_page(prj):
    url = get_url(prj,1)
    data = get_one_page(url)
    return data.get('total_page')if 'total_page' in data.keys() else None
def get_info_from_page(data):
    current_page= data.get('curr_page') if 'curr_page' in data.keys() else None
    search_result= data.get('engine_search_result') if'engine_search_result' in data.keys() else None
    all_position = list()
    if current_page:
        print('现在处理第'+current_page+'页的信息')
        if search_result:
            for position in search_result:
                job_href = position.get('job_href')if 'job_href' in position.keys()else None
                job_name = position.get('job_name')if 'job_name' in position.keys()else None
                job_title = position.get('job_title')if 'job_title' in position.keys()else None
                company_href = position.get('company_href')if 'company_href' in position.keys()else None
                company_name = position.get('company_name')if 'company_name' in position.keys()else None
                providesalary_text =position.get('providesalary_text')if 'providesalary_text' in position.keys()else None
                workarea_text = position.get('workarea_text') if 'workarea_text' in position.keys() else None
                updatedate = position.get('updatedate') if 'updatedate' in position.keys() else None
                companytype_text = position.get('companytype_text') if 'companytype_text' in position.keys() else None
                degreefrom = position.get('degreefrom') if 'degreefrom' in position.keys() else None
                workyear = position.get('workyear') if 'workyear' in position.keys() else None
                jobwelf = position.get('jobwelf') if 'jobwelf' in position.keys() else None
                attribute_text = position.get('attribute_text') if 'attribute_text' in position.keys() else None
                companysize_text = position.get('companysize_text') if 'companysize_text' in position.keys() else None
                companyind_text = position.get('companyind_text') if 'companyind_text' in position.keys() else None
                # pos={
                #     'job_href':job_href,
                #     'job_name':job_name,
                #     'job_title' :job_title,
                #     'company_href':company_href,
                #     'company_name':company_name,
                #     'providesalary_text':providesalary_text,
                #     'workarea_text':workarea_text,
                #     'updatedate':updatedate,
                #     'companytype_text':companytype_text,
                #     'degreefrom':degreefrom,
                #     'workyear':workyear,
                #     'jobwelf':jobwelf,
                #     'attribute_text':attribute_text,
                #     'companysize_text':companysize_text,
                #     'companyind_text':companyind_text
                #
                # }
                all_position.append((job_href,job_name,job_title,company_href,company_name,companyind_text,providesalary_text
                                    ,workarea_text,updatedate,degreefrom,workyear,jobwelf   ,companysize_text,companytype_text))
    return all_position

def writeCsv(file,data,mode='a',encoding='utf-8'):
    with open(file,mode=mode,encoding=encoding,newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data) if'w'==mode else writer.writerows(data)
        f.close()
def write_csv_header(filename):
    data = ("职位详情","职位","职位名","公司详情","公司名","公司行业","薪资","公司地点","招聘更新日期","经验","工作年限","公司待遇","公司规模","公司性质")
    writeCsv(filename,data=data,mode='w',encoding='gbk')
def main(prj,page,filename):
    url = get_url(prj,page)
    all_data = get_one_page(url)
    positions = get_info_from_page(all_data)
    # print(positions)
    writeCsv(filename,data=positions,encoding='gbk')
if __name__ == '__main__':
    total_page_1= total_page(project)
    total_page_1=int(total_page_1) if total_page_1 else 1
    fn ='51job'+project+"+"+time.strftime('%Y%m%d-%H%M%S',time.localtime())+".csv"
    write_csv_header(fn)
    for page in range(1,total_page_1+1):
        main(project,page,fn)