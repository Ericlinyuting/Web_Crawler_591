# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:18:11 2024

@author: 2293
"""

import pandas as pd
import numpy as np
import re
import geopandas as gp 
townname = ['成功鎮', '佳冬鄉', '麥寮鄉', '綠島鄉', '蘭嶼鄉', '田中鎮', '社頭鄉', 
            '竹田鄉', '萬丹鄉', '三灣鄉', '峨眉鄉', '南庄鄉', '太保市', '中埔鄉', 
            '番路鄉', '水上鄉', '員林市', '小港區', '蘇澳鎮', '五結鄉', '宜蘭市', 
            '壯圍鄉', '南竿鄉', '莒光鄉', '金寧鄉', '烏坵鄉', '羅東鎮', '員山鄉', 
            '冬山鄉', '三星鄉', '大同鄉', '竹東鎮', '新埔鎮', '關西鎮', '湖口鄉', 
            '芎林鄉', '橫山鄉', '北埔鄉', '尖石鄉', '五峰鄉', '龍井區', '大雅區', 
            '沙鹿區', '梧棲區', '湖西鄉', '金峰鄉', '太麻里鄉', '苗栗市', '卓蘭鎮', 
            '大湖鄉', '公館鄉', '銅鑼鄉', '頭屋鄉', '三義鄉', '西湖鄉', '造橋鄉', 
            '獅潭鄉', '泰安鄉', '彰化市', '和美鎮', '線西鄉', '伸港鄉', '秀水鄉', 
            '花壇鄉', '芬園鄉', '溪湖鎮', '東石鄉', '大村鄉', '埔鹽鄉', '埔心鄉', 
            '永靖鄉', '二水鄉', '二林鎮', '埤頭鄉', '芳苑鄉', '大城鄉', '竹塘鄉', 
            '溪州鄉', '南投市', '埔里鎮', '草屯鎮', '竹山鎮', '集集鎮', '名間鄉', 
            '鹿谷鄉', '中寮鄉', '魚池鄉', '國姓鄉', '水里鄉', '信義鄉', '仁愛鄉', 
            '斗六市', '斗南鎮', '虎尾鎮', '西螺鎮', '土庫鎮', '北港鎮', '古坑鄉', 
            '大埤鄉', '莿桐鄉', '林內鄉', '二崙鄉', '崙背鄉', '東勢鄉', '褒忠鄉', 
            '元長鄉', '水林鄉', '朴子市', '大林鎮', '民雄鄉', '溪口鄉', '新港鄉', 
            '六腳鄉', '義竹鄉', '鹿草鄉', '竹崎鄉', '梅山鄉', '大埔鄉', '阿里山鄉', 
            '屏東市', '潮州鎮', '長治鄉', '麟洛鄉', '九如鄉', '里港鄉', '鹽埔鄉', 
            '高樹鄉', '萬巒鄉', '內埔鄉', '新埤鄉', '崁頂鄉', '南州鄉', '琉球鄉', 
            '三地門鄉', '霧臺鄉', '瑪家鄉', '泰武鄉', '來義鄉', '春日鄉', '獅子鄉', 
            '鹿野鄉', '池上鄉', '延平鄉', '光復鄉', '瑞穗鄉', '富里鄉', '馬公市', 
            '白沙鄉', '西嶼鄉', '望安鄉', '七美鄉', '暖暖區', '大安區', '文山區', 
            '鹽埕區', '新興區', '前金區', '前鎮區', '頭城鎮', '南澳鄉', '竹北市', 
            '新豐鄉', '苑裡鎮', '通霄鎮', '竹南鎮', '後龍鎮', '鹿港鎮', '福興鄉', 
            '臺西鄉', '四湖鄉', '口湖鄉', '布袋鎮', '東港鎮', '枋寮鄉', '新園鄉', 
            '林邊鄉', '車城鄉', '滿州鄉', '枋山鄉', '牡丹鄉', '台東市', '卑南鄉', 
            '東河鄉', '吉安鄉', '壽豐鄉', '秀林鄉', '楠梓區', '鳳山區', '大寮區', 
            '大樹區', '大社區', '仁武區', '鳥松區', '岡山區', '橋頭區', '燕巢區', 
            '田寮區', '阿蓮區', '路竹區', '湖內區', '旗山區', '美濃區', '六龜區', 
            '甲仙區', '杉林區', '內門區', '茂林區', '桃源區', '那瑪夏區', '永和區', 
            '新店區', '土城區', '蘆洲區', '五股區', '坪林區', '平溪區', '烏來區', 
            '豐原區', '東勢區', '后里區', '神岡區', '新社區', '石岡區', '外埔區', 
            '大肚區', '和平區', '新營區', '鹽水區', '白河區', '後壁區', '麻豆區', 
            '下營區', '六甲區', '官田區', '大內區', '佳里區', '學甲區', '西港區', 
            '新化區', '新市區', '安定區', '玉井區', '楠西區', '南化區', '左鎮區', 
            '仁德區', '歸仁區', '關廟區', '龍崎區', '永康區', '北區', '林園區', 
            '茄萣區', '永安區', '彌陀區', '梓官區', '淡水區', '瑞芳區', '林口區', 
            '三芝區', '八里區', '大甲區', '大安區', '北門區', '安南區', '蘆竹區', 
            '龜山區', '復興區', '東區', '西區', '達仁鄉', '大武鄉', '關山鎮', 
            '海端鄉', '北區', '香山區', '礁溪鄉', '玉里鎮', '卓溪鄉', '頭份市', 
            '清水區', '南區', '東區', '安平區', '中西區', '大溪區', '八德區', 
            '桃園區', '大園區', '楊梅區', '七堵區', '仁愛區', '信義區', '中正區', 
            '中山區', '安樂區', '三峽區', '鶯歌區', '中和區', '樹林區', '深坑區', 
            '板橋區', '石碇區', '新莊區', '泰山區', '三重區', '雙溪區', '貢寮區', 
            '汐止區', '萬里區', '金山區', '石門區', '苓雅區', '三民區', '新屋區', 
            '觀音區', '北竿鄉', '東引鄉', '烈嶼鄉', '旗津區', '長濱鄉', '豐濱鄉', 
            '霧峰區', '大里區', '南區', '烏日區', '中區', '西區', '南屯區', '北區', 
            '西屯區', '北屯區', '潭子區', '信義區', '萬華區', '中正區', '松山區', 
            '大同區', '中山區', '士林區', '北投區', '花蓮市', '新城鄉', '善化區', 
            '山上區', '北斗鎮', '田尾鄉', '金城鎮', '金沙鎮', '金湖鎮', '柳營區', 
            '東山區', '七股區', '將軍區', '鼓山區', '左營區', '中壢區', '寶山鄉', 
            '東區', '恆春鎮', '東區', '太平區', '鳳林鎮', '萬榮鄉', '龍潭區', '平鎮區', '南港區', '內湖區']
def process_price_range(row):
    try:
        # 將字串根據"~"分割成兩部分
        prices = row["單價"].split("~")
        
        # 將兩部分轉換為浮點數
        price1 = float(prices[0])
        price2 = float(prices[1])
        
        # 計算平均值
        average_price = (price1 + price2) / 2
        
        # 將平均值轉換為整數
        return int(average_price) if average_price.is_integer() else average_price
    except (ValueError, IndexError,AttributeError):
        # 如果轉換失敗或索引錯誤，返回原始值
        return row["單價"]
def extract_county(row):
    try:
        # 使用正規表達式搜尋縣市名稱
        match = re.search(r"(台北市|新北市|桃園市|台中市|台南市|高雄市|基隆市|新竹市|嘉義市|新竹縣|苗栗縣|彰化縣|南投縣|雲林縣|嘉義縣|屏東縣|宜蘭縣|花蓮縣|台東縣|澎湖縣|金門縣|連江縣)", row["基地地址"])
        
        # 如果找到匹配，返回匹配的縣市名稱
        if match:
            return match.group(0)
        else:
            return None
    except (TypeError, AttributeError):
        # 如果發生錯誤，返回None
        return None
def extract_district(row):
    # 台灣縣市名稱列表
    town_name = townname
    for district in town_name:
        if district in row["基地地址"]:
            return district
    return None
def extract_SDW_brands(row):
    try:
        # 使用正規表達式搜尋指定的廠牌關鍵字前的文字
        matches = re.findall(r"(住友|EDS|KVM|JFE|EPS|新日鐵)", row["建材說明"])
        no_brand = re.findall(r"(位移型高韌性鋼板阻尼器)", row["建材說明"])
        # 如果找到匹配，返回匹配的文字
        if matches:
            return ", ".join(matches)
        elif no_brand:
            return "No Brand"
        else:
            return None
    except (TypeError, AttributeError):
        # 如果發生錯誤，返回None
        return None
def extract_SDB_brands(row):
    try:
        # 使用正規表達式搜尋指定的廠牌關鍵字前的文字
        matches = re.findall(r"(UBB|JEF)", row["建材說明"])
        no_brand = re.findall(r"(斜撐)", row["建材說明"])
        # 如果找到匹配，返回匹配的文字
        if matches:
            return ", ".join(matches)
        elif no_brand:
            return "No Brand"
        else:
            return None
    except (TypeError, AttributeError):
        # 如果發生錯誤，返回None
        return None
def extract_FVD_brands(row):
    try:
        # 使用正規表達式搜尋指定的廠牌關鍵字前的文字
        matches = re.findall(r"(Taylor|KYB|SENQCIA|瑪格巴)", row["建材說明"])
        no_brand = re.findall(r"(制震阻尼器|黏彈性阻尼器)", row["建材說明"])
        # 如果找到匹配，返回匹配的文字
        if matches:
            return ", ".join(matches)
        elif no_brand:
            return "No Brand"
        else:
            return None
    except (TypeError, AttributeError):
        # 如果發生錯誤，返回None
        return None
def AST(row):
    try:
        # 使用正規表達式搜尋指定的廠牌關鍵字前的文字
        matches = re.search(r"(制震宅)", row["建案標籤"])
        damper = re.search(r"(阻尼器)",row["建材說明"])
        # 如果找到匹配，返回匹配的文字
        if matches or damper:
            return True
        else:
            return False
    except (TypeError, AttributeError):
        # 如果發生錯誤，返回None
        return None

path = r"E:\CodeProject\591WebCrawler"
raw_data = pd.read_excel(path+"\\"+"newhouse591_data.xlsx")
raw_data.drop("Unnamed: 0",axis=1,inplace=True)

# region 處理單價
raw_data["單價"] = raw_data["單價"].str.replace("萬/坪", "")
raw_data["單價"] = raw_data.apply(process_price_range, axis=1)
# endregion

# region 處理縣市區域
raw_data["縣市"] = raw_data.apply(extract_county, axis=1)
raw_data["區域"] = raw_data.apply(extract_district, axis=1)
# endregion

# region 處理制震器
# AST_data = raw_data[raw_data["建案標籤"].str.contains("制震宅")]
raw_data["制震宅"] = raw_data.apply(AST,axis=1)
raw_data["建材說明"].str.replace("泰勒", "Taylor")
raw_data["建材說明"].str.replace("NS高韌性鋼板制震壁", "新日鐵制震壁")
# 創建新的欄位，並應用自定義函數
raw_data["制震壁"] = raw_data.apply(extract_SDW_brands, axis=1)
raw_data["斜撐"] = raw_data.apply(extract_SDB_brands, axis=1)
raw_data["阻尼器"] = raw_data.apply(extract_FVD_brands, axis=1)
raw_data["制震宅"] = np.where(raw_data["制震壁"].notna()|raw_data["斜撐"].notna()|raw_data["阻尼器"].notna(), True, raw_data["制震宅"])
# endregion

selling_data = raw_data[raw_data["建案標籤"].notna() & raw_data["建案標籤"].str.contains("在售")]
columns = ['建案名稱','單價', '單位','營造公司', '網址', '縣市','制震宅', '制震壁', '斜撐', '阻尼器']
data = selling_data[columns]
data.to_excel("ALL_data.xlsx")
AST_data = data[data["制震宅"].notna() & data["制震宅"]]
AST_data.to_excel("AST_data.xlsx")

