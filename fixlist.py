file2 = open('gmailpass.txt', 'w', encoding="UTF-8", errors="ignore")
with open('alleged-gmail-passwords.txt', 'r', encoding="UTF-8", errors="ignore") as file:
    for line in file:
        if line.strip() != '':
            file2.write(line.strip() + '\n')
            
file2.close()
