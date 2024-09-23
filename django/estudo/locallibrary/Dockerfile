FROM python:3.12.3
LABEL mantainer="Marlon Bento"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . .
#RUN python manage.py collectstatic --no-input

EXPOSE 8000

#docker build -t back-locallibrary .
#docker run -p 8000:8000 back-locallibrary