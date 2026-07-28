# Configuração de Domínio Próprio (DNS) & Certificado SSL/HTTPS na AWS

Registramos o processo de vinculação de um domínio personalizado (ex: `seusite.com.br`) e emissão de certificado SSL/HTTPS gratuito na AWS.

## Passos para Configuração:
1. **Comprar Domínio**: No Registro.br (`.com.br`) ou Amazon Route 53 (`.com`, `.dev`).
2. **Hosted Zone (Route 53)**: Criar Hosted Zone e colar os 4 registros NS no registrador do domínio.
3. **AWS Certificate Manager (ACM)**: Solicitar certificado SSL público gratuito na região `us-east-1` para `seusite.com.br` e `*.seusite.com.br` com validação DNS automática via Route 53.
4. **Vinculação do Frontend**: Adicionar CNAME no CloudFront e criar registro Type A (Alias) no Route 53.
5. **Vinculação do Backend**: Adicionar Custom Domain no AWS App Runner (ex: `api.seusite.com.br`) e vincular CNAMEs no Route 53.
