import src.arguments as commands

from src.test import CreateTestPdfFile
from src.configuration import InitConfigurations
from src.configuration import ShowConfigurations

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
