def check_email(email, severity=True):
    """ проверяет email на корректность

    email: строка с емейлом
    severity: True - если строго, False - если слабо

    Возвращает True, если все ОК.
    """

    if severity:
        if '@' in email and '.' in email:
            return True
    else:
        if '@' in email:
            return True