import importlib
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from django.contrib.auth.models import User

@pytest.mark.selenium
def test_create_test_user(create_super_user):
    assert create_super_user.__str__() == "admin"



@pytest.mark.selenium
def test_admin_login(live_server,db_fixture_setup,chrome_browser_instance):
    """
    Test login page of Django admin
    """

    user = User.objects.get(id=1)
    print(user.password)
    browser = chrome_browser_instance
    browser.get(("%s%s" % (live_server.url,"/admin/login/")))

    user_name = browser.find_element(By.NAME,"username")
    user_password = browser.find_element(By.NAME,"password")
    submit = browser.find_element(By.XPATH,'//input[@value="Log in"]')    

    user_name.send_keys("admin")
    user_password.send_keys("admin")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source