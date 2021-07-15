from sys import argv
def pay():
    time, stavka, premiya = map(int, argv[1:4])
    if len(argv) == 4:
        print(f"Заработная плата - {time * stavka + premiya}")
    else:
        print ('Введите выработку, ставку в час и размер премии через пробел')
pay()