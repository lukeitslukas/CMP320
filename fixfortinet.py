file2 = open('fortinet.txt', 'w', encoding="UTF-8", errors="ignore")
with open('fortinet-2021.txt', 'r', encoding="UTF-8", errors="ignore") as file:
    for line in file:
        if len(line.strip().split(':')) == 2:
            if line.strip().split(':')[1] != '':
                file2.write(line.strip().split(':')[1] + '\n')
            
file2.close()
