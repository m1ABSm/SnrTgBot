FROM python:3.11-slim

WORKDIR /app

# Установим зависимости
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libpoppler-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
