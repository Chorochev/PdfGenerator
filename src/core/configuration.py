import configparser


def InitConfigurations():

    global CONFIGURATION

    file_path = 'config.ini'

    with open(file_path, 'r') as file:
        file_content = file.read()

    CONFIGURATION = configparser.ConfigParser(allow_no_value=True)
    CONFIGURATION.read_string(file_content)


def ShowConfigurations():

    print('[CONNECTION_STRING]')
    print(' driver: ' + CONFIGURATION.get('CONNECTION_STRING', 'driver'))
    print(' server: ' + CONFIGURATION.get('CONNECTION_STRING', 'server'))
    print(' database: ' + CONFIGURATION.get('CONNECTION_STRING', 'database'))
    print('[SQL_QUERIES]')
    print(' employee_view_sql: ' +
          CONFIGURATION.get('SQL_QUERIES', 'employee_view_sql'))
    print('[REPORT]')
    print(' default_font: ' + CONFIGURATION.get('REPORT', 'default_font'))
    print(' font_size: ' + CONFIGURATION.get('REPORT', 'font_size'))
