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

# 给BeautifulSoup指定一个解析器，这里指定的是lxml
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
# 1. 获取所有的tr标签
trs = soup.find_all('tr')
print(trs)
print('*'*100)
# 2. 获取第２个tr标签
tr_2 = soup.find_all('tr',limit=2)[1]
print(tr_2)
print('*'*100)
# 3. 获取所有class等于even的标签
# class_even = soup.find_all(class_='even')
# print(class_even)

# 3. 获取所有class等于even的标签 使用属性的方式
class_even =soup.find_all(attrs={'class':'even'})
print(class_even)
print('*'*100)

#4 通过类名查找  .类名
# 选择所有包含有类名是odd的标签
class_odd = soup.select('.odd')
print(class_odd)
print('*'*100)
#5 通过id查找 #id
# 查找id=prev的标签
id_prev = soup.select('#prev')[0]
print(id_prev)

#6 组合查找 不在同一节点的空格隔开，同一节点的不加空格
# 查找id=prev，并且属性class=noactive的标签
tag = soup.select('#prev ,noactice')[0]
print(tag)
#6 组合查找
# 查找标签tr -- td -- a，并且a具有属性href="javascript:;" 或 a具有id=prev
tag = soup.select('tr td a#prev')
print(tag)
#7 获取所有a标签的href属性
alist = soup.select('a')
for a in alist:
    print(a['href'])
#8 获取所有的职位文本
trs = soup.select('tr')[1:-1]
for tr in trs:
    infos = list(tr.stripped_strings)
    print(infos)