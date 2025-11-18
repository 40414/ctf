FROM python:3.13.0-alpine3.20

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:1337", "--access-logfile","-","--error-logfile","-","app:app"]