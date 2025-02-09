from src.tsql.connect import GetConnection
import src.core.configuration as config


def GetEmployees():

    driver = config.CONFIGURATION.get('CONNECTION_STRING', 'driver')
    server = config.CONFIGURATION.get('CONNECTION_STRING', 'server')
    database = config.CONFIGURATION.get('CONNECTION_STRING', 'database')

    conn = GetConnection(driver, server, database)

    file_path = config.CONFIGURATION.get('SQL_QUERIES', 'employee_view_sql')

    with open(file_path, 'r') as file:
        SQL_QUERY = file.read()

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)

    records = cursor.fetchall()

    return records
