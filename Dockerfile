FROM python:3.11
ENV PYTHONDONTWRITENYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . /tudu
WORKDIR /tudu

RUN pip install -r requirements.txt