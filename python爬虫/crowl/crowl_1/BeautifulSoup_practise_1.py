html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tr class="h">
        <td class="l" width="374">职位名称</td>
        <td>职位类别</td>
        <td>人数</td>
        <td>地点</td>
        <td>发布时间</td>
    </tr>

    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=44650&keywords=python&tid=0&lid=2175">29310-腾讯云智慧零售交付架构师（上海）</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>上海</td>
        <td>2018-10-16</td>
    </tr>

    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=44643&keywords=python&tid=0&lid=2175">25927-移动游戏测试经理（上海）</a></td>
        <td>技术类</td>
        <td>2</td>
        <td>上海</td>
        <td>2018-10-16</td>
    </tr>

    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=44633&keywords=python&tid=0&lid=2175">PCG09-内容平台算法组TeamLeader</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>上海</td>
        <td>2018-10-16</td>
    </tr>

    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=44638&keywords=python&tid=0&lid=2175">25924-视频图像算法高级研究员（上海）</a></td>
        <td>技术类</td>
        <td>2</td>
        <td>上海</td>
        <td>2018-10-16</td>
    </tr>

    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=44375&keywords=python&tid=0&lid=2175">19332-数据挖掘组leader（上海）</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>上海</td>
        <td>2018-10-16</td>
    </tr>

    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=44260&keywords=python&tid=0&lid=2175">19332-企点大数据开发工程师（上海）</a></td>
        <td>技术类</td>
        <td>2</td>
        <td>上海</td>
        <td>2018-10-16</td>
    </tr>

    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=44163&keywords=python&tid=0&lid=2175">25927-应用开发高级工程师（上海）</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>上海</td>
        <td>2018-10-16</td>
    </tr>

    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=44106&keywords=python&tid=0&lid=2175">25927-自然语言处理高级工程师（上海）</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>上海</td>
        <td>2018-10-16</td>
    </tr>

    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=43961&keywords=python&tid=0&lid=2175">20503-优图专项测试工程师（上海）</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>上海</td>
        <td>2018-10-16</td>
    </tr>

    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=43957&keywords=python&tid=0&lid=2175">20503-AI应用Linux后台研发工程师（上海）</a></td>
        <td>技术类</td>
        <td>1</td>
        <td>上海</td>
        <td>2018-10-16</td>
    </tr>

    <tr class="f">
        <td colspan="5">
            <div class="left">共<span class="lightblue total">39</span>个职位</div>
            <div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?keywords=python&tid=0&lid=2175&start=10#a">2</a><a href="position.php?keywords=python&tid=0&lid=2175&start=20#a">3</a><a href="position.php?keywords=python&tid=0&lid=2175&start=30#a">4</a><a href="position.php?keywords=python&tid=0&lid=2175&start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
            <div class="clr"></div>
        </td>
    </tr>
</table>
"""
# 引入beautifulsoup模块
from bs4 import BeautifulSoup

# 给BeautifulSoup加载需要获取内容的文档，并指定一个解析器，如lxml
soup = BeautifulSoup(html,'lxml')
# 如果不指定解析器，则用BeautifulSoup自己的解析器

# 1. 获取所有的tr标签
print(soup.find_all('tr'))

# 2. 获取第２个tr标签  可以使用limit指定获得几个标签
print(soup.find_all('tr',limit=2)[1])
# 3. 获取所有class等于even的标签
print(soup.find_all('tr',attrs={'class':'even'}))

# 3. 获取所有class等于even的标签 -- 使用attrsl来实现

# 4. 将所有id等于prev，class也等于noactive的a标签提取出来
print(soup.find_all('a',id='prev',class_='noactive'))
#4 上例采用attrs来实现

# 5. 获取所有a标签的href属性
a_s = soup.find_all('a')
for a in a_s:
    print(a)
    print(a['href'])
    print('$'*100)


# 6. 获取所有的职位信息（纯文本）

# 分析： 第一个tr不需要, class='f'也不要
trs = soup.find_all('tr')[1:]
trs = [tr for tr in trs if tr['class'][0]!='f']
postion_list=list()
for tr in trs:
    tds = tr.find_all('td')
    url = tds[0].find('a')['href']
    title = tds[1].string
    category = tds[2].string
    city = tds[3].string
    pubtime = tds[4].string

    postion = {
        'url':"https://hr.tencent.com/"+url,
        'title':title,
        'category':category,
        'city':city,
        'pubtime':pubtime
    }
    postion_list.append(postion)
print(postion_list)
# 6. 获取所有的职位信息（纯文本）,直接获取标签文本内容的方式。 标签.string, strings, stripped_strings, get_text()....

trs = soup.find_all('tr')[1:]
trs = [tr for tr in trs if tr['class'][0]!='f']
for tr in trs:
    print(tr.text)
    infos = list(tr.stripped_strings)
    print(infos)
# 分析： 第一个tr不需要, class='f'也不要
