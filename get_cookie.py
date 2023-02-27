# Получение cookie

from selenium import webdriver


def get_cookie():
   driver = webdriver.Chrome('chromedriver.exe')
   print('Получение доступа (cookie) к аккаунту Steam')
   link = input('Введите ссылку на веб-страницу ')
   driver.get(link)
   login = input('Для продолжения нажмите кнопку Enter...')
   cookie = driver.get_cookies()
   print(cookie)
   for i in range(13):
      cookie_file = open('auth' + str(i) + '.txt', mode='w+', encoding='utf8')
      cookie_file.write(str(cookie[i]))
   print('\nДанные для входа были успешно получены!')
   cookie_file.close()
   e = input()


get_cookie()
   

   
