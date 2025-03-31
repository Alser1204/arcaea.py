from discord.ext import commands, tasks
import discord
import os
from os.path import join, dirname
import random
import secrets
from dotenv import load_dotenv
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import asyncio
import io
import math
from collections import defaultdict
import json
import datetime

# サーバーごとのデフォルト設定を保持する辞書
server_settings = {}

def first_time_action():
    global server_settings
    if not server_settings:
        # 初期設定（例: 全サーバーにデフォルトの設定を追加）
        server_settings = {}

first_time_action()

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True  # メンバー管理の権限
intents.message_content = True  # メッセージの内容を取得する権限

IMAGE_DIR = './images'
YAJU_DIR = './yaju'

bot = commands.Bot(
    command_prefix="!",
    case_insensitive=True,
    intents=intents
)

@bot.event
async def on_ready():
    print(f'ログインしました: {bot.user}')
    send_file.start()

@bot.command(aliases=["dman"])
async def deeman(ctx, bad:str="deeman"):
    await ctx.send("deemanはカス")

@bot.command(aliases=["frtk"])
async def frtkshop(ctx, bad:str="frtkshop"):
    await ctx.send("ふらつきショップはカス")

@bot.command()
async def alser(ctx, bad:str="alser"):
    await ctx.send("Alserはカス")

CHANNEL_ID = 1355100431105130527

@tasks.loop(hours=1)  # 1時間ごとに実行
async def send_file():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(file=discord.File('counts.json'))
@bot.command()
async def fmeigen(ctx):
    responses = ["ふらつきショップってそういう…", "Heavenly caress神譜面スギィ！！！", "13.2未満全員赤ポテ", "全部出していいよ","俺はテンペPMだぞ！！","うるせぇまんこまんこまんこ","13.2未満全員赤ポテ","でもお前赤ポテじゃん","風唄4回で鳥なのにガチ恋ラビリンスS","@つわ","俺は14歳","イキスギィ！","ニィロウの愛液つゆだくトッピング","ちんぽイクイクたろう","しゃわる","ウー"]
    response = random.choice(responses)
    await ctx.send(response)

@bot.command()
async def dmeigen(ctx):
    emoji = discord.utils.get(ctx.guild.emojis, name="hiroyuki_narita")
    responses = ["共用の…強要！", "アルターエゴ楽しすぎる", "末代まで祟ってやる", "生きててごめんなさい…", "今キンタマに篭城してます", "ピュピュピュピュピュピュ ピュ〜〜〜〜〜〜〜〜", "おじさんを、持参！", "イクーーーーッ！！！", "おやふら","おまんこ壊れちゃう〜(><)","いちごパンツで抜くと濃いのでる","ボルテ19以上3時間触るよりアーケア1時間やるほうが疲れる", "初めまして、ドけんた食堂です\n\n今日はたこ焼きを食べていきたいと思います\n\nドピュビュルル(たこ焼きを食べる音)\n\nビュボボ…(たこ焼きを食べる音)\n\nドガーンガシャガシャ(たこ焼きを食べる音)\n\nウィーンピポピポドドドドドドガッシャンガッシャン(たこ焼きを食べる音)\n\n……\n\n粋スギィ！(満面の笑み)","おふろ",str(emoji) + "<お前を殺す。","デカいウンコの恐竜、デカウンコザウルス","死んでてありがとう","(トイレ…？ヒントか…？)"]
    response = random.choice(responses)
    await ctx.send(response)

# データの読み込み
def load_data():
    try:
        with open("counts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return defaultdict(lambda: defaultdict(int))  # ファイルがないときは新規辞書作成


# データの保存
def save_data():
    with open("counts.json", "w") as file:
        json.dump(user_counts, file)

# ユーザーごとのカウントを管理
user_counts = load_data()
    
SECRET = ["マン屁ラップバトル"]

N = ["アナニー","チクニー","レイプ","放尿","フェラ","露出プレイ","催眠","時間停止","睡眠姦","ソフトSM","おもらし","逆レイプ","手コキ","足コキ","匂い","お姉さん","巨乳","レイプ目","目隠し","貧乳","無乳","授乳手コキ","触手","壁尻","腋コキ","あまあま","ヤンデレ","ツンデレ","クーデレ","サキュバス","唾液","パイズリ","素股","ペド","ロリババア","口内射精","ぶっかけ"]

R = ["排便","ロリレイプ","男の娘","ふたなり","ケモ","アナルヒクヒク","オホ声","アヘ顔","緊縛","球体関節","常識改変","ボテ腹","近親相姦","キメセク","首絞め","髪コキ","人外","人形","メカ","義妹","イラマチオ"]

SR = ["アルマジロのケツマンコ","小笠原祐子","熟女陵辱プレイ","フィギュアぶっかけ","四肢欠損","リョナ","獣姦","超乳","実妹"]

SSR = ["陰毛着火","ゲロモンスター","淫夢","ドラゴンカーセックス","ガナニー","ガンダム","首ちんこ","蟲姦", "梅沢富美男のTSマン屁","ゲップオナサポ","スカトロASMR","複乳"]

UR = ["ジジイの顔面騎乗下痢噴射","メガレックウザ"]

# 確率に応じた選択
def random_choice():
    roll = random.random()
    if roll < 0.50:
        return "N " + random.choice(N), "N"
    elif roll < 0.80:
        return "R " + random.choice(R), "R"
    elif roll < 0.96:
        return "SR " + random.choice(SR), "SR"
    elif roll < 0.99:
        return "SSR " + random.choice(SSR), "SSR"
    elif roll < 0.998:
        return "UR " + random.choice(UR), "UR"
    elif roll < 0.9999:
        return "!!!SECRET!!! " + random.choice(SECRET), "SECRET"
    else:
        return "!!!!!ULTIMATE SECRET!!!!!\n!!!!!!! d e e m a n !!!!!!!", "???"

in_battle = False
in_battle_2 = False
battle_member = []
battle_score = []
battle_i = 0
battle_member_2 = []
battle_score_2 = []
battle_i_2 = 0

@bot.command()
async def dgacha(ctx, n: int = 10):
    global battle_member, battle_score, in_battle, battle_i
    global battle_member_2, battle_score_2, in_battle_2, battle_i_2
    user_name = ctx.author.name  # user_name に変更
    gacha_score = 0

    # ユーザーのデータがなければ初期化
    if user_name not in user_counts:
        user_counts[user_name] = {"total": 0, "N": 0, "R": 0, "SR": 0, "SSR": 0, "UR": 0, "SECRET": 0,"???":0, "Rate":1000, "coin":0}

    results = []
    for _ in range(n):
        item, rarity = random_choice()
        results.append(item)

        if rarity not in user_counts[user_name]:
            user_counts[user_name][rarity] = 0
            
        user_counts[user_name][rarity] += 1
        user_counts[user_name]["total"] += 1

        if in_battle:
            if user_name not in battle_member:
                battle_member.append(user_name)  # user_name を格納
                battle_score.append(0)

            idx = battle_member.index(user_name)

            # レアリティごとのスコア加算
            score = {
                "N": 1,
                "R": 2,
                "SR": 3,
                "SSR": 5,
                "UR": 10,
                "SECRET": 15,
                "???": 100,
            }.get(rarity, 0)

            battle_score[idx] += score

        score = {
                "N": 1,
                "R": 2,
                "SR": 3,
                "SSR": 5,
                "UR": 10,
                "SECRET": 15,
                "???": 100,
            }.get(rarity, 0)

        gacha_score += score
        user_counts[user_name]["coin"] += round(score/10)
            
        if in_battle_2:
            if user_name not in battle_member_2:
                battle_member_2.append(user_name)  # user_name を格納
                battle_score_2.append(0)
                
            idx_2 = battle_member_2.index(user_name)

            # レアリティごとのスコア加算
            score = {
                "N": 1,
                "R": 2,
                "SR": 3,
                "SSR": 5,
                "UR": 10,
                "SECRET": 15,
                "???": 100,
            }.get(rarity, 0)

            battle_score_2[idx_2] += score

    save_data()  # データ保存

    count_details = "\n".join(
        f"{rarity}: {user_counts[user_name][rarity]}" for rarity in ["N", "R", "SR", "SSR", "UR", "SECRET","???"]
    )

    await ctx.send(f"{user_name} さんが {n}回 ガチャを引きました。\n"
                   f"結果:\n{'\n'.join(results)}\n"
                   f"スコア:{gacha_score}\n")
    if in_battle:
        idx = battle_member.index(user_name)
        if battle_score[idx] == n and n>=10:
            await ctx.send(f"Nが一致です！{round(n*2.5)}のボーナス！")
            battle_score[idx]+=round(n*2.5)
        
    
    battle_i += 1
    battle_i_2 += 1

@bot.command()
async def dgacha_check(ctx):
    user_name = ctx.author.name  # user_name に変更
    
    if user_name not in user_counts:
        await ctx.send(f"{user_name} さんのデータが見つかりませんでした。")
        return

    total_count = user_counts[user_name]["total"]

    if total_count == 0:
        await ctx.send(f"{user_name} さんのデータはすべて0です。")
        return

    # カウント詳細の作成
    count_details = "\n".join(
        f"{rarity}: {user_counts[user_name][rarity]} "
        f"({(user_counts[user_name][rarity] / total_count * 100):.2f}%)"
        for rarity in ["N", "R", "SR", "SSR", "UR", "SECRET","???"]
    )

    # レート情報の追加
    count_details += f"\nレート: {user_counts[user_name]['Rate']}"

    await ctx.send(f"{user_name} さんの累計ガチャ結果:\n"
                   f"ガチャ回数: {total_count}\n"
                   f"カウント詳細:\n{count_details}")


@bot.command()
async def dgacha_reset(ctx):
    user_name = ctx.author.name

    if user_name in user_counts:
        Rate = user_counts[user_name]['Rate']
        # 初期化データを作成
        user_counts[user_name] = {
            "total": 0,
            "N": 0,
            "R": 0,
            "SR": 0,
            "SSR": 0,
            "UR": 0,
            "SECRET": 0,
            "???":0,
            "Rate": Rate
            
        }
        await ctx.send(f"{user_name} さんのガチャ記録をリセットしました。")
    else:
        await ctx.send(f"{user_name} さんのデータが見つかりませんでした。")

from collections import defaultdict

@bot.command()
async def dgacha_battle(ctx):
    global in_battle, battle_member, battle_score, battle_i
    
    if in_battle:
        battle_value = []
        in_battle = False
        max_score = 0
        max_member = []  # 複数の勝者を保持するリスト

        await ctx.send("dgacha_battleが終わりました！\n結果:")

        for i in range(len(battle_member)):
            await ctx.send(f"{battle_member[i]}さんのスコア: {battle_score[i]}")

            if battle_score[i] > max_score:  # 新たに最大スコアが見つかった場合
                max_score = battle_score[i]
                max_member = [battle_member[i]]  # 勝者をリセットして新たに追加
            elif battle_score[i] == max_score:  # 同点の場合、勝者リストに追加
                max_member.append(battle_member[i])

        # スコア順にソート
        sorted_member, sorted_score = zip(*sorted(zip(battle_member, battle_score), key=lambda x: x[1]))

        # グループ化して同点者をまとめる
        score_groups = defaultdict(list)
        for i in range(len(sorted_member)):
            score_groups[sorted_score[i]].append(sorted_member[i])

        # リストに戻す
        sorted_member = list(sorted_member)
        sorted_score = list(sorted_score)
        average = sum(sorted_score) / len(sorted_score)

        # 各グループごとにレート変動を計算
        rank = 0  # 順位カウント
        for score, members in score_groups.items():
            # グループ内で同じレート変動を計算
            value = score - average + 2 * (rank + (len(members) / 2) - len(sorted_score) / 2)
            for member in members:
                user_counts[member]["Rate"] += round(value)
                battle_value.append(value)
                rank += 1  # 次の順位へ

        # 最大スコアの持ち主を発表
        await ctx.send(f"\n{'、'.join(max_member)}さんがスコア{max_score}で勝利です！")
        await ctx.send("参加者のレートが変動しました！")

        for i in range(len(sorted_member)):
            await ctx.send(f"{sorted_member[i]}さん {user_counts[sorted_member[i]]['Rate']} ({battle_value[i]:+.2f})")
        
        return
    
    # バトルが始まる場合
    await ctx.send("dgacha_battleが始まりました！")
    in_battle = True
    battle_i = 0
    battle_member = []  # 新しいバトルのためにリセット
    battle_score = []  # 新しいバトルのためにリセット


from collections import defaultdict

@bot.command()
async def dgacha_battle2(ctx, n: int = 10):
    global in_battle_2, battle_member_2, battle_score_2, battle_i_2
    
    if in_battle_2:
        battle_value = []
        in_battle_2 = False
        expected_value = round(1.84 * n, 2)  # 小数第2位まで四捨五入

        closest_score = float('inf')
        closest_member = []

        await ctx.send(f"dgacha_battle2が終わりました！\n結果: 期待値: {expected_value}")

        for i in range(len(battle_member_2)):
            await ctx.send(f"{battle_member_2[i]}さんのスコア: {battle_score_2[i]}")
            score_diff = abs(battle_score_2[i] - expected_value)

            if score_diff < closest_score:
                closest_score = score_diff
                closest_member = [battle_member_2[i]]
            elif score_diff == closest_score:
                closest_member.append(battle_member_2[i])

        await ctx.send(f"\n{'、'.join(closest_member)}さんが期待値{expected_value}に最も近いスコアで勝利です！")
        await ctx.send("参加者のレートが変動しました！")

        score_diffs = [abs(score - expected_value) for score in battle_score_2]

        # グループ化して同点者をまとめる
        score_groups = defaultdict(list)
        for i in range(len(battle_member_2)):
            score_groups[score_diffs[i]].append(battle_member_2[i])

        # スコア差をソートしてレート変動計算
        sorted_score_diffs = sorted(score_groups.keys())
        average = sum(score_diffs) / len(score_diffs)

        # battle_member_2をscore_diffsの降順に並べ替え
        sorted_member_2 = [member for _, member in sorted(zip(score_diffs, battle_member_2))]

        # 各グループごとにレート変動を計算
        rank = 0
        for score_diff in sorted_score_diffs:
            members = score_groups[score_diff]
            value = round(score_diff - average + 2 * (rank + (len(members) / 2) - len(score_diffs) / 2))

            for i in range(len(members)):
                user_counts[sorted_member_2[i]]["Rate"] += value
                battle_value.append(value)

            rank += len(members)  # グループごとにrankを増加

        # レートの更新結果を表示
        for i in range(len(battle_member_2)):
            await ctx.send(f"{battle_member_2[i]}さん {user_counts[battle_member_2[i]]['Rate']} ({battle_value[i]:+.2f})")

        return



    # バトルが始まる場合
    await ctx.send("dgacha_battle2が始まりました！")
    in_battle_2 = True
    battle_i_2 = 0
    battle_member_2 = []  # 新しいバトルのためにリセット
    battle_score_2 = []  # 新しいバトルのためにリセット


@bot.command()
async def debug(ctx, directory: str, query: str):
    # 指定されたディレクトリの存在を確認
    if not os.path.exists(directory) or not os.path.isdir(directory):
        await ctx.send("指定されたディレクトリが存在しません。")
        return
    
    # 指定ディレクトリ内のファイルを検索
    matched_files = [f for f in os.listdir(directory) if query.lower() in f.lower()]
    
    if not matched_files:
        await ctx.send("該当する画像が見つかりませんでした。")
        return
    
    for file in matched_files:
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):  # ファイルであることを確認
            await ctx.send(f"ファイル名: {file}", file=discord.File(file_path))

@bot.command()
async def setDefaultGuessc(ctx, DefaultDivision: float):
    """サーバーごとにDefaultGを設定"""
    server_id = str(ctx.guild.id)
    
    # サーバーがまだ設定されていない場合、初期設定を追加
    if server_id not in server_settings:
        server_settings[server_id] = {'DefaultG': 6, 'DefaultM': 80}
    
    # 入力値を検証
    if DefaultDivision < 1 or DefaultDivision > 20:
        await ctx.send("エラー: 分割数は1以上20以下の値を指定してください。")
        return
    
    # サーバーごとの設定を更新
    server_settings[server_id]['DefaultG'] = DefaultDivision
    await ctx.send(f"サーバーのデフォルト分割数を {DefaultDivision} に設定しました。")

@bot.command()
async def getDefaultGuessc(ctx):
    """サーバーごとのDefaultGを取得"""
    server_id = str(ctx.guild.id)

    # サーバーがまだ設定されていない場合、デフォルト値を返す
    if server_id not in server_settings:
        await ctx.send("このサーバーにはまだデフォルト分割数が設定されていません。デフォルト値は 6 です。")
        return

    # 現在のデフォルト分割数設定を取得
    default_guessc = server_settings[server_id].get('DefaultG', 6)
    await ctx.send(f"このサーバーのデフォルト分割数は {default_guessc} です。")

@bot.command()
async def setDefaultMosaic(ctx, DefaultMosaic: int):
    """サーバーごとにDefaultMを設定"""
    server_id = str(ctx.guild.id)
    
    # サーバーがまだ設定されていない場合、初期設定を追加
    if server_id not in server_settings:
        server_settings[server_id] = {'DefaultG': 6, 'DefaultM': 80}
    
    # 入力値を検証
    if DefaultMosaic < 5 or DefaultMosaic > 500:
        await ctx.send("エラー: 分割数は5以上500以下の値を指定してください。")
        return
    
    # サーバーごとの設定を更新
    server_settings[server_id]['DefaultM'] = DefaultMosaic
    await ctx.send(f"サーバーのデフォルトモザイク分割数を {DefaultMosaic} に設定しました。")

@bot.command()
async def getDefaultMosaic(ctx):
    """サーバーごとのDefaultMを取得"""
    server_id = str(ctx.guild.id)

    # サーバーがまだ設定されていない場合、デフォルト値を返す
    if server_id not in server_settings:
        await ctx.send("このサーバーにはまだデフォルトモザイクが設定されていません。デフォルト値は 100 です。")
        return

    # 現在のデフォルトモザイク設定を取得
    default_mosaic = server_settings[server_id].get('DefaultM', 80)
    await ctx.send(f"このサーバーのデフォルトモザイク分割数は {default_mosaic} です。")
    

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
async def mosaic(ctx, block_size: int = None ,yaju: str='null'):
    server_id = str(ctx.guild.id)
    
    # サーバーのデフォルト設定を参照
    if server_id not in server_settings:
        server_settings[server_id] = {'DefaultG': 6, 'DefaultM': 80}
    DefaultM = server_settings[server_id]['DefaultM']
    # block_sizeが指定されていなければデフォルト値を使用
    if block_size is None:
        if DefaultM is not None:
            block_size = DefaultM
        else:
            block_size = 80  # デフォルトの値をここに設定（もしデフォルト値がない場合）
    try:
        if block_size < 5 or block_size > 500:
            await ctx.send("分割数は5以上500以下の数にしてください。")
            return

        # 画像の選択
        image_files = [f for f in os.listdir(IMAGE_DIR) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]
        if not image_files:
            await ctx.send("画像が見つかりません。")
            return

        random_image = secrets.choice(image_files)
        image_path = os.path.join(IMAGE_DIR, random_image)

        if(yaju=='yaju'):
            image_files = [f for f in os.listdir(YAJU_DIR) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]
            if not image_files:
                await ctx.send("画像が見つかりません。")
                return
            random_image = secrets.choice(image_files)
            image_path = os.path.join(YAJU_DIR, random_image)

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
async def guessc(ctx, n: float = None):
    server_id = str(ctx.guild.id)
    
    # サーバーのデフォルト設定を参照
    if server_id not in server_settings:
        server_settings[server_id] = {'DefaultG': 6, 'DefaultM': 80}
    DefaultG = server_settings[server_id]['DefaultG']
    # block_sizeが指定されていなければデフォルト値を使用
    if n is None:
        if DefaultG is not None:
            n = DefaultG
        else:
            n = 6  # デフォルトの値をここに設定（もしデフォルト値がない場合）
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

rootnum = 5
num = rootnum ** 2
position = [["" for _ in range(rootnum)] for _ in range(rootnum)]
color = [["" for _ in range(rootnum)] for _ in range(rootnum)]
turn=0
img = None
img_buffer = None
imgleader = None
imgleader_buffer = None
chance=0
chancenum=0
redcount=0
bluecount=0
FLAG=1
FLAGS=0
allowed_numbers=[]
log_list=[]
font=[["" for _ in range(rootnum)] for _ in range(rootnum)]

@bot.command()
async def blue(ctx, target:str):
    global position,color
    x, y = None, None
    found=False
    for i, row in enumerate(position):
        for j, value in enumerate(row):
            if value == target:
                y, x = i, j  # (x, y) のタプルで返す
                found=True

    if not found:
        found_count = 0
        for i, row in enumerate(position):
            for j, value in enumerate(row):
                if target in value:  # 部分一致
                    y, x = i, j
                    found_count+=1
    if found_count > 1:
        await ctx.send(f"{target} という文字列は複数の場所にあります。もう一度選択してください。")
        return

    # `target` が見つからなかった場合
    if x is None or y is None:
        await ctx.send(f"{target} は見つかりませんでした。")
        return
    global FLAG,FLAGS
    FLAGS=0
    if(FLAG==1):
        return
    global allowed_numbers
    global rootnum
    global bluecount,redcount
    global turn
    global chance
    global img
    global log_list
    global font
    draw = ImageDraw.Draw(img)
    if 10*x+y in allowed_numbers:
        await ctx.send("すでに選ばれました。")
        return
    #await ctx.send("チャンスは"+str(chance)+"回あります。")
    if(turn==1):
        await ctx.send("今は赤のターンです。")
        return
    if(chance==0):
        await ctx.send("まずは値をセットしてください")
        return
    await ctx.send(position[y][x]+"は……？")
    await asyncio.sleep(0.8)
    x0, y0 = 20 + x * 160, 20 + y * 120
    x1, y1 = x0 + 120, y0 + 80
    if(color[y][x]=="blue"):
        draw.rectangle([x0, y0, x1, y1], fill="blue", outline="black", width=1)
        draw.text(((x0 + x1) / 2, (y0 + y1) / 2), position[y][x], fill="white" if color[y][x] != "white" else "black", font=font[j][i], anchor="mm")
        await ctx.send("正解！"+position[y][x]+"は青色です。")
        log_list.append("  !blue "+target+" 青")
        await asyncio.sleep(0.8)
        if(chance-1!=0):
            await ctx.send("チャンスはあと"+str(chance-1)+"回あります。")
        allowed_numbers.append(10*x+y)
        bluecount+=1
    elif(color[y][x]=="red"):
        draw.rectangle([x0, y0, x1, y1], fill="red", outline="black", width=1)
        draw.text(((x0 + x1) / 2, (y0 + y1) / 2), position[y][x], fill="white" if color[y][x] != "white" else "black", font=font[j][i], anchor="mm")
        turn=1
        await ctx.send("はずれ！"+position[y][x]+"は赤色です。")
        log_list.append("  !blue "+target+" 赤")
        await asyncio.sleep(0.8)
        await ctx.send("次は赤のターンです。")
        allowed_numbers.append(10*x+y)
        redcount+=1
    elif(color[y][x]=="gray"):
        draw.rectangle([x0, y0, x1, y1], fill="gray", outline="black", width=1)
        draw.text(((x0 + x1) / 2, (y0 + y1) / 2), position[y][x], fill="white" if color[y][x] != "white" else "black", font=font[j][i], anchor="mm")
        await ctx.send("はずれ！"+position[y][x]+"は灰色です。")
        log_list.append("  !blue "+target+" 灰")
        await asyncio.sleep(0.8)
        await ctx.send("次は赤のターンです。")
        turn=1
        allowed_numbers.append(10*x+y)
    elif(color[y][x]=="black"):
        draw.rectangle([x0, y0, x1, y1], fill="black", outline="black", width=1)
        draw.text(((x0 + x1) / 2, (y0 + y1) / 2), position[y][x], fill="white" if color[y][x] != "white" else "black", font=font[j][i], anchor="mm")
        await ctx.send("残念！"+position[y][x]+"は黒色です！")
        log_list.append("  !blue "+target+" 黒")
        await asyncio.sleep(0.8)
        turn=2
    chance-=1
    if(chance==0 and turn==0):
        await ctx.send("チャンスを使い切りました。")
        await ctx.send("次は赤のターンです。")
        turn=1
        return
    if(redcount==8 or bluecount==9 or turn==2 or turn==3):
        command = bot.get_command("finish")
        await ctx.invoke(command)

@bot.command()
async def red(ctx, target:str):
    global position,color
    x, y = None, None
    found=False
    for i, row in enumerate(position):
        for j, value in enumerate(row):
            if value == target:
                y, x = i, j  # (x, y) のタプルで返す
                found=True

    if not found:
        found_count = 0
        for i, row in enumerate(position):
            for j, value in enumerate(row):
                if target in value:  # 部分一致
                    y, x = i, j
                    found_count+=1
    if found_count > 1:
        await ctx.send(f"{target} という文字列は複数の場所にあります。もう一度選択してください。")
        return

    # `target` が見つからなかった場合
    if x is None or y is None:
        await ctx.send(f"{target} は見つかりませんでした。")
        return
        
    global FLAG,FLAGS
    FLAGS=0
    if(FLAG==1):
        return
    global allowed_numbers
    global rootnum
    global bluecount,redcount
    global chance
    global img
    global turn
    global log_list
    global font
    draw = ImageDraw.Draw(img)
    if 10*x+y in allowed_numbers:
        await ctx.send("すでに選ばれました。")
        return
    #await ctx.send("チャンスは"+str(chance)+"回あります。")
    if(turn==0):
        await ctx.send("今は青のターンです。")
        return
    if(chance==0):
        await ctx.send("まずは値をセットしてください")
        return
    await ctx.send(position[y][x]+"は……？")
    await asyncio.sleep(0.8)
    x0, y0 = 20 + x * 160, 20 + y * 120
    x1, y1 = x0 + 120, y0 + 80
    if(color[y][x]=="blue"):
        draw.rectangle([x0, y0, x1, y1], fill="blue", outline="black", width=1)
        draw.text(((x0 + x1) / 2, (y0 + y1) / 2), position[y][x], fill="white" if color[y][x] != "white" else "black", font=font[j][i], anchor="mm")
        turn=0
        await ctx.send("はずれ！"+position[y][x]+"は青色です。")
        log_list.append("  !red "+target+" 青")
        await asyncio.sleep(0.8)
        await ctx.send("次は青のターンです。")
        allowed_numbers.append(10*x+y)
        bluecount+=1
    elif(color[y][x]=="red"):
        draw.rectangle([x0, y0, x1, y1], fill="red", outline="black", width=1)
        draw.text(((x0 + x1) / 2, (y0 + y1) / 2), position[y][x], fill="white" if color[y][x] != "white" else "black", font=font[j][i], anchor="mm")
        await ctx.send("正解！"+position[y][x]+"は赤色です。")
        log_list.append("  !red "+target+" 赤")
        await asyncio.sleep(0.8)
        if(chance-1!=0):
            await ctx.send("チャンスはあと"+str(chance-1)+"回あります。")
        allowed_numbers.append(10*x+y)
        redcount+=1
    elif(color[y][x]=="gray"):
        draw.rectangle([x0, y0, x1, y1], fill="gray", outline="black", width=1)
        draw.text(((x0 + x1) / 2, (y0 + y1) / 2), position[y][x], fill="white" if color[y][x] != "white" else "black", font=font[j][i], anchor="mm")
        await ctx.send("はずれ！"+position[y][x]+"は灰色です。")
        log_list.append("  !red "+target+" 灰")
        await asyncio.sleep(0.8)
        await ctx.send("次は青のターンです。")
        turn=0
        allowed_numbers.append(10*x+y)
    elif(color[y][x]=="black"):
        draw.rectangle([x0, y0, x1, y1], fill="black", outline="black", width=1)
        draw.text(((x0 + x1) / 2, (y0 + y1) / 2), position[y][x], fill="white" if color[y][x] != "white" else "black", font=font[j][i], anchor="mm")
        await ctx.send("残念！"+position[y][x]+"は黒色です！")
        log_list.append("  !red "+target+" 黒")
        await asyncio.sleep(0.8)
        turn=3
    chance-=1
    if(chance==0 and turn==1):
        await ctx.send("チャンスを使い切りました。")
        await ctx.send("次は青のターンです。")
        turn=0
        return
    if(redcount==8 or bluecount==9 or turn==2 or turn==3):
        command = bot.get_command("finish")
        await ctx.invoke(command)

@bot.command()
async def logs(ctx):
    global log_list
    await ctx.send("\n".join(log_list))

@bot.command()
async def next(ctx):
    global FLAG,turn
    global FLAGS
    FLAGS=0
    if(FLAG==1):
        return
    if(turn==0):
        turn=1
        await ctx.send("次は赤のターンです。")
    elif(turn==1):
        turn=0
        await ctx.send("次は青のターンです。")

@bot.command()
async def set(ctx, vain:str, n:int):
    global FLAG
    global FLAGS
    FLAGS=0
    if(FLAG==1):
        return
    log_list.append("!set "+vain+" "+str(n))
    global chance,chancenum
    chance = n+1
    chancenum = n+1
    await ctx.send("チャンスは"+str(chance)+"回あります。")

@bot.command()
async def finish(ctx):
    global FLAG,FLAGS
    global img
    global imgleader
    global img_buffer
    global imgleader_buffer
    global once
    if(once==1):
        return
    if(FLAG==1):
        return
    global bluecount,redcount
    if(turn==2):
        await ctx.send("青が黒カードを選択したので、赤の勝利です！")
    elif(turn==3):
        await ctx.send("赤が黒カードを選択したので、青の勝利です！")
    elif(bluecount==9):
        await ctx.send("青が取った枚数:"+str(bluecount))
        await ctx.send("赤が取った枚数:"+str(redcount))
        await ctx.send("青の勝利です！")
    elif(redcount==8):
        await ctx.send("青が取った枚数:"+str(bluecount))
        await ctx.send("赤が取った枚数:"+str(redcount))
        await ctx.send("赤の勝利です！")
    else:
        await ctx.send("強制終了")
    FLAG=0
    global imgleader
    global imgleader_buffer

    # img が更新されていない場合はエラーメッセージを返す
    if imgleader is None or imgleader_buffer is None:
        await ctx.send("画像が正しく描画されていません。")
        return
    once=1

    # バッファに画像を保存
    imgleader_buffer = io.BytesIO()
    imgleader.save(imgleader_buffer, format="PNG")
    imgleader_buffer.seek(0)  # バッファを最初に戻す

    # Discord に送信
    await ctx.send(file=discord.File(imgleader_buffer, "leaderoutput.png"))
    command = bot.get_command("display")
    await ctx.invoke(command)

once=0

@bot.command()
async def ldisplay(ctx):
    global FLAG,FLAGS
    global imgleader
    global imgleader_buffer
    if(FLAG==1):
        return
    if(FLAGS==1):
        return

    # img が更新されていない場合はエラーメッセージを返す
    if imgleader is None or imgleader_buffer is None:
        await ctx.send("画像が正しく描画されていません。")
        return

    # バッファに画像を保存
    imgleader_buffer = io.BytesIO()
    imgleader.save(imgleader_buffer, format="PNG")
    imgleader_buffer.seek(0)  # バッファを最初に戻す

    # Discord に送信
    await ctx.author.send("あなたはリーダーです。\nキーワードを考えチームを勝利へと導きましょう！")
    await ctx.author.send(file=discord.File(imgleader_buffer, "leaderoutput.png"))

@bot.command()
async def display(ctx):
    global FLAG,FLAGS
    global img
    global img_buffer
    if(FLAG==1):
        return

    # img が更新されていない場合はエラーメッセージを返す
    if img is None or img_buffer is None:
        await ctx.send("画像が正しく描画されていません。")
        return

    # バッファに画像を保存
    img_buffer = io.BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)  # バッファを最初に戻す

    # Discord に送信
    await ctx.send(file=discord.File(img_buffer, "output.png"))
    FLAGS=1
    
@bot.command()
async def codename_help(ctx):
    await ctx.send("このゲームは、青チームと赤チームに分かれ、リーダーのヒントをもとに自チームの単語だと思うものを当てていくゲームです。\n!codename:ゲーム開始\n!bmember(もしくはrmember) [任意の数の名前] (-l or -d):チームへのメンバーの追加。引数-lをつけると先頭の引数をリーダーに、-dをつけると引数のメンバーを削除。特にゲーム内容に関係は無い。\n!member:現在のメンバーを表示\n!display:現在の状況を表示\n!ldisplay:リーダー用の画像をDMにて表示\n!set [ヒントの単語] [数]:リーダーがヒントの単語と数をセット\n!blue [単語]:青チームが青色だと思う単語を宣言\n!red [単語]:赤チームが赤色だと思う単語を宣言\n!next:ターンをスキップ\n!logs:これまでのログを表示\n!finish:ゲームを終了")
    
rmember_list=[]
bmember_list=[]

@bot.command()
async def bmember(ctx, *args):
    global FLAG
    if(FLAG==1):
        return
    global bmember_list
    deleted_list=[]
    added_list=[]

    args = list(args)
    if(args[-1]=="-l"):
        args.remove("-l")
        if(args[0] in bmember_list):
            bmember_list.remove(args[0])
        if args:  # argsが空でないかを確認
            bmember_list.insert(0, args[0])  # args[0]をbmember_listの最初に追加
        else:
            await ctx.send("エラー: -lオプションの前にメンバー名が必要です。")
            return
        await ctx.send("青チームのリーダーは"+args[0]+"さんです。")
    elif(args[-1]=="-d"):
        args.remove("-d")
        if not args:  # argsが空の場合、削除対象がないためエラーメッセージを返す
            await ctx.send("エラー: -dオプションの前に削除するメンバー名が必要です。")
            return
        for name in args:
            if name in bmember_list:
                bmember_list.remove(name)
                deleted_list.append(name)
        await ctx.send("青チーム削除メンバー:"+",".join(deleted_list))
    else:
        for name in args:
            bmember_list.append(name)
            added_list.append(name)
        await ctx.send("青チーム追加メンバー:"+",".join(added_list))

@bot.command()
async def rmember(ctx, *args):
    global FLAG
    if(FLAG==1):
        return
    global bmember_list
    deleted_list=[]
    added_list=[]

    args = list(args)
    if(args[-1]=="-l"):
        args.remove("-l")
        if(args[0] in rmember_list):
            rmember_list.remove(args[0])
        if args:  # argsが空でないかを確認
            rmember_list.insert(0, args[0])  # args[0]をrmember_listの最初に追加
        else:
            await ctx.send("エラー: -lオプションの前にメンバー名が必要です。")
            return
        await ctx.send("赤チームのリーダーは"+args[0]+"さんです。")
    elif(args[-1]=="-d"):
        args.remove("-d")
        if not args:  # argsが空の場合、削除対象がないためエラーメッセージを返す
            await ctx.send("エラー: -dオプションの前に削除するメンバー名が必要です。")
            return
        for name in args:
            if name in bmember_list:
                rmember_list.remove(name)
                deleted_list.append(name)
        await ctx.send("赤チーム削除メンバー:"+",".join(deleted_list))
    else:
        for name in args:
            rmember_list.append(name)
            added_list.append(name)
        await ctx.send("赤チーム追加メンバー:"+",".join(added_list))

@bot.command()
async def member(ctx):
    global rmember_list,bmember_list
    if rmember_list or bmember_list:
        await ctx.send("**青チームメンバーリスト:**\nLeader:" + "\n".join(bmember_list)+"\n\n**赤チームメンバーリスト:**\nLeader:" + "\n".join(rmember_list))
    else:
        await ctx.send("リストは空です！")

@bot.command()
async def codename(ctx, genre:str="原神"):
    global position
    global color
    global img
    global imgleader
    global rootnum
    global num
    global once
    global turn,chance,chancenum,redcount,bluecount,allowed_numbers
    global rmember_list,bmember_list,log_list
    global font
    rmember_list=[]
    bmember_list=[]
    log_list=[]
    once=0
    rootnum = 5
    num = rootnum ** 2
    position = [["" for _ in range(rootnum)] for _ in range(rootnum)]
    color = [["" for _ in range(rootnum)] for _ in range(rootnum)]
    font=[["" for _ in range(rootnum)] for _ in range(rootnum)]
    turn=0
    chance=0
    chancenum=0
    redcount=0
    bluecount=0
    allowed_numbers=[]
    double=1
    imgleader = Image.new("RGB", (800, 600), "white")
    img = Image.new("RGB", (800, 600), "white")
    drawleader = ImageDraw.Draw(imgleader)
    draw = ImageDraw.Draw(img)
    

    num_list = list(range(num))  # 0 から num-1 までのリスト

    if(genre=="原神"):
        text_file="Genshin.txt"
    elif(genre=="学マス" or genre=="学園アイドルマスター"):
        text_file="GakuenIMAS.txt"
    elif(genre=="ブルアカ" or genre=="ブルーアーカイブ"):
        text_file="BlueArchive.txt"
    elif(genre=="Arcaea" or genre=="アーケア"):
        text_file="Arcaea.txt"
        double=1.8
    # 文字データの読み込み
    try:
        with open(text_file, "r", encoding="utf-8") as file:
            char_list = file.read().strip().split('\n')
            print(char_list)
    except FileNotFoundError:
        char_list = ["文字"] * num  # ファイルがない場合、"文字" のリストを用意

    def choose(lst):
        chosen = random.choice(lst)
        lst.remove(chosen)
        return chosen

    # マスを描画
    for j in range(rootnum):
        for i in range(rootnum):
            randnum = choose(num_list)
            randchar = choose(char_list)

            x0, y0 = 20 + i * 160, 20 + j * 120
            x1, y1 = x0 + 120, y0 + 80  # 幅120, 高さ80の矩形

            # 色の割り当て
            if randnum <= 8:
                color[j][i] = "blue"
            elif randnum <= 16:
                color[j][i] = "red"
            elif randnum <= 23:
                color[j][i] = "gray"
            elif randnum == 24:
                color[j][i] = "black"
            else:
                color[j][i] = "white"

            # 矩形を描画
            drawleader.rectangle([x0, y0, x1, y1], fill=color[j][i], outline="black", width=1)
            draw.rectangle([x0, y0, x1, y1], "white", outline="black", width=1)
            # 文字を描画
            font[j][i] = ImageFont.truetype("meiryo.ttc", int(double*120/len(randchar)))
            drawleader.text(((x0 + x1) / 2, (y0 + y1) / 2), randchar, fill="white" if color[j][i] != "white" else "black", font=font[j][i], anchor="mm")
            draw.text(((x0 + x1) / 2, (y0 + y1) / 2), randchar, fill="black" if color[j][i] != "white" else "black", font=font[j][i], anchor="mm")
            position[j][i]=randchar
    

    global FLAG
    global FLAGS
    FLAG=0
    FLAGS=0


    # 画像をバッファに保存
    global img_buffer
    global imgleader_buffer
    imgleader_buffer = io.BytesIO()
    imgleader.save(imgleader_buffer, format="PNG")
    imgleader_buffer.seek(0)
    img_buffer = io.BytesIO()
    img.save(img_buffer, format="PNG")
    img_buffer.seek(0)

    # Discord に送信
    await ctx.send("最初は青のターンからです！")
    #await ctx.send(file=discord.File(imgleader_buffer, "leaderoutput.png"))
    await ctx.send(file=discord.File(img_buffer, "output.png"))
    
    
@bot.command()
async def wordwolf(ctx, text_file: str, num: int):
    # テキストファイルの選択
    if text_file == "原神":
        text_file = "Genshin.txt"
    elif text_file in ["学マス", "学園アイドルマスター"]:
        text_file = "GakuenIMAS.txt"
    elif text_file in ["ブルアカ", "ブルーアーカイブ"]:
        text_file = "BlueArchive.txt"
    elif text_file in ["Arcaea", "アーケア"]:
        text_file = "Arcaea.txt"

    # ファイルを読み込む
    with open(text_file, "r", encoding="utf-8") as file:
        char_list = file.read().strip().split("\n")

    # 2つのワードを選ぶ
    def choose(lst):
        chosen = random.choice(lst)
        lst.remove(chosen)
        return chosen

    majority = choose(char_list)
    minority = choose(char_list)

    # 参加者を集める
    participants = []

    await ctx.send(f"{num} 人が `join` と送信するとゲームが開始されます！")

    def check(m):
        return m.content.lower() == "join" and m.channel == ctx.channel and m.author not in participants

    while len(participants) < num:
        msg = await bot.wait_for("message", check=check)
        participants.append(msg.author)
        await ctx.send(f"{msg.author.mention} が参加しました！ ({len(participants)}/{num})")

    # 参加者リストをシャッフル
    random.shuffle(participants)

    # ワードを配布
    for i, player in enumerate(participants):
        word = majority if i < num - 1 else minority
        await player.send(f"あなたのワードは {word} です。")

    await ctx.send("全員にワードを送信しました！ゲームを開始してください！")


bot.run(TOKEN)
