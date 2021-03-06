# Load the datasets
%run setting_environment.py

# input 建案網址 return 建案建案詳情欄位
# 產出為建案名與12個建案資訊
def getData(url):
    request_url='https://newhouse.591.com.tw/home/housing/info?hid='+str(url).strip()
    headers=headers
    res=requests.get(request_url, headers = headers)
    #bs=BeautifulSoup(res.text,'html.parser')

    if res.status_code == 200:
        bs=BeautifulSoup(res.text,'html.parser')
        #先宣告變數為NULL 若無撈到資料則寫入NULL
        title='NULL'
        size='NULL'
        htype='NULL'
        htype2='NULL'
        htype3='NULL'
        htype4='NULL'
        htype5='NULL'
        htype6='NULL'
        htype7='NULL'
        htype8='NULL'
        htype9='NULL'
        htype10='NULL'
        htype11='NULL'

        # 利用 beautfiulsoup 的 find function 利用 css selector 定位 並撈出指定資料
        title=bs.find('h1').text
        size=bs.find("dl", {'class':"clearfix"}).findNext("dd").text.strip()
        htype=bs.find("dt", text="建案類別：").findNext("dd").string.strip()
        htype2=bs.find("dt", text="建物形態：").findNext("dd").string.strip().replace(' ', '').replace('\n', '、')
        htype3=bs.find("dt", text="公開銷售：").findNext("dd").string.strip()
        htype4=bs.find("dt", text="基地地址：").findNext("dd").contents[0].string.strip()
        htype5=bs.find("dt", text="交屋屋況：").findNext("dd").string.strip()
        htype6=bs.find("div",{'class':"flex_5 stonefont"}).findNext('span',{'class':''}).text.strip().replace(' ', '')
        htype7=bs.find("dt", text="投資建設：").findNext("dd").string.strip()
        htype8=bs.find("dt", text="營造公司：").findNext("dd").string.strip()
        htype9=bs.find("dt", text="棟戶規劃：").findNext("dd").string.strip()
        htype10=bs.find("dt", text="樓層規劃：").findNext("dd").string.strip()
        htype11=bs.find("dt", text="用途規劃：").findNext("dd").string.strip()
                
        return title,size,htype, htype2, htype3, htype4, htype5, htype6, htype7, htype8, htype9, htype10, htype11
    else:
        print('link expired:', url)
        return 404, 404, 404, 404, 404, 404, 404
