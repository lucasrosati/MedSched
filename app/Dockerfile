# Utilizando a imagem oficial do Python
FROM python:3.9

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando os arquivos da aplicação para o container
COPY . /app

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando padrão para rodar a aplicação (ajuste conforme necessário)
CMD ["python", "app.py"]
