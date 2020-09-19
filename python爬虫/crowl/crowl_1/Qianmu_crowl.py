import  requests
from lxml import  etree

rank_url = 'http://www.qianmu.org/ranking/1528.htm'

# headers = {
#
# }

def get_page(url):
    try:
        resp = requests.get(url)
        return resp.text if resp.status_code==200 else None
    except Exception as  e:
        print(e)
        return None

def parse_page(data):
    parser = etree.HTMLParser(encoding='utf8')
    try:
        html = etree.HTML(data,parser=parser)
        table = html.xpath('//div[@class="rankItem"]/table')[0]
        trs = table.xpath('.//tr')[1:]
        for tr in trs:
            rank = tr.xpath('.//td[1]/p')[0].text
            urls = tr.xpath('.//td[2]/a/@href')
            url = urls[0] if urls else None
            universitys = tr.xpath('.//td[2]/a')
            if not universitys:
                universitys = tr.xpath('.//td[2]')
            university = universitys[0].text
            English_name = tr.xpath('.//td[3]/p')[0].text
            contry = tr.xpath('.//td[4]')[0].text
            yield {
                'rank':rank,
                'url':url,
                'university':university,
                'English_name':English_name,
                'contry':contry
            }
            print(rank,url,university,English_name,contry)
           # print(etree.tostring(table,encoding='utf8').decode('utf8'))
    except Exception as e:
        print(e)
        return  None

#
# def get_datail_info(url):
#     try:
#         resp =requests.get(url)
#         return  resp.text if resp.status_code==200 else None
#     except:
#         print()
#获得单个学校的信息方法::::: parse_detail_page
def parse_detail_page(data,rank,university):
    info_dict={
        'rank': rank,
        'university': university,
    }
    parser = etree.HTMLParser(encoding='utf8')
    html = etree.HTML(data,parser=parser)
    tables = html.xpath('.//dic[@class="infobox"]/table')
    table = tables[0] if tables else  None
    if not table:
        return info_dict
    trs = table.xpath('.//tr')
    for tr in trs:
        keys = tr.xpath('.//td[1]/p')
        key = keys[0].text if keys else None
        if not key:
            keys = tr.xpath('.//td[1]/p/a')
            key = keys[0].text if keys else None
        if key:
            values = tr.xpath('.//td[2]/p')
            value = values[0].text if values else ""
            if not value:
                values = tr.xpath('.//td[2]/p/a')
                value = values[0].text if values else ""
            info_dict.setdefault(key,value)
    yield info_dict

def main():
    data = get_page(rank_url)
    # print(data)  获得的是页面源码
    print(parse_page(data))
    if data:
       for info in  parse_page(data):
           url = info.get('url')
           print(url)
           if url:
               detail_info = get_page(url)
               print(detail_info )
               if detail_info:
                 for infos in parse_detail_page(detail_info,info.get('rank'),info.get('university')):
                     print(infos)
        # print(data)

if __name__ == '__main__':
    main()