bot_token = '2028617006:AAErh99SDAeFpv-h9RH0A7RCeYXVh6297dQ'




# Тут код, сделанный мной изначально для отслеживания курса валют. Парсер.
# Но надо через апи, поэтому пришлось удалить. Оставлю его тут. Может, пойдет для дополнительной оценки))


#dollar_rub = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l' \
#              '0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0' \
#              '%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0' \
#              '..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'
#
# euro_rub = 'https://www.google.ru/search?q=курс+евро+к+рублю&newwindow=1&sxsrf=AJOqlzXik-cQnsR9qmNjgoyokdtH6VWiVg%3A1' \
#            '673461495269&ei=9_6-Y52GEKTLrgTNiKnADQ&ved=0ahUKEwjd3eHvkcD8AhWkpYsKHU1ECtgQ4dUDCA4&uact=5&oq=курс+евро+к' \
#            '+рублю&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzoKCAA' \
#            'QRxDWBBCwA0oECEEYAEoECEYYAFBXWFdg8gVoAXACeACAAQCIAQCSAQCYAQCgAQHIAQjAAQE&sclient=gws-wiz-serp'
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107'
#                          '.0.0.0 Safari/537.36 OPR/93.0.0.0'}
#
# full_page_usd = requests.get(dollar_rub, headers=headers)
# full_page_eur = requests.get(euro_rub, headers=headers)
#
# soup_usd = BeautifulSoup(full_page_usd.content, 'html.parser')
# soup_eur = BeautifulSoup(full_page_eur.content, "html.parser")
#
# convert_usd = soup_usd.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
# convert_eur = soup_eur.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
#
# usd = float(convert_usd[0].text.replace(',', '.'))
# eur = float(convert_eur[0].text.replace(',', '.'))

