import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    # Створення об'єкту для керування браузером
    driver = webdriver.Chrome(
        service=Service(r"C:\Users\Admin\Become-QA-Auto" + "chromedriver.exe")
    )

    # Відкриваємо сторінку http://github.com/login
    driver.get("http://github.com/login")

    # Знаходимо поле, в яке будемо вводити неправильне ім'я користувача обо пошту
    login_elem = driver.find_element(By.ID, "login_field")

    # Вводимо неправильне ім'я користувача або пошту
    login_elem.send_keys("IevgenSmerechynskyi@mistakeinemail.com")
    
    # Знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    # Вводимо неправильний пароль
    pass_elem.send_keys("wrong password")
    
    # Знаходимо кнопку Sign in
    btn_elem = driver.find_element(By.NAME, "commit")

    # Емітуємо клік лівою кнопкою мишки
    btn_elem.click()
    
    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"
    

    # Закріваємо браузер
    driver.close()
