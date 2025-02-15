import time
import random

print("Это программа, которая замеряет скорость печати.")
print("Вам будет показана случайная фраза, нужно будет напечатать её самостоятельно. Готовы?")
input("Нажмите Enter, если готовы:")

phrase1 = "Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства."
phrase2 = "В чащах юга жил бы цитрус? Да, но фальшивый экземпляр!"
phrase3 = "Съешь ещё этих мягких французских булок да выпей же чаю."

random_number = random.randint(1,3)
if random_number == 1:
    print(phrase1)
if random_number == 2:
    print(phrase2)
if random_number == 3:
    print(phrase3)

start_time = time.time()

user_input = input("Напечатайте фразу выше")

end_time = time.time()

elapsed_time = end_time - start_time
len_text = len(user_input)
symbols_per_minute = len_text / elapsed_time * 60

print(f"Ваша скорость печати: {symbols_per_minute} символов в минуту.")
print(f"Время, затраченное на печать: {elapsed_time} секунд.")