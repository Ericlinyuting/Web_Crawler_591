# 591 新建案爬蟲

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)

---

## 專案簡介

針對台灣 [591 新建案](https://newhouse.591.com.tw) 平台開發的網路爬蟲，自動批次擷取新建案的基本資訊、地址、格局、建材及制震系統等欄位，並輸出為 Excel 供後續分析使用。

原始程式架構參考 [此篇文章](https://lucachuang.medium.com/591%E5%94%AE%E5%B1%8B%E7%B6%B2-python%E7%88%AC%E8%9F%B2-35f2b0cda067)（2021 年版），惟 591 網站歷經改版，欄位結構已大幅變動，故重新編寫資料擷取邏輯，並強化反爬蟲機制。

---

## 功能特色

- **批次爬取建案列表**：透過 591 搜尋 API 自動分頁，取得所有在售建案 ID
- **完整建案資訊擷取**：建案名稱、單價、地址、格局規劃、建材說明、投資建設、棟戶樓層等
- **制震系統辨識**：自動標記制震壁（住友、EDS、KVM…）、斜撐（UBB、JEF）、阻尼器（Taylor、KYB…）等品牌
- **地址解析**：從地址字串自動拆分縣市、區域（支援全台 200+ 行政區）
- **進度追蹤**：每完成 5% 自動儲存中間結果，降低中斷損失
- **反爬蟲措施**：Proxy 輪換、偽造 User-Agent、隨機 Sleep 延遲

---

## 輸出檔案

| 檔案 | 說明 |
|------|------|
| `newhouse591_data.xlsx` | 原始爬取資料（所有建案） |
| `ALL_data.xlsx` | 清洗後資料（僅保留「在售」狀態） |
| `AST_data.xlsx` | 篩選後資料（制震宅建案） |

---

## 技術棧

| 套件 | 用途 |
|------|------|
| [requests](https://docs.python-requests.org) | HTTP 請求 |
| [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) | HTML 解析 |
| [Pandas](https://pandas.pydata.org) | 資料處理與 Excel 匯出 |
| [Scraper API](https://www.scraperapi.com) | Proxy 代理（反爬蟲） |

---

## 反爬蟲機制

1. **Proxy 代理**：使用 [Scraper API](https://www.scraperapi.com) 輪換 IP
2. **偽造 Header**：模擬 Chrome 瀏覽器 User-Agent
3. **隨機 Sleep**：每次請求間隔 5–15 秒，避免頻率觸發封鎖

---

## 使用方式

提供兩個版本，擇一執行：

### Google Colab 版（建議新手）
開啟 `newhouse591_colab.ipynb`，依序執行儲存格即可。

### 本地版
```bash
# 1. 安裝相依套件
pip install -r requirements.txt

# 2. 開啟 Notebook
jupyter notebook newhouse591_local.ipynb
```

### Conda 環境（選用）
```bash
conda env create -f environment.yml
conda activate <env_name>
jupyter notebook newhouse591_local.ipynb
```

> 需自行申請 [Scraper API](https://www.scraperapi.com) 的 API Key 並填入程式碼中。
