def error_converter(error) -> dict:
    error_dict = {}
    if error and isinstance(error, object):
        error = str(error)
        if 'PHONE_NUMBER_INVALID' in error:
            error_dict['phone'] = 'Неправильный номер телефона'
        elif 'password is required' in error:
            error_dict['password'] = 'У вас включена двухфакторная аутентификация. Введите пароль'
        elif 'API_ID_INVALID' in error:
            error_dict['api_id'] = 'Неправильно введенные данные'
            error_dict['api_hash'] = 'Неправильно введенные данные'
        elif 'PHONE_CODE_EXPIRED' in error:
            error_dict['code'] = 'Истекло время ожидания кода. Повторите попытку'
        elif 'PHONE_CODE_INVALID' in error:
            error_dict['code'] = 'Неверный код подтверждения'
        else:
            error_dict['uncommon'] = 'Неизвестная ошибка'
    elif error:
        error_dict['uncommon'] = error
    return error_dict
