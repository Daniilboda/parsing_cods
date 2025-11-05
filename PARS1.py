from bs4 import BeautifulSoup
import lxml
import re
with open('C:\\Users\\Daniil\\IdeaProjects\\PARSING_Data\\index.html', encoding='utf-8') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')

title = soup.title
print(title)
print(title.text)


page_h1 = soup.find_all('h1')
print(page_h1)

user_name = soup.find('div', class_= 'user__name').find('span').text
print(user_name)

info = soup.find('div', class_='user__info').find_all('span')
print(info)
for item in info:
    print(item.text.strip())

links = soup.find('div', class_='social__networks').find('ul').find_all('a')
print(links)
links = soup.find_all('a')
for link in links:
    item_txt = link.text
    item_url = link.get('href')
    print(f'{item_txt }: {item_url}')


# .find_parent() .find_parents()
p = soup.find(class_="post__text").find_parent()
print(p)



#.next_element .find_next()

n = soup.find(class_= "post__title").find_next().text
print(n)

n = soup.find(class_= "post__date").find_previous_sibling().text
print(n)

clothes = soup.find('a', string=re.compile('Instagram')).text
print(clothes)