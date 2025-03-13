import requests
import re

def extract_h2_with_re(url):
    # 發送HTTP請求以獲取網頁內容
    response = requests.get(url)
    if response.status_code == 200:
        # 使用正則表達式查找所有<div class="ProductCardNormalGrid__viewBox__1JSHC">中的<h2>標籤的內容
        pattern = r'<div class="ProductCardNormalGrid__viewBox__1JSHC">.*?<h2>(.*?)</h2>'
        h2_contents = re.findall(pattern, response.text, re.DOTALL)
        return h2_contents
    else:
        return None
# 執行
url = "https://www.asus.com/tw/laptops/for-gaming/rog-republic-of-gamers/filter?SubSeries=ROG-Zephyrus"
h2_contents_re = extract_h2_with_re(url)
print(h2_contents_re)