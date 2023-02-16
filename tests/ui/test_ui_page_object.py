from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui 
def test_check_incorrect_username_page_object():
    # Створення об'кту сторінки
    sign_in_page = SignInPage()

    # Відкривамо сторінку
    sign_in_page.go_to()

    # Виконуємо спробу увійти в систему GitHub
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Перевіряємо, що назва сторінки така, яку ми очікуємо
    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Закриваємо
    sign_in_page.close()
    