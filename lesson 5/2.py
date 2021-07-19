st = 0
with open('1.txt', 'r') as file:
    file.seek(0)
    for i in file:
        st += 1
        a = len(i.split())
        print(f'Количество слов в {st} строке = {a}')
print(f"Количество строк = {st}")
