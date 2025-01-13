from checkout_functions import checkout_text_is_present

def test_nikto_zero_errors():
    cmd = "nikto -h https://test-stand.gb.ru/ -ssl -Tuning 4"
    text = "0 error(s)"
    assert checkout_text_is_present(cmd, text), "test_nikto_zero_errors FAILED"