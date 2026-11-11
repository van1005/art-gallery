import streamlit as st
import streamlit.components.v1 as components
import json
import base64
import os

# 1. 頁面全域設定：寬版全螢幕模式
st.set_page_config(
    page_title="跨時代全球藝術家作品與生命歷程互動圖譜",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 本地圖片優先轉 Base64 工具（直接讀取 GitHub 根目錄檔案，徹底避免跨域阻擋）
def file_to_base64(filepath, fallback_url):
    if os.path.exists(filepath):
        try:
            with open(filepath, "rb") as f:
                data = f.read()
                return f"data:image/jpeg;base64,{base64.b64encode(data).decode('utf-8')}"
        except Exception:
            pass
    return fallback_url

# 2. 結構化深度資料庫（直接對齊 GitHub 上的真實檔案）
ARTISTS_DATABASE = {
    "米開朗基羅": {
        "title": "米開朗基羅 (Michelangelo Buonarroti)",
        "period": "文藝復興全盛期 (1475–1564)",
        "category": "大理石雕塑 / 濕壁畫 / 建築設計",
        "identity": "文藝復興三傑 ｜ 西方雕塑史的不朽神聖巨匠",
        "color": "#C5854B", "frame": "#9C5B2B", "icon": "🗿",
        "quote": "「我看見天使在巨石裡，我雕刻直到使他重獲自由。」",
        "artworks": [
            {
                "name": "《大衛像》 (David, 1501–1504)",
                "file": "米開朗基羅_大衛.jpg",
                "desc": "文藝復興雕塑的巔峰代表作，高達5公尺，精準捕捉迎戰巨人歌利亞前蓄勢待發的堅定眼神與肌理張力。",
                "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Michelangelo%27s_David_-_right_view_2.jpg/640px-Michelangelo%27s_David_-_right_view_2.jpg"
            },
            {
                "name": "《聖殤》 (Pietà, 1498–1499)",
                "file": "米開朗基羅的《聖殤》_5450_裁剪清理版.jpg",
                "desc": "聖伯多祿大殿鎮館之寶，以極致優雅的大理石褶皺展現聖母哀悼耶穌基督的靜謐與悲憫。",
                "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Michelangelo%27s_Pieta_5450_cropncleaned.jpg/640px-Michelangelo%27s_Pieta_5450_cropncleaned.jpg"
            },
            {
                "name": "《創世紀：創造亞當》 (1508–1512)",
                "file": "Creación_de_Adán_(Miguel_Ángel).jpg",
                "desc": "西斯汀禮拜堂天頂壁畫核心，上帝與亞當即將觸碰的食指成為西方文明最具象徵性的構圖。",
                "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg/640px-Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg"
            }
        ],
        "extract": (
            "### 📌 雕刻家的靈魂與對石材的虔誠\n\n"
            "米開朗基羅出生於卡普雷塞，深受佛羅倫斯美第奇家族的人文主義薰陶。他畢生自視為「純粹的雕刻家」，認為雕刻的真諦不是塑造形體，而是將隱藏並禁錮在沉重冷硬大理石中的靈魂釋放出來。他對人體結構與肌肉張力的掌握達到神聖無比的高度。\n\n"
            "### 🗿 雄渾震撼的英雄人體美學\n\n"
            "米開朗基羅的作品充滿了強大的男性力量美感與緊繃的內在張力（Terribilità）。在教皇朱利奧二世的委託下，他歷時四年仰頭在西斯汀禮拜堂天頂獨力創作出宏偉的《創世紀》濕壁畫，將神性創生與人類痛苦抗爭的龐大場面展現得淋漓盡致；其晚年設計的聖伯多祿大殿圓頂更奠定歐洲巴洛克與古典建築的典範。\n\n"
            "### 🏛️ 西方雕塑的極致象徵\n\n"
            "他將人體的解剖力學與靈魂深處的悲劇命運完美結合，被同時代人尊稱為「神聖的米開朗基羅（Il Divino）」，對西方美術史產生了無可撼動的深遠影響。"
        ),
        "representative": (
            "* **《大衛像》 (David, 1501–1504)**：文藝復興雕塑的絕對代表作，捕捉少年英雄堅定無畏的眼神。\n\n"
            "* **《聖殤》 (Pietà, 1498–1499)**：大理石雕塑的至高典範，展現超越世俗痛苦的神聖寧靜。\n\n"
            "* **《創世紀：創造亞當》 (1508–1512)**：神人指尖相碰瞬間傳遞生命的永恆經典。\n\n"
            "* **《最後的審判》 (1536–1541)**：西斯汀祭壇後壁宏偉畫作，展現翻騰壯烈的救贖與審判。"
        ),
        "link": "https://zh.wikipedia.org/wiki/米开朗基罗"
    },
    "梵谷": {
        "title": "文森·梵谷 (Vincent van Gogh)",
        "period": "後印象派 (1853–1890)",
        "category": "油畫 / 後印象派表現主義",
        "identity": "現代表現主義先驅 ｜ 燃燒靈魂的悲劇巨匠",
        "color": "#C5854B", "frame": "#9C5B2B", "icon": "🌌",
        "quote": "「我夢想著繪畫，然後我畫下了我的夢想。」",
        "artworks": [
            {
                "name": "《星夜》 (The Starry Night, 1889)",
                "file": "vangogh.jpg",
                "desc": "紐約現代藝術博物館藏，以旋渦天體、柏樹與靜謐小鎮展現深層的精神掙扎與超凡想像。",
                "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/640px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
            }
        ],
        "extract": (
            "### 📌 坎坷生平與創作狂熱\n\n"
            "梵谷出生於荷蘭南部，早年曾任藝術品店員、教師與傳教士，直到接近三十歲才正式投身繪畫。他一生飽受精神疾病、貧困與不被理解的孤獨折磨，但在其生命的最後十年間，以驚人的創作狂熱完成兩千餘幅作品。\n\n"
            "### 🎨 厚塗旋渦與情感表現\n\n"
            "梵谷完全顛覆了傳統寫實色彩的用法，大膽採用鮮烈的高彩度原色與厚塗技法（Impasto），將內心劇烈起伏的情感直接傾注於畫布之上，開啟了20世紀現代表現主義的大門。"
        ),
        "representative": (
            "* **《星夜》 (1889)**：超凡旋渦星雲與生命探索。\n\n"
            "* **《向日葵》系列 (1888–1889)**：金黃色調歌頌陽光與生命力。\n\n"
            "* **《麥田群鴉》 (1890)**：深邃動盪的天空與告別象徵。"
        ),
        "link": "https://zh.wikipedia.org/wiki/文森特·梵高"
    },
    "達文西": {
        "title": "李奧納多·達文西 (Leonardo da Vinci)",
        "period": "文藝復興全盛期 (1452–1519)",
        "category": "油畫 / 跨學科手稿 / 解剖研究",
        "identity": "文藝復興三傑 ｜ 人類史上最偉大的全才博學大師",
        "color": "#C5854B", "frame": "#9C5B2B", "icon": "🖼️",
        "quote": "「簡約是細膩的極致。觀察是唯一的智慧泉源。」",
        "artworks": [
            {
                "name": "《蒙娜麗莎》 (Mona Lisa, 約1503–1519)",
                "file": "davinci.jpg",
                "desc": "羅浮宮鎮館之寶，以劃時代的暈塗法與神秘微笑聞名全球。",
                "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/640px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg"
            }
        ],
        "extract": (
            "### 📌 托斯卡尼的私生子與全方位的求知狂熱\n\n"
            "達文西跨越解剖學、工程學、流體力學、光學與建築，被譽為人類史上最博學全才。\n\n"
            "### 🎨 革命性技法：暈塗法與空氣透視\n\n"
            "發明微透明層次暈塗消除硬邊輪廓，以漸層模糊描摹遠方山巒，創造震撼的立體深度。"
        ),
        "representative": (
            "* **《蒙娜麗莎》 (約1503–1519)**：暈塗法的巔峰之作。\n\n"
            "* **《最後的晚餐》 (1495–1498)**：嚴格單點透視與瞬間戲劇張力。\n\n"
            "* **《維特魯威人》 (約1490)**：人體黃金比例的經典圖標。"
        ),
        "link": "https://zh.wikipedia.org/wiki/列奥纳多·达·芬奇"
    },
    "莫內": {
        "title": "克勞德·莫內 (Claude Monet)",
        "period": "印象派奠基人 (1840–1926)",
        "category": "油畫 / 外光派印象主義",
        "identity": "印象派之父 ｜ 追逐光影與剎那時間的色彩魔法師",
        "color": "#C5854B", "frame": "#9C5B2B", "icon": "🌸",
        "quote": "「世上沒有固定不變的色彩，只有特定瞬間的光線折射。」",
        "artworks": [
            {
                "name": "《睡蓮》 (Water Lilies)",
                "file": "monet.jpg",
                "desc": "長達三十餘年對吉維尼池塘的極致凝視，消解地平線與空間輪廓的印象派巨作。",
                "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Claude_Monet_-_Water_Lilies_-_Google_Art_Project.jpg/640px-Claude_Monet_-_Water_Lilies_-_Google_Art_Project.jpg"
            }
        ],
        "extract": (
            "### 📌 外光寫生革命與印象派誕生\n\n"
            "走入自然進行外光寫生，以《印象·日出》震撼歐洲畫壇，正式奠定印象派。\n\n"
            "### 🌸 晚年吉維尼花園與抽象先聲\n\n"
            "晚年憑藉色彩直覺創作超大尺幅《睡蓮》，直接啟蒙了後世的抽象表現主義。"
        ),
        "representative": (
            "* **《印象·日出》 (1872)**：印象派定名之作。\n\n"
            "* **《睡蓮》系列 (1897–1926)**：池塘光影熔鑄的極致凝視。"
        ),
        "link": "https://zh.wikipedia.org/wiki/克洛德·莫奈"
    },
    "畢卡索": {
        "title": "巴勃羅·畢卡索 (Pablo Picasso)",
        "period": "現代立體派 (1881–1973)",
        "category": "油畫 / 拼貼 / 雕塑 / 現代主義",
        "identity": "立體主義創始人 ｜ 20世紀現代藝術最多產的天才巨擘",
        "color": "#C5854B", "frame": "#9C5B2B", "icon": "🧩",
        "quote": "「每個孩子都是藝術家，問題在於長大後如何保持。」",
        "artworks": [
            {
                "name": "《格爾尼卡》 (Guernica, 1937)",
                "file": "picasso.jpg",
                "desc": "黑白灰純色調鋪陳的史詩級反戰名作，描繪西班牙內戰平民慘遭轟炸的巨大悲鳴。",
                "fallback": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Guernica_reproduction_at_the_UN.jpg/640px-Guernica_reproduction_at_the_UN.jpg"
            }
        ],
        "extract": (
            "### 📌 神童早慧與風格變奏\n\n"
            "徹底打破自文藝復興以來的單點透視，將物體解構、旋轉並置在同一畫布上。\n\n"
            "### 🕊️ 人文關懷與永恆傳奇\n\n"
            "以強烈的反戰精神創作《格爾尼卡》，展現藝術家作為時代良心的力量。"
        ),
        "representative": (
            "* **《格爾尼卡》 (1937)**：反戰立體主義史詩。\n\n"
            "* **《亞維農的少女》 (1907)**：立體主義開山之作。"
        ),
        "link": "https://zh.wikipedia.org/wiki/巴勃罗·毕加索"
    }
}

# 3. 狀態管理
if "current_artist" not in st.session_state:
    st.session_state.current_artist = ""

def select_artist(name):
    st.session_state.current_artist = name

def reset_to_lobby():
    st.session_state.current_artist = ""

# 4. 側邊欄
with st.sidebar:
    st.title("🏛️ 策展導覽台")
    st.caption("數位像素美術館 ｜ 古典漫遊系統")
    st.divider()
    
    if st.session_state.current_artist:
        st.success(f"🎟️ 目前參觀：**{st.session_state.current_artist}** 專屬展廳")
        if st.button("🚪 離開展廳，返回接待大廳", use_container_width=True):
            reset_to_lobby()
            st.rerun()
    else:
        st.info("🛋️ 狀態：**接待大廳等待中**\n\n請在上方搜尋或點選標籤領取門票！")

    st.divider()
    st.subheader("🎮 展廳互動指南")
    st.markdown("""
    * **未搜尋**：漫步於古典接待大廳。
    * **搜尋人名後**：只開放**該名家的專屬古典展廳拱門**！
    * **操作鍵位**：`↑` `↓` `←` `→` 或 `W / A / S / D` 移動；按 `空白鍵` 查看真實代表作真跡！
    """)

# 5. 主標題樣式（沉穩深藍漸層）
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@600;900&display=swap');

    .custom-main-title {
        font-family: 'Noto Serif TC', 'PingFang TC', 'Microsoft JhengHei', serif;
        font-size: 2.7rem;
        font-weight: 900;
        letter-spacing: 2px;
        line-height: 1.25;
        margin-bottom: 0.3rem;
        background: linear-gradient(135deg, #7DD3FC 0%, #0284C7 35%, #0369A1 70%, #0C4A6E 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 4px 18px rgba(3, 105, 161, 0.45);
    }
    .custom-subtitle {
        font-family: 'Noto Serif TC', 'PingFang TC', 'Microsoft JhengHei', serif;
        font-size: 1.1rem;
        color: #94A3B8;
        letter-spacing: 1.5px;
        margin-bottom: 1.2rem;
    }
    .blue-accent { color: #38BDF8; font-weight: bold; }

    .stTabs [data-baseweb="tab-panel"] p,
    .stTabs [data-baseweb="tab-panel"] li,
    .stTabs [data-baseweb="tab-panel"] a {
        font-size: 1.35rem !important;
        line-height: 1.95 !important;
        color: #E2E8F0 !important;
    }
    div[data-testid="stAlert"] p {
        font-size: 1.25rem !important;
        line-height: 1.7 !important;
    }
    .stTabs [data-baseweb="tab-panel"] h3 {
        font-size: 1.6rem !important;
        color: #38BDF8 !important;
        margin-top: 1.4rem !important;
        margin-bottom: 0.7rem !important;
    }
</style>

<div class="custom-main-title">跨時代全球藝術家作品與生命歷程互動圖譜</div>
<div class="custom-subtitle">痕跡與靈魂 <span class="blue-accent">｜</span> 結合像素古典漫遊與多維生命脈絡之開放藝術平台</div>
""", unsafe_allow_html=True)

# 6. 搜尋與標籤區
col_search, col_tags = st.columns([2, 3])

with col_search:
    user_input = st.text_input(
        "🔍 搜尋藝術家（輸入後即刻開放專屬拱門）：",
        value=st.session_state.current_artist,
        placeholder="請輸入藝術家姓名（例如：米開朗基羅、達文西、梵谷...）"
    )
    if user_input != st.session_state.current_artist:
        st.session_state.current_artist = user_input
        st.rerun()

with col_tags:
    st.write("✨ **點選名家直接開啟專屬展廳：**")
    tag_cols = st.columns(len(ARTISTS_DATABASE))
    for i, name in enumerate(ARTISTS_DATABASE.keys()):
        if tag_cols[i].button(name, key=f"tag_btn_{name}", use_container_width=True):
            select_artist(name)
            st.rerun()

st.markdown("---")

current_query = st.session_state.current_artist.strip()
is_in_gallery = (current_query != "")

target_artist_data = None
for name, d in ARTISTS_DATABASE.items():
    if current_query and (current_query.lower() in name.lower() or current_query.lower() in d["title"].lower()):
        target_artist_data = d.copy()
        target_artist_data["matched_name"] = name
        break

# 本地圖片優先轉 Base64 處理
if target_artist_data:
    processed_artworks = []
    for art in target_artist_data.get("artworks", []):
        art_copy = art.copy()
        art_copy["b64"] = file_to_base64(art.get("file", ""), art.get("fallback", ""))
        processed_artworks.append(art_copy)
    target_artist_data["artworks"] = processed_artworks

exhibit_json = json.dumps(target_artist_data, ensure_ascii=False) if target_artist_data else "{}"
mode_str = "gallery" if is_in_gallery else "lobby"

col_game, col_info = st.columns([3, 2], gap="large")

with col_game:
    if is_in_gallery:
        st.subheader(f"🏛️ 【{target_artist_data['matched_name']}】專屬古典展廳大門")
        st.caption("操縱紳士漫步至正前方古典拱門，按【空白鍵 (Space)】鑑賞真實館藏代表作！")
    else:
        st.subheader("🛋️ 古典接待大廳 (Grand Entrance Lobby)")
        st.caption("紳士漫步於古典大廳中；請於上方搜尋或點選名家標籤以開啟專屬展廊！")

    # 採用圖二色票二號：#43475D, #677C93, #C19066, #C5854B, #9C5B2B 渲染
    pixel_game_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <meta name="referrer" content="no-referrer">
    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: #242735;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Noto Serif TC', serif;
            overflow: hidden;
            user-select: none;
        }}
        #game-box {{
            position: relative;
            width: 660px;
            height: 520px;
            box-shadow: 0 14px 45px rgba(0, 0, 0, 0.95), 0 0 25px rgba(197, 133, 75, 0.35);
            border: 3px solid #9C5B2B;
            border-radius: 10px;
            overflow: hidden;
            background: #43475D;
        }}
        canvas {{
            display: block;
            image-rendering: pixelated;
        }}
        #guide-bar {{
            position: absolute;
            top: 12px;
            left: 12px;
            background: rgba(67, 71, 93, 0.96);
            color: #F8ECE1;
            padding: 6px 14px;
            border-radius: 6px;
            font-size: 12px;
            border: 1px solid #C19066;
            pointer-events: none;
            letter-spacing: 0.5px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.6);
        }}
        #interact-prompt {{
            position: absolute;
            display: none;
            color: #FFFFFF;
            background: rgba(156, 91, 43, 0.96);
            border: 1.5px solid #C5854B;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            pointer-events: none;
            transform: translate(-50%, -100%);
            white-space: nowrap;
            box-shadow: 0 4px 15px rgba(0,0,0,0.8);
            animation: bounce 0.8s infinite alternate;
        }}
        @keyframes bounce {{
            from {{ margin-top: 0px; }}
            to {{ margin-top: -6px; }}
        }}
        /* 彈跳視窗：典雅濕壁畫色系卡片 */
        #rpg-modal {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 560px;
            background: linear-gradient(145deg, #43475D 0%, #2D3040 100%);
            border: 2px solid #C5854B;
            box-shadow: 0 20px 50px rgba(0,0,0,0.98), 0 0 25px rgba(197, 133, 75, 0.45);
            border-radius: 12px;
            padding: 16px 20px;
            display: none;
            z-index: 100;
            color: #FFFDF9;
        }}
        .modal-body {{
            display: flex;
            gap: 16px;
            align-items: center;
        }}
        .modal-img-box {{
            flex: 0 0 210px;
            height: 250px;
            border-radius: 8px;
            overflow: hidden;
            border: 2px solid #9C5B2B;
            background: #1C1E26;
            box-shadow: 0 4px 15px rgba(0,0,0,0.7);
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .modal-img-box img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
            display: block;
        }}
        .modal-info {{
            flex: 1;
        }}
        .modal-info h3 {{
            margin: 0 0 4px 0;
            color: #C5854B;
            font-size: 18px;
        }}
        .period-tag {{
            display: inline-block;
            background: #9C5B2B;
            color: #FFF2E6;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 11px;
            margin-bottom: 8px;
            border: 1px solid #C5854B;
        }}
        .quote {{
            font-style: italic;
            color: #E2E8F0;
            font-size: 12.5px;
            line-height: 1.45;
            background: rgba(0, 0, 0, 0.45);
            border-left: 3.5px solid #C5854B;
            padding: 6px 10px;
            margin: 6px 0 8px 0;
            border-radius: 0 4px 4px 0;
        }}
        .nav-dots {{
            display: flex;
            gap: 6px;
            margin-top: 8px;
        }}
        .nav-btn {{
            background: #677C93;
            color: #FFFDF9;
            border: 1px solid #C19066;
            padding: 4px 8px;
            font-size: 11px;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .nav-btn:hover {{
            background: #C5854B;
            color: #FFFFFF;
        }}
        .close-hint {{
            margin-top: 10px;
            text-align: right;
            font-size: 11px;
            color: #CBD5E1;
        }}
    </style>
    </head>
    <body>

    <div id="game-box">
        <canvas id="gameCanvas" width="660" height="520"></canvas>
        <div id="guide-bar">🚶 [WASD / 方向鍵] 移動紳士</div>
        <div id="interact-prompt">❗ [空白鍵] 鑑賞代表作真跡</div>

        <div id="rpg-modal">
            <div class="modal-body">
                <div class="modal-img-box">
                    <img id="modal-img" src="" alt="真實作品真跡大圖">
                </div>
                <div class="modal-info">
                    <h3 id="modal-title">🎨 作品名稱</h3>
                    <span class="period-tag" id="modal-period">時代時期</span>
                    <div class="quote" id="modal-quote">經典名言</div>
                    <div id="modal-desc" style="font-size:12px; color:#E2E8F0; line-height:1.45;">作品解析</div>
                    <div class="nav-dots" id="modal-nav"></div>
                </div>
            </div>
            <div class="close-hint">按 [Space] 或 任意方向鍵 關閉視窗</div>
        </div>
    </div>

    <script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const prompt = document.getElementById('interact-prompt');
    const modal = document.getElementById('rpg-modal');
    const guide = document.getElementById('guide-bar');

    const mode = "{mode_str}";
    const currentArtist = {exhibit_json};

    const player = {{
        x: 330,
        y: mode === "gallery" ? 440 : 380,
        speed: 3.6,
        dir: 'up',
        walkFrame: 0
    }};

    if (mode === "gallery") {{
        guide.innerHTML = `🚶 [WASD / 方向鍵] 紳士漫步 ｜ 前方為【${{currentArtist.matched_name}}】古典拱門`;
    }} else {{
        guide.innerHTML = `🛋️ 古典接待大廳 ｜ 請於上方搜尋或點選名家領取門票`;
    }}

    const singleDoor = {{
        x: 290,
        y: 45,
        w: 80,
        h: 95
    }};

    const keys = {{}};
    let isNearDoor = false;
    let isModalOpen = false;
    let currentArtIndex = 0;

    window.addEventListener('keydown', (e) => {{
        if(["ArrowUp","ArrowDown","ArrowLeft","ArrowRight"," "].includes(e.key)) {{
            e.preventDefault();
        }}
        keys[e.key.toLowerCase()] = true;

        if ((e.key === " " || e.key === "Enter") && mode === "gallery") {{
            if (isNearDoor) {{
                toggleModal();
            }}
        }}
    }});

    window.addEventListener('keyup', (e) => {{
        keys[e.key.toLowerCase()] = false;
    }});

    function switchArtwork(idx) {{
        currentArtIndex = idx;
        const art = currentArtist.artworks[idx];
        document.getElementById('modal-img').src = art.b64;
        document.getElementById('modal-title').innerHTML = `${{currentArtist.icon}} ${{art.name}}`;
        document.getElementById('modal-desc').innerText = art.desc;
    }}

    function toggleModal() {{
        if (isModalOpen) {{
            modal.style.display = 'none';
            isModalOpen = false;
        }} else {{
            currentArtIndex = 0;
            const artworks = currentArtist.artworks || [];
            if (artworks.length > 0) {{
                const first = artworks[0];
                document.getElementById('modal-img').src = first.b64;
                document.getElementById('modal-title').innerHTML = `${{currentArtist.icon}} ${{first.name}}`;
                document.getElementById('modal-desc').innerText = first.desc;
            }}
            document.getElementById('modal-period').innerText = `【${{currentArtist.matched_name}}】${{currentArtist.period}}`;
            document.getElementById('modal-quote').innerText = currentArtist.quote;

            const nav = document.getElementById('modal-nav');
            nav.innerHTML = '';
            if (artworks.length > 1) {{
                artworks.forEach((a, i) => {{
                    const btn = document.createElement('button');
                    btn.className = 'nav-btn';
                    btn.innerText = `作品 ${{i+1}}`;
                    btn.onclick = () => switchArtwork(i);
                    nav.appendChild(btn);
                }});
            }}

            modal.style.display = 'block';
            isModalOpen = true;
        }}
    }}

    function update() {{
        let moving = false;
        if (keys['arrowup'] || keys['w']) {{ player.y -= player.speed; player.dir = 'up'; moving = true; }}
        if (keys['arrowdown'] || keys['s']) {{ player.y += player.speed; player.dir = 'down'; moving = true; }}
        if (keys['arrowleft'] || keys['a']) {{ player.x -= player.speed; player.dir = 'left'; moving = true; }}
        if (keys['arrowright'] || keys['d']) {{ player.x += player.speed; player.dir = 'right'; moving = true; }}

        if (moving) {{
            player.walkFrame += 0.22;
            if (isModalOpen) {{
                modal.style.display = 'none';
                isModalOpen = false;
            }}
        }}

        player.x = Math.max(30, Math.min(canvas.width - 30, player.x));
        player.y = Math.max(mode === "gallery" ? 145 : 180, Math.min(canvas.height - 35, player.y));

        if (mode === "gallery") {{
            let dist = Math.hypot(player.x - (singleDoor.x + singleDoor.w / 2), player.y - (singleDoor.y + singleDoor.h));
            isNearDoor = (dist < 60);

            if (isNearDoor && !isModalOpen) {{
                prompt.style.display = 'block';
                prompt.style.left = player.x + 'px';
                prompt.style.top = (player.y - 25) + 'px';
            }} else {{
                prompt.style.display = 'none';
            }}
        }}
    }}

    // 繪製古典接待大廳（應用圖二色票二號）
    function drawLobby() {{
        // 牆面：沉穩石板藍灰 #43475D
        ctx.fillStyle = '#43475D';
        ctx.fillRect(0, 0, canvas.width, 160);

        // 天花板與線條：霧藍灰 #677C93 與 陶土金棕 #C19066
        ctx.fillStyle = '#677C93';
        ctx.fillRect(0, 0, canvas.width, 16);
        ctx.fillStyle = '#C19066';
        ctx.fillRect(0, 16, canvas.width, 3);
        ctx.fillStyle = '#9C5B2B';
        ctx.fillRect(0, 156, canvas.width, 4);

        // 地磚：陶土金棕與深赭木交錯質感
        const tileSize = 44;
        for (let x = 0; x < canvas.width; x += tileSize) {{
            for (let y = 160; y < canvas.height; y += tileSize) {{
                ctx.fillStyle = ((x / tileSize + y / tileSize) % 2 === 0) ? '#C19066' : '#A9754C';
                ctx.fillRect(x, y, tileSize, tileSize);
            }}
        }}

        // 大廳中央諮詢處：深赭木 #9C5B2B 搭配 琥珀焦糖 #C5854B
        ctx.fillStyle = '#9C5B2B';
        ctx.fillRect(230, 80, 200, 48);
        ctx.fillStyle = '#C5854B';
        ctx.fillRect(226, 76, 208, 8);
        ctx.fillStyle = '#FFFDF9';
        ctx.font = 'bold 13px serif';
        ctx.textAlign = 'center';
        ctx.fillText('🏛️ 美術館接待諮詢處', 330, 108);

        // 典雅盆栽
        ctx.fillStyle = '#677C93';
        ctx.beginPath();
        ctx.arc(80, 130, 24, 0, Math.PI * 2);
        ctx.arc(580, 130, 24, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#9C5B2B';
        ctx.fillRect(70, 130, 20, 25);
        ctx.fillRect(570, 130, 20, 25);

        // 長沙發：石板藍 #43475D 搭配 琥珀焦糖飾邊
        ctx.fillStyle = '#43475D';
        ctx.fillRect(80, 260, 40, 90);
        ctx.fillRect(540, 260, 40, 90);
        ctx.fillStyle = '#C5854B';
        ctx.fillRect(76, 260, 4, 90);
        ctx.fillRect(580, 260, 4, 90);

        // 中央古典導引道
        ctx.fillStyle = 'rgba(197, 133, 75, 0.22)';
        ctx.fillRect(280, 160, 100, canvas.height - 160);

        ctx.fillStyle = '#F8ECE1';
        ctx.font = 'bold 15px serif';
        ctx.textAlign = 'center';
        ctx.fillText('✨ 請於上方搜尋藝術家，或點選名家標籤開啟專屬拱門 ✨', 330, 220);
        ctx.fillStyle = '#E2E8F0';
        ctx.font = '12px serif';
        ctx.fillText('（紳士目前在大廳休憩，領取門票後將步入專屬展廳）', 330, 245);
    }}

    // 繪製古典展覽長廊（應用圖二色票二號）
    function drawGallery() {{
        // 牆面：石板藍灰 #43475D
        ctx.fillStyle = '#43475D';
        ctx.fillRect(0, 0, canvas.width, 130);

        ctx.fillStyle = '#677C93';
        ctx.fillRect(0, 0, canvas.width, 14);
        ctx.fillStyle = '#C19066';
        ctx.fillRect(0, 14, canvas.width, 2.5);
        ctx.fillStyle = '#9C5B2B';
        ctx.fillRect(0, 126, canvas.width, 6);

        // 地面拼木地磚
        const tileSize = 40;
        for (let x = 0; x < canvas.width; x += tileSize) {{
            for (let y = 132; y < canvas.height; y += tileSize) {{
                ctx.fillStyle = ((x / tileSize + y / tileSize) % 2 === 0) ? '#C19066' : '#A9754C';
                ctx.fillRect(x, y, tileSize, tileSize);
            }}
        }}

        // 迎賓長地毯：琥珀焦糖金 #C5854B
        const carpetW = 120;
        const carpetX = (canvas.width - carpetW) / 2;
        ctx.fillStyle = '#C5854B';
        ctx.fillRect(carpetX, 132, carpetW, canvas.height - 132);

        // 兩側深赭木飾邊 #9C5B2B
        ctx.fillStyle = '#9C5B2B';
        ctx.fillRect(carpetX - 3, 132, 3, canvas.height - 132);
        ctx.fillRect(carpetX + carpetW, 132, 3, canvas.height - 132);

        // 暖光光暈
        ctx.fillStyle = 'rgba(248, 236, 225, 0.28)';
        ctx.beginPath();
        ctx.arc(330, 85, 80, 0, Math.PI * 2);
        ctx.fill();

        // 拱門外框：深赭木 #9C5B2B 搭配 琥珀焦糖邊線
        ctx.fillStyle = '#9C5B2B';
        ctx.fillRect(singleDoor.x, singleDoor.y, singleDoor.w, singleDoor.h);
        ctx.fillStyle = '#C5854B';
        ctx.fillRect(singleDoor.x - 4, singleDoor.y - 4, singleDoor.w + 8, 8);

        // 門內景深：石板藍色塊
        ctx.fillStyle = '#43475D';
        ctx.fillRect(singleDoor.x + 8, singleDoor.y + 12, singleDoor.w - 16, singleDoor.h - 12);

        ctx.font = '34px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(currentArtist.icon || '🎨', 330, singleDoor.y + 45);

        // 銘牌
        ctx.fillStyle = '#9C5B2B';
        ctx.fillRect(singleDoor.x - 14, singleDoor.y + singleDoor.h + 8, singleDoor.w + 28, 26);
        ctx.strokeStyle = '#C5854B';
        ctx.lineWidth = 1.5;
        ctx.strokeRect(singleDoor.x - 14, singleDoor.y + singleDoor.h + 8, singleDoor.w + 28, 26);
        
        ctx.fillStyle = '#FFFDF9';
        ctx.font = 'bold 13px serif';
        ctx.fillText(`【${{currentArtist.matched_name}}】展廳門`, 330, singleDoor.y + singleDoor.h + 24);
    }}

    // 繪製身著古典禮服的像素紳士
    function drawPlayer() {{
        ctx.fillStyle = 'rgba(0, 0, 0, 0.45)';
        ctx.beginPath();
        ctx.ellipse(player.x, player.y + 10, 11, 5, 0, 0, Math.PI * 2);
        ctx.fill();

        const bob = Math.sin(player.walkFrame) * 2;

        // 紳士長褲與皮鞋
        ctx.fillStyle = '#2D3040';
        ctx.fillRect(player.x - 6, player.y + 3 + bob, 5, 9);
        ctx.fillRect(player.x + 1, player.y + 3 + bob, 5, 9);

        // 雙排扣深藍燕尾禮服大衣
        ctx.fillStyle = '#43475D';
        ctx.fillRect(player.x - 7, player.y - 6 + bob, 14, 11);

        // 襯衫與領結
        ctx.fillStyle = '#FFFDF9';
        ctx.fillRect(player.x - 2, player.y - 6 + bob, 4, 6);
        ctx.fillStyle = '#9C5B2B';
        ctx.fillRect(player.x - 2, player.y - 6 + bob, 4, 2);

        // 臉部膚色
        ctx.fillStyle = '#FED7AA';
        ctx.fillRect(player.x - 5, player.y - 15 + bob, 10, 9);

        // 古典高頂禮帽
        ctx.fillStyle = '#2D3040';
        ctx.fillRect(player.x - 9, player.y - 18 + bob, 18, 3);
        ctx.fillRect(player.x - 6, player.y - 27 + bob, 12, 10);
        ctx.fillStyle = '#C5854B'; // 焦糖金色緞帶
        ctx.fillRect(player.x - 6, player.y - 20 + bob, 12, 2.5);

        // 眼神
        ctx.fillStyle = '#1A120B';
        if (player.dir === 'down') {{
            ctx.fillRect(player.x - 3, player.y - 11 + bob, 2, 2.5);
            ctx.fillRect(player.x + 1, player.y - 11 + bob, 2, 2.5);
        }} else if (player.dir === 'left') {{
            ctx.fillRect(player.x - 4, player.y - 11 + bob, 2, 2.5);
        }} else if (player.dir === 'right') {{
            ctx.fillRect(player.x + 2, player.y - 11 + bob, 2, 2.5);
        }}
    }}

    function loop() {{
        update();
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        if (mode === "gallery") {{
            drawGallery();
        }} else {{
            drawLobby();
        }}
        drawPlayer();
        requestAnimationFrame(loop);
    }}

    loop();
    </script>
    </body>
    </html>
    """

    components.html(pixel_game_html, height=540)

# 7. 右側資訊欄
with col_info:
    if is_in_gallery and target_artist_data:
        st.subheader(f"🖼️ 【{target_artist_data['matched_name']}】代表作全覽")
        
        artworks = target_artist_data.get("artworks", [])
        if artworks:
            art_tabs = st.tabs([art["name"].split(' ')[0] for art in artworks])
            for i, tab in enumerate(art_tabs):
                with tab:
                    art = artworks[i]
                    st.markdown(
                        f"""
                        <div style="text-align: center; margin-bottom: 10px;">
                            <img src="{art['b64']}" style="max-width: 100%; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.6); border: 2px solid #9C5B2B;">
                            <div style="font-size: 13.5px; color: #FFFDF9; margin-top: 6px; font-weight: bold;">{art['name']}</div>
                            <div style="font-size: 12.5px; color: #C19066; margin-top: 3px;">{art['desc']}</div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        
        st.markdown(f"### {target_artist_data['title']}")
        st.info(f"🏷️ **身份地位：** {target_artist_data['identity']}")
        
        tab_bio, tab_detail = st.tabs(["📜 深度生命脈絡與轉折", "🎨 傳世代表作解析與媒材"])
        with tab_bio:
            st.markdown(target_artist_data["extract"])
            st.markdown(f"[🔗 前往維基百科閱讀權威典藏文獻]({target_artist_data['link']})")
        with tab_detail:
            st.markdown(target_artist_data["representative"])
            st.divider()
            st.markdown(f"""
            ⏳ **活躍年代：** {target_artist_data['period']}  
            🎨 **主要媒材：** {target_artist_data.get('category', '油畫 / 雕塑')}
            """)
    else:
        st.subheader("🏛️ 美術館迎賓服務處")
        st.markdown("""
        ### 歡迎光臨跨時代數位美術館！
        本館典藏文藝復興、印象派至現代主義之劃時代藝術大師與雕塑家。
        
        #### 🎫 參觀動線說明：
        1. **領取展覽門票**：請於上方 **「搜尋藝術家」** 輸入人名，或直接點選 **「熱門名家標籤」**。
        2. **啟程漫遊專屬展廳**：領取門票後，左側畫面將只為您開啟該藝術家的**唯一專屬展廊拱門**！
        3. **深度互動鑑賞**：操縱紳士走至展門正前方並按下 **【空白鍵 (Space)】**，即可欣賞代表作真跡照片並同步解鎖其生平脈絡。
        """)
        st.info("💡 試著點擊上方標籤「**米開朗基羅**」、「**達文西**」或「**梵谷**」，立即開啟獨立專屬展廳！")
