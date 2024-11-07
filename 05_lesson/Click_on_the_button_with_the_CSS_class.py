from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException

# Путь к chromedriver
service = Service(executable_path=r'C:\Users\user\Desktop\chrome driver\chromedriver-win32\chromedriver.exe')

# Запуск веб-драйвера
driver = webdriver.Chrome(service=service)

# Шаг 1: Открытие страницы
driver.get("http://uitestingplayground.com/classattr")

# Шаг 2: Клик на синюю кнопку
try:
    # Явное ожидание, чтобы убедиться, что кнопка доступна для клика
    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary"))  # Ищем по CSS
    )
    button.click()  # Кликаем на кнопку
    print("Кнопка успешно нажата.")
except TimeoutException:
    print("Время ожидания истекло: кнопка не была найдена или не стала доступной для клика.")
except NoSuchElementException:
    print("Элемент не найден: кнопка с заданным XPATH отсутствует на странице.")
except ElementClickInterceptedException:
    print("Не удалось кликнуть по элементу: кнопка перекрыта другим элементом.")
except Exception as e:
    print(f"Произошла ошибка: {e}")  # Выводим сообщение об ошибке
finally:
    # Закрытие браузера
    driver.quit()