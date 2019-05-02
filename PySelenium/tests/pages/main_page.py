from selenpy.element.text_box import TextBox
from selenpy.element.combo_box import ComboBox
from selenpy.element.base_element import BaseElement
from selenpy.support.conditions import be, have

class MainPage():
    
    _btn_overview = BaseElement("xpath=//a[text()='Overview']")
    
    _cbb_repository = ComboBox("id=repository")
    _txt_username = TextBox("id=username")
    _txt_password = TextBox("id=password")
    _btn_login = BaseElement("class=btn-login")

    def __init__(self):
        pass
    
    def login(self,repository, username, password):
        self._cbb_repository.select_by_value(repository)
        self._txt_username.send_keys(username)
        self._txt_password.send_keys(password)
        self._btn_login.click()

    def search(self, key_word):
        # self._txt_search.wait_for_visible()
        self._txt_search.wait_until(be.visible)
        self._txt_search.send_keys(key_word)
        self._txt_search.wait_until(have.value(key_word))
