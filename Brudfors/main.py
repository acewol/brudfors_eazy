import itertools
import string

def brute_password(password, min_len, max_len): #Указывание минимальное кол-во символов и максимальное
    chars = string.ascii_letters + string.digits #Алфавит и цифры. По которым будет подбор.
    atempt = 0

    for lenght in range(min_len, max_len):
        for guess in itertools.product(chars, repeat=lenght):
            atempt += 1
            guess = ''.join(guess)
            print(f"Попытка №{atempt}. {guess}")
            if guess == password:
                print("Пароль найден")
                return

password = '1234'
result = brute_password(password, 1, 5) #Можно поставить нужное кол-во символов в пароле
print(result)
