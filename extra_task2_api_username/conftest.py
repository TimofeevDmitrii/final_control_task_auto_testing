import pytest
import yaml
from test_page_api import OperationHelperAPI

with open("./test_data.yaml") as conf_f:
    data_yaml = yaml.safe_load(conf_f)



@pytest.fixture(scope="session")
def get_auth_token_and_user_data():
    test_api = OperationHelperAPI(data_yaml["api_url_login"])
    result = test_api.login(data_yaml["user_name"], data_yaml["passwd"])
    token = result[0]["token"]
    user_id = result[0]["id"]
    user_name = result[0]["username"]
    user_roles = result[0]["roles"]
    return token, user_id, user_name, user_roles





