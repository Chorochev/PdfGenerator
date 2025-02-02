import configparser


def InitConfigurations():

    global configuration

    file_path = 'config.ini'

    with open(file_path, 'r') as file:
        file_content = file.read()

    configuration = configparser.ConfigParser(allow_no_value=True)
    configuration.read_string(file_content)


def ShowConfigurations():

    print('[CONNECTION_STRING]')
    print('server: ' + configuration.get('CONNECTION_STRING', 'server'))
    print('database: ' + configuration.get('CONNECTION_STRING', 'database'))
