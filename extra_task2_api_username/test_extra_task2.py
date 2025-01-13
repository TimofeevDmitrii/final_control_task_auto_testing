from test_page_api import OperationHelperAPI
import logging
import yaml

with open ("test_data.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)

def test_api_check_username(get_auth_token_and_user_data):
    logging.info("test_api_check_username is starting...")
    profile_url = data_yaml["api_url_profile"].replace("{id}", str(get_auth_token_and_user_data[1]))
    test_api = OperationHelperAPI(profile_url)
    result = test_api.get_user_profile(get_auth_token_and_user_data[0])
    assert result[1] == 200 and result[0]["username"] == get_auth_token_and_user_data[2],\
        "test_api_check_username FAILED"



