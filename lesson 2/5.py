rating = [50, 50, 50, 40, 30, 20]
print('Рейтинг - ', rating)
a = int(input('Введите рейтинг - '))
count = 0
for i in rating:
    if a > i:
        rating.insert(count, a)
        break
    if a == i:
        rating.insert(count + rating.count(i), a)
        break
    count += 1
if a < rating[len(rating) - 1]:
    rating.append(a)
print(rating)
