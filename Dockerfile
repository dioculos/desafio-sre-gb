# Dockerfile - Desafio SRE
FROM python:2.7
COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
RUN python database_setup.py
CMD ["app.py"]
