s = str(int(input()))

def palindrome(s):
    """проверяет строку, является ли она палиндромом"""
    s = s.lower().replace(' ', '')
    if s == s [::-1]:
        return  'Палиндром'
    else:
        return 'Не палиндром'
print(palindrome(s))
