import shutil

if __name__ == '__main__':
    if '{{ cookiecutter.service_account_file }}' == '':
        raise Exception()
    shutil.copy('{{ cookiecutter.service_account_file }}', './app/serviceAccount.json')
