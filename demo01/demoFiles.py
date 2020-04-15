class OpenFileandRead():
    def __init__(self):
        pass

    def readFile(self, filePath, fileName):
        fileLocation = filePath + fileName
        try:
            with open(fileLocation) as fl_object:
                contents = fl_object.read()
        except FileNotFoundError:
            print('File not fount')
        else:
            print(contents)


if __name__ == '__main__':
    openfile = OpenFileandRead()
    openfile.readFile('','newTest.txt')