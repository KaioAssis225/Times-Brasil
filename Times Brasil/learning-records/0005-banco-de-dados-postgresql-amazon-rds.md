# Banco de Dados PostgreSQL no Amazon RDS

Registramos o procedimento para provisionar e conectar o banco de dados relacional PostgreSQL usando Amazon RDS para a API FastAPI.

## Principais Aprendizados:
1. **Amazon RDS vs Instância Própria**: Vantagens de backups diários automáticos, patches de segurança sem queda e gerenciamento completo sem lidar com sistema operacional Linux.
2. **Security Groups & Porta 5432**: Liberação do acesso apenas para o backend da API ou IP de dev.
3. **Variáveis de Ambiente**: A string `DATABASE_URL` contendo `postgresql://usuario:senha@endpoint:5432/nome_banco` deve ser configurada no App Runner (nunca gravada diretamente no código).
4. ** SQLAlchemy / SQLModel**: Conexão nativa em Python lendo `os.getenv("DATABASE_URL")`.
