import re, json, sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("Original length:", len(content))

# ===== 1. CUST_DATA: update 8월, add 9월 =====
content = re.sub(r'\{w:"8월",n:\d+,r:\d+\}', '{w:"8월",n:315,r:106}', content)
if re.search(r'\{w:"9월",n:\d+,r:\d+\}', content):
    content = re.sub(r'\{w:"9월",n:\d+,r:\d+\}', '{w:"9월",n:15,r:5}', content)
else:
    content = re.sub(
        r'(\{w:"8월",n:315,r:106\})',
        r'\1,\n  {w:"9월",n:15,r:5}',
        content
    )
print("CUST_DATA updated")

# ===== 2. CONV_DATA: update 8월, add 9월 =====
content = re.sub(r'\{w:"8월",v:\d+,b:\d+,o:\d+,r:[\d.]+\}',
                 '{w:"8월",v:100816,b:1792,o:427,r:0.42}', content)
if re.search(r'\{w:"9월",v:\d+,b:\d+,o:\d+,r:[\d.]+\}', content):
    content = re.sub(r'\{w:"9월",v:\d+,b:\d+,o:\d+,r:[\d.]+\}',
                     '{w:"9월",v:4395,b:62,o:21,r:0.46}', content)
else:
    content = re.sub(
        r'(\{w:"8월",v:100816,b:1792,o:427,r:0\.42\})',
        r'\1,\n  {w:"9월",v:4395,b:62,o:21,r:0.46}',
        content
    )
print("CONV_DATA updated")

# ===== 3. CART_BEST: replace 8월 and 9월 =====
CB_8 = [
    {"name":"Initial Necklace","exp":4048,"cart":194,"crate":4.79},
    {"name":"Pear Drop Necklace (Silver)","exp":1084,"cart":107,"crate":9.87},
    {"name":"Flare Skirt Layered Overall (Navy)","exp":2374,"cart":71,"crate":2.99},
    {"name":"Clarks X Cus Wallabee Charm Set (Maple Suede)","exp":1049,"cart":46,"crate":4.39},
    {"name":"Floral Jacquard Knit Pullover (Ivory)","exp":1405,"cart":43,"crate":3.06},
    {"name":"Clarks X Cus Wallabee Charm Set (Black Suede)","exp":908,"cart":43,"crate":4.74},
    {"name":"Rose Cosmetic Pouch (Green Mix)","exp":795,"cart":40,"crate":5.03},
    {"name":"Clarks X Cus Wallabee Charm Set (Cola Suede)","exp":863,"cart":39,"crate":4.52},
    {"name":"Romantic Mac Coat (Pink)","exp":1301,"cart":38,"crate":2.92},
    {"name":"[수지 착용] Graphic Mini Skirt (Cream)","exp":883,"cart":32,"crate":3.62},
    {"name":"Mini Apple Necklace Set (Silver Gold)","exp":662,"cart":32,"crate":4.83},
    {"name":"Double Floral Artwork Hood Zip-Up (Yellow)","exp":1012,"cart":31,"crate":3.06},
    {"name":"Balloon Puff Layered Sleeve (Charcoal)","exp":1602,"cart":29,"crate":1.81},
    {"name":"V-Neck Flare Knit (Black)","exp":1159,"cart":29,"crate":2.5},
    {"name":"Rose Drop Ring (Silver)","exp":399,"cart":28,"crate":7.02}
]
CB_9 = [
    {"name":"WOOL BLEND CREW SOCKS (5 COLORS)","exp":51,"cart":14,"crate":27.45},
    {"name":"Clarks X Cus Wallabee Charm Set (Maple Suede)","exp":318,"cart":8,"crate":2.52},
    {"name":"Clarks X Cus Wallabee Charm Set (Cola Suede)","exp":242,"cart":6,"crate":2.48},
    {"name":"Horse Charm Necklace (Silver Gold)","exp":21,"cart":5,"crate":23.81},
    {"name":"Ruffle String Bag Ver.2 (Black)","exp":9,"cart":4,"crate":44.44},
    {"name":"Rose Frill Hoodie Zipup (Rose)","exp":11,"cart":3,"crate":27.27},
    {"name":"SN Flower Overfit Cardigan (Cream)","exp":7,"cart":3,"crate":42.86},
    {"name":"Color Block Washed Work Jacket (Brown Purple)","exp":17,"cart":3,"crate":17.65},
    {"name":"Initial Necklace","exp":27,"cart":2,"crate":7.41},
    {"name":"WOOL BLEND CREW SOCKS (Melange Grey)","exp":9,"cart":2,"crate":22.22},
    {"name":"WOOL BLEND CREW SOCKS (Black)","exp":10,"cart":2,"crate":20.0},
    {"name":"Color Block Tiered Maxi Skirt (Black)","exp":39,"cart":2,"crate":5.13},
    {"name":"Lace Patch Sheer Knit (Pink)","exp":64,"cart":2,"crate":3.12},
    {"name":"Sinoon Logo Card Wallet (Black)","exp":8,"cart":1,"crate":12.5},
    {"name":"V-Neck Basic Knit (Melange Grey)","exp":1,"cart":1,"crate":100.0}
]

# Find CART_BEST line and update it
cb_match = re.search(r'const CART_BEST=(\{.*?\});', content)
if cb_match:
    try:
        cb_data = json.loads(cb_match.group(1))
    except:
        cb_data = {}
    cb_data['8월'] = CB_8
    cb_data['9월'] = CB_9
    new_cb = 'const CART_BEST=' + json.dumps(cb_data, ensure_ascii=False) + ';'
    content = content[:cb_match.start()] + new_cb + content[cb_match.end():]
    print("CART_BEST updated")
else:
    print("WARNING: CART_BEST not found")

# ===== 4. CART_ABD: replace 8월 and 9월 =====
CA_8 = [
    {"name":"Initial Necklace","cart":194,"abd":161,"arate":82.99},
    {"name":"Pear Drop Necklace (Silver)","cart":107,"abd":91,"arate":85.05},
    {"name":"Flare Skirt Layered Overall (Navy)","cart":71,"abd":56,"arate":78.87},
    {"name":"Romantic Mac Coat (Pink)","cart":38,"abd":31,"arate":81.58},
    {"name":"Floral Jacquard Knit Pullover (Ivory)","cart":43,"abd":29,"arate":67.44},
    {"name":"Double Floral Artwork Hood Zip-Up (Yellow)","cart":31,"abd":28,"arate":90.32},
    {"name":"Clarks X Cus Wallabee Charm Set (Black Suede)","cart":43,"abd":28,"arate":65.12},
    {"name":"Mini Apple Necklace Set (Silver Gold)","cart":32,"abd":27,"arate":84.38},
    {"name":"Clarks X Cus Wallabee Charm Set (Cola Suede)","cart":39,"abd":27,"arate":69.23},
    {"name":"Rose Cosmetic Pouch (Green Mix)","cart":40,"abd":25,"arate":62.5},
    {"name":"[수지 착용] Graphic Mini Skirt (Cream)","cart":32,"abd":24,"arate":75.0},
    {"name":"V-Neck Flare Knit (Black)","cart":29,"abd":24,"arate":82.76},
    {"name":"Balloon Puff Layered Sleeve (Charcoal)","cart":29,"abd":22,"arate":75.86},
    {"name":"Clarks X Cus Wallabee Charm Set (Maple Suede)","cart":46,"abd":22,"arate":47.83},
    {"name":"Braided One-Shoulder T-Shirt (Navy)","cart":22,"abd":20,"arate":90.91}
]
CA_9 = [
    {"name":"WOOL BLEND CREW SOCKS (5 COLORS)","cart":14,"abd":13,"arate":92.86},
    {"name":"Clarks X Cus Wallabee Charm Set (Maple Suede)","cart":8,"abd":5,"arate":62.5},
    {"name":"Ruffle String Bag Ver.2 (Black)","cart":4,"abd":4,"arate":100.0},
    {"name":"Horse Charm Necklace (Silver Gold)","cart":5,"abd":4,"arate":80.0},
    {"name":"Clarks X Cus Wallabee Charm Set (Cola Suede)","cart":6,"abd":4,"arate":66.67},
    {"name":"Rose Frill Hoodie Zipup (Rose)","cart":3,"abd":3,"arate":100.0},
    {"name":"SN Flower Overfit Cardigan (Cream)","cart":3,"abd":3,"arate":100.0},
    {"name":"WOOL BLEND CREW SOCKS (Black)","cart":2,"abd":2,"arate":100.0},
    {"name":"Color Block Washed Work Jacket (Brown Purple)","cart":3,"abd":2,"arate":66.67},
    {"name":"Lace Patch Sheer Knit (Pink)","cart":2,"abd":2,"arate":100.0},
    {"name":"Sinoon Logo Card Wallet (Black)","cart":1,"abd":1,"arate":100.0},
    {"name":"V-Neck Basic Knit (Melange Grey)","cart":1,"abd":1,"arate":100.0},
    {"name":"[우기 착용] Rose Frill Mini Skirt (White)","cart":1,"abd":1,"arate":100.0},
    {"name":"Wool-Blend Pleated Knit Dress (Grey)","cart":1,"abd":1,"arate":100.0},
    {"name":"Sinoon Pleated Maxi Skirt (Beige)","cart":1,"abd":1,"arate":100.0}
]

ca_match = re.search(r'const CART_ABD=(\{.*?\});', content)
if ca_match:
    try:
        ca_data = json.loads(ca_match.group(1))
    except:
        ca_data = {}
    ca_data['8월'] = CA_8
    ca_data['9월'] = CA_9
    new_ca = 'const CART_ABD=' + json.dumps(ca_data, ensure_ascii=False) + ';'
    content = content[:ca_match.start()] + new_ca + content[ca_match.end():]
    print("CART_ABD updated")
else:
    print("WARNING: CART_ABD not found")

# ===== 5. FUNNEL_DATA 9월: insert after 8월 block =====
FUNNEL_9 = """\n  '9월':{
    period:'2026-09-01 ~ 2026-09-02',
    steps:[
      {stage:'방문',s:4395,cr:100.0,churn:43.4,churn_n:1908,cr_chg:null},
      {stage:'상세페이지 조회',s:2487,cr:56.6,churn:97.5,churn_n:2425,cr_chg:3.9},
      {stage:'장바구니 추가',s:62,cr:1.4,churn:61.3,churn_n:38,cr_chg:null},
      {stage:'주문서 작성',s:24,cr:0.5,churn:12.5,churn_n:3,cr_chg:-0.7},
      {stage:'주문 완료',s:21,cr:0.5,churn:4.8,churn_n:1,cr_chg:null},
      {stage:'결제 완료',s:20,cr:0.5,churn:0.0,churn_n:20,cr_chg:-0.6}
    ]}"""

# Remove any existing 9월 FUNNEL block (bad or good)
content = re.sub(r"\s*,?'9월':\{.*?\]\}", '', content, flags=re.DOTALL)

# Find FUNNEL_DATA and 8월 block
fd_start = content.find('var FUNNEL_DATA=')
if fd_start == -1:
    fd_start = content.find('FUNNEL_DATA=')

if fd_start != -1:
    m8_pos = content.find("'8월':{", fd_start)
    if m8_pos != -1:
        steps_start = content.find('steps:[', m8_pos)
        depth = 0
        i = steps_start + len('steps:')
        while i < len(content):
            if content[i] == '[':
                depth += 1
            elif content[i] == ']':
                depth -= 1
                if depth == 0:
                    j = i + 1
                    while j < len(content) and content[j] in ' \n\r':
                        j += 1
                    if content[j] == '}':
                        k = j + 1
                        while k < len(content) and content[k] in ' ,':
                            k += 1
                        content = content[:i] + ']},' + FUNNEL_9 + content[k:]
                        print("FUNNEL_DATA 9월 inserted after 8월 block")
                    break
            i += 1
    else:
        print("WARNING: '8월':{ not found in FUNNEL_DATA")
else:
    print("WARNING: FUNNEL_DATA not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! Final length:", len(content))

# Verify
if "'9월':{" in content and 'FUNNEL_DATA' in content:
    idx = content.find('FUNNEL_DATA')
    idx9 = content.find("'9월':{", idx)
    if idx9 > 0:
        print("FUNNEL 9월 block found at position", idx9)
        print(content[idx9:idx9+100])
