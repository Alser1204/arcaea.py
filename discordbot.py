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
from discord.utils import escape_markdown
import csv

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

ULT_SECRET = ["!!!!!!! d e e m a n !!!!!!!"]

SECRET = ["マン屁ラップバトル", "World of Tanks"]

N = ["アナニー","チクニー","レイプ","放尿","フェラ","露出プレイ","催眠","時間停止","睡眠姦","ソフトSM","おもらし","逆レイプ","手コキ","足コキ","匂い","お姉さん","巨乳","レイプ目","目隠し","貧乳","無乳","授乳手コキ","触手","壁尻","腋コキ","あまあま","ヤンデレ","ツンデレ","クーデレ","サキュバス","唾液","パイズリ","素股","ペド","ロリババア","口内射精","ぶっかけ", "どこにも居場所がカニ"]

R = ["排便","ロリレイプ","男の娘","ふたなり","ケモ","アナルヒクヒク","オホ声","アヘ顔","緊縛","球体関節","常識改変","ボテ腹","近親相姦","キメセク","首絞め","髪コキ","人外","人形","メカ","義妹","イラマチオ", "毛蟹"]

SR = ["アルマジロのケツマンコ","小笠原祐子","熟女陵辱プレイ","フィギュアぶっかけ","四肢欠損","リョナ","獣姦","超乳","実妹","梅沢富美男のTSマン屁", "ビルオナ", "豚ヅラアクメ", "飲ザー"]

SSR = ["陰毛着火","ゲロモンスター","淫夢","ドラゴンカーセックス","ガナニー","ガンダム","首ちんこ","蟲姦","ゲップオナサポ","スカトロASMR","複乳", "スケベガニ", "ケツ毛パスタ"]

UR = ["ジジイの顔面騎乗下痢噴射","メガレックウザ","夏井いつき", "エッチガニ"]

# 通常排出率
def random_choice():
    roll = random.random()
    if roll < 0.50:
        name = random.choice(N)
        return f"N {name}", name, "N"
    elif roll < 0.80:
        name = random.choice(R)
        return f"R {name}", name, "R"
    elif roll < 0.96:
        name = random.choice(SR)
        return f"SR {name}", name, "SR"
    elif roll < 0.99:
        name = random.choice(SSR)
        return f"SSR {name}", name, "SSR"
    elif roll < 0.998:
        name = random.choice(UR)
        return f"UR {name}", name, "UR"
    elif roll < 0.9999:
        name = random.choice(SECRET)
        return f"!!!SECRET!!! {name}", name, "SECRET"
    else:
        name = random.choice(ULT_SECRET)
        return f"!!!!!ULTIMATE SECRET!!!!!\n{name}", name, "ULT_SECRET"
"""
# デバッグ用
def random_choice():
    roll = random.random()
    if roll < 0.50:
        name = random.choice(ULT_SECRET)
        return f"!!!!!ULTIMATE SECRET!!!!!\n{name}", name, "ULT_SECRET"
    elif roll < 0.80:
        name = random.choice(R)
        return f"R {name}", name, "R"
    elif roll < 0.96:
        name = random.choice(SR)
        return f"SR {name}", name, "SR"
    elif roll < 0.99:
        name = random.choice(SSR)
        return f"SSR {name}", name, "SSR"
    elif roll < 0.998:
        name = random.choice(UR)
        return f"UR {name}", name, "UR"
    elif roll < 0.9999:
        name = random.choice(SECRET)
        return f"!!!SECRET!!! {name}", name, "SECRET"
    else:
        name = random.choice(ULT_SECRET)
        return f"!!!!!ULTIMATE SECRET!!!!!\n{name}", name, "ULT_SECRET"
"""

# レアガチャ排出率
def random_choice_rare():
    roll = random.random()
    if roll < 0.76:
        return "SR " + random.choice(SR), "SR"
    elif roll < 0.91:
        return "SSR " + random.choice(SSR), "SSR"
    elif roll < 0.975:
        return "UR " + random.choice(UR), "UR"
    elif roll < 0.995:
        return "!!!SECRET!!! " + random.choice(SECRET), "SECRET"
    else:
        return "!!!!!ULTIMATE SECRET!!!!!\n"+ random.choice(ULT_SECRET), "ULT_SECRET"

# ============================
# ① レアリティ定義
# ============================

GACHA_POOL = {
    "N": set(N),
    "R": set(R),
    "SR": set(SR),
    "SSR": set(SSR),
    "UR": set(UR),
    "SECRET": set(SECRET),
    "ULT_SECRET": set(ULT_SECRET)
}

# ============================
# ② 実績レア度
# ============================

TIER_ICON = {
    "NORMAL": "⚪",
    "RARE": "🔵",
    "EPIC": "🟣",
    "LEGEND": "👑"
}

# ============================
# ③ 実績定義
# ============================

ACHIEVEMENTS = {}

# --- 混合特定キャラセット ---
ACHIEVEMENTS["H_clab_4"] = {
    "type": "specific_set",
    "characters": {"エッチガニ", "毛蟹", "どこにも居場所がカニ", "スケベガニ"},
    "name": "Hなカニ4選",
    "description": "Hなカニ4選を揃える",
    "tier": "LEGEND"
}

ACHIEVEMENTS["masterbation"] = {
    "type": "specific_set",
    "characters": {"アナニー", "チクニー", "ビルオナ", "ガナニー"},
    "name": "オナニーズ",
    "description": "オナニーを揃える",
    "tier": "EPIC"
}

ACHIEVEMENTS["pain"] = {
    "type": "specific_set",
    "characters": {"四肢欠損", "リョナ", "陰毛着火", "首ちんこ"},
    "name": "痛そう",
    "description": "痛そうな性癖を揃える",
    "tier": "EPIC"
}

ACHIEVEMENTS["get_ULT_SECRET"] = {
    "type": "specific_set",
    "characters": {"!!!!!!! d e e m a n !!!!!!!"},
    "name": "YOU ARE DEEMAN",
    "description": "deemanを引く",
    "tier": "LEGEND"
}

ACHIEVEMENTS["get_RAP_BATTLE"] = {
    "type": "specific_set",
    "characters": {"マン屁ラップバトル"},
    "name": "プロマン屁ラップバトラー",
    "description": "マン屁ラップバトルを引く",
    "tier": "EPIC"
}

ACHIEVEMENTS["get_WoT"] = {
    "type": "specific_set",
    "characters": {"World of Tanks"},
    "name": "ARE YOU DEEMAN?",
    "description": "World of Tanksを引く",
    "tier": "EPIC"
}

# --- 枚数系 ---
ACHIEVEMENTS["double_SECRET"] = {
    "type": "count_rarity",
    "rarity": "SECRET",
    "count": 2,
    "name": "SECRET SECRET",
    "description": "1回のガチャでSECRETを二枚引く",
    "tier": "RARE"
}

ACHIEVEMENTS["all_n_10plus"] = {
    "type": "all_same_rarity",
    "rarity": "N",
    "min_pull": 10,
    "name": "完全爆死",
    "description": "10連以上で全てNを引く",
    "tier": "RARE"
}

ACHIEVEMENTS["first_win"] = {
    "type": "win_count",
    "count": 1,
    "name": "初勝利",
    "description": "dgacha_battleで初勝利する",
    "tier": "NORMAL"
}

ACHIEVEMENTS["achievement_master"] = {
    "type": "complete_all",
    "name": "全実績制覇",
    "description": "すべての実績を獲得する",
    "tier": "LEGEND"
}

ACHIEVEMENTS["ur_double_10pull"] = {
    "type": "count_rarity_10",   # 枚数系
    "rarity": "UR",
    "count": 2,               # 条件: 2枚以上
    "required_n": 10,         # 10回限定
    "name": "URダブル",
    "description": "10連ガチャでURを2枚以上引く",
    "tier": "EPIC"
}

ACHIEVEMENTS["first_pull"] = {
    "type": "first_pull",
    "name": "初ガチャ",
    "description": "初めてガチャを回した",
    "tier": "NORMAL"
}

# ============================
# ④ 実績判定関数
# ============================

def check_achievements(user, pulled_names, pulled_rarities):

    user_counts[user].setdefault("Achievements", {})
    unlocked = []

    pulled_set = set(pulled_names)
    rarity_counter = Counter(pulled_rarities)

    for key, value in ACHIEVEMENTS.items():

        if user_counts[user]["Achievements"].get(key, False):
            continue

        success = False
        achievement_type = value["type"]

        # --- レアリティ完全制覇 ---
        if achievement_type == "rarity_complete":
            rarity = value["rarity"]
            required = value["characters"]

            pulled_target = {
                name for name in pulled_set
                if name in GACHA_POOL[rarity]
            }

            if required.issubset(pulled_target):
                success = True

        # --- 混合特定セット ---
        elif achievement_type == "specific_set":
            if value["characters"].issubset(pulled_set):
                success = True

        # --- 枚数系 ---
        elif achievement_type == "count_rarity":
            if rarity_counter.get(value["rarity"], 0) >= value["count"]:
                success = True
                
        elif achievement_type == "count_rarity_10":
            # 10連限定なら pulled_names の長さで判定
            required_n = value.get("required_n", 0)
            if required_n > 0 and len(pulled_names) != required_n:
                continue  # 条件に合わないので判定しない
        
            if rarity_counter.get(value["rarity"], 0) >= value["count"]:
                success = True
                
        elif achievement_type == "all_same_rarity":
            target_rarity = value["rarity"]
            min_pull = value.get("min_pull", 1)

            if len(pulled_rarities) >= min_pull:
                if all(r == target_rarity for r in pulled_rarities):
                    success = True
                    
        elif achievement_type == "win_count":
            if user_counts[user].get("win_count", 0) >= value["count"]:
                success = True
                
        elif achievement_type == "complete_all":
            user_achievements = user_counts[user].get("Achievements", {})

            # コンプリート実績自身を除外
            total_achievements = [
                key for key in ACHIEVEMENTS.keys()
                if ACHIEVEMENTS[key]["type"] != "complete_all"
            ]

            if all(user_achievements.get(key, False) for key in total_achievements):
                success = True

        elif achievement_type == "first_pull":
            # Achievements にまだ記録がなければ解放
            if not user_counts[user].get("Achievements", {}).get(key, False):
                success = True

        # --- 解放 ---
        if success:
            user_counts[user]["Achievements"][key] = True
            icon = TIER_ICON.get(value["tier"], "")

            unlocked.append(
                f"{icon}【{value['name']}】\n"
                f"{value['description']}"
            )

    return unlocked


# ============================
# ⑤ ガチャコマンド
# ============================

in_battle = False
in_battle_2 = False
battle_member = []
battle_score = []
battle_i = 0
battle_member_2 = []
battle_score_2 = []
battle_i_2 = 0

@bot.command()
async def achievements(ctx):
    """獲得済み実績だけ表示"""
    user = ctx.author.name

    if user not in user_counts or "Achievements" not in user_counts[user]:
        await ctx.send("まだ実績はありません。")
        return

    unlocked = [
        ACHIEVEMENTS[key]["name"]
        for key, got in user_counts[user]["Achievements"].items()
        if got
    ]

    if unlocked:
        await ctx.send("🏆 獲得済み実績:\n" + "\n".join(unlocked))
    else:
        await ctx.send("まだ実績はありません。")

@bot.command()
async def dgacha(ctx, n: int = 10):
    if n>100:
        await ctx.send("ガチャの回数は100回以内にしてください。\n")
        return
    global battle_member, battle_score, in_battle, battle_i
    global battle_member_2, battle_score_2, in_battle_2, battle_i_2
    user_name = ctx.author.name  # user_name に変更
    gacha_score = 0

    # ユーザーのデータがなければ初期化
    if user_name not in user_counts:
        user_counts[user_name] = {
            "total": 0,
            "N": 0, "R": 0, 
            "SR": 0, 
            "SSR": 0, 
            "UR": 0, 
            "SECRET": 0,
            "ULT_SECRET":0,
            "Rate":1000, 
            "coin":0, 
            "battle_count": 0,
            "win_count": 0,
            "Achievements": {},
            "dbreed": {"level":0},
            "profile": None
        }

    results = []
    pulled_names = []
    pulled_rarities = []
    for _ in range(n):

        item_display, item_name, rarity = random_choice()

        results.append(item_display)
        pulled_names.append(item_name)
        pulled_rarities.append(rarity)

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
                "ULT_SECRET": 100,
            }.get(rarity, 0)

            battle_score[idx] += score

        score = {
                "N": 1,
                "R": 2,
                "SR": 3,
                "SSR": 5,
                "UR": 10,
                "SECRET": 15,
                "ULT_SECRET": 100,
            }.get(rarity, 0)

        gacha_score += score
            
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
                "ULT_SECRET": 100,
            }.get(rarity, 0)

            battle_score_2[idx_2] += score
            
    # 実績判定
    unlocked = check_achievements(
        user_name,
        pulled_names,
        pulled_rarities
    )

    save_data()  # データ保存

    count_details = "\n".join(
        f"{rarity}: {user_counts[user_name].get(rarity, 0)}"
        for rarity in ["N", "R", "SR", "SSR", "UR", "SECRET", "ULT_SECRET"]
    )

    if gacha_score == n and n>=10:
            await ctx.send(f"Nが一致です！{round(n*2.5)}のボーナス！")
            gacha_score += round(n*2.5)
            
    profile_raw = user_counts[user_name].get("profile")

    if profile_raw:
        profile = f"[{profile_raw}]"
    else:
        profile = ""

    await ctx.send(f"{profile}{user_name} さんが {n}回 ガチャを引きました。\n"
                   f"結果:\n{'\n'.join(results)}\n"
                   f"スコア:{gacha_score}\n")
    user_counts[user_name]["coin"] += round(gacha_score/10)
    if in_battle:
        idx = battle_member.index(user_name)
        if battle_score[idx] == n and n>=10:
            await ctx.send(f"Nが一致です！{round(n*2.5)}のボーナス！")
            battle_score[idx]+=round(n*2.5)
        
    # 実績表示
    for msg in unlocked:
        await ctx.send(f"🎉 アチーブ解放！\n{msg}")
    battle_i += 1
    battle_i_2 += 1

        

@bot.command()
async def dgacha_rare(ctx, n: int = 10):
    if n>100:
        await ctx.send("ガチャの回数は100回以内にしてください。\n")
        return
    global battle_member, battle_score, in_battle, battle_i
    global battle_member_2, battle_score_2, in_battle_2, battle_i_2
    user_name = ctx.author.name  # user_name に変更
    gacha_score = 0

    # ユーザーのデータがなければ初期化
    if user_name not in user_counts:
        user_counts[user_name] = {"total": 0, "N": 0, "R": 0, "SR": 0, "SSR": 0, "UR": 0, "SECRET": 0,"ULT_SECRET":0, "Rate":1000, "coin":0}

    results = []
    for _ in range(n):
        item, rarity = random_choice_rare()
        results.append(item)

        if rarity not in user_counts[user_name]:
            user_counts[user_name][rarity] = 0

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
                "ULT_SECRET": 100,
            }.get(rarity, 0)

            battle_score[idx] += score

        score = {
                "N": 1,
                "R": 2,
                "SR": 3,
                "SSR": 5,
                "UR": 10,
                "SECRET": 15,
                "ULT_SECRET": 100,
            }.get(rarity, 0)

        gacha_score += score
            
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
                "ULT_SECRET": 100,
            }.get(rarity, 0)

            battle_score_2[idx_2] += score

    save_data()  # データ保存

    count_details = "\n".join(
        f"{rarity}: {user_counts[user_name][rarity]}" for rarity in ["N", "R", "SR", "SSR", "UR", "SECRET","ULT_SECRET"]
    )

    if gacha_score == n and n>=10:
            await ctx.send(f"Nが一致です！{round(n*2.5)}のボーナス！")
            gacha_score += round(n*2.5)
            
    profile_raw = user_counts[user_name].get("profile")

    if profile_raw:
        profile = f"[{profile_raw}]"
    else:
        profile = ""

    await ctx.send(f"{profile}{user_name} さんが {n}回 ガチャを引きました。\n"
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
async def dbreed(ctx, up: int=1):
    user_name = ctx.author.name

    if user_name not in user_counts:
        await ctx.send(f"{user_name} さんのデータが見つかりませんでした。")
        return

    coin = user_counts[user_name]["coin"]

    if coin < 50:
        await ctx.send("コインが足りません。")
        return

    max_up = coin // 50

    if up > max_up:
        await ctx.send(
            f"{up}回育成にはコインが足りません。{max_up}回育成します。"
        )
        up = max_up

    user_counts[user_name].setdefault("dbreed", {"level": 0})

    gain = 0
    for i in range(up):
        gain += random.randint(0, 1)

    user_counts[user_name]["coin"] -= 50 * up
    user_counts[user_name]["dbreed"]["level"] += gain

    await ctx.send(
        f"{up}回育成して、レベルが{gain}上がりました！"
        f"(現在レベル: {user_counts[user_name]['dbreed']['level']})"
        f"(残りコイン: {user_counts[user_name]['coin']})"
    )
    
    
prof_0 = [
    "の",
    "を",
    "に",
    "が",
    "な",
    "への",
    "と",
    "へ",
    "で",
    "や",
    "より",
    "まで",
    "から",
    "だけ",
    "ほど",
    "こそ",
    "すら",
    "さえ",
    "でも",
    "とか",
    "って",
    "なり"
]
prof_5 = [
    "優秀",
    "有能",
    "実力派",
    "堅実",
    "挑戦者",
    "達人",
    "専門家",
    "実践者",
    "成長株",
    "経験豊富"
]
prof_10 = N.copy()
prof_15 = [
    "上級者",
    "熟練者",
    "エース",
    "第一人者",
    "成功者",
    "先駆者",
    "開拓者",
    "実力者",
    "リーダー",
    "カリスマ"
]
prof_20 = R.copy()
prof_25 = [
    "天才",
    "鬼才",
    "英雄",
    "覇者",
    "王者",
    "怪物",
    "革命家",
    "逸材",
    "猛者",
    "支配者"
]
prof_30 = SR.copy()
prof_35 = [
    "神",
    "神童",
    "魔王",
    "覇王",
    "創造主",
    "絶対者",
    "伝説",
    "超越者",
    "救世主",
    "無双"
]
prof_40 = SSR.copy()
prof_45 = [
    "絶対",
    "至高",
    "究極",
    "最強",
    "無敵",
    "圧倒的",
    "伝説級",
    "規格外",
    "完全体",
    "唯一無二"
]
prof_50 = UR.copy()
prof_60 = SECRET.copy()
prof_70 = ULT_SECRET.copy()

@bot.command()
async def dprof(ctx, prof_1: str=None, prof_2: str=None, prof_3: str=None):
    user_name = ctx.author.name

    # ユーザー存在確認
    if user_name not in user_counts:
        await ctx.send(f"{user_name} さんのデータが見つかりませんでした。")
        return

    # デフォルト作成
    user_counts[user_name].setdefault("profile", None)
    user_counts[user_name].setdefault("dbreed", {"level": 0})

    level = user_counts[user_name]["dbreed"]["level"]

    # 引数なし → 現在のプロフィール表示
    if prof_1 is None and prof_2 is None and prof_3 is None:
        current = user_counts[user_name]["profile"]
        if current:
            await ctx.send(f"現在の称号：{current}")
        else:
            await ctx.send("称号はまだ設定されていません。")
            
        level = user_counts[user_name]["dbreed"]["level"]
        unlocking = 5 * (level // 5)

        lines = []
        lines.append(f"{user_name} の使用可能称号一覧\n")
        lines.append(f"現在レベル: {level}")
        lines.append(f"解放帯: Lv{unlocking}\n")

        if unlocking >= 5:
            lines.append("▼Lv5")
            lines.append(" / ".join(prof_5))
            lines.append("")

        if unlocking >= 15:
            lines.append("▼Lv15")
            lines.append(" / ".join(prof_15))
            lines.append("")

        if unlocking >= 25:
            lines.append("▼Lv25")
            lines.append(" / ".join(prof_25))
            lines.append("")

        if unlocking >= 35:
            lines.append("▼Lv35")
            lines.append(" / ".join(prof_35))
            lines.append("")

        if unlocking >= 45:
            lines.append("▼Lv45")
            lines.append(" / ".join(prof_45))
            lines.append("")

        lines.append("▼助詞")
        lines.append(" / ".join(prof_0))

        text = "\n".join(lines)

        # ファイル書き出し
        with open("profile_list.txt", "w", encoding="utf-8") as f:
            f.write(text)

        await ctx.send(file=discord.File("profile_list.txt"))
        return

    # レベル制限（5刻み）
    unlocking = 5 * (level // 5)

    # 使える単語をまとめる
    available_words = []
    if unlocking >= 5:
        available_words += prof_5
    if unlocking >= 10:
        available_words += prof_10
    if unlocking >= 15:
        available_words += prof_15
    if unlocking >= 20:
        available_words += prof_20
    if unlocking >= 25:
        available_words += prof_25
    if unlocking >= 30:
        available_words += prof_30
    if unlocking >= 35:
        available_words += prof_35
    if unlocking >= 40:
        available_words += prof_40
    if unlocking >= 45:
        available_words += prof_45
    if unlocking >= 50:
        available_words += prof_50
    if unlocking >= 60:
        available_words += prof_60
    if unlocking >= 70:
        available_words += prof_70

    available_words += prof_0  # 助詞は常にOK

    # 入力チェック
    for word in [prof_1, prof_2, prof_3]:
        if word is not None and word not in available_words:
            await ctx.send(f"{word} はまだ使用できません。")
            return

    # 結合
    profile = f"{prof_1 or ''}{prof_2 or ''}{prof_3 or ''}"

    # 保存
    user_counts[user_name]["profile"] = profile

    await ctx.send(f"新しい称号：{profile}")

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
        for rarity in ["N", "R", "SR", "SSR", "UR", "SECRET","ULT_SECRET"]
    )

    # レート情報の追加
    count_details += f"\nレート: {user_counts[user_name]['Rate']}\nコイン: {user_counts[user_name]['coin']}\n"
    
    profile_raw = user_counts[user_name].get("profile")

    if profile_raw:
        profile = f"[{profile_raw}]"
    else:
        profile = ""

    await ctx.send(f"{profile}{user_name} さんの累計ガチャ結果:\n"
                   f"ガチャ回数: {total_count}\n"
                   f"カウント詳細:\n{count_details}")


@bot.command()
async def dgacha_reset(ctx):
    user_name = ctx.author.name

    if user_name in user_counts:
        Rate = user_counts[user_name]['Rate']
        coin = user_counts[user_name]['coin']
        # 初期化データを作成
        user_counts[user_name] = {
            "total": 0,
            "N": 0,
            "R": 0,
            "SR": 0,
            "SSR": 0,
            "UR": 0,
            "SECRET": 0,
            "ULT_SECRET":0,
            "Rate": Rate,
            "coin": coin
            
        }
        await ctx.send(f"{user_name} さんのガチャ記録をリセットしました。")
    else:
        await ctx.send(f"{user_name} さんのデータが見つかりませんでした。")

from collections import defaultdict

@bot.command()
async def dgacha_battle(ctx):
    global in_battle, battle_member, battle_score, battle_i, user_counts

    # ==========================
    # バトル終了処理
    # ==========================
    if in_battle:
        in_battle = False

        if len(battle_member) == 0:
            await ctx.send("参加者がいません。")
            return

        await ctx.send("dgacha_battleが終わりました！\n結果:")

        # スコア表示
        for i in range(len(battle_member)):
            await ctx.send(f"{battle_member[i]}さんのスコア: {battle_score[i]}")

        # --------------------------
        # 勝者判定（同点あり）
        # --------------------------
        max_score = max(battle_score)
        max_members = [
            battle_member[i]
            for i in range(len(battle_member))
            if battle_score[i] == max_score
        ]

        # --------------------------
        # ソート（スコア昇順）
        # --------------------------
        sorted_data = sorted(
            zip(battle_member, battle_score),
            key=lambda x: x[1]
        )

        sorted_member = [x[0] for x in sorted_data]
        sorted_score = [x[1] for x in sorted_data]

        n = len(sorted_score)
        average = sum(sorted_score) / n

        # --------------------------
        # 同点グループ化
        # --------------------------
        score_groups = defaultdict(list)
        for idx, score in enumerate(sorted_score):
            score_groups[score].append(idx)

        # --------------------------
        # レート変動計算
        # --------------------------
        rate_changes = [0.0] * n

        for score, indices in score_groups.items():

            group_size = len(indices)

            # 同順位は「平均順位」にする
            avg_rank = sum(indices) / group_size

            for idx in indices:
                value = (
                    (sorted_score[idx] - average)
                    + 2 * (avg_rank - (n - 1) / 2)
                )
                rate_changes[idx] = value

        # --------------------------
        # 丸め処理（平均保存補正）
        # --------------------------
        rounded_changes = [round(v) for v in rate_changes]
        total_change = sum(rounded_changes)

        # 合計が0になるよう補正
        if total_change != 0:
            rounded_changes[-1] -= total_change

        # --------------------------
        # レート反映
        # --------------------------
        for i in range(n):
            user_counts[sorted_member[i]]["Rate"] += rounded_changes[i]

        # ==========================
        # 参加者の回数加算
        # ==========================
        for member in battle_member:

            user_counts.setdefault(member, {})
            user_counts[member].setdefault("battle_count", 0)
            user_counts[member].setdefault("win_count", 0)
            user_counts[member].setdefault("Achievements", {})

            # 参加回数＋1
            user_counts[member]["battle_count"] += 1

        # ==========================
        # 勝者の勝利回数加算
        # ==========================
        for winner in max_members:
            user_counts[winner]["win_count"] += 1

        # ==========================
        # 実績判定
        # ==========================
        for member in battle_member:

            unlocked = check_achievements(
                member,
                pulled_names=[],
                pulled_rarities=[]
            )

            for msg in unlocked:
                await ctx.send(f"🎉 {member} さんが実績解放！\n{msg}")

        # --------------------------
        # 勝者発表
        # --------------------------
        await ctx.send(
            f"\n{'、'.join(max_members)}さんがスコア{max_score}で勝利です！"
        )
        await ctx.send("参加者のレートが変動しました！")

        for i in range(n):
            await ctx.send(
                f"{sorted_member[i]}さん "
                f"{user_counts[sorted_member[i]]['Rate']} "
                f"({rounded_changes[i]:+})"
            )

        return

    # ==========================
    # バトル開始処理
    # ==========================
    await ctx.send("dgacha_battleが始まりました！")
    in_battle = True
    battle_i = 0
    battle_member = []
    battle_score = []


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
from PIL import ImageOps

@bot.command(aliases=["m"])
async def mosaic(ctx, hard: str='null', block_size: int = None, yaju: str='null'):
    server_id = str(ctx.guild.id)
    
    if server_id not in server_settings:
        server_settings[server_id] = {'DefaultG': 6, 'DefaultM': 80}
    DefaultM = server_settings[server_id]['DefaultM']
    
    if block_size is None:
        block_size = DefaultM if DefaultM is not None else 80

    try:
        if block_size < 5 or block_size > 500:
            await ctx.send("分割数は5以上500以下の数にしてください。")
            return

        image_files = [f for f in os.listdir(IMAGE_DIR) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]
        if not image_files:
            await ctx.send("画像が見つかりません。")
            return

        random_image = secrets.choice(image_files)
        image_path = os.path.join(IMAGE_DIR, random_image)

        if yaju == 'yaju':
            image_files = [f for f in os.listdir(YAJU_DIR) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]
            if not image_files:
                await ctx.send("画像が見つかりません。")
                return
            random_image = secrets.choice(image_files)
            image_path = os.path.join(YAJU_DIR, random_image)

        img = Image.open(image_path)

        # hard が指定されていたらモノクロ化
        if hard == 'hard':
            img = img.convert("L").convert("RGB")

        img_width, img_height = img.size
        img_array = np.array(img)

        for y in range(0, img_height, block_size):
            for x in range(0, img_width, block_size):
                block = img_array[y:y + block_size, x:x + block_size]
                avg_color = np.mean(block, axis=(0, 1)).astype(int)
                img_array[y:y + block_size, x:x + block_size] = avg_color

        mosaic_img = Image.fromarray(img_array)
        temp_image_path = 'temp_image.png'
        mosaic_img.save(temp_image_path)

        sent_message = await ctx.send(file=discord.File(temp_image_path))
        os.remove(temp_image_path)

        def check(m):
            return m.channel == ctx.channel and m.reference is not None and m.reference.message_id == sent_message.id

        start_time = asyncio.get_event_loop().time()
        FRAG = 1

        while asyncio.get_event_loop().time() - start_time < 30:
            try:
                response = await asyncio.wait_for(bot.wait_for('message', check=check), timeout=30.0)
                if (response.content.lower() == os.path.splitext(random_image)[0].lower()) or \
                   (len(response.content) >= 3 and response.content.lower() in os.path.splitext(random_image)[0].lower()) or \
                   (len(response.content) >= 3 and is_acronym(response.content, os.path.splitext(random_image)[0])):
                    await response.reply("正解です！")
                    FRAG = 0
                    break
                elif response.content.lower() in ["!s", "!skip"]:
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
async def guessc(ctx, hard: str='null', n: float = None):
    server_id = str(ctx.guild.id)
    
    if server_id not in server_settings:
        server_settings[server_id] = {'DefaultG': 6, 'DefaultM': 80}
    DefaultG = server_settings[server_id]['DefaultG']
    
    if n is None:
        n = DefaultG if DefaultG is not None else 6

    try:
        if n < 1 or n > 20:
            await ctx.send("分割数は1以上20以下の数にしてください。")
            return

        image_files = [f for f in os.listdir(IMAGE_DIR) if f.endswith(('png', 'jpg', 'jpeg', 'gif'))]
        if not image_files:
            await ctx.send("画像が見つかりません。")
            return

        random_image = secrets.choice(image_files)
        image_path = os.path.join(IMAGE_DIR, random_image)

        img = Image.open(image_path)

        # hard が指定されていたらモノクロ化
        if hard == 'hard':
            img = img.convert("L").convert("RGB")

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

        selected_tile = secrets.choice(tiles)

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
                if (response.content.lower() == os.path.splitext(random_image)[0].lower()) or \
                   (len(response.content) >= 3 and response.content.lower() in os.path.splitext(random_image)[0].lower()) or \
                   (len(response.content) >= 3 and is_acronym(response.content, os.path.splitext(random_image)[0])):
                    await response.reply("正解です！")
                    FRAG = 0
                    break
                elif response.content.lower() in ["!s", "!skip"]:
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
found_count = 0
allowed_numbers=[]
log_list=[]
font=[["" for _ in range(rootnum)] for _ in range(rootnum)]

@bot.command()
async def blue(ctx, target:str):
    global position,color, found_count
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
    global position,color, found_count
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
async def sets(ctx, vain:str, n:int):
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

def for_csv_read(csv_file, num):
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # attribute / country ごとにグループ化
    attr_groups = {}
    country_groups = {}

    for r in rows:
        attr_groups.setdefault(r["attribute"], []).append(r["name"])
        country_groups.setdefault(r["country"], []).append(r["name"])

    # 2人以上いるグループだけ残す
    valid_groups = [
        v for v in list(attr_groups.values()) + list(country_groups.values())
        if len(v) >= num + 1
    ]

    if not valid_groups:
        raise ValueError("共通項目を持つキャラが不足しています")

    group = random.choice(valid_groups)
    random.shuffle(group)

    majority = group[:num]
    minority = majority.copy()
    minority[-1] = random.choice([x for x in group if x not in majority])

    random.shuffle(minority)
    return majority, minority

current_wolf = None
    
@bot.command()
async def wordwolf(ctx, text_file: str, num:int=3, reveal_wolf: bool = False, reveal_vil: bool = False):
    if num < 1:
        await ctx.send("カード枚数は1以上にしてください")
        return
    use_csv = False
    # テキストファイルの選択
    if text_file == "原神":
        text_file = "Genshin.txt"
        name = "原神"
    elif text_file == "はらがみ":
        text_file = "Genshin.csv"
        name = "共通要素アリ原神"
        use_csv = True
        num = 1
    elif text_file in ["学マス", "学園アイドルマスター"]:
        text_file = "GakuenIMAS.txt"
        name = "学マス"
    elif text_file in ["ブルアカ", "ブルーアーカイブ"]:
        text_file = "BlueArchive.txt"
        name = "ブルアカ"
    elif text_file in ["Arcaea", "アーケア"]:
        text_file = "Arcaea.txt"
        name = "Arcaea"
    elif text_file in ["プロセカhard", "プロジェクトセカイhard"]:
        text_file = "PJSekai.txt"
        name = "プロセカ(詳細なし版)"
    elif text_file in ["プロセカ", "プロジェクトセカイ", "プロジェクトセカイ カラフルステージ feat. 初音ミク"]:
        text_file = "PJSekai.csv"
        name = "プロセカ"
    elif text_file in ["国", "国名"]:
        text_file = "Country.txt"
        name = "国名"
    elif text_file in ["バンドリ", "ガルパ"]:
        text_file = "BanGDream.csv"
        name = "バンドリ"
    elif text_file in ["バンドリhard", "ガルパhard"]:
        text_file = "BanGDream.txt"
        name = "バンドリ(詳細なし版)"
    elif text_file in ["英語", "english", "English"]:
        text_file = "English.csv"
        name = "英語"
    elif text_file in ["MyGO!!!!!", "Mygo", "mygo", "まいご", "迷子"]:
        text_file = "Mygo.txt"
        name = "MyGO!!!!!"
    elif text_file in ["マイクラ", "マインクラフト"]:
        text_file = "Minecraft_item.txt"
        name = "マイクラ"
    elif text_file in ["minecraft", "マイクラ英語", "マイクラen", "マイクラEN"]:
        text_file = "Minecraft_item_en.txt"
        name = "マイクラ(英語)"
    else:
        await ctx.send("対応していないジャンルです")
        return

    # ファイル読み込み
    if not use_csv:
        with open(text_file, "r", encoding="utf-8") as file:
            char_list = file.read().strip().split("\n")

    def choose(lst):
        chosen = random.choice(lst)
        lst.remove(chosen)
        return chosen

    majority = []
    minority = []

    if use_csv:
        majority, minority = for_csv_read(text_file, num)
    else:
        for _ in range(num):
            majority.append(choose(char_list))
        minority = majority.copy()
        minority[-1] = choose(char_list)
        random.shuffle(minority)

    participants = []

    await ctx.send(
        "参加する人は `join` と送信してください。\n"
        "全員集まったら `start` と送ると開始します。"
    )

    def check(m):
        return (
            m.channel == ctx.channel and
            (
                (m.content.lower() == "join" and m.author not in participants) or
                (m.content.lower() == "start" and m.author == ctx.author)
            )
        )

    while True:
        msg = await bot.wait_for("message", check=check)

        if msg.content.lower() == "join":
            participants.append(msg.author)
            await ctx.send(f"{msg.author.mention} が参加しました！ ({len(participants)}人)")
        elif msg.content.lower() == "start":
            await ctx.send(f"ジャンル：{name}")
            break

    random.shuffle(participants)
    participants_num = len(participants)
    global current_wolf
    current_wolf = random.choice(participants)

    for player in participants:
        random.shuffle(majority)
        is_wolf = (player == current_wolf)
        hand = minority if is_wolf else majority
    
        message_lines = []
    
        # 役職通知
        if is_wolf and reveal_wolf:
            message_lines.append("あなたは **人狼** です。")
        if (not is_wolf) and reveal_vil:
            message_lines.append("あなたは **村人** です。")
    
        # 手札は必ず表示
        message_lines.append(f"あなたの手札：{', '.join(hand)}")
    
        await player.send("\n".join(message_lines))

    await ctx.send("全員にワードを送信しました！ゲームを開始してください！")

@bot.command()
async def wolf(ctx):
    global current_wolf
    await ctx.send(f"人狼は{current_wolf.mention}でした！")
    current_wolf = None
    

# --- Arcaea.txt から単語リストを読み込み ---
def load_words(filename="Arcaea.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        print("⚠️ Arcaea.txt が見つかりません。")
        return []

trash = load_words()

# ゲームの状態を保存する辞書
games = {}

import re
import unicodedata

# ひらがな⇄カタカナ変換テーブル
HIRA_TO_KATA = str.maketrans(
    {chr(i): chr(i + 0x60) for i in range(0x3041, 0x3097)}  # ひらがな→カタカナ
)
KATA_TO_HIRA = str.maketrans(
    {chr(i): chr(i - 0x60) for i in range(0x30A1, 0x30F7)}  # カタカナ→ひらがな
)

def normalize_japanese(text: str):
    """日本語を正規化（全角/半角・カタカナ→ひらがな変換）"""
    text = unicodedata.normalize("NFKC", text)  # 全角→半角統一
    text = text.translate(KATA_TO_HIRA)         # カタカナ→ひらがな
    return text


def analyze_word_characters(word: str) -> str:
    """単語中の文字種の割合を返す"""
    categories = {
        "ひらがな": r"[ぁ-ん]",
        "カタカナ": r"[ァ-ヶ]",
        "漢字": r"[一-龯々]",
        "英字": r"[A-Za-z]",
        "数字": r"[0-9]",
    }

    total = len(word)
    if total == 0:
        return "（文字なし）"

    counts = {name: len(re.findall(pattern, word)) for name, pattern in categories.items()}
    matched = sum(counts.values())
    counts["記号など"] = total - matched

    result_parts = []
    for name, count in counts.items():
        if count > 0:
            pct = (count / total) * 100
            result_parts.append(f"{name} {pct:.0f}%")

    return "、".join(result_parts)

default_text_files = {}

@bot.command()
async def hangman(ctx, text_file:str=None, num:int=6):

    channel_id = ctx.channel.id

    if text_file is None:
        text_file = default_text_files.get(channel_id, "Arcaea")

    if text_file == "原神":
        text_file = "Genshin.txt"
        name = "原神"
    elif text_file in ["学マス", "学園アイドルマスター"]:
        text_file = "GakuenIMAS.txt"
        name = "学マス"
    elif text_file in ["ブルアカ", "ブルーアーカイブ"]:
        text_file = "BlueArchive.txt"
        name = "ブルアカ"
    elif text_file in ["Arcaea", "アーケア"]:
        text_file = "Arcaea.txt"
        name = "Arcaea"
    elif text_file in ["プロセカhard", "プロジェクトセカイhard", "プロセカ(詳細なし版)"]:
        text_file = "PJSekai.txt"
        name = "プロセカ(詳細なし版)"
    elif text_file in ["プロセカ", "プロジェクトセカイ", "プロジェクトセカイ カラフルステージ feat. 初音ミク"]:
        text_file = "PJSekai.csv"
        name = "プロセカ"
    elif text_file in ["国", "国名"]:
        text_file = "Country.txt"
        name = "国名"
    elif text_file in ["バンドリ", "ガルパ"]:
        text_file = "BanGDream.csv"
        name = "バンドリ"
    elif text_file in ["バンドリhard", "ガルパhard", "バンドリ(詳細なし版)"]:
        text_file = "BanGDream.txt"
        name = "バンドリ(詳細なし版)"
    elif text_file in ["英語", "english", "English"]:
        text_file = "English.csv"
        name = "英語"
    elif text_file in ["MyGO!!!!!", "Mygo", "mygo", "まいご", "迷子"]:
        text_file = "Mygo.txt"
        name = "MyGO!!!!!"
    elif text_file in ["マイクラ", "マインクラフト"]:
        text_file = "Minecraft_item.txt"
        name = "マイクラ"
    elif text_file in ["minecraft", "マイクラ英語", "マイクラen", "マイクラEN", "マイクラ(英語)"]:
        text_file = "Minecraft_item_en.txt"
        name = "マイクラ(英語)"
    else:
        await ctx.send("対応していないジャンルです")
        return

    default_text_files[channel_id] = name

        
    # ファイルを読み込む
    if text_file == "English.csv":
        WORDS = []
        EXPLANATIONS = []
        JP_WORDS = None
        TYPE = None
        BAND = None
        with open(text_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # ヘッダーがあれば読み飛ばす
            for row in reader:
                if len(row) >= 2:
                    WORDS.append(row[0].strip())
                    EXPLANATIONS.append(row[1].strip())
                elif len(row) == 1:
                    WORDS.append(row[0].strip())
                    EXPLANATIONS.append(None)
    elif text_file in ["BanGDream.csv", "PJSekai.csv"]:
        WORDS = []
        EXPLANATIONS = None
        JP_WORDS = None
        TYPE = []
        BAND = []
        with open(text_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # ヘッダーがあれば読み飛ばす
            for row in reader:
                if len(row) >= 3:
                    WORDS.append(row[0].strip())
                    TYPE.append(row[1].strip())
                    BAND.append(row[2].strip())
                elif len(row) == 2:
                    WORDS.append(row[0].strip())
                    TYPE.append(row[1].strip())
                    BAND.append(None)
                elif len(row) == 1:
                    WORDS.append(row[0].strip())
                    TYPE.append(None)
                    BAND.append(None)
    elif text_file == "Minecraft_item_en.txt":
        # 英語ファイルを読み込み
        with open("Minecraft_item_en.txt", "r", encoding="utf-8") as f:
            WORDS = [line.strip() for line in f if line.strip()]
    
        # 日本語ファイルも読み込む
        with open("Minecraft_item.txt", "r", encoding="utf-8") as f:
            JP_WORDS = [line.strip() for line in f if line.strip()]
    
        # 説明・タイプ・バンドは使わないので初期化
        EXPLANATIONS = None
        TYPE = None
        BAND = None
    else:
        EXPLANATIONS = None
        JP_WORDS = None
        TYPE = None
        BAND = None
        with open(text_file, "r", encoding="utf-8") as file:
            WORDS = [line.strip() for line in file if line.strip()]


    
    """ハングマンを開始"""
    if ctx.channel.id in games:
        await ctx.send("すでにゲームが進行中です！")
        return

    if not WORDS:
        await ctx.send("単語リストが空です。Arcaea.txt を確認してください。")
        return

    # CSV の場合は index を合わせて explanation を取得
    idx = random.randrange(len(WORDS))
    raw_word = WORDS[idx]
    word = WORDS[idx].lower()
    explanation = EXPLANATIONS[idx] if EXPLANATIONS else None
    jp_word = JP_WORDS[idx] if text_file == "Minecraft_item_en.txt" else None
    song_type = TYPE[idx] if TYPE else None
    band = BAND[idx] if BAND else None
    hidden = ["ˍ" if re.match(r"[A-Za-z0-9ぁ-んァ-ヶ一-龯々]", c) else c for c in word]  # 記号はそのまま表示

    games[ctx.channel.id] = {
        "word": word,
        "raw_word":raw_word,
        "hidden": hidden,
        "tries": num,
        "guessed": [],
        "explanation": explanation,
        "jp_word": jp_word,
        "song_type": song_type,
        "band": band
    }

    composition = analyze_word_characters(word)
    if song_type and band:
        msg = (
            f"🎯 **ハングマン開始！**\n"
            f"単語の長さ: {len(word)} 文字\n"
            f"単語: {escape_markdown(' '.join(hidden))}\n"
            f"文字構成: {composition}\n"
            f"出題ジャンル: {name}\n"
            f"楽曲タイプ: {song_type}\n"
            f"演奏バンド: {band}\n"
            f"残りミス: {num}\n"
            f"文字を `!hang(!h) 文字列` の形で入力してください！"
        )

    else:
        msg = (
            f"🎯 **ハングマン開始！**\n"
            f"単語の長さ: {len(word)} 文字\n"
            f"単語: {escape_markdown(' '.join(hidden))}\n"
            f"文字構成: {composition}\n"
            f"出題ジャンル: {name}\n"
            f"残りミス: {num}\n"
            f"文字を `!hang(!h) 文字列` の形で入力してください！"
        )
    await ctx.send(msg)
    
@bot.command()
async def hangfinish(ctx):
    """現在のハングマンゲームを強制終了"""
    if ctx.channel.id in games:
        game = games[ctx.channel.id]
        await ctx.send("🛑 ハングマンゲームを強制終了しました。")
        await ctx.send(f"正解は `{game["raw_word"]}` でした。")
        if game["explanation"]:
            await ctx.send(f"📘 **解説:** {game['explanation']}")
        if game["jp_word"]:
            await ctx.send(f"📘 **日本語名:** {game['jp_word']}")
        del games[ctx.channel.id]
    else:
        await ctx.send("現在、このチャンネルで進行中のゲームはありません。")

def char_category(ch):
    # ひらがな
    if 'ぁ' <= ch <= 'ゖ':
        return "kana"  # ひらがな・カタカナ共通カテゴリ
    # カタカナ
    if 'ァ' <= ch <= 'ヶ':
        return "kana"  # ひらがな・カタカナ共通カテゴリ
    # 漢字
    if '\u4E00' <= ch <= '\u9FFF':
        return "kanji"
    # 英字
    if ch.isalpha():
        return "alpha"
    # 数字
    if ch.isdigit():
        return "digit"
    return "other"


@bot.command(aliases=["h"])
async def hang(ctx, letters: str=None):
    if ctx.channel.id not in games:
        await ctx.send("まず `!hangman` でゲームを始めてください。")
        return

    game = games[ctx.channel.id]

    if letters is None:
        if game["guessed"]:
            sorted_letters = sorted(game["guessed"])
            await ctx.send(f"📌 これまでに使われた文字: {', '.join(sorted_letters)}")
        else:
            await ctx.send("まだ使われた文字はありません。")
        return
    word = game["word"]

    # ✅ 英字のみ小文字化（日本語はそのまま）
    letters = "".join(ch.lower() if "A" <= ch <= "Z" else ch for ch in letters)

    # ✅ 有効な文字判定（英数字・日本語のみ）
    if not re.match(r"^[A-Za-z0-9ぁ-んァ-ヶ一-龯々ー]+$", letters):
        await ctx.send("英字または日本語の文字を入力してください。")
        return

    new_letters = [ch for ch in letters if ch not in game["guessed"]]
    if not new_letters:
        await ctx.send("すべての文字がすでに使われています。")
        return

    hidden_categories = {
        char_category(c)
        for c, h in zip(word, game["hidden"])
        if h == "ˍ"   # 未解答部分のみ
    }

    input_categories = {char_category(c) for c in new_letters}

    # 1つも共通カテゴリがない場合 → 文字種が違うので return
    if input_categories.isdisjoint(hidden_categories):
        await ctx.send("その文字種はこの単語に含まれていません。")
        return

    game["guessed"].extend(new_letters)

    correct_letters = []
    wrong_letters = []

    for letter in new_letters:
        # ✅ ひらがな⇄カタカナを無視して比較
        normalized_letter = normalize_japanese(letter)
        normalized_word = normalize_japanese(word)
    
        if normalized_letter in normalized_word:
            correct_letters.append(letter)
            for i, c in enumerate(word):
                if normalize_japanese(c) == normalized_letter:
                    game["hidden"][i] = c
        else:
            wrong_letters.append(letter)
            game["tries"] -= 1

    # 表示処理
    msg = ""
    if correct_letters:
        msg += f"✅ 正解の文字: {', '.join(correct_letters)}\n"
    if wrong_letters:
        msg += f"❌ ハズレの文字: {', '.join(wrong_letters)}\n"
    msg += f"残りミス: {game['tries']}\n{' '.join(game['hidden'])}"
    await ctx.send(msg)

    # 勝敗判定
    if "ˍ" not in game["hidden"] and game["tries"] > 0:
        await ctx.send(f"🎉 クリア！単語は `{game["raw_word"]}` でした！")
        if game["explanation"]:
            await ctx.send(f"📘 **解説:** {game['explanation']}")
        if game["jp_word"]:
            await ctx.send(f"📘 **日本語名:** {game['jp_word']}")
        del games[ctx.channel.id]
    elif game["tries"] <= 0:
        await ctx.send(f"💀 ゲームオーバー！正解は `{game["raw_word"]}` でした。")
        if game["explanation"]:
            await ctx.send(f"📘 **解説:** {game['explanation']}")
        if game["jp_word"]:
            await ctx.send(f"📘 **日本語名:** {game['jp_word']}")
        del games[ctx.channel.id]



JSON_PATH = 'songs.json'

# 現在出題中の問題保持
game_state = {
'answer': None,
'hints': None,
'used_hints': [] # 追加: 今まで出したヒントを保存
}

# ---- JSON 読み取り ----
def load_songs():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

# ---- !quiz / !q ----
@bot.command(name='quiz', aliases=['q'])
async def quiz(ctx):
    songs = load_songs()
    title = random.choice(list(songs.keys()))
    info = songs[title]

    game_state['answer'] = title
    game_state['hints'] = info
    game_state['used_hints'] = []

    await ctx.send("クイズ！ この曲は何でしょう？\n回答は **!answer** または **!a**")

# ---- !answer / !a ----
@bot.command(name='answer', aliases=['ans'])
async def answer(ctx, *, user_answer: str = None):


    if game_state['answer'] is None:
        await ctx.send("今は問題が出ていません。!quiz で開始してください。")
        return
    
    
    if user_answer is None:
        await ctx.send("回答を入力してください: 例) !a 曲名")
        return
    
    correct = game_state['answer']
    ua = user_answer.strip()
    
    if ua.lower() in correct.lower() and len(ua)>=3 or ua.lower()==correct.lower():
        await ctx.send(f"正解！🎉 曲名は **{correct}** でした！")
        game_state['answer'] = None
        game_state['hints'] = None
        game_state['used_hints'] = []
    elif ua == "giveup":
        await ctx.send(f"ギブアップ！曲名は **{correct}** でした！")
        game_state['answer'] = None
        game_state['hints'] = None
        game_state['used_hints'] = []
    else:
        await ctx.send("不正解！ もう一度どうぞ。")

# ---- !hint ----
@bot.command(name='hint')
async def hint(ctx, key: str = None):
    if game_state['hints'] is None:
        await ctx.send("現在ヒントのある問題がありません。!quiz を実行してください。")
        return

    # ---- !hint all → これまでのヒント ----
    if key == 'all':
        if not game_state['used_hints']:
            await ctx.send("まだヒントは出ていません。")
        else:
            formatted = "\n".join([f"{k}: {v}" for k, v in game_state['used_hints']])
            await ctx.send(f"今までに出したヒント：\n{formatted}")
        return

    # キー未指定 → ヒント一覧を見せる
    if key is None:
        available = ', '.join(game_state['hints'].keys())
        await ctx.send(
            f"利用可能なヒントキー: {available}\n"
            f"`!hint all` で今までに出したヒント一覧を表示"
        )
        return

    if key in ["作曲者", "コンポーザー"]:
        key = "composer"
    if key in ["アートワーク", "絵師"]:
        key = "artwork"
    if key in ["譜面製作者", "譜面制作者", "チャーター", "chart", "charter"]:
        key = "chart designer"
    if key in ["難易度", "レベル", "difficulty"]:
        key = "level"
    if key in ["定数", "譜面定数"]:
        key = "constants"
    if key in ["長さ", "曲の長さ", "演奏時間"]:
        key = "length"
    if key in ["BPM"]:
        key = "bpm"
    if key in ["パック"]:
        key = "pack"
    if key in ["サイド", "属性"]:
        key = "side"
    if key in ["モバイル", "モバイル版"]:
        key = "mobile"
    if key in ["スイッチ", "スイッチ版"]:
        key = "switch"
        
    # キーが存在しない
    info = game_state['hints']
    if key not in info:
        await ctx.send("そのヒントキーは存在しません。")
        return

    # ヒントを返す
    value = info[key]
    # 履歴に追加
    if (key, value) not in game_state['used_hints']:
        game_state['used_hints'].append((key, value))


    await ctx.send(f"ヒント ({key}): {value}")

# ==================
# ゲーム状態
# ==================
participants = []
player_cards = {}
game_active = False
field_life = 3
round_num = 1
max_rounds = 10

# 全カードの正しい順
sorted_all_cards = []

# 出たカード
used_numbers = []


# ==================
# ラウンド開始
# ==================
async def start_round(ctx):
    global player_cards, participants, field_life, round_num
    global sorted_all_cards, used_numbers

    await ctx.send(f"--- ラウンド {round_num} 開始 ---")

    available_numbers = list(range(1, 101))

    player_cards.clear()
    sorted_all_cards = []
    used_numbers = []

    for p in participants:
        cards = random.sample(available_numbers, round_num)

        for c in cards:
            available_numbers.remove(c)

        cards.sort()
        player_cards[p] = cards

        try:
            await p.send(f"あなたに配られた数字は {cards} です。\n小さい順に出してください。")
        except:
            await ctx.send(f"{p.mention} にDMを送れませんでした。")

        sorted_all_cards.extend(cards)

    sorted_all_cards.sort()

    await ctx.send(
        f"カードを配布しました。\n"
        f"場のライフ: {field_life}\n"
        f"`!push <数字>` で数字を出してください！"
    )


# ==================
# ゲーム開始
# ==================
@bot.command()
async def ito(ctx, a:str=None):
    global participants, game_active, field_life, round_num, player_cards

    if a == "reset":
        await reset_game(ctx)
        return

    if game_active:
        await ctx.send("すでにゲーム中です！")
        await ctx.send("リセットする場合は!ito resetと送信してください！")
        return

    participants = []
    game_active = True
    field_life = 3
    round_num = 1
    player_cards = {}

    await ctx.send("`join` → 参加\n`start` → ゲーム開始")

    def check(m):
        return m.channel == ctx.channel and m.content.lower() in ["join", "start"]

    while True:
        msg = await bot.wait_for("message", check=check)

        if msg.content.lower() == "join":
            if msg.author not in participants:
                participants.append(msg.author)
                await ctx.send(f"{msg.author.mention} が参加！（{len(participants)}人）")
            else:
                await ctx.send("あなたはすでに参加しています。")
        else:
            if len(participants) == 0:
                await ctx.send("参加者がいません！")
            else:
                await ctx.send("ゲーム開始！")
                break

    await start_round(ctx)


# ==================
# push コマンド
# ==================
@bot.command()
async def push(ctx, num_input: int):
    global field_life, game_active, sorted_all_cards, used_numbers
    global round_num, max_rounds

    if not game_active:
        await ctx.send("ゲームは開始されていません。")
        return

    player = ctx.author

    if player not in player_cards:
        await ctx.send(f"{player.mention} はゲームに参加していません。")
        return

    # 手札にない数字
    if num_input not in player_cards[player]:
        field_life -= 1
        await ctx.send(
            f"{player.mention} 手札にない数字です！\n"
            f"ライフ -1 → {field_life}"
        )
        if field_life <= 0:
            await ctx.send("ライフが0！ゲーム終了！")
            await reset_game(ctx)
        return

    # 既に出された数字は無効
    if num_input in used_numbers:
        await ctx.send(f"{player.mention} その数字はすでに出されています！")
        return

    # 「次に正しく出すべき数字」
    correct_number = sorted_all_cards[len(used_numbers)]

    # 正解
    if num_input == correct_number:
        used_numbers.append(num_input)
        await ctx.send(f"{player.mention} 正解！ → {num_input}")
    
    else:
        # 飛ばした枚数を計算
        correct_index = sorted_all_cards.index(correct_number)
        wrong_index = sorted_all_cards.index(num_input)

        skipped = [x for x in sorted_all_cards if x < num_input and x not in used_numbers] # 飛ばした数字
        used_numbers.extend(skipped)
        used_numbers.append(num_input)
        
        missed_count = len(skipped)
        field_life -= missed_count

        await ctx.send(
            f"{player.mention} 不正解！\n"
            f"{missed_count}枚飛ばしました。\n"
            f"ライフ -{missed_count} → {field_life}\n"
            f"出した数字 → {num_input}"
        )

        if field_life <= 0:
            await ctx.send("ライフが0！ゲーム終了！")
            await reset_game(ctx)
            return

    # すべてのカードを使い切った？
    if len(used_numbers) == len(sorted_all_cards):
        if round_num >= max_rounds:
            await ctx.send("最大ラウンド到達！ゲームクリア！")
            await reset_game(ctx)
            return

        await ctx.send(f"ラウンド {round_num} クリア！ 次のラウンドへ！")
        round_num += 1

        if field_life < 3:
            field_life += 1

        await start_round(ctx)


# ==================
# ゲームリセット
# ==================
async def reset_game(ctx):
    global participants, game_active, field_life, round_num
    global player_cards, sorted_all_cards, used_numbers

    participants.clear()
    player_cards.clear()
    sorted_all_cards.clear()
    used_numbers.clear()

    field_life = 3
    round_num = 1
    game_active = False

    await ctx.send("ゲームをリセットしました。")

@bot.command()
async def rand(ctx):
    number=random.randint(1,100)
    await ctx.send(f"乱数：{number}")

@bot.command()
async def odai(ctx):
    try:
        with open("Odai.txt", "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip()]
        
        if not words:
            await ctx.send("Odai.txt に単語が入っていません。")
            return

        word = random.choice(words)
        await ctx.send(f"お題：{word}")

    except FileNotFoundError:
        await ctx.send("Odai.txt が見つかりません。")

@bot.command(aliases=["angman"])
async def anagram(ctx, text_file: str=None, num: int = 6):
    channel_id = ctx.channel.id

    if text_file is None:
        text_file = default_text_files.get(channel_id, "Arcaea")

    if text_file == "原神":
        text_file = "Genshin.txt"
        name = "原神"
    elif text_file in ["学マス", "学園アイドルマスター"]:
        text_file = "GakuenIMAS.txt"
        name = "学マス"
    elif text_file in ["ブルアカ", "ブルーアーカイブ"]:
        text_file = "BlueArchive.txt"
        name = "ブルアカ"
    elif text_file in ["Arcaea", "アーケア"]:
        text_file = "Arcaea.txt"
        name = "Arcaea"
    elif text_file in ["プロセカhard", "プロジェクトセカイhard", "プロセカ(詳細なし版)"]:
        text_file = "PJSekai.txt"
        name = "プロセカ(詳細なし版)"
    elif text_file in ["プロセカ", "プロジェクトセカイ", "プロジェクトセカイ カラフルステージ feat. 初音ミク"]:
        text_file = "PJSekai.csv"
        name = "プロセカ"
    elif text_file in ["国", "国名"]:
        text_file = "Country.txt"
        name = "国名"
    elif text_file in ["バンドリ", "ガルパ"]:
        text_file = "BanGDream.csv"
        name = "バンドリ"
    elif text_file in ["バンドリhard", "ガルパhard", "バンドリ(詳細なし版)"]:
        text_file = "BanGDream.txt"
        name = "バンドリ(詳細なし版)"
    elif text_file in ["英語", "english", "English"]:
        text_file = "English.csv"
        name = "英語"
    elif text_file in ["MyGO!!!!!", "Mygo", "mygo", "まいご", "迷子"]:
        text_file = "Mygo.txt"
        name = "MyGO!!!!!"
    elif text_file in ["マイクラ", "マインクラフト"]:
        text_file = "Minecraft_item.txt"
        name = "マイクラ"
    elif text_file in ["minecraft", "マイクラ英語", "マイクラen", "マイクラEN", "マイクラ(英語)"]:
        text_file = "Minecraft_item_en.txt"
        name = "マイクラ(英語)"
    else:
        await ctx.send("対応していないジャンルです")
        return

    default_text_files[channel_id] = name

        
    # ファイルを読み込む
    if text_file == "English.csv":
        WORDS = []
        EXPLANATIONS = []
        JP_WORDS = None
        TYPE = None
        BAND = None
        with open(text_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # ヘッダーがあれば読み飛ばす
            for row in reader:
                if len(row) >= 2:
                    WORDS.append(row[0].strip())
                    EXPLANATIONS.append(row[1].strip())
                elif len(row) == 1:
                    WORDS.append(row[0].strip())
                    EXPLANATIONS.append(None)
    elif text_file in ["BanGDream.csv", "PJSekai.csv"]:
        WORDS = []
        EXPLANATIONS = None
        JP_WORDS = None
        TYPE = []
        BAND = []
        with open(text_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # ヘッダーがあれば読み飛ばす
            for row in reader:
                if len(row) >= 3:
                    WORDS.append(row[0].strip())
                    TYPE.append(row[1].strip())
                    BAND.append(row[2].strip())
                elif len(row) == 2:
                    WORDS.append(row[0].strip())
                    TYPE.append(row[1].strip())
                    BAND.append(None)
                elif len(row) == 1:
                    WORDS.append(row[0].strip())
                    TYPE.append(None)
                    BAND.append(None)
    elif text_file == "Minecraft_item_en.txt":
        # 英語ファイルを読み込み
        with open("Minecraft_item_en.txt", "r", encoding="utf-8") as f:
            WORDS = [line.strip() for line in f if line.strip()]
    
        # 日本語ファイルも読み込む
        with open("Minecraft_item.txt", "r", encoding="utf-8") as f:
            JP_WORDS = [line.strip() for line in f if line.strip()]
    
        # 説明・タイプ・バンドは使わないので初期化
        EXPLANATIONS = None
        TYPE = None
        BAND = None
    else:
        EXPLANATIONS = None
        JP_WORDS = None
        TYPE = None
        BAND = None
        with open(text_file, "r", encoding="utf-8") as file:
            WORDS = [line.strip() for line in file if line.strip()]

    if channel_id in games:
        await ctx.send("すでにゲームが進行中です！")
        return

    if not WORDS:
        await ctx.send("単語リストが空です")
        return

    idx = random.randrange(len(WORDS))
    raw_word = WORDS[idx]
    word = raw_word.lower()

    # ====== シャッフル（元と同じは禁止） ======
    chars = list(word)
    shuffled = chars[:]
    
    if len(set(chars)) > 1:
        while shuffled == chars:
            random.shuffle(shuffled)

    composition = analyze_word_characters(word)

    explanation = EXPLANATIONS[idx] if EXPLANATIONS else None
    jp_word = JP_WORDS[idx] if JP_WORDS else None
    song_type = TYPE[idx] if TYPE else None
    band = BAND[idx] if BAND else None

    games[channel_id] = {
        "type": "anagram",
        "word": word,
        "raw_word": raw_word,
        "shuffled": shuffled,
        "tries": num,
        "revealed": 0,
        "explanation": explanation,
        "jp_word": jp_word,
        "song_type": song_type,
        "band": band
    }

    msg = (
        f"🔀 **アナグラム開始！**\n"
        f"並び替えられた文字:\n"
        f"`{' '.join(shuffled)}`\n"
        f"文字数: {len(word)}\n"
        f"文字構成: {composition}\n"
        f"出題ジャンル: {name}\n"
    )

    if song_type and band:
        msg += f"楽曲タイプ: {song_type}\n演奏バンド: {band}\n"

    msg += (
        f"残り挑戦回数: {num}\n"
        f"`!ana(!a) 単語` で回答してください！"
    )

    await ctx.send(msg)

def make_hint(word, revealed):
    hint = []
    for i, c in enumerate(word):
        if i < revealed:
            hint.append(c)
        else:
            hint.append("＿")
    return " ".join(hint)


@bot.command(aliases=["a"])
async def ana(ctx, *, guess: str):
    channel_id = ctx.channel.id

    if channel_id not in games:
        return

    game = games[channel_id]
    if game["type"] != "anagram":
        return

    # 正解判定
    if guess.strip().lower() == game["word"]:
        msg = f"🎉 **正解！**\n答えは **{game['raw_word']}** でした！"

        if game["explanation"]:
            msg += f"\n📖 {game['explanation']}"
        if game["jp_word"]:
            msg += f"\n🇯🇵 日本語名: {game['jp_word']}"

        await ctx.send(msg)
        del games[channel_id]
        return

    # 不正解処理
    game["tries"] -= 1
    game["revealed"] = min(
        game["revealed"] + 1,
        len(game["word"])
    )

    if game["tries"] <= 0:
        msg = f"💀 **失敗！**\n正解は **{game['raw_word']}** でした"

        if game["explanation"]:
            msg += f"\n📖 {game['explanation']}"
        if game["jp_word"]:
            msg += f"\n🇯🇵 日本語名: {game['jp_word']}"

        await ctx.send(msg)
        del games[channel_id]
        return

    hint = make_hint(game["word"], game["revealed"])
    shuffled = " ".join(game["shuffled"])

    await ctx.send(
        f"❌ 不正解！\n"
        f"ヒント：`{hint}`\n"
        f"並び替え：`{shuffled}`\n"
        f"残り {game['tries']} 回"
    )

from collections import Counter

def minus_count(A: str, B: str) -> str:
    cnt = Counter(B)
    result = []

    for c in A:
        if cnt[c] > 0:
            cnt[c] -= 1
        else:
            result.append(c)

    return "".join(result)


@bot.command()
async def minus(ctx, A: str, B: str):
    """
    文字列Aから、文字列Bに含まれる文字を回数分だけ削除する
    使用例: !minus aaabbb aab
    """
    result = minus_count(A, B)

    if result == "":
        await ctx.send("（すべて削除されました）")
    else:
        await ctx.send(f"結果: `{result}`")


@bot.command()
async def anafinish(ctx):
    if ctx.channel.id in games:
        game = games[ctx.channel.id]
        await ctx.send("🛑 アナグラムゲームを強制終了しました。")
        await ctx.send(f"正解は `{game["raw_word"]}` でした。")
        if game["explanation"]:
            await ctx.send(f"📘 **解説:** {game['explanation']}")
        if game["jp_word"]:
            await ctx.send(f"📘 **日本語名:** {game['jp_word']}")
        del games[ctx.channel.id]
    else:
        await ctx.send("現在、このチャンネルで進行中のゲームはありません。")



bot.run(TOKEN)
