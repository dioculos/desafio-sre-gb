# Dockerfile - Desafio SRE
FROM python:2.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
RUN python database-setup.py
CMD ["app.py"]
