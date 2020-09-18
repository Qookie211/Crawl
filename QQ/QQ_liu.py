import json
from urllib.error import HTTPError

import requests

url ='https://user.qzone.qq.com/proxy/domain/m.qzone.qq.com/cgi-bin/new/get_msgb?uin=3121791866&hostUin=271016840&num=10&start=20&hostword=0&essence=1&r=0.7475786995170415&iNotice=0&inCharset=utf-8&outCharset=utf-8&format=jsonp&ref=qzone&g_tk=702310148&qzonetoken=83907f31331acb439329fc9af2a80584480d5cb6978f13e901db7390711f0f667ee9a4df519dde0c2e11a1&g_tk=702310148'

def get_url(url):
    headers = {
        'cookie': 'pgv_pvi=1777660928; RK=vDogJrxMta; ptcz=28db73cec5ed132bc02c5fa88d804f39e4e11dd4008f3b69a6f27df4740e6433; zzpaneluin=; zzpanelkey=; pgv_si=s3935411200; _qpsvr_localtk=0.9503075270716932; uin=o3121791866; skey=@QC1QmWMEA; p_uin=o3121791866; pt4_token=4ji6IFM6FvqjXlb49G-Gp39KzgdPIxBKChNqLX5WeC8_; p_skey=wN*Tau8GQw6OvrXMcFUOF69ZApyLfwGJiEybaYX-ma8_; Loading=Yes; __Q_w_s_hat_seed=1; pgv_pvid=8052285540; pgv_info=ssid=s9233872728; __Q_w_s__QZN_TodoMsgCnt=1',
        'user - agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 76.0.3809.100Safari / 537.36'
    }
    try:
        resp = requests.get(url, headers=headers)
        return resp.text if resp.status_code == 200 else None
    except requests.exceptions.ConnectionError:
        print("error")
    except Exception as  e:
        print(e)
        print("error!")

def get_total(url):
    data = get_url(url)
    data_json = json.loads(data[10:-2])
    all_data = data_json.get('data')
    data_total = int(all_data.get('total'))
    return data_total

if __name__ == '__main__':
    data = get_url(url)
    # data = json.loads(data)
    data_json = json.loads(data[10:-2])
    all_data = data_json.get('data')
    id_comentList = all_data.get('commentList')
    for id_1 in id_comentList:
        print(id_1.get('pubtime'))
        print(id_1.get('ubbContent'))
    data_total = get_total(url)
    print(data_total)

