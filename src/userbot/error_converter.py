def error_converter(error) -> dict:
    error_dict = {}
    if error and isinstance(error, object):
        if 'PHONE_NUMBER_INVALID' in str(error):
            error_dict['phone'] = 'Неправильный номер телефона'
        elif 'password is required' in str(error):
            error_dict['password'] = 'У вас включена двухфакторная аутентификация. Введите пароль'
        elif 'API_ID_INVALID' in str(error):
            error_dict['api_id'] = 'Неправильно введенные данные'
            error_dict['api_hash'] = 'Неправильно введенные данные'
        elif 'PHONE_CODE_EXPIRED' in str(error):
            error_dict['code'] = 'Истекло время ожидания кода. Повторите попытку'
        elif 'PHONE_CODE_INVALID' in str(error):
            error_dict['code'] = 'Неверный код подтверждения'
        elif 'PHONE_CODE_INVALID' in str(error):
            error_dict['code'] = 'Неверный код подтверждения'
        elif 'seconds is required' in str(error):
            error_dict['uncommon'] = f'Слишком много запросов. Подождите {error.seconds} сек.'
        else:
            # error_dict['uncommon'] = 'Неизвестная ошибка'
            error_dict['uncommon'] = str(error)
    elif error:
        error_dict['uncommon'] = error
    return error_dict
