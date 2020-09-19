from lxml import etree
parser = etree.HTMLParser(encoding='utf8')
html = etree.parse('1.html',parser=parser)
divs = html.xpath('//div[@class="e"]')
position_list = []
for div in  divs:
    # print(div)
    titles = div.xpath('.//span[@class="jname at"]/text()')[0]
    # print(titles)
    # for title in titles:
    #     print(title)
    pubtimes= div.xpath('.//span[@class="time"]/text()')[0]
    # for pubtime in pubtimes:
    #     print(pubtime)
    sals = div.xpath('.//span[@class="sal"]/text()')
    # for sal in sals:
    #     print(sal)
    dats_city = div.xpath('.//span[@class="d at"]/text()')[0]
    # print(dats_city)
    # for dat_city in dats_city:
    #     print(dat_city)
    numbers = div.xpath('.//p[@class="dc at"]/text()')[0]
    # for number in numbers:
    #     print(number)
    elecits = div.xpath('.//p[@class="int at"]/text()')[0]
    # for elecit in elecits:
    #     print(elecit)
    position = {
        # 'url':urls,
        'title':titles,
        'category':sals,
        'number':numbers,
        'city':dats_city,
        'pubtime':pubtimes
    }
    position_list.append(position)

for position_r in position_list:
    print(position_r)

