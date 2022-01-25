# This is a sample Python script.
import os

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def createFile(name):
    # Use a breakpoint in the code line below to debug your script.
    os.remove(f'testfolder/{name}.txt')
    f = open(f'testfolder/{name}.txt', "x")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createFile('test')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
