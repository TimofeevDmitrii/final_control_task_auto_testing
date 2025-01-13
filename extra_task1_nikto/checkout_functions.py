import subprocess as subp

def checkout_text_is_present(cmd, text):
    result = subp.run(cmd, shell=True, stdout=subp.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False