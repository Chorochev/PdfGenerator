import src.core.arguments as commands

from src.test import CreateTestPdfFile
from src.core.configuration import InitConfigurations
from src.core.configuration import ShowConfigurations
from src.tsql.connect import GetSqlServerDriver
from src.report.EmployeeReport import EmployeeReport
from src.tsql.employee_view import GetEmployees

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
        pdf = EmployeeReport()
        pdf.create(records, "./temp/report1.pdf")
