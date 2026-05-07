FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    swig \
    && apt-get clean

RUN git clone --depth 1 https://github.com/taku910/mecab.git /tmp/mecab && \
    mkdir -p /app/ipadic_csv && \
    cp /tmp/mecab/mecab-ipadic/*.csv /app/ipadic_csv/ && \
    rm -rf /tmp/mecab

# mecabrcのシンボリックリンクを作成
RUN ln -s /etc/mecabrc /usr/local/etc/mecabrc

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "discordbot.py"]
