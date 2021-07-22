time = int(input('Введите количество секунд - '))
sec = time % 60
hour = time // 3600
min = (time - hour * 3600) // 60
zero = str(0)
if hour < 10:
    hour = zero + str(hour)
else: hour = str(hour)
if min < 10:
    min = zero +str(min)
else: min = str(min)
if sec < 10:
    sec = zero + str(sec)
else: sec = str(sec)
print(hour + ':' + min + ':' +sec)