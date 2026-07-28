# Mapeamento da Arquitetura AWS para Stack FastAPI + TypeScript + PostgreSQL + Docker

O usuário especificou a stack real do projeto:
- Frontend: TypeScript / Node (React/Vite/Next)
- Backend: FastAPI (Python)
- Banco de Dados: PostgreSQL
- Empacotamento: Docker / Docker Compose

## Decisão de Arquitetura AWS Recomendada:
1. **Frontend**: Amazon S3 + Amazon CloudFront (CDN global + HTTPS automático).
2. **Backend FastAPI**: AWS App Runner (ou Amazon ECR + EC2 com Docker), onde a imagem Docker do FastAPI roda de forma isolada e escalável.
3. **Banco de Dados**: Amazon RDS para PostgreSQL (gerenciado, seguro e com backups automáticos).
4. **Imagens Docker**: Amazon ECR (Elastic Container Registry).

## Implicações para Próximas Lições:
- **Lição 02**: Arquitetura visual passo a passo para FastAPI + TS + Postgres + Docker na AWS.
- **Lição 03**: Como empacotar e enviar o FastAPI com Docker para o Amazon ECR / App Runner.
- **Lição 04**: Como subir o PostgreSQL no Amazon RDS e conectar com a variável `DATABASE_URL` do FastAPI.
- **Lição 05**: Deploy do Frontend TypeScript com S3 + CloudFront e conexão de CORS com o FastAPI.
