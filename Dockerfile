# Pythonの公式イメージをベースにする
FROM python:3.12-slim

# MeCabとIPAdicをインストール
RUN apt-get update && apt-get install -y \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    swig \
    && apt-get clean

# 作業ディレクトリを作成
WORKDIR /app

# 必要な依存関係をコピーする
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトのソースコードをコピー
COPY . .

# ボットを起動する
CMD ["python", "discordbot.py"]
