def palindrome(s):
    """проверяет строку, является ли она палиндромом"""
    s = s.lower().replace(' ', '')
    if s == s [::-1]:
        return  'Палиндром'
    else:
        return 'Не палиндром'

def prime(number):
    """проверить, что число простое"""
  n = int(number)
  if n == 1:
      return None
  for i in range(2, n//2 + 1):
      if n % i == 0:
          return True
      return False

def power2(number):
    """проверить, является ли число степенью двойки"""
    # 2, 4, 8, 16, 32, 64
    k = 3
    n = 8
    while n < int(number):
        k += 1
        n = n * 2
    if 2 ** k == int(number):
        return True
    else:
        return False


def chek_pin(pin):
    """проверить пинкод"""
    a = prime(pin[0])
    b = palindrome(pin[1])
    c = True
    if a and b and c:
        return 'Корректен'
    else:
        return 'Некорректен'

def main():
    pincode = input().split('-')
    # '1-710-5' -> ['1', '710', '5']
    print(chek_pin(pincode))


main()
