FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    swig \
    && apt-get clean

# mecabrcのシンボリックリンクを作成
RUN ln -s /etc/mecabrc /usr/local/etc/mecabrc

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "discordbot.py"]
