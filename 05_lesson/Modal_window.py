from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Указываем путь к исполняемому файлу Firefox
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Проверьте, что путь к Firefox верный

# Настройка опций Firefox
options = Options()
options.binary_location = firefox_binary_path

# Путь к geckodriver для Firefox
service = Service(executable_path=r'C:\Users\user\Desktop\gecodriver\geckodriver.exe')

# Запуск Firefox-драйвера с указанием пути к Firefox
driver = webdriver.Firefox(service=service, options=options)

# Шаг 1: Открытие страницы
driver.get("http://the-internet.herokuapp.com/entry_ad")

try:
    # Шаг 2: Явное ожидание появления модального окна и кнопки "Close"
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='modal-footer']/p"))
    )

    # Шаг 3: Клик на кнопку "Close" в модальном окне
    close_button.click()
    print("Модальное окно закрыто.")

except TimeoutException:
    print("Время ожидания истекло: кнопка 'Close' не была найдена.")
except NoSuchElementException:
    print("Элемент не найден: модальное окно или кнопка отсутствует на странице.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()