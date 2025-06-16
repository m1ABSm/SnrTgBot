def get_next_letter_number():
    # Пример простого автоинкремента
    from database import get_last_number
    last = get_last_number()
    if not last:
        return "А001"
    letter, num = last[0], int(last[1:])
    if num >= 999:
        letter = chr(ord(letter) + 1)
        num = 1
    else:
        num += 1
    return f"{letter}{num:03d}"