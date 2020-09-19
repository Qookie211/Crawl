from bs4 import BeautifulSoup
# html = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
# <p class="story">...</p>
# """
# # 引入beautifulsoup模块
# from bs4 import BeautifulSoup
#
# # 利用html字符串建立bs对象，并指定lxml解析方式
# soup = BeautifulSoup(html,'lxml')
#
# # 查看bs完善后的html内容
# print(soup.prettify())
#
# # 查看bs对象的title标签的内容
# print(soup.title.string)
#
# # 显示soup的title标签，以及它的数据类型
# print(soup.title)
# print(type(soup.title))
#
# # 显示soup的head标签
# print(soup.head)
#
# # 显示soup的p标签
# print(soup.p)
#
# # 获取soup的title标签的name属性
# print(soup.title.name)
#
# # 获取soup的p标签的name属性
# print(soup.p.attrs['name'])
# print(soup.p['name'])
#
# # 获取soup的p标签的内容
# print(soup.p.text)
#
# # 获取soup的head标签下的title标签的内容
# print(soup.head.title.string)
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
# soup = BeautifulSoup(html,'lxml')
# # 获取soup的p标签的内容
# import  re
# print(soup.p.contents)
# 获取soup的p标签的子标签
# print(soup.p.children)
# for idex,child in enumerate(soup.p.children):
#     print(idex,child)

# 获取soup的p标签的所有后代内容
# print(soup.p.descendants)
# for idex,child in enumerate(soup.p.descendants):
#     print(idex,child)

# 后去soup的p标签的父标签
# print(soup.p.parent)
# # 显示soup的a标签的所有父标签内容
# for idex,child in enumerate(soup.p.parent):
#     print(idex,child)
# # 显示soup的a标签的所有兄弟标签
# print(list(enumerate(soup.a.next_siblings)))


html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')

# 查找soup内所有的ul标签


# 查找soup下所有的ul标签，每个ul标签内所有的li标签
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
# 查找soup下所有的id=list-1的标签内容 -- 利用字典指定标签的属性和属性内容
soup.find_all(attrs={'id':'list-1'})
# 查找soup下所有的name=elements的标签内容 -- 利用字典指定标签的属性和属性内容

# 查找soup下所有的id='list-1'的标签内容 -- 利用属性关键字指定属性内容
print(soup.find_all(id='list-1'))
# 查找soup下所有的class_='element'的标签内容 -- 利用属性关键字指定属性内容

# 查找所有指定的文本内容，如text='Foo'
print(soup.find_all(text='Foo'))

# soup下第一个ul，及数据类型
print(soup.find('ul'))
print(type(soup.find('ul')))

# 查找一个不存在的标签
# find_parents() find_parent()
#
# find_parents()返回所有祖先节点，find_parent()返回直接父节点。
#
# find_next_siblings() find_next_sibling()
#
# find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
#
# find_previous_siblings() find_previous_sibling()
#
# find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。
#
# find_all_next() find_next()
#
# find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
#
# find_all_previous() 和 find_previous()
#
# find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点

# 使用css定位器，查找soup下类标签panel 下的类选择 panel-heading
print(soup.select('.panel,panel-heading'))
# 使用css定位器，查找标签ul下的li标签
print(soup.select('ul li'))

# css定位器，查找id=list-2下的element类选择
print(soup.select('#list-2,element'))
# 查找第一个ul标签
print(soup.select('ul')[0])
# css选择器，ul标签的li标签
for ul in soup.select('ul'):
    print(ul.select('li'))

# css选择器，每个ul标签的id属性
for ul in soup.select('ul'):
    print(ul.attrs['id'])

# 每个li标签的文本内容
for li in soup.select('li'):
    print(li.string)