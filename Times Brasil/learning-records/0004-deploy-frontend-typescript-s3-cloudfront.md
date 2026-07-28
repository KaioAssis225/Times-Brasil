# Hospedagem do Frontend TypeScript / Node com Amazon S3 & CloudFront

Registramos o processo para publicar o frontend estático compilado (`dist/` do React/Vite/Next) na infraestrutura global da AWS com SSL/HTTPS e integração com o backend FastAPI.

## Passos do Deploy do Frontend:
1. **Build Estático**: `npm run build` gerando a pasta `dist/`.
2. **Amazon S3**: Criação do Bucket e sincronização via CLI (`aws s3 sync dist/ s3://meu-bucket --delete`).
3. **Amazon CloudFront**: Configuração de CDN com distribuição global, redirecionamento para HTTPS, restrição de acesso por OAC (Origin Access Control) e regra de resposta para rotas SPA (403/404 -> `/index.html` 200).
4. **CORS no Backend**: Configuração do `CORSMiddleware` na API FastAPI autorizando a URL do CloudFront/domínio customizado.
