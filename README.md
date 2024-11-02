Простой брутфорс пароля на python.
**Функционал**
Используется базовая библиотека itertools, для работы с данными.
После пишем:
def brute_password(password, min_len, max_len): 
    chars = string.ascii_letters + string.digits 
    atempt = 0
Указываем brute_password, что означает жесткий перебор пароля, методом подбора. В нем уже прописываем минимальное и максимальное кол-во символов в пароле.
    for lenght in range(min_len, max_len):
        for guess in itertools.product(chars, repeat=lenght):
            atempt += 1
            guess = ''.join(guess)
            print(f"Попытка №{atempt}. {guess}")
            if guess == password:
                print("Пароль найден")
                return
Далее генерируем список из всех разных паролей по длине.
password = '1234'
result = brute_password(password, 1, 5) #Можно поставить нужное кол-во символов в пароле
print(result)
В конце уже прописываем пароль, который будет брудфорситься и выбираем допустимое кол-во символов в пароле.
