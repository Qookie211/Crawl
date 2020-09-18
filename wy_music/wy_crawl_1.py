import os
import urllib
from urllib import request
import  requests
from bs4 import  BeautifulSoup
url ='https://music.163.com/playlist?id=2182968685'
def get_url_page(url):

    headers = {
                  'accept': '* / *',
                  'accept - encoding': 'gzip, deflate, br',
                  'accept - language': 'zh - CN, zh;q = 0.9',
                  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    try:
        resp =requests.get(url,headers=headers)
        return resp.text if resp.status_code==200 else None
    except Exception as e:
        print(e)
        return  None
def parseCookie(string):
    string = string.replace("document.cookie='", "")
    clearance = string.split(';')[0]
    return {clearance.split('=')[0]: clearance.split('=')[1]}
def get_songid(html):
    soup = BeautifulSoup(html,'lxml')
    ul = soup.find('ul', {'class': 'f-hide'})
    music_ids = []
    for music in ul.find_all('a'):
        list = []
        musicUrl = 'http://music.163.com/song/media/outer/url' + music['href'][5:]+".mp3"
       # ' http: // music.163.com / song / media / outer / url?id = 29593937.mp3'
        print(musicUrl)
        musicName = music.text
        list.append(musicName)
        list.append(musicUrl)
        music_ids.append(list)
    return music_ids
def download_a_song(lists):
    download_path = os.getcwd() + r"\download/"
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    filename = download_path
    print(filename)
    for i in lists:
        url = i[1]
        name = i[0]
        try:
            print('正在下载', name)
            urllib.request.urlretrieve(url,'./%s.mp3'% name)

            print('{0}下载成功'.format(name))
        except:
            print('{0}下载失败'.format(name))
if __name__ == '__main__':
    data =get_url_page(url)
    sids = get_songid(data)
    download_a_song(sids)