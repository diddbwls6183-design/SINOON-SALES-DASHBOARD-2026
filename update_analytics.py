import re, json

with open('index.html', encoding='utf-8') as f:
    c = f.read()

c = re.sub(r'const CUST_DATA=\[.*?\];',
    'const CUST_DATA=[{w:"1월",n:1589,r:199},{w:"2월",n:196,r:50},{w:"3월",n:1709,r:303},{w:"4월",n:477,r:190},{w:"5월",n:1499,r:561},{w:"6월",n:157,r:185},{w:"7월",n:515,r:430},{w:"8월",n:315,r:106},{w:"9월",n:15,r:5}];',
    c, flags=re.DOTALL)

c = re.sub(r'const CONV_DATA=\[.*?\];',
    'const CONV_DATA=[{w:"1월",v:289641,b:1778,o:1851,r:0.61},{w:"2월",v:198136,b:246,o:250,r:0.12},{w:"3월",v:359115,b:2001,o:2118,r:0.56},{w:"4월",v:119294,b:658,o:699,r:0.55},{w:"5월",v:172776,b:2023,o:2205,r:1.17},{w:"6월",v:74533,b:326,o:357,r:0.44},{w:"7월",v:124584,b:934,o:956,r:0.75},{w:"8월",v:100816,b:1792,o:427,r:0.42},{w:"9월",v:4395,b:62,o:21,r:0.46}];',
    c, flags=re.DOTALL)

cart8=[{"name":"Initial Necklace","exp":4048,"cart":194,"crate":4.79},{"name":"Pear Drop Necklace (Silver)","exp":1084,"cart":107,"crate":9.87},{"name":"Flare Skirt Layered Overall (Navy)","exp":2374,"cart":71,"crate":2.99},{"name":"Clarks X Cus Wallabee Charm Set (Maple Suede)","exp":1049,"cart":46,"crate":4.39},{"name":"Floral Jacquard Knit Pullover (Ivory)","exp":1405,"cart":43,"crate":3.06},{"name":"Clarks X Cus Wallabee Charm Set (Black Suede)","exp":908,"cart":43,"crate":4.74},{"name":"Rose Cosmetic Pouch (Green Mix)","exp":795,"cart":40,"crate":5.03},{"name":"Clarks X Cus Wallabee Charm Set (Cola Suede)","exp":863,"cart":39,"crate":4.52},{"name":"Romantic Mac Coat (Pink)","exp":1301,"cart":38,"crate":2.92},{"name":"[수지 착용] Graphic Mini Skirt (Cream)","exp":883,"cart":32,"crate":3.62},{"name":"Mini Apple Necklace Set (Silver Gold)","exp":662,"cart":32,"crate":4.83},{"name":"Double Floral Artwork Hood Zip-Up (Yellow)","exp":1012,"cart":31,"crate":3.06},{"name":"Balloon Puff Layered Sleeve (Charcoal)","exp":1602,"cart":29,"crate":1.81},{"name":"V-Neck Flare Knit (Black)","exp":1159,"cart":29,"crate":2.5},{"name":"Rose Drop Ring (Silver)","exp":399,"cart":28,"crate":7.02},{"name":"Cherry Lantern Ring (Silver)","exp":186,"cart":25,"crate":13.44},{"name":"Color Block Tiered Maxi Skirt (Black)","exp":1730,"cart":23,"crate":1.33},{"name":"Side Tie T-Shirt (Ivory)","exp":1007,"cart":23,"crate":2.28},{"name":"Braided One-Shoulder T-Shirt (Navy)","exp":650,"cart":22,"crate":3.38},{"name":"Bloom Brush Necklace (Silver Gold)","exp":438,"cart":22,"crate":5.02},{"name":"Lace Patch Sheer Knit (Pink)","exp":644,"cart":22,"crate":3.42},{"name":"Lace Patch Sheer Knit (Ivory)","exp":1396,"cart":22,"crate":1.58},{"name":"Cloven Garlic Necklace (Silver Gold)","exp":256,"cart":20,"crate":7.81},{"name":"Home Charm Necklace (Silver Gold)","exp":398,"cart":20,"crate":5.03},{"name":"Lace-Up Ribbon Knit (Beige)","exp":1050,"cart":20,"crate":1.9},{"name":"Rose Frill Sleep Mask (Yellow)","exp":611,"cart":19,"crate":3.11},{"name":"Rose Cotton Skirt (Light Blue)","exp":850,"cart":19,"crate":2.24},{"name":"Sinoon Smocking Flared Skirt (Navy)","exp":309,"cart":18,"crate":5.83},{"name":"Satin Lace Ribbon Onepiece (Moss Green)","exp":1496,"cart":18,"crate":1.2},{"name":"Tiny Ponies T-Shirt (Ivory)","exp":287,"cart":18,"crate":6.27}]
cart9=[{"name":"WOOL BLEND CREW SOCKS (5 COLORS)","exp":51,"cart":14,"crate":27.45},{"name":"Clarks X Cus Wallabee Charm Set (Maple Suede)","exp":318,"cart":8,"crate":2.52},{"name":"Clarks X Cus Wallabee Charm Set (Cola Suede)","exp":242,"cart":6,"crate":2.48},{"name":"Horse Charm Necklace (Silver Gold)","exp":21,"cart":5,"crate":23.81},{"name":"Ruffle String Bag Ver.2 (Black)","exp":9,"cart":4,"crate":44.44},{"name":"Rose Frill Hoodie Zipup (Rose)","exp":11,"cart":3,"crate":27.27},{"name":"SN Flower Overfit Cardigan (Cream)","exp":7,"cart":3,"crate":42.86},{"name":"Color Block Washed Work Jacket (Brown Purple)","exp":17,"cart":3,"crate":17.65},{"name":"Initial Necklace","exp":27,"cart":2,"crate":7.41},{"name":"WOOL BLEND CREW SOCKS (Melange Grey)","exp":9,"cart":2,"crate":22.22},{"name":"WOOL BLEND CREW SOCKS (Black)","exp":10,"cart":2,"crate":20.0},{"name":"Color Block Tiered Maxi Skirt (Black)","exp":39,"cart":2,"crate":5.13},{"name":"Lace Patch Sheer Knit (Pink)","exp":64,"cart":2,"crate":3.12}]
abd8=[{"name":"Initial Necklace","cart":194,"abd":161,"arate":82.99},{"name":"Pear Drop Necklace (Silver)","cart":107,"abd":91,"arate":85.05},{"name":"Flare Skirt Layered Overall (Navy)","cart":71,"abd":56,"arate":78.87},{"name":"Romantic Mac Coat (Pink)","cart":38,"abd":31,"arate":81.58},{"name":"Floral Jacquard Knit Pullover (Ivory)","cart":43,"abd":29,"arate":67.44},{"name":"Double Floral Artwork Hood Zip-Up (Yellow)","cart":31,"abd":28,"arate":90.32},{"name":"Clarks X Cus Wallabee Charm Set (Black Suede)","cart":43,"abd":28,"arate":65.12},{"name":"Mini Apple Necklace Set (Silver Gold)","cart":32,"abd":27,"arate":84.38},{"name":"Clarks X Cus Wallabee Charm Set (Cola Suede)","cart":39,"abd":27,"arate":69.23},{"name":"Rose Cosmetic Pouch (Green Mix)","cart":40,"abd":25,"arate":62.5},{"name":"[수지 착용] Graphic Mini Skirt (Cream)","cart":32,"abd":24,"arate":75.0},{"name":"V-Neck Flare Knit (Black)","cart":29,"abd":24,"arate":82.76},{"name":"Balloon Puff Layered Sleeve (Charcoal)","cart":29,"abd":22,"arate":75.86},{"name":"Clarks X Cus Wallabee Charm Set (Maple Suede)","cart":46,"abd":22,"arate":47.83},{"name":"Braided One-Shoulder T-Shirt (Navy)","cart":22,"abd":20,"arate":90.91},{"name":"Rose Drop Ring (Silver)","cart":28,"abd":20,"arate":71.43},{"name":"Color Block Tiered Maxi Skirt (Black)","cart":23,"abd":20,"arate":86.96},{"name":"Cherry Lantern Ring (Silver)","cart":25,"abd":19,"arate":76.0},{"name":"Lace Patch Sheer Knit (Ivory)","cart":22,"abd":19,"arate":86.36},{"name":"Cloven Garlic Necklace (Silver Gold)","cart":20,"abd":17,"arate":85.0}]
abd9=[{"name":"WOOL BLEND CREW SOCKS (5 COLORS)","cart":14,"abd":13,"arate":92.86},{"name":"Clarks X Cus Wallabee Charm Set (Maple Suede)","cart":8,"abd":5,"arate":62.5},{"name":"Ruffle String Bag Ver.2 (Black)","cart":4,"abd":4,"arate":100.0},{"name":"Horse Charm Necklace (Silver Gold)","cart":5,"abd":4,"arate":80.0},{"name":"Clarks X Cus Wallabee Charm Set (Cola Suede)","cart":6,"abd":4,"arate":66.67},{"name":"Rose Frill Hoodie Zipup (Rose)","cart":3,"abd":3,"arate":100.0},{"name":"SN Flower Overfit Cardigan (Cream)","cart":3,"abd":3,"arate":100.0}]

lines = c.split('\n')
for i,l in enumerate(lines):
    if l.startswith('const CART_BEST='):
        j = json.loads(l[len('const CART_BEST='):-1])
        j['8월'] = cart8
        j['9월'] = cart9
        lines[i] = 'const CART_BEST=' + json.dumps(j, ensure_ascii=False) + ';'
    if l.startswith('const CART_ABD='):
        j = json.loads(l[len('const CART_ABD='):-1])
        j['8월'] = abd8
        j['9월'] = abd9
        lines[i] = 'const CART_ABD=' + json.dumps(j, ensure_ascii=False) + ';'
c = '\n'.join(lines)

f9 = "  ,'9월':{period:'2026-09-01 ~ 2026-09-02',steps:[{stage:'방문',s:4395,cr:100.0,churn:43.4,churn_n:1908,cr_chg:None},{stage:'상세페이지 조회',s:2487,cr:56.6,churn:97.5,churn_n:2425,cr_chg:3.9},{stage:'장바구니 추가',s:62,cr:1.4,churn:61.3,churn_n:38,cr_chg:None},{stage:'주문서 작성',s:24,cr:0.5,churn:12.5,churn_n:3,cr_chg:-0.7},{stage:'주문 완료',s:21,cr:0.5,churn:4.8,churn_n:1,cr_chg:None},{stage:'결제 완료',s:20,cr:0.5,churn:0.0,churn_n:20,cr_chg:-0.6}]}"
f9 = f9.replace('None','null')
lines = c.split('\n')
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip() == ']},':
        ctx = '\n'.join(lines[max(0,i-3):i+3])
        if 'steps' in ctx and i > 4400:
            if "'9월'" not in '\n'.join(lines[i:i+3]):
                lines.insert(i+1, f9)
            break
c = '\n'.join(lines)

with open('index.html','w',encoding='utf-8') as f:
    f.write(c)
print('done')
