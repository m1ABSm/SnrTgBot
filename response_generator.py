from database import get_letter_by_number

def generate_response(letter_number):
    data = get_letter_by_number(letter_number)
    if not data:
        return "Ошибка: письмо не найдено."
    number, company, sender_name, email, subject, date = data
    return f"Уважаемый {sender_name},\n\nБлагодарим за обращение в нашу компанию. Ваше письмо от {date} по теме '{subject}' зарегистрировано под номером {number}. В ближайшее время мы с вами свяжемся.\n\nС уважением,\n[Ваша компания]"