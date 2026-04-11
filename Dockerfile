FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    swig \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .

# キャッシュを無効化するためにupgradeも追加
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "discordbot.py"]
