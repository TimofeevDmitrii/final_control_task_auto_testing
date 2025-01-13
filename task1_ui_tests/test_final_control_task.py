from test_page_ui import OperationsHelperUI
import logging
import yaml
import time

with open ("test_data.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)

class TestUI:

    def test_ui_successful_login(self, browser_driver):
        logging.info("test_ui_successful_login is starting...")
        test_page = OperationsHelperUI(browser_driver)
        test_page.go_to_site()
        test_page.enter_login(data_yaml["user_name"])
        test_page.enter_password(data_yaml["passwd"])
        test_page.click_login_btn()
        assert test_page.get_hello_user_text() == "Hello, {}".format(data_yaml["user_name"]),\
            "test_ui_successful_login FAILED"



    def test_ui_click_about(self, browser_driver):
        logging.info("test_ui_contact_us is starting...")
        results = []

        test_page = OperationsHelperUI(browser_driver)
        test_page.click_about_link()
        time.sleep(3)
        results.append(test_page.get_about_title_text() == "About Page")
        results.append(test_page.get_about_title_font_size() == "32px")

        assert all(results), "test_ui_click_about FAILED"
