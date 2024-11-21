# Imagem base do Python
FROM python:3.10-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar todos os arquivos da aplicação para o contêiner
COPY . .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta padrão para Flask
EXPOSE 5000

# Comando para iniciar o servidor Flask
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
