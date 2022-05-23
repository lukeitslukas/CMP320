import re
from collections import Counter


class Password:
    def __init__(self, filename):
        self.filename = filename
        self.passwordList, self.passwordLength = self.openList()
        self.minimum, self.maximum = self.findMinMax()
        self.symbols, self.allSymbols, self.statistics = self.stats()

    def openList(self):
        passwordList = []
        passwordLength = {}

        with open(self.filename + '.txt', 'r') as passwordFile:
            for i in passwordFile:
                passwordList.append(i.strip())
                passwordLength[len(i.strip())] = passwordLength.get(len(i.strip()), 0) + 1

        passwordFile.close()

        return passwordList, passwordLength #yes

    def findMinMax(self):
        minimum = self.passwordList[0]
        maximum = self.passwordList[0]

        for password in self.passwordList:
            if len(password) < len(minimum):
                minimum = password
            if len(password) > len(maximum):
                maximum = password

        return minimum, maximum

    def stats(self):
        symbols = []
        allSymbols = []
        statistics = [0, 0, 0, 0]

        for password in self.passwordList:
            symbolQuery = re.findall('[^a-zA-Z0-9]', password)
            # list [lower, upper, alpha, alphanumeric]
            if password.islower(): statistics[0] += 1
            if password.isupper(): statistics[1] += 1
            if password.isalpha(): statistics[2] += 1
            if password.isalnum(): statistics[3] += 1
            for i in symbolQuery:
                allSymbols.append(i)
                if i not in symbols:
                    symbols.append(i)

        for i in range(0, len(statistics)):
            statistics[i] = round(((statistics[i] / len(self.passwordList)) * 100), 2)

        symbols.sort(key=Counter(allSymbols).get, reverse=True)
        return symbols, allSymbols, statistics
