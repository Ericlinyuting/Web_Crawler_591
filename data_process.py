# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 15:18:11 2024

@author: 2293
"""

import pandas as pd
import re

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
        match = re.search(r"(台灣省|台灣|臺灣省|臺灣|台北市|新北市|桃園市|台中市|台南市|高雄市|基隆市|新竹市|嘉義市|新竹縣|苗栗縣|彰化縣|南投縣|雲林縣|嘉義縣|屏東縣|宜蘭縣|花蓮縣|台東縣|澎湖縣|金門縣|連江縣)", row["基地地址"])
        
        # 如果找到匹配，返回匹配的縣市名稱
        if match:
            return match.group(0)
        else:
            return None
    except (TypeError, AttributeError):
        # 如果發生錯誤，返回None
        return None
def extract_SDW_brands(row):
    try:
        # 使用正規表達式搜尋指定的廠牌關鍵字前的文字
        matches = re.findall(r"(住友|EDS|KVM|NS|JFE|EPS)", row["建材說明"])
        
        # 如果找到匹配，返回匹配的文字
        if matches:
            return ", ".join(matches)
        else:
            return None
    except (TypeError, AttributeError):
        # 如果發生錯誤，返回None
        return None
def extract_SDB_brands(row):
    try:
        # 使用正規表達式搜尋指定的廠牌關鍵字前的文字
        matches = re.findall(r"(UBB)", row["建材說明"])
        
        # 如果找到匹配，返回匹配的文字
        if matches:
            return ", ".join(matches)
        else:
            return None
    except (TypeError, AttributeError):
        # 如果發生錯誤，返回None
        return None
def extract_FVD_brands(row):
    try:
        # 使用正規表達式搜尋指定的廠牌關鍵字前的文字
        matches = re.findall(r"(Taylor|KYB)", row["建材說明"])
        
        # 如果找到匹配，返回匹配的文字
        if matches:
            return ", ".join(matches)
        else:
            return None
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

# region 處理單價
raw_data["縣市"] = raw_data.apply(extract_county, axis=1)
# endregion

# region 處理制震器
AST_data = raw_data[raw_data["建案標籤"].str.contains("制震宅")]
AST_data["建材說明"].str.replace("泰勒", "Taylor")
# 創建新的欄位，並應用自定義函數
AST_data["制震壁"] = AST_data.apply(extract_SDW_brands, axis=1)
AST_data["斜撐"] = AST_data.apply(extract_SDB_brands, axis=1)
AST_data["阻尼器"] = AST_data.apply(extract_FVD_brands, axis=1)
# region

#還要處理NS 新日鐵廠牌重複計算問題
# FVD_data = AST_data[AST_data["建材說明"].notna() & AST_data["建材說明"].str.contains("制震器")]