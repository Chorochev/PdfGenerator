import src.arguments as commands

from src.test import CreateTestPdfFile

commands.init()

if(commands.args.test):  

    if(commands.args.fileName):
        fileName = commands.args.fileName
    else:
        fileName = "./temp/test.pdf"    

    CreateTestPdfFile(fileName)