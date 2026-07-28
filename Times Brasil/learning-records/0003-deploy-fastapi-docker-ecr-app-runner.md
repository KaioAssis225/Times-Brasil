# Passo a Passo do Deploy de FastAPI com Docker no Amazon ECR & App Runner

Registramos o procedimento oficial para colocar uma API FastAPI (Python) empacotada em Docker em produção na AWS.

## Fluxo do Deploy:
1. **Dockerfile**: Configurado com `python:3.11-slim`, expondo a porta `8000` e rodando Uvicorn escutando em `0.0.0.0`.
2. **Amazon ECR**: Criado o repositório privado `fastapi-backend` para armazenar as imagens.
3. **Push da Imagem**: Autenticação com `aws ecr get-login-password`, `docker build`, `docker tag` e `docker push`.
4. **AWS App Runner**: Serviço configurado apontando para o ECR com variável de ambiente `DATABASE_URL` e SSL automático.
