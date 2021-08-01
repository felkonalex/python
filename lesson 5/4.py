dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре" }
with open('3replaced.txt', 'w', encoding='utf-8') as file2:
    with open('3.txt', 'r', encoding='utf-8') as file1:
        for i in file1:
            file2.write(f'{dict.get(i.split()[0])} ')
            file2.write(f'{i.split()[1]} ')
            file2.write(f'{i.split()[2]} \n')