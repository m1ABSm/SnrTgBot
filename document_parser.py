def extract_text_from_pdf_or_image(file_bytes):
    try:
        images = convert_from_bytes(file_bytes)
        text = "\n".join(pytesseract.image_to_string(img, lang='rus+eng') for img in images)
    except:
        image = Image.open(io.BytesIO(file_bytes))
        text = pytesseract.image_to_string(image, lang='rus+eng')
    return text

def process_file(file_bytes):
    text = extract_text_from_pdf_or_image(file_bytes)
    company = re.search(r"(?:ООО|ЗАО|АО|ИП)\s+\"?([\w\s\-]+)\"?", text)
    name = re.search(r"(?:С уважением|От:)\s*(.*)", text)
    email = re.search(r"[\w.]+@[\w.]+", text)
    subject = "запрос КП" if "коммерческое предложение" in text.lower() else "другое"

    return {
        "company": company.group(1) if company else "Неизвестно",
        "sender_name": name.group(1)[:100] if name else "Неизвестно",
        "email": email.group(0) if email else "Не найдено",
        "subject": subject
    }