# Newhouse-591-Web-Crawler 20231229

# dependency package
pip freeze > requirements.txt
pip install -r requirements.txt

# Conda Environment
conda env export > environment.yml
conda env create -f environment.yml

程式碼架構大致參考此篇
https://lucachuang.medium.com/591%E5%94%AE%E5%B1%8B%E7%B6%B2-python%E7%88%AC%E8%9F%B2-35f2b0cda067

然而大大事在2021開發，中間591網也歷經更新，因此舊有程式碼無法正確撈取欄位資料，
因此將重新編寫撈取資料程式碼，並增加proxy 加長sleep秒數等反爬蟲技術

專案中有兩個版本：
1. colab版本：只要依序執行，照著步驟繼續就可以正確運行
2. local版本：可能會需要額外安裝部分套件，但理應不存在什麼版本衝突。

## 主要用的反爬蟲技術
1. proxy 代理([Scraper API](https://www.scraperapi.com))
1. header 資訊
1. random sleep
