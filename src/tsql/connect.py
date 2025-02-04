import pyodbc


def GetConnection(driver: str, server: str, database: str):

    connectionString = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

    conn = pyodbc.connect(connectionString)

    return conn


def GetSqlServerDriver():
    driver_name = ''
    driver_names = [x for x in pyodbc.drivers(
    ) if x.endswith(' for SQL Server')]
    if driver_names:
        driver_name = driver_names[0]
        print(driver_name)
    else:
        print('(No suitable driver found. Cannot connect.)')
