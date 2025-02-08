import src.arguments as commands

from src.test import CreateTestPdfFile
from src.configuration import InitConfigurations
from src.configuration import ShowConfigurations
from src.tsql.employee_view import GetEmployees
from src.tsql.connect import GetSqlServerDriver
from src.pdf.document import PDF

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

if (commands.args.testPdf):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)
    for i in range(1, 41):
        pdf.cell(
            0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")
    pdf.output("./temp/new-tuto2.pdf")
