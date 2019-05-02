from .test_base import TestBase
from selenpy.support import browser
from tests.pages.main_page import MainPage
from tests.pages.login_page import LoginPage
from tests.pages import login_page, main_page

class LoginTest(TestBase):
    
    login_page = LoginPage()
    main_page = MainPage()

    def  DA_LOGIN_TC001(self):
        browser.open_url("http://192.168.188.99/TADashboard/2f9njff6y9.page")
        login_page.login(self, "SampleRepository", "administrator", "")
        assert main_page._btn_overview.is_enabled()
    
