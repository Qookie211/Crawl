import requests
from bs4 import BeautifulSoup
songUrl = ' http://f2.htqyy.com/play8/{}/mp3/9'
songUr2 = ' http://f2.htqyy.com/play8/{}/m4a/9'
all_url = 'http://www.htqyy.com/'

def get_all_sid():
    try:
        resp = requests.get(all_url).text
        soup = BeautifulSoup(resp,'lxml')
        ul = soup.find_all(class_='songList')[0]
        #ul_1 = soup.select('ul.songList')
        result = list()
        alist = ul.find_all('a')[:-1]
        for a in alist:
            sid = a.get('sid')
            if sid:
                result.append(sid)
        # print(result)
        return  result
    except Exception as e:
        print()
# def get_all_name():
#     try:
#         resp = requests.get(all_url).text
#         soup = BeautifulSoup(resp,'lxml')
#         ul = soup.find_all(class_='songList')[0]
#         result_name=list()
#         alist = ul.select('a[class=song]')
#         for a in alist:
#             title = a.get('title')
#             if title:
#                 result_name.append(title)
#         return result_name
#     except Exception as e:
#         print()
def download_a_song(song_id):
    url = songUrl.format(song_id)
    # print(url)
    resp  = requests.get(url).content
    print(len(resp))
    if len(resp)<5000:
        url = songUr2.format(song_id)
        resp = requests.get(url).content
    # names = get_all_name()
    # for name in names:
    with open(song_id+'.mp3','wb') as f:
         f.write(resp)
def main():
    sids= get_all_sid()
    print(sids)
    get_all_sid()
    if sids:
        for sid in sids:
            download_a_song(sid)

if __name__ == '__main__':
    main()