import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#user_id = input('Введите id пользователя: ')
profile_id = '11111111111111111' #steam_id


profile_link = 'https://steamcommunity.com/profiles/' + profile_id + '/games/?tab=all'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://steamcommunity.com/')
for j in range(13):
   cookie = open('auth'+str(j)+'.txt', encoding='utf8')
   c = cookie.readlines()[0][1:-2].replace(',', '').replace("'", '').replace(':', '').split()
   c1 = {}
   print(c)
   c[0] = 'https://'+c[1]
   for i in range(0,len(c),2):
      if c[i+1] == 'False':
         c1[c[i]] = False
      elif c[i+1] == 'True':
         c1[c[i]] = False
      elif c[i+1].isdigit():
         if c[i] == 'value':
            c1[c[i]] = c[i+1]+',0'
         else: c1[c[i]] = int(c[i+1])
      else: c1[c[i]] = c[i+1]
   print(c1)
   driver.add_cookie(c1)

   cookie.close()
   print(j)


driver.get(profile_link)

games_names = []
games_ids = []
games_costs = []
games_time = []
sum_of_time = 0
digits = [i for i in range(10)]
parse_games_ids = driver.find_elements_by_class_name('gameListRow')
parse_games_names = driver.find_elements_by_class_name('gameListRowItemName')
parse_games_time = driver.find_elements_by_class_name('hours_played')

for i in range(len(parse_games_ids)):
   games_ids.append(str(parse_games_ids[i].get_attribute('id')))
   games_ids[i] = games_ids[i][games_ids[i].index('_')+1:]
   games_names.append(str(parse_games_names[i].get_attribute('innerHTML')))
   games_time.append(str(parse_games_time[i].get_attribute('innerHTML')))
   if len(games_time[i]) > 0: games_time[i] = float(games_time[i].replace(',', '.')[:games_time[i].index(' ')])
   else: games_time[i] = 0

sum_of_time = sum(games_time)

print(games_ids)
#print()
#print(games_names)
#print()
#print(games_time)
#print(str(results))
for i in range( len(games_ids)):
   link = 'https://store.steampowered.com/app/' + games_ids[i]
   driver.get(link)
   birth_agree = driver.find_elements_by_class_name('agegate_birthday_desc')
   sorry = driver.find_elements_by_class_name('error')
   if len(sorry) > 0:
      price = 0
      print(str(price) + 'Доступ закрыт')
      games_costs.append(price)
      continue
   if len(birth_agree) > 0:
      btn = driver.find_element_by_xpath('//*[@id="ageYear"]/option[91]')
      btn.click()
      try:
         btn = driver.find_element_by_xpath('//*[@id="app_agegate"]/div[1]/div[4]/a[1]/span')
         btn.click()
      except:
         btn = driver.find_element_by_xpath('//*[@id="app_agegate"]/div[1]/div[3]/a[1]/span')
         btn.click()
      
      time.sleep(2)
   if driver.current_url != 'https://store.steampowered.com/':
      try: price = driver.find_elements_by_class_name('price')[0].get_attribute('innerHTML')
      except:
         try: price = driver.find_elements_by_class_name('discount_original_price')[0].get_attribute('innerHTML')
         except: price = driver.find_elements_by_class_name('discount_final_price')[0].get_attribute('innerHTML')
      if 'Бесплатно' in price: price = 0 
      elif 'Demo' in price or 'Демо' in price:
         try: price = driver.find_elements_by_class_name('discount_original_price')[0].get_attribute('innerHTML')
         except: price = driver.find_elements_by_class_name('discount_final_price')[0].get_attribute('innerHTML')
         price = float(price.replace(',', '.')[:price.index(' ')])
      else: price = float(price.replace(',', '.')[:price.index(' ')])
   else: price = 0
   print(price)
   games_costs.append(price)

   time.sleep(2)
print(games_costs) 
sum_of_costs = sum(games_costs)
print(f'Итого: {sum_of_costs} руб.')
print(f'Всего потрачено времени на игры: {sum_of_time} ч.')
print(f'Кол-во игр: {len(games_ids)}')


'''
# Получаем cookie
cookie = open('auth.txt', encoding='utf8')
c = cookie.readlines()[0].replace(',', '').split()
print(c)
driver.add_cookie({'domain': '.bookmate.com', 'expiry': 1605111862, 'httpOnly': True, 'name': 'bms', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'ThsGRNMY%2Fziw6oZH%2FTWVIs9JBUpJlJ4m9BudCSqzMQ91Cfzx8Ikczyf3xf9BRbhiY51IhMn6UtcU%2BgKMdiI1AFs%2Fb7mGJryTPNOmIDCxKFCSvqCaxaHQiVBrX1IXY7ZSemqxJhWbQTiwNLGdO6Kv5qbRnJlm93JuQNxJ9mjaNHkiTXVyeB6F%2FtzlMwhV87PlGea9gOLXhq826jAEQeLY7LtnV%2Fz5fVAAPXRhejpK2I1XFpMRAVwKO84I5ms2--MSByTPBgj6spEO1I--I2YLWOH%2Fklyew5ovGRTfBw%3D%3D'})

cookie.close()
'''

