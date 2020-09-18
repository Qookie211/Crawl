import requests
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
url = 'https://search.51job.com/list/010000,000000,0000,00,9,99,java,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
data = get_one_page(url)
# print(data) if data else print("get one page Failure")
print(data)

if('total_page' in data.keys()):
    print('total_page = ',data.get('total_page'))
if('engine_search_result' in data.keys()):
    print('engine_search_result = ',data.get('engine_search_result'))