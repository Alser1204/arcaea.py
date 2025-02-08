from discord.ext import commands
import discord
from PIL import Image
import os
from os.path import join, dirname
import random
import io
import asyncio
import secrets
from dotenv import load_dotenv

has_run = False

def first_time_action():
    global has_run
    if not has_run:
        global Default
        Default = 6
        has_run = True

first_time_action()

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.getenv("DISCORD_TOKEN")
print(TOKEN)


intents = discord.Intents.default()
intents.members = True # メンバー管理の権限
intents.message_content = True # メッセージの内容を取得する権限

IMAGE_DIR = './images'


bot = commands.Bot(
    command_prefix="!", # $コマンド名　でコマンドを実行できるようになる
    case_insensitive=True, # 大文字小文字を区別しない ($hello も $Hello も同じ!)
    intents=intents # 権限を設定
)

@bot.event
async def on_ready():
    print(f'ログインしました: {bot.user}')
    channel = bot.get_channel(1320752464374530139)
    await channel.send("ログインしました")

@bot.command()
async def setDefault(ctx, DefaultDivision: float):
    global Default
    # 入力値を検証
    if DefaultDivision < 1 or DefaultDivision > 20:
        await ctx.send("エラー: 分割数は1以上20以下の値を指定してください。")
        return
    
    Default = DefaultDivision
    await ctx.send(f"デフォルトの分割数を {Default} に設定しました。")

@bot.command(aliases=["p"])
async def potential(ctx: commands.context, const: float, score: float) -> None:

    FRAG = 0

    if (score < 0) or (const < 0):
        await  ctx.send("Error:譜面定数、スコアは正の値を入力してください。")
        FRAG = -1
    if const > score:
        a = const
        const = score
        score = a
    while score<1000000:
        score *= 10
    if score>=10000000:
        potential = const + 2.0
    elif score>=9800000:
        potential = const + 1.0 + (score - 9800000)/200000
    else:
        potential = const + (score - 9500000)/300000
    if FRAG == 0:
        if potential < 0:
            await  ctx.send("0")
        else:
            await ctx.send(potential)


@bot.command(aliases=["s"])
async def skip(ctx):
    global skip_flag
    skip_flag = True
    await ctx.send("出題をスキップしました！")


def is_acronym(input_str, answer_str):
    """入力が正解の頭文字を取った省略形であるか確認"""
    acronym = ''.join(word[0] for word in answer_str.split() if word)
    return input_str.lower() == acronym.lower()

# モザイク処理の追加
@bot.command(aliases=["m"])
async def mosaic(ctx, block_size: int = 5):
    try:
        # 画像の選択
        image_files = [f for f in os.listdir(IMAGE_DIR) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]
        if not image_files:
            await ctx.send("画像が見つかりません。")
            return

        random_image = secrets.choice(image_files)
        image_path = os.path.join(IMAGE_DIR, random_image)

        # 画像の読み込み
        img = Image.open(image_path)
        img_width, img_height = img.size
        img_array = np.array(img)

        # モザイク処理
        for y in range(0, img_height, block_size):
            for x in range(0, img_width, block_size):
                block = img_array[y:y + block_size, x:x + block_size]
                avg_color = np.mean(block, axis=(0, 1)).astype(int)
                img_array[y:y + block_size, x:x + block_size] = avg_color

        # モザイク画像を保存
        mosaic_img = Image.fromarray(img_array)
        temp_image_path = 'temp_image.png'
        mosaic_img.save(temp_image_path)

        # モザイク画像を送信
        sent_message = await ctx.send(file=discord.File(temp_image_path))
        
        # ファイル削除前に送信したメッセージに関連するファイルパスを保持
        os.remove(temp_image_path)

        def check(m):
            return m.channel == ctx.channel and m.reference is not None and m.reference.message_id == sent_message.id

        start_time = asyncio.get_event_loop().time()
        FRAG = 1

        while asyncio.get_event_loop().time() - start_time < 30:
            try:
                response = await asyncio.wait_for(bot.wait_for('message', check=check), timeout=30.0)
                if (response.content.lower() == os.path.splitext(random_image)[0].lower()) or (len(response.content) >= 3 and response.content.lower() in os.path.splitext(random_image)[0].lower()) or (len(response.content) >= 3 and is_acronym(response.content, os.path.splitext(random_image)[0])):
                    await response.reply("正解です！")
                    FRAG = 0
                    break
                elif (response.content.lower() == ("!s" or "!skip")):
                    break
                else:
                    await response.reply("残念！もう一度お試しください。")
            except asyncio.TimeoutError:
                continue

        if FRAG:
            await ctx.send("時間切れです！")
        await ctx.send(f"正解は `{os.path.splitext(random_image)[0]}` でした！")
        await ctx.send(file=discord.File(image_path))

    except Exception as e:
        await ctx.send(f"エラーが発生しました: {e}")




@bot.command(aliases=["g"])
async def guessc(ctx, n: float = 6):
    global Default
    if Default is not None:
        n = Default
    try:
        # nが1以上の数であることを確認
        if n < 1 or n > 20:
            await ctx.send("分割数は1以上20以下の数にしてください。")
            return

        # 画像の選択
        image_files = [f for f in os.listdir(IMAGE_DIR) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]
        if not image_files:
            await ctx.send("画像が見つかりません。")
            return

        random_image = secrets.choice(image_files)
        image_path = os.path.join(IMAGE_DIR, random_image)

        # 画像の分割処理
        img = Image.open(image_path)
        img_width, img_height = img.size
        tile_width = int(img_width // n)
        tile_height = int(img_height // n)

        tiles = []
        for i in range(int(n)):
            for j in range(int(n)):
                left = j * tile_width
                upper = i * tile_height
                right = left + tile_width
                lower = upper + tile_height
                tiles.append(img.crop((left, upper, right, lower)))

        # ランダムなタイルを選択
        selected_tile = secrets.choice(tiles)

        # 一時ファイルとして保存
        temp_path = 'temp_image.png'
        selected_tile.save(temp_path)

        sent_message = await ctx.send(file=discord.File(temp_path))
        os.remove(temp_path)

        def check(m):
            return m.channel == ctx.channel and m.reference is not None and m.reference.message_id == sent_message.id

        start_time = asyncio.get_event_loop().time()
        FRAG = 1

        while asyncio.get_event_loop().time() - start_time < 30:
            try:
                response = await asyncio.wait_for(bot.wait_for('message', check=check), timeout=30.0)
                if (response.content.lower() == os.path.splitext(random_image)[0].lower()) or (len(response.content) >= 3 and response.content.lower() in os.path.splitext(random_image)[0].lower()) or (len(response.content) >= 3 and is_acronym(response.content, os.path.splitext(random_image)[0])):
                    await response.reply("正解です！")
                    FRAG = 0
                    break
                elif (response.content.lower() == ("!s" or "!skip")):
                    break
                else:
                    await response.reply("残念！もう一度お試しください。")
            except asyncio.TimeoutError:
                continue

        if FRAG:
            await ctx.send("時間切れです！")
        await ctx.send(f"正解は `{os.path.splitext(random_image)[0]}` でした！")
        await ctx.send(file=discord.File(image_path))

    except Exception as e:
        await ctx.send(f"エラーが発生しました: {e}")


bot.run(TOKEN)
