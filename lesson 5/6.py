dict = {}
with open("5.txt", encoding="utf-8") as file:
    for st in file:
        name, val = st.split(':')
        namesum = sum(map(int, "".join([i for i in val if i == ' ' or (i >= '0' and i <= '9')]).split()))
        dict[name] = namesum
print(dict)
