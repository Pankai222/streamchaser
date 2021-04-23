FROM python:3.9

COPY . /app/backend
COPY .env /app/backend
COPY requirements.txt /app/backend

WORKDIR /app/backend

RUN pip install -r requirements.txt

EXPOSE 1337

CMD [ "uvicorn", "src.main:app", "--host=0.0.0.0", \
      "--port=1337", "--reload" ]