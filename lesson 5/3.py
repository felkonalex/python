with open('2.txt', encoding='utf-8') as file:
    val = {st.split()[0]: int(st.split()[1]) for st in file}
    print(f'Средний доход сотрудников - {round(sum(val.values()) / len(val), 3)}')
    print(f'Оклад менее 20 тысяч у {[e[0] for e in val.items() if e[1] < 20000]}'      )
