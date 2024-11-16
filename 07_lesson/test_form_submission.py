import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from form_page import TestFormPage  # Импортируем класс страницы


@pytest.fixture(scope="module")
def driver():
    # Запуск Chrome-драйвера с использованием ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_form_submission(driver):
    # Создаем объект страницы
    form_page = TestFormPage(driver)

    # Открыть страницу с формой
    form_page.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем форму
    form_page.fill_form(
        first_name='Иван',
        last_name='Петров',
        address='Ленина, 55-3',
        email='test@skypro.com',
        phone='+7985899998787',
        zip_code='',
        city='Москва',
        country='Россия',
        job_position='QA',
        company='SkyPro'
    )

    # Отправляем форму
    form_page.submit_form()

    # Ожидаем появления всех предупреждений
    form_page.wait_for_alerts()

    # Получаем все элементы предупреждений
    alerts = form_page.get_alerts()

    # Проверяем предупреждения
    form_page.check_alerts(alerts)