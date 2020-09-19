html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# 引入pyquery
from  pyquery import PyQuery as pq
from lxml import  etree

# 使用pyquery获取处理的文本字符串
py_doc = pq(html)
# 获得所有的li标签
lis = py_doc('li')
for li in lis :
    print(etree.tostring(li,encoding='utf8').decode('utf8').strip())

# 引入pyquery
from pyquery import PyQuery as pq
# 使用pyquery初始化url https://www.baidu.com
doc = pq(url='https://www.baidu.com')
# 显示页面的head标签
print(doc('head'))
# 引入pyquery
from pyquery import PyQuery as pq
# # 使用文件初始化pyquery  如tencent.html
# doc = pq(filename='tencent.html')
# 获得所有的li标签
lis = doc('li')
for li in lis :
    print(etree.tostring(li,encoding='utf8').decode('utf8').strip())

html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''

# 利用css选择器获得所有的li标签 （使用层级选择器 id='container' class='list' li）
from pyquery import PyQuery as pq
doc1 = pq(html)
lis1 = doc1('#container .list li')
print(lis1)

# 利用find查找文本中的 class=list，并显示结果items的类型

# 在items中查找所有li标签，并显示结果类型

doc_1 = pq(html)
items = doc.find('.list')
print(type(items))

lis_2 = items('li')
# 继续上个例子，利用children方法查找items的子元素，并显示结果类型
it_c = items.children()
# 继续上个例子，利用children方法查找items的，具有class=active的子元素
it_c1 = items.children('.active')
doc1('.item-0.active')

a = doc('.item-0.active a')
a_text = a.text()
a1 =a.attr('href')

doc_1.html()



