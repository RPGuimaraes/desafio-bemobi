FROM python:latest

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY entrypoint.sh /
RUN chmod 744 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["python","manage.py","runserver"]



