# 使用するベースイメージを指定 (例: Python 3.9)
FROM python:3.9-slim

# 作業ディレクトリを作成
WORKDIR /app

# ローカルのrequirements.txtをコンテナにコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクトのソースコードをコンテナにコピー
COPY . .

# コンテナ起動時に実行するコマンド（例: main.pyの実行）
CMD ["python3", "discordbot.py"]
