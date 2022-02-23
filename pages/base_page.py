from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def cheking_result(self, expected, result, url):                            #метод проверяет полученный результат с ожидаемым, в случае несоответствия
        result_dimension = WebDriverWait(                                       #возвращает ошибку с ожидаемым и полученным результатом и ссылкой на страницу
            self.browser, 5).until(EC.presence_of_element_located((result))     #принимает ожидаемый результат, полученный результат, и адрес страницы, на которой прохидит проверка
        ).text
        assert expected in result_dimension,\
        f'the result obtained does not correspond to the expected: {expected}, {result_dimension}, {url}'

    def entering_request_in_value(self, request, value):                        #метод вводит нужное значение в нужное поле для ввода
        search_value = WebDriverWait(                                           #принимает информацию для ввода в виде str и селектор поля ввода
            self.browser, 10).until(EC.presence_of_element_located((value))     #при необходимости удаляет автозаполнение
        )
        lenght = len(search_value.get_attribute('value'))
        if lenght > 0:
            search_value.send_keys(lenght * Keys.DELETE)
        search_value.send_keys(request)

    def is_element_present(self, element, url):                                 #метод проверяет наличие элемента на странице
        try:                                                                    #принимает селектор элемента и адрес страницы, на которой идет проверка
            WebDriverWait(
            self.browser, 5).until(EC.presence_of_element_located((element))
        )
        except (NoSuchElementException):
            print(f'{element} not found on the page {url}')
            return False
        return True

    def move_to_element(self, element):                                         #метод для прокрутки страницы до элемента
        button = WebDriverWait(                                                 #принимает селектор элемента
            self.browser, 5).until(EC.presence_of_element_located((element))
        )
        button.location_once_scrolled_into_view

    def open(self):                                                             #метод открытия главное страницы
        self.browser.get(self.url)

    def open_page(self, page):                                                  #метод открытия страницы по гиперссылки на странице
        new_page = WebDriverWait(                                               #принимает селектор поиска гиперссылки
            self.browser, 10).until(EC.presence_of_element_located((page))
        )
        new_page.click()

    def push_on_button(self, button):                                           #метод для нажатия на необходимую кнопку
        pressed_button = WebDriverWait(                                         #принимает селектор кнопки
            self.browser, 10).until(EC.element_to_be_clickable((button))
        )
        pressed_button.click()    
