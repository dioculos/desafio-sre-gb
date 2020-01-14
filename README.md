# desafio-sre
Repositório para o Desafio de SRE


# Descrição

Esta aplicação é uma API REST construída em Flask, utilizando SQLAlchemy para persistência de dados, Docker e Docker-Compose para conter a aplicação em containers, Git para versionamento de arquivos e Jenkins para Integração/Deployment Contínuos, modelada utilizando os princípios de MVC e contendo testes unitários utilizando unittest para garantir a qualidade.


# Requerimentos 

Para rodar este sistema é necessário ter os seguintes componentes:
- Docker Container Engine v19.03 ou superior;
- Docker Compose v1.2.5 ou superior;

# Instruções

Para subir esta aplicação, você pode baixar a imagem contida em Docker e rodá-la localmente utilizando o Docker Composer. A imagem se encontra no seguinte link: https://hub.docker.com/repository/docker/oculosdeoculos/desafio-sre.

Utilizando o console de comando do seu sistema operacional de preferência, você pode enviar o comando:

docker pull oculosdeoculos/desafio-sre:latest

Após coletar a imagem do container, você pode rodá-la utilizando o seguinte comando:

docker-compose up --build -d

Este comando irá montar corretamente o ambiente e omitir do console principal as mensagens de log, permitindo a você continuar a utilizar o console enquanto o container roda ao fundo.


# API

A API REST contida neste sistema possui uma série de funções, com o objetivo de registrar e medir o tempo gasto em cada deploy. Para tal, a API aceita requisições POST contendo um JSON com os seguintes parâmetros:

- component (string): Componente que está em processo de deploy
- version (string): Versão que está sendo entregue
- owner (string): Nome do membro do time de engenharia que está realizando o processo de deploy
- status (string): Status do processo de deploy

Abaixo um exemplo em cURL para enviar um novo registro a API:

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"component":"server-interface","version":"2.1","owner":"aoliveira","status":"deployed"}' \
  http://127.0.0.1:5000/api/


Ao receber um novo registro corretamente, a API persiste este registro em um banco de dados, retornando o registro completo com identificação única (id), data e hora que o registro foi realizado no banco de dados, em um formato JSON.

A API também oferece o resgate de registros individuais através de sua ID, bem como a atualização e remoção de tais registros, utilizando os verbos HTTP GET, PUT e DELETE.

