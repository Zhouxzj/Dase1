import re

import pandas as pd

data = pd.read_excel(r'D:\Dase1\final\豆瓣电影Top250.xlsx')
data = data.iloc[:, :]
ranks = data['rank'].tolist()
years = data['years'].tolist()
locations = data['location'].tolist()
styles = data['type'].tolist()
nums = data['rating_num'].tolist()
comments = data['comments'].tolist()
USAs = []
UKs = []
Japans = []
Koreans = []
Frances = []
CNs = []
Other_countries = []
# 动画、剧情、爱情、动作、科幻、喜剧、冒险、历史
cartoons = []
features = []
loves = []
moves = []
sfs = []
comics = []
advs = []
histories = []

for location in locations:
    tag = 1
    if re.search(pattern="美国", string=location) is not None:
        tag = 0
        USAs.append(location)
    if re.search(pattern="英国", string=location) is not None:
        tag = 0
        UKs.append(location)
    if re.search(pattern="日本", string=location) is not None:
        tag = 0
        Japans.append(location)
    if re.search(pattern="韩国", string=location) is not None:
        tag = 0
        Koreans.append(location)
    if re.search(pattern="法国", string=location) is not None:
        tag = 0
        Frances.append(location)
    if re.search(pattern="中国", string=location) is not None:
        tag = 0
        CNs.append(location)
    if tag == 1:
        Other_countries.append(location)

countries = []
countries.append({
    "USA": len(USAs),
    "UK": len(UKs),
    "CN": len(CNs),
    "Korean": len(Koreans),
    "France": len(Frances),
    "Japan": len(Japans),
    "Else": len(Other_countries)
})

for style in styles:
    tag = 1
    if re.search(pattern="剧情", string=style) is not None:
        tag = 0
        features.append(style)
    if re.search(pattern="爱情", string=style) is not None:
        tag = 0
        loves.append(style)
    if re.search(pattern="科幻", string=style) is not None:
        tag = 0
        sfs.append(style)
    if re.search(pattern="动画", string=style) is not None:
        tag = 0
        cartoons.append(style)
    if re.search(pattern="动作", string=style) is not None:
        tag = 0
        moves.append(style)
    if re.search(pattern="历史", string=style) is not None:
        tag = 0
        histories.append(style)
    if re.search(pattern="冒险", string=style) is not None:
        tag = 0
        advs.append(style)
    if re.search(pattern="喜剧", string=style) is not None:
        tag = 0
        comics.append(style)

Kinds = []
Kinds.append({
    "爱情": len(loves),
    "剧情": len(features),
    "动作": len(moves),
    "科幻": len(sfs),
    "历史": len(histories),
    "动画": len(cartoons),
    "冒险": len(advs),
    "喜剧": len(comics)
})

df = pd.DataFrame(countries)
# 通过DataFrame来构造数据列表用于形成Excel文件
df.to_excel("./豆瓣电影Top250国家分布.xlsx")

df = pd.DataFrame(Kinds)
# 通过DataFrame来构造数据列表用于形成Excel文件
df.to_excel("./豆瓣电影Top250剧情分布.xlsx")

