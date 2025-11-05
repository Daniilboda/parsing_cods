import json

from bs4 import BeautifulSoup
import lxml
import requests
#
# url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}
# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# with open("food.html", "w", encoding="utf-8") as file_w:
#     print(src, file=file_w)


# with open("food.html", "r", encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_products_href = soup.find_all(class_='mzr-tc-group-item-href')
#
#
# all_cat_dict = {}
# for element in all_products_href:
#     element_txt = element.text
#     element_href = 'https://health-diet.ru' + element.get('href')
#     all_cat_dict[element_txt] = element_href
#
# print(all_cat_dict)
# with open('all_cat_dict.json', 'w', encoding='utf-8') as file_w:
#     json.dump(all_cat_dict, file_w, indent=4, ensure_ascii=False)

with open('all_cat_dict.json', 'r', encoding='utf-8') as file:
    all_categories = json.load(file)

for cat_name, cat_href in all_categories.items():
    rep = [' ', ',', '-']
    for el in rep:
        if el in cat_name:
            cat_name = cat_name.replace(el, '_')
    print(cat_name)
    req = requests.get(url=cat_href, headers=headers)
    src = req.text