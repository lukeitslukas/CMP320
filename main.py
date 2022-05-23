from Password import Password
from collections import Counter
import textwrap
import os


def report(run):
    os.makedirs(os.path.dirname(run.filename + '/'), exist_ok=True)
    output = open(run.filename + '/Output.txt', 'w')

    output.write('Estimated Password Policy \n')
    output.write('Length: ' + str(len(run.minimum)) + '-' + str(len(run.maximum)) + '\n')
    output.write('None Alphanumeric Symbols: \n')
    wrapper = textwrap.TextWrapper(width=50)
    string = wrapper.fill(text=''.join(map(str, run.symbols)))
    output.write(string + '\n')
    if run.statistics[0] > 0.5 and run.statistics[1] > 0.5:
        output.write('Char Case enforcement unlikely\n')
    else:
        output.write('Char case enforcement likely\n')

    output.write('\nStatistics\n')

    output.write('Shortest Length : ' + str(len(run.minimum)) + '\n')
    output.write(run.minimum + '\n\n')
    output.write('Longest Length : ' + str(len(run.maximum)) + '\n')
    output.write(run.maximum + '\n\n')

    output.write('Most Popular Passwords \n')
    passwords = Counter(run.passwordList)
    for i in range(1, len(passwords.most_common(11))):
        output.write(str(i) + '. ' + passwords.most_common(11)[i-1][0] + ', ' + str(passwords.most_common(11)[i-1][1]))
        output.write('\n')
    output.write('\n')

    with open(run.filename + '/PasswordsOutput.csv', 'w') as csvOutput:
        csvOutput.write('password, occurrences\n')
        for i in range(1, len(passwords.most_common(101))):
            csvOutput.write(passwords.most_common(101)[i-1][0] + ', ' + str(passwords.most_common(101)[i-1][1]))
            csvOutput.write('\n')

    output.write('Password Lengths\n')

    for value in sorted(run.passwordLength, key=run.passwordLength.get, reverse=True):
        if round((run.passwordLength[value] / len(run.passwordList) * 100), 2) > 5:
            output.write(str(value) + ' : ' + str(round((run.passwordLength[value] / len(run.passwordList) * 100), 2)) +
                         '%\n')
    output.write('\n')

    with open(run.filename + '/PasswordLenOutput.csv', 'w') as csvOutput:
        csvOutput.write('length, occurrences\n')
        for key, value in run.passwordLength.items():
            csvOutput.write(str(key) + ', ' + str(value) + '\n')

    output.write('Percentages\n')
    output.write('Number of passwords: ' + str(len(run.passwordList)) + '\n')
    output.write('All Uppercase: ' + str(run.statistics[0]) + '%\n')
    output.write('All Lowercase: ' + str(run.statistics[1]) + '%\n')
    output.write('All Alphabet: ' + str(run.statistics[2]) + '%\n')
    output.write('All Alphanumerical: ' + str(run.statistics[3]) + '%\n')
    output.write('\n')

    count = Counter(run.allSymbols)
    for i in range(1, len(count.most_common(11))):
        output.write(str(i) + '. ' + count.most_common(11)[i-1][0] + ' : ' + str(count.most_common(11)[i-1][1]))
        output.write('\n')

    output.close()


def main():
    print("What's the file name?")
    run = Password(input())

    report(run)

    print('Output: ' + run.filename + 'Output.txt')


main()
