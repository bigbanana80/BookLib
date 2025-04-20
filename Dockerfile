FROM python:3.13.3-bookworm
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD ["python3","manage.py","runserver","8000"]
