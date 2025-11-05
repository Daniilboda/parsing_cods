import json
from bs4 import BeautifulSoup
import lxml
import requests
import csv
from time import sleep
import random
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
iter_count = int(len(all_categories)) - 1
print(f'Всего иттераци: {iter_count}')
counter = 0

for cat_name, cat_href in all_categories.items():
    if counter == 0:
        rep = [' ', ',', '-']
        for el in rep:
            if el in cat_name:
                cat_name = cat_name.replace(el, '_')

        req = requests.get(url=cat_href, headers=headers)
        src = req.text
        with open(f'data/{counter}_{cat_name}.html', 'w', encoding='utf-8') as file_w:
            print(src, file=file_w)
        with open(f'data/{counter}_{cat_name}.html', 'r', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')

        alert_block = soup.find(class_='uk-alert-danger')
        if alert_block is not None:
            continue
        table_head = soup.find(class_='uk-overflow-container').find('tr').find_all('th')
        product = table_head[0].text
        kkal = table_head[1].text
        protein = table_head[2].text
        fat = table_head[3].text
        carbs = table_head[4].text
        with open(f'data/{counter}_{cat_name}.csv', 'w', encoding='windows-1251', newline='') as file1:
            writer = csv.writer(file1, delimiter=';')
            writer.writerow(
                (
                    product,
                    kkal,
                    protein,
                    fat,
                    carbs
                )
            )
        product_data = soup.find(class_='uk-overflow-container').find('tbody').find_all('tr')

        product_info = []
        for item in product_data:
            product_tds = item.find_all('td')
            product = product_tds[0].find('a').text
            kkal = product_tds[1].text
            protein = product_tds[2].text
            fat = product_tds[3].text
            carbs = product_tds[4].text

            product_info.append({
                'Product': product,
                'Kkal': kkal,
                'Protein': protein,
                'Fat': fat,
                'Carbs': carbs
            })

            with open(f'data/{counter}_{cat_name}.csv', 'a', encoding='windows-1251', newline='') as file1:
                writer = csv.writer(file1, delimiter=';')
                writer.writerow(
                    (
                        product,
                        kkal,
                        protein,
                        fat,
                        carbs
                    )
                )
        with open(f'data/{counter}_{cat_name}.json', 'a', encoding='utf-8') as file2:
            json.dump(product_info, file2, indent=4, ensure_ascii=False)
        counter += 1
        print(f'|Итерация {counter}: {cat_name} записан...|')
        iter_count -= 1
        if iter_count == 0:
            print('ГОТОВО!')
            break
        print(f'Осталось иттераций: {iter_count}')
        sleep(random.randrange(1, 3))

