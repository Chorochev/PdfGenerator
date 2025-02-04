import src.arguments as commands

from src.test import CreateTestPdfFile
from src.configuration import InitConfigurations
from src.configuration import ShowConfigurations
from src.tsql.employee_view import GetEmployees
from src.tsql.connect import GetSqlServerDriver

commands.init()

InitConfigurations()

if (commands.args.test):

    if (commands.args.fileName):
        fileName = commands.args.fileName
    else:
        fileName = "./temp/test.pdf"

    CreateTestPdfFile(fileName)

if (commands.args.configs):
    ShowConfigurations()

if (commands.args.getSqlServerDriver):
    GetSqlServerDriver()

if (commands.args.report):
    if (commands.args.report == 'employee'):
        records = GetEmployees()
        # print(records)
        # print()
        for r in records:
            print(f"{r.BusinessEntityID}\t{r.FirstName}\t{r.LastName}")
