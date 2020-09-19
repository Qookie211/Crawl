# # 正则表达式
# # 使用***re, match匹配，学习使用基本的开头，结尾，单个字母，数字，空格的匹配
# # 显示匹配结果，了解匹配结果的基本属性
# import re
# content = 'Hello 123 4567 World_This is a Regex Demo'
# result = re.match('^Hello\s\d\d\d\s\d\d\d\d\sWorld_This\s\w\w\s\w\sRegex\sDemo$',content)
# print(result)
# result_1 = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}\s\w{2}\s\w\s\w{5}\s\w{4}$',content)
# print(result_1)
# # re.search 扫描整个字符串并返回第一个成功的匹配。
# result_2 = re.search('H.*?(\d+).*Demo',content)
# print(result_2)

import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

# 在 经典老歌列表中，找出li标签中，具有属性值class是active的歌手，及歌曲名
result_3 = re.search('<li.*?class="active".*?singer="(.*?)">(.*?)</a>',html,re.S)
if(result_3):
    print(result_3.group(1),result_3.group(2))
# 匹配第一个具有singer属性的li标签，并显示改标签对应的歌手，歌曲名
result_4 = re.search('<li.*?singer="(.*?)">(.*?)</a>',html,re.S)
if result_4:
    print(result_4.group(1),result_4.group(2))
# 如果不使用匹配模式re.S，表示li标签和歌手，歌曲名这些在同一行。(中间没有换行)
result_5 = re.search('<li.*?singer="(.*?)">(.*?)</a>',html)
if result_5:
    print(result_5.group(1),result_5.group(2))

# re.findall
# 搜索字符串，以列表形式返回全部能匹配的子串。
result_6 = re.findall('<li.*?singer="(.*?)">(.*?)</a>',html)
if result_6:
    print(result_6)

# 所有歌曲的链接，歌名，歌手，如果缺少就用空格表示\
# 正则中的()，可以表示整体，整体的有或者没有，可以用()?来表示，？表示没有或者一个
result_7 = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
print(result_7)
for alink,song,_ in result_7:
    url=""
    singer=""
    if(alink):
       r = re.search('<a.*?href="(.*?)".*?singer="(.*?)">',alink,re.S)
       url = r.group(1)
       singer = r.group(2)
    print(url,singer,song)

# re.sub
# 替换字符串中每一个匹配的子串后返回替换后的字符串。
# 去掉字符串中所有数字
import re
content = 'Extra stings Hello 1234567 World_This is a Regex Demo Extra stings'
result_8 = re.sub('\d+','x',content)
print(result_8)


