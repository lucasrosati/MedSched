# Usa a imagem oficial do Python como base
FROM python:3.9

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos da aplicação para o diretório de trabalho
COPY . /app

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para executar a aplicação
CMD ["python", "app.py"]
