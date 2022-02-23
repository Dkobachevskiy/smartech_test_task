from .base_page import BasePage


class YandexPage(BasePage):                                                     #класс-пустышка для дальнейшего расширения тестов
    def __init__(self, *args, **kwargs):
        super(YandexPage, self).__init__(*args, **kwargs)
