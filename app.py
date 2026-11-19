import streamlit as st
import streamlit.components.v1 as components
import json
import base64
from pathlib import Path

# 1. 頁面全域設定（必須是第一個 Streamlit 指令）
st.set_page_config(
    page_title="跨時代全球藝術家作品與生命歷程互動圖譜",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# 網站外觀模組（原 web_style.py，已合併進來）
# ============================================================
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;700;900&family=Noto+Sans+TC:wght@400;500;700&display=swap');

:root {
  --bg: #1B2630;
  --bg-2: #25333E;
  --panel: #2F3E4A;
  --blue: #547791;
  --sky: #B9D9F6;
  --cream: #E2E1B5;
  --gold: #B7B082;
  --rust: #AA5D4C;
}

/* ---------- 1. 拿掉 Streamlit 的「App 感」 ---------- */
#MainMenu, footer, header[data-testid="stHeader"],
[data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"], [data-testid="stSidebar"],
[data-testid="collapsedControl"], [data-testid="stSidebarCollapsedControl"] {
  display: none !important;
}

.stApp {
  background:
    radial-gradient(1200px 500px at 50% -10%, rgba(84,119,145,.35), transparent 70%),
    linear-gradient(180deg, var(--bg) 0%, #141C23 100%);
  font-family: 'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', sans-serif;
  color: var(--cream);
}
.block-container {
  max-width: 1240px !important;
  padding: 0 28px 40px 28px !important;
}
html { scroll-behavior: smooth; }

/* ---------- 2. 固定導覽列 ---------- */
.site-nav {
  position: sticky; top: 0; z-index: 999;
  display: flex; align-items: center; justify-content: space-between;
  margin: 0 -28px 0 -28px; padding: 14px 32px;
  background: rgba(20,28,35,.82);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(185,217,246,.18);
}
.site-nav .brand {
  font-family: 'Noto Serif TC', serif; font-weight: 900; font-size: 1.15rem;
  letter-spacing: 2px; color: var(--sky);
}
.site-nav .brand span { color: var(--rust); }
.site-nav .links a {
  color: var(--cream); text-decoration: none; margin-left: 26px;
  font-size: .95rem; letter-spacing: 1px; padding-bottom: 3px;
  border-bottom: 2px solid transparent; transition: all .2s;
}
.site-nav .links a:hover { color: var(--sky); border-bottom-color: var(--rust); }

/* ---------- 3. Hero 主視覺 ---------- */
.hero {
  margin: 0 -28px 34px -28px; padding: 84px 32px 70px 32px; text-align: center;
  background:
    linear-gradient(180deg, rgba(27,38,48,.35), var(--bg) 100%),
    radial-gradient(700px 300px at 20% 30%, rgba(170,93,76,.32), transparent 70%),
    radial-gradient(700px 320px at 80% 20%, rgba(84,119,145,.45), transparent 70%);
}
.hero.compact { padding: 38px 32px 30px 32px; margin-bottom: 22px; }
.hero .eyebrow {
  display: inline-block; font-size: .8rem; letter-spacing: 4px; color: var(--gold);
  border: 1px solid rgba(183,176,130,.5); padding: 5px 16px; border-radius: 30px;
  margin-bottom: 22px;
}
.hero h1 {
  font-family: 'Noto Serif TC', serif; font-weight: 900; letter-spacing: 3px;
  font-size: clamp(2rem, 4.6vw, 3.5rem); line-height: 1.25; margin: 0 0 16px 0;
  background: linear-gradient(135deg, #FFFFFF 0%, var(--sky) 45%, var(--blue) 100%);
  -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
}
.hero.compact h1 { font-size: clamp(1.5rem, 3vw, 2.2rem); }
.hero p { color: var(--gold); font-size: 1.1rem; letter-spacing: 1.5px; margin: 0; }
.hero .stats { display: flex; justify-content: center; gap: 46px; margin-top: 34px; }
.hero .stats div b { display: block; font-size: 1.8rem; color: var(--sky); font-family: 'Noto Serif TC', serif; }
.hero .stats div span { font-size: .85rem; color: var(--cream); opacity: .8; letter-spacing: 2px; }

/* ---------- 4. 區塊標題 ---------- */
.section-title {
  font-family: 'Noto Serif TC', serif; font-size: 1.5rem; font-weight: 700;
  color: var(--sky); letter-spacing: 2px; margin: 8px 0 4px 0;
  padding-left: 14px; border-left: 4px solid var(--rust);
}
.section-sub { color: var(--gold); font-size: .95rem; margin: 0 0 14px 18px; }
h2, h3 { font-family: 'Noto Serif TC', serif !important; color: var(--sky) !important; }

/* ---------- 5. 搜尋框、按鈕 → 網站風格 ---------- */
.stTextInput input {
  background: rgba(255,255,255,.06) !important; color: var(--cream) !important;
  border: 1px solid rgba(185,217,246,.35) !important; border-radius: 30px !important;
  padding: 12px 20px !important; font-size: 1rem !important;
}
.stTextInput input:focus { border-color: var(--sky) !important; box-shadow: 0 0 0 3px rgba(185,217,246,.18) !important; }
.stTextInput label p { color: var(--cream) !important; font-size: .95rem !important; }

.stButton > button {
  background: transparent; color: var(--cream);
  border: 1px solid rgba(185,217,246,.45); border-radius: 30px;
  padding: 8px 14px; font-weight: 500; letter-spacing: 1px; transition: all .25s;
}
.stButton > button:hover {
  background: var(--rust); border-color: var(--rust); color: #fff;
  transform: translateY(-2px); box-shadow: 0 8px 20px rgba(170,93,76,.4);
}
.stButton > button:focus:not(:active) { border-color: var(--sky); color: var(--sky); }

/* ---------- 6. 卡片化 ---------- */
.card {
  background: rgba(47,62,74,.55); border: 1px solid rgba(185,217,246,.14);
  border-radius: 16px; padding: 18px;
}
.artwork-card { text-align: center; margin-bottom: 14px; }
.artwork-card img {
  max-width: 100%; border-radius: 10px; border: 1px solid rgba(185,217,246,.3);
  box-shadow: 0 10px 30px rgba(0,0,0,.55); transition: transform .35s;
}
.artwork-card img:hover { transform: scale(1.025); }
.artwork-card .t { font-weight: 700; color: var(--cream); margin-top: 10px; }
.artwork-card .d { font-size: .9rem; color: var(--sky); margin-top: 4px; line-height: 1.6; }

/* ---------- 7. 分頁、提示框、內文 ---------- */
.stTabs [data-baseweb="tab-list"] { gap: 6px; border-bottom: 1px solid rgba(185,217,246,.2); }
.stTabs [data-baseweb="tab"] { color: var(--cream); border-radius: 10px 10px 0 0; padding: 8px 16px; }
.stTabs [aria-selected="true"] { color: var(--sky) !important; background: rgba(84,119,145,.25); }
.stTabs [data-baseweb="tab-highlight"] { background-color: var(--rust) !important; }
.stTabs [data-baseweb="tab-panel"] p, .stTabs [data-baseweb="tab-panel"] li {
  font-size: 1.12rem !important; line-height: 1.95 !important; color: var(--cream) !important;
}
.stTabs [data-baseweb="tab-panel"] h3 { font-size: 1.35rem !important; margin: 1.2rem 0 .6rem !important; }
.stTabs [data-baseweb="tab-panel"] a { color: var(--sky) !important; }
div[data-testid="stAlert"] {
  background: rgba(84,119,145,.22); border: 1px solid rgba(185,217,246,.25); border-radius: 12px;
}
div[data-testid="stAlert"] p { color: var(--cream) !important; font-size: 1.05rem !important; line-height: 1.7 !important; }
hr { border-color: rgba(185,217,246,.14) !important; }

/* 遊戲 iframe 圓角 */
iframe { border-radius: 14px; }

/* ---------- 8. 頁尾 ---------- */
.site-footer {
  margin: 50px -28px -40px -28px; padding: 34px 32px; text-align: center;
  background: #10171D; border-top: 1px solid rgba(185,217,246,.14);
  color: var(--gold); font-size: .88rem; letter-spacing: 1.5px; line-height: 2;
}
.site-footer b { color: var(--sky); font-family: 'Noto Serif TC', serif; }

/* ---------- 9. 手機版 ---------- */
@media (max-width: 760px) {
  .site-nav { padding: 12px 16px; }
  .site-nav .links { display: none; }
  .hero { padding: 54px 16px 44px 16px; }
  .hero .stats { gap: 22px; }
  .block-container { padding: 0 14px 30px 14px !important; }
}
"""


def inject_web_style():
    st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


def render_navbar():
    st.markdown(
        '<div class="site-nav">'
        '<div class="brand">ART<span>·</span>MUSEUM 數位美術館</div>'
        '<div class="links"><a href="#search">探索名家</a><a href="#gallery">展廳漫遊</a><a href="#about">關於本館</a></div>'
        '</div>',
        unsafe_allow_html=True,
    )


def render_hero(in_gallery: bool, artist_count: int, artwork_count: int):
    if in_gallery:
        st.markdown(
            '<div class="hero compact">'
            '<h1>跨時代全球藝術家作品與生命歷程互動圖譜</h1>'
            '<p>痕跡與靈魂 ｜ 像素古典漫遊 × 多維生命脈絡</p>'
            '</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            '<div class="hero">'
            '<div class="eyebrow">DIGITAL ART MUSEUM</div>'
            '<h1>跨時代全球藝術家作品<br>與生命歷程互動圖譜</h1>'
            '<p>痕跡與靈魂 ｜ 結合像素古典漫遊與多維生命脈絡之開放藝術平台</p>'
            f'<div class="stats"><div><b>{artist_count}</b><span>位名家</span></div>'
            f'<div><b>{artwork_count}</b><span>件代表作</span></div>'
            '<div><b>500+</b><span>年藝術史</span></div></div>'
            '</div>',
            unsafe_allow_html=True,
        )


def section_title(title: str, sub: str = "", anchor: str = ""):
    anchor_html = f'<a id="{anchor}"></a>' if anchor else ""
    sub_html = f'<div class="section-sub">{sub}</div>' if sub else ""
    st.markdown(f'{anchor_html}<div class="section-title">{title}</div>{sub_html}', unsafe_allow_html=True)


def render_footer():
    st.markdown(
        '<a id="about"></a><div class="site-footer">'
        '<b>ART·MUSEUM 數位美術館</b><br>'
        '操作說明：方向鍵 / WASD 移動，走到拱門前按空白鍵鑑賞真跡<br>'
        '資料來源：Wikipedia、Wikimedia Commons ｜ © 2026 跨時代藝術家互動圖譜'
        '</div>',
        unsafe_allow_html=True,
    )


# ============================================================
# 2. 優先讀取專案內的本地圖片並轉成 Base64，避開跨域阻擋
# ============================================================
ROOT_DIR = Path(__file__).resolve().parent

def resolve_artwork_image(keywords, fallback_url):
    try:
        for file in ROOT_DIR.iterdir():
            if file.is_file():
                filename_lower = file.name.lower()
                for kw in keywords:
                    if kw.lower() in filename_lower:
                        with open(file, "rb") as f:
                            data = f.read()
                            ext = file.suffix.lower().replace(".", "")
                            mime = "png" if ext == "png" else "jpeg"
                            return f"data:image/{mime};base64,{base64.b64encode(data).decode('utf-8')}"
    except Exception:
        pass
    return fallback_url

# 3. 藝術家資料庫
ARTISTS_DATABASE = {
    "莫內": {
        "title": "克勞德·莫內 (Claude Monet)",
        "period": "印象派奠基人 (1840–1926)",
        "category": "油畫 / 外光派印象主義",
        "identity": "印象派之父 ｜ 追逐光影與剎那時間的色彩魔法師",
        "color": "#AA5D4C", "frame": "#547791", "icon": "🌸",
        "quote": "「世上沒有固定不變的色彩，只有特定瞬間的光線折射。」",
        "artworks": [
            {
                "name": "《印象·日出》 (Impression, Sunrise, 1872)",
                "keywords": ["impressi", "日出", "sunrise"],
                "desc": "印象派定名之作。以勒阿弗爾港口的迷濛晨霧與橙紅旭日，徹底打破學院派精細勾勒的傳統，開啟現代視覺革命。",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Monet_-_Impression%2C_Sunrise.jpg/640px-Monet_-_Impression%2C_Sunrise.jpg"
            },
            {
                "name": "《阿讓特伊雪景》 (Snow at Argenteuil, 1875)",
                "keywords": ["argente", "snow", "雪景"],
                "desc": "外光派代表名作。莫內以敏銳的色彩直覺捕捉冬天積雪上的微藍冷光與夕陽暖調，呈現出空氣中流動的真實溫度。",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Monet_Snow_at_Argenteuil.jpg/640px-Monet_Snow_at_Argenteuil.jpg"
            }
        ],
        "extract": (
            "### 📌 外光寫生革命與印象派誕生\n\n"
            "莫內出生於巴黎，自幼展露過人素描天賦，後師從尤金·布丹走出畫室，進入戶外大自然從事「外光寫生（En plein air）」。1874年，莫內與雷諾瓦等人舉辦獨立展覽，展出其名作《印象·日出》，遭受保守藝評家嘲諷，這群革新者反而自豪地以「印象派」為名，正式掀起近代美術史最偉大的視覺革命。\n\n"
            "### 🎨 光影的瞬間性與連作系列\n\n"
            "莫內突破了傳統繪畫以物體固有色上色的慣例，改用短促碎裂的純色筆觸直接並列在畫布上，讓色彩在觀者眼中自然融合；晚年打造睡蓮水上花園，即使飽受眼疾之苦，依然憑藉純粹色彩直覺創作超大尺幅壁畫，直接啟蒙後世抽象表現主義。"
        ),
        "representative": (
            "* **《印象·日出》 (1872)**：印象派定名之作，捕捉晨霧與光影瞬間。\n\n"
            "* **《阿讓特伊雪景》 (1875)**：外光雪景經典，呈現藍紫光影與冷冽氛圍。\n\n"
            "* **《睡蓮》系列 (1897–1926)**：長達三十餘年對吉維尼池塘的極致凝視。"
        ),
        "link": "https://zh.wikipedia.org/wiki/克洛德·莫奈"
    },
    "米開朗基羅": {
        "title": "米開朗基羅 (Michelangelo Buonarroti)",
        "period": "文藝復興全盛期 (1475–1564)",
        "category": "大理石雕塑 / 濕壁畫 / 建築設計",
        "identity": "文藝復興三傑 ｜ 西方雕塑史的不朽神聖巨匠",
        "color": "#AA5D4C", "frame": "#547791", "icon": "🗿",
        "quote": "「我看見天使在巨石裡，我雕刻直到使他重獲自由。」",
        "artworks": [
            {
                "name": "《大衛像》 (David, 1501–1504)",
                "keywords": ["大衛", "david"],
                "desc": "文藝復興雕塑的巔峰代表作，高達5公尺，精準捕捉迎戰巨人歌利亞前蓄勢待發的堅定眼神與肌肉張力。",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Michelangelo%27s_David_-_right_view_2.jpg/640px-Michelangelo%27s_David_-_right_view_2.jpg"
            },
            {
                "name": "《聖殤》 (Pietà, 1498–1499)",
                "keywords": ["聖殤", "pieta", "5450"],
                "desc": "聖伯多祿大殿鎮館之寶，以極致優雅的大理石褶皺展現聖母哀悼耶穌基督的靜謐與悲憫。",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Michelangelo%27s_Pieta_5450_cropncleaned.jpg/640px-Michelangelo%27s_Pieta_5450_cropncleaned.jpg"
            },
            {
                "name": "《創世紀：創造亞當》 (1508–1512)",
                "keywords": ["亞當", "adan", "creacion", "adam"],
                "desc": "西斯汀禮拜堂天頂壁畫核心，上帝與亞當即將觸碰的食指成為西方文明最具象徵性的構圖。",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg/640px-Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg"
            }
        ],
        "extract": (
            "### 📌 雕刻家的靈魂與對石材的虔誠\n\n"
            "米開朗基羅出生於卡普雷塞，深受佛羅倫斯美第奇家族的人文主義薰陶。他畢生自視為「純粹的雕刻家」，認為雕刻的真諦不是塑造形體，而是將隱藏並禁錮在沉重冷硬大理石中的靈魂釋放出來。他對人體結構與肌肉張力的掌握達到神聖無比的高度。\n\n"
            "### 🗿 雄渾震撼的英雄人體美學\n\n"
            "米開朗基羅的作品充滿了強大的男性力量美感與緊繃的內在張力（Terribilità）。在教皇朱利奧二世的委託下，他歷時四年仰頭在西斯汀禮拜堂天頂獨力創作出宏偉的《創世紀》濕壁畫，將神性創生與人類痛苦抗爭的龐大場面展現得淋漓盡致；其晚年設計的聖伯多祿大殿圓頂更奠定歐洲巴洛克與古典建築的典範。"
        ),
        "representative": (
            "* **《大衛像》 (David, 1501–1504)**：文藝復興雕塑的絕對代表作，捕捉少年英雄堅定無畏的眼神。\n\n"
            "* **《聖殤》 (Pietà, 1498–1499)**：大理石雕塑的至高典範，展現超越世俗痛苦的神聖寧靜。\n\n"
            "* **《創世紀：創造亞當》 (1508–1512)**：神人指尖相碰瞬間傳遞生命的永恆經典。"
        ),
        "link": "https://zh.wikipedia.org/wiki/米开朗基罗"
    },
    "梵谷": {
        "title": "文森·梵谷 (Vincent van Gogh)",
        "period": "後印象派 (1853–1890)",
        "category": "油畫 / 後印象派表現主義",
        "identity": "現代表現主義先驅 ｜ 燃燒靈魂的悲劇巨匠",
        "color": "#AA5D4C", "frame": "#547791", "icon": "🌌",
        "quote": "「我夢想著繪畫，然後我畫下了我的夢想。」",
        "artworks": [
            {
                "name": "《星夜》 (The Starry Night, 1889)",
                "keywords": ["星夜", "vangogh", "gogh", "starry"],
                "desc": "紐約現代藝術博物館藏，以旋渦天體、柏樹與靜謐小鎮展現深層的精神掙扎與超凡想像。",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/640px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
            }
        ],
        "extract": (
            "### 📌 坎坷生平與創作狂熱\n\n"
            "梵谷一生飽受精神疾病與孤獨折磨，但在其生命的最後十年間，以驚人的創作狂熱完成兩千餘幅作品。\n\n"
            "### 🎨 厚塗旋渦與情感表現\n\n"
            "梵谷完全顛覆了傳統寫實色彩的用法，大膽採用鮮烈的高彩度原色與厚塗技法（Impasto），開啟了20世紀現代表現主義的大門。"
        ),
        "representative": (
            "* **《星夜》 (1889)**：超凡旋渦星雲與生命探索。\n\n"
            "* **《向日葵》系列 (1888–1889)**：金黃色調歌頌陽光與生命力。"
        ),
        "link": "https://zh.wikipedia.org/wiki/文森特·梵高"
    },
    "達文西": {
        "title": "李奧納多·達文西 (Leonardo da Vinci)",
        "period": "文藝復興全盛期 (1452–1519)",
        "category": "油畫 / 跨學科手稿 / 解剖研究",
        "identity": "文藝復興三傑 ｜ 人類史上最偉大的全才博學大師",
        "color": "#AA5D4C", "frame": "#547791", "icon": "🖼️",
        "quote": "「簡約是細膩的極致。觀察是唯一的智慧泉源。」",
        "artworks": [
            {
                "name": "《蒙娜麗莎》 (Mona Lisa, 約1503–1519)",
                "keywords": ["蒙娜麗莎", "davinci", "mona", "lisa"],
                "desc": "羅浮宮鎮館之寶，以劃時代的暈塗法與神秘微笑聞名全球。",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/640px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg"
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
            "* **《最後的晚餐》 (1495–1498)**：嚴格單點透視與瞬間戲劇張力。"
        ),
        "link": "https://zh.wikipedia.org/wiki/列奥纳多·达·芬奇"
    },
    "畢卡索": {
        "title": "巴勃羅·畢卡索 (Pablo Picasso)",
        "period": "現代立體派 (1881–1973)",
        "category": "油畫 / 拼貼 / 雕塑 / 現代主義",
        "identity": "立體主義創始人 ｜ 20世紀現代藝術最多產的天才巨擘",
        "color": "#AA5D4C", "frame": "#547791", "icon": "🧩",
        "quote": "「每個孩子都是藝術家，問題在於長大後如何保持。」",
        "artworks": [
            {
                "name": "《格爾尼卡》 (Guernica, 1937)",
                "keywords": ["格爾尼卡", "picasso", "guernica"],
                "desc": "黑白灰純色調鋪陳的史詩級反戰名作，描繪西班牙內戰平民慘遭轟炸的巨大悲鳴。",
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Guernica_reproduction_at_the_UN.jpg/640px-Guernica_reproduction_at_the_UN.jpg"
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

# 4. 狀態管理
if "current_artist" not in st.session_state:
    st.session_state.current_artist = ""

def select_artist(name):
    st.session_state.current_artist = name

def reset_to_lobby():
    st.session_state.current_artist = ""

# 5. 網站外觀：樣式、導覽列、主視覺
inject_web_style()
render_navbar()
render_hero(
    in_gallery=bool(st.session_state.current_artist.strip()),
    artist_count=len(ARTISTS_DATABASE),
    artwork_count=sum(len(d["artworks"]) for d in ARTISTS_DATABASE.values()),
)

# 6. 搜尋與標籤區
section_title("探索名家", "輸入姓名，或點選標籤直接進入專屬展廳", anchor="search")

col_search, col_tags = st.columns([2, 3])

with col_search:
    user_input = st.text_input(
        "🔍 搜尋藝術家：",
        value=st.session_state.current_artist,
        placeholder="請輸入藝術家姓名（例如：莫內、米開朗基羅、達文西、梵谷...）"
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
    if st.session_state.current_artist:
        if st.button("🚪 返回接待大廳", key="leave_btn"):
            reset_to_lobby()
            st.rerun()

st.markdown("---")

# 7. 比對藝術家
current_query = st.session_state.current_artist.strip()

target_artist_data = None
for name, d in ARTISTS_DATABASE.items():
    if current_query and (current_query.lower() in name.lower() or current_query.lower() in d["title"].lower()):
        target_artist_data = d.copy()
        target_artist_data["matched_name"] = name
        break

if target_artist_data:
    processed_artworks = []
    for art in target_artist_data.get("artworks", []):
        art_copy = art.copy()
        art_copy["final_src"] = resolve_artwork_image(art.get("keywords", []), art.get("url", ""))
        processed_artworks.append(art_copy)
    target_artist_data["artworks"] = processed_artworks

# 有輸入但查無此人時，留在大廳並提示
is_in_gallery = target_artist_data is not None
if current_query and not is_in_gallery:
    st.warning(f"館內暫無「{current_query}」的專屬展廳，請試試上方的名家標籤。")

exhibit_json = json.dumps(target_artist_data, ensure_ascii=False) if target_artist_data else "{}"
mode_str = "gallery" if is_in_gallery else "lobby"

# 8. 像素遊戲 HTML（用 .replace 代入變數，JS 大括號不必跳脫）
PIXEL_GAME_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="referrer" content="no-referrer">
<style>
    body { margin:0; padding:0; background-color:transparent; display:flex; justify-content:center;
           align-items:center; font-family:'Noto Serif TC', serif; overflow:hidden; user-select:none; }
    #game-box { position:relative; width:660px; height:520px; border:3px solid #547791; border-radius:10px;
                overflow:hidden; background:#547791;
                box-shadow:0 14px 45px rgba(0,0,0,.95), 0 0 25px rgba(170,93,76,.35); }
    canvas { display:block; image-rendering:pixelated; }
    #guide-bar { position:absolute; top:12px; left:12px; background:rgba(84,119,145,.96); color:#E2E1B5;
                 padding:6px 14px; border-radius:6px; font-size:12px; border:1px solid #B9D9F6;
                 pointer-events:none; letter-spacing:.5px; box-shadow:0 2px 8px rgba(0,0,0,.6); }
    #interact-prompt { position:absolute; display:none; color:#FFF; background:rgba(170,93,76,.96);
                       border:1.5px solid #B9D9F6; padding:5px 12px; border-radius:20px; font-size:12px;
                       font-weight:bold; pointer-events:none; transform:translate(-50%,-100%);
                       white-space:nowrap; box-shadow:0 4px 15px rgba(0,0,0,.8); animation:bounce .8s infinite alternate; }
    @keyframes bounce { from { margin-top:0px; } to { margin-top:-6px; } }
    #rpg-modal { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:560px;
                 background:linear-gradient(145deg,#547791 0%,#374E5F 100%); border:2px solid #B9D9F6;
                 box-shadow:0 20px 50px rgba(0,0,0,.98), 0 0 25px rgba(185,217,246,.4); border-radius:12px;
                 padding:16px 20px; display:none; z-index:100; color:#E2E1B5; }
    .modal-body { display:flex; gap:16px; align-items:center; }
    .modal-img-box { flex:0 0 210px; height:250px; border-radius:8px; overflow:hidden; border:2px solid #B7B082;
                     background:#25333E; box-shadow:0 4px 15px rgba(0,0,0,.7); display:flex;
                     align-items:center; justify-content:center; }
    .modal-img-box img { width:100%; height:100%; object-fit:contain; display:block; }
    .modal-info { flex:1; }
    .modal-info h3 { margin:0 0 4px 0; color:#B9D9F6; font-size:18px; }
    .period-tag { display:inline-block; background:#AA5D4C; color:#FFF; padding:2px 8px; border-radius:4px;
                  font-size:11px; margin-bottom:8px; border:1px solid #B7B082; }
    .quote { font-style:italic; color:#E2E1B5; font-size:12.5px; line-height:1.45; background:rgba(37,51,62,.6);
             border-left:3.5px solid #AA5D4C; padding:6px 10px; margin:6px 0 8px 0; border-radius:0 4px 4px 0; }
    .nav-dots { display:flex; gap:6px; margin-top:8px; }
    .nav-btn { background:#AA5D4C; color:#FFF; border:1px solid #B9D9F6; padding:4px 8px; font-size:11px;
               border-radius:4px; cursor:pointer; transition:all .2s; }
    .nav-btn:hover { background:#B9D9F6; color:#2F3E4A; }
    .close-hint { margin-top:10px; text-align:right; font-size:11px; color:#B7B082; }
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
                <img id="modal-img" src="" alt="真實作品真跡大圖" referrerpolicy="no-referrer">
            </div>
            <div class="modal-info">
                <h3 id="modal-title">🎨 作品名稱</h3>
                <span class="period-tag" id="modal-period">時代時期</span>
                <div class="quote" id="modal-quote">經典名言</div>
                <div id="modal-desc" style="font-size:12px; color:#B7B082; line-height:1.45;">作品解析</div>
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

const mode = "__MODE__";
const currentArtist = __ARTIST__;

const player = { x: 330, y: mode === "gallery" ? 440 : 380, speed: 3.6, dir: 'up', walkFrame: 0 };

if (mode === "gallery") {
    guide.innerHTML = `🚶 [WASD / 方向鍵] 紳士漫步 ｜ 前方為【${currentArtist.matched_name}】古典拱門`;
} else {
    guide.innerHTML = `🛋️ 古典接待大廳 ｜ 請於上方搜尋或點選名家領取門票`;
}

const singleDoor = { x: 290, y: 45, w: 80, h: 95 };

const keys = {};
let isNearDoor = false;
let isModalOpen = false;
let currentArtIndex = 0;

window.addEventListener('keydown', (e) => {
    if (["ArrowUp","ArrowDown","ArrowLeft","ArrowRight"," "].includes(e.key)) { e.preventDefault(); }
    keys[e.key.toLowerCase()] = true;
    if ((e.key === " " || e.key === "Enter") && mode === "gallery") {
        if (isNearDoor) { toggleModal(); }
    }
});
window.addEventListener('keyup', (e) => { keys[e.key.toLowerCase()] = false; });

function switchArtwork(idx) {
    currentArtIndex = idx;
    const art = currentArtist.artworks[idx];
    document.getElementById('modal-img').src = art.final_src;
    document.getElementById('modal-title').innerHTML = `${currentArtist.icon} ${art.name}`;
    document.getElementById('modal-desc').innerText = art.desc;
}

function toggleModal() {
    if (isModalOpen) {
        modal.style.display = 'none';
        isModalOpen = false;
    } else {
        currentArtIndex = 0;
        const artworks = currentArtist.artworks || [];
        if (artworks.length > 0) { switchArtwork(0); }
        document.getElementById('modal-period').innerText = `【${currentArtist.matched_name}】${currentArtist.period}`;
        document.getElementById('modal-quote').innerText = currentArtist.quote;

        const nav = document.getElementById('modal-nav');
        nav.innerHTML = '';
        if (artworks.length > 1) {
            artworks.forEach((a, i) => {
                const btn = document.createElement('button');
                btn.className = 'nav-btn';
                btn.innerText = `作品 ${i+1}`;
                btn.onclick = () => switchArtwork(i);
                nav.appendChild(btn);
            });
        }
        modal.style.display = 'block';
        isModalOpen = true;
    }
}

function update() {
    let moving = false;
    if (keys['arrowup'] || keys['w']) { player.y -= player.speed; player.dir = 'up'; moving = true; }
    if (keys['arrowdown'] || keys['s']) { player.y += player.speed; player.dir = 'down'; moving = true; }
    if (keys['arrowleft'] || keys['a']) { player.x -= player.speed; player.dir = 'left'; moving = true; }
    if (keys['arrowright'] || keys['d']) { player.x += player.speed; player.dir = 'right'; moving = true; }

    if (moving) {
        player.walkFrame += 0.22;
        if (isModalOpen) { modal.style.display = 'none'; isModalOpen = false; }
    }

    player.x = Math.max(30, Math.min(canvas.width - 30, player.x));
    player.y = Math.max(mode === "gallery" ? 145 : 180, Math.min(canvas.height - 35, player.y));

    if (mode === "gallery") {
        let dist = Math.hypot(player.x - (singleDoor.x + singleDoor.w / 2), player.y - (singleDoor.y + singleDoor.h));
        isNearDoor = (dist < 60);
        if (isNearDoor && !isModalOpen) {
            prompt.style.display = 'block';
            prompt.style.left = player.x + 'px';
            prompt.style.top = (player.y - 25) + 'px';
        } else {
            prompt.style.display = 'none';
        }
    }
}

function drawLobby() {
    ctx.fillStyle = '#547791'; ctx.fillRect(0, 0, canvas.width, 160);
    ctx.fillStyle = '#374E5F'; ctx.fillRect(0, 0, canvas.width, 16);
    ctx.fillStyle = '#B9D9F6'; ctx.fillRect(0, 16, canvas.width, 3);
    ctx.fillStyle = '#B7B082'; ctx.fillRect(0, 156, canvas.width, 4);

    const tileSize = 44;
    for (let x = 0; x < canvas.width; x += tileSize) {
        for (let y = 160; y < canvas.height; y += tileSize) {
            ctx.fillStyle = ((x / tileSize + y / tileSize) % 2 === 0) ? '#E2E1B5' : '#B7B082';
            ctx.fillRect(x, y, tileSize, tileSize);
        }
    }

    ctx.fillStyle = '#AA5D4C'; ctx.fillRect(230, 80, 200, 48);
    ctx.fillStyle = '#B9D9F6'; ctx.fillRect(226, 76, 208, 8);
    ctx.fillStyle = '#E2E1B5'; ctx.font = 'bold 13px serif'; ctx.textAlign = 'center';
    ctx.fillText('🏛️ 美術館接待諮詢處', 330, 108);

    ctx.fillStyle = '#374E5F';
    ctx.beginPath(); ctx.arc(80, 130, 24, 0, Math.PI * 2); ctx.arc(580, 130, 24, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#AA5D4C'; ctx.fillRect(70, 130, 20, 25); ctx.fillRect(570, 130, 20, 25);

    ctx.fillStyle = '#547791'; ctx.fillRect(80, 260, 40, 90); ctx.fillRect(540, 260, 40, 90);
    ctx.fillStyle = '#AA5D4C'; ctx.fillRect(76, 260, 4, 90); ctx.fillRect(580, 260, 4, 90);

    ctx.fillStyle = 'rgba(185, 217, 246, 0.35)'; ctx.fillRect(280, 160, 100, canvas.height - 160);

    ctx.fillStyle = '#2F3E4A'; ctx.font = 'bold 15px serif'; ctx.textAlign = 'center';
    ctx.fillText('✨ 請於上方搜尋藝術家，或點選名家標籤開啟專屬拱門 ✨', 330, 220);
    ctx.fillStyle = '#547791'; ctx.font = '12px serif';
    ctx.fillText('（紳士目前在大廳休憩，領取門票後將步入專屬展廳）', 330, 245);
}

function drawGallery() {
    ctx.fillStyle = '#547791'; ctx.fillRect(0, 0, canvas.width, 130);
    ctx.fillStyle = '#374E5F'; ctx.fillRect(0, 0, canvas.width, 14);
    ctx.fillStyle = '#B9D9F6'; ctx.fillRect(0, 14, canvas.width, 2.5);
    ctx.fillStyle = '#B7B082'; ctx.fillRect(0, 126, canvas.width, 6);

    const tileSize = 40;
    for (let x = 0; x < canvas.width; x += tileSize) {
        for (let y = 132; y < canvas.height; y += tileSize) {
            ctx.fillStyle = ((x / tileSize + y / tileSize) % 2 === 0) ? '#E2E1B5' : '#B7B082';
            ctx.fillRect(x, y, tileSize, tileSize);
        }
    }

    const carpetW = 120;
    const carpetX = (canvas.width - carpetW) / 2;
    ctx.fillStyle = '#AA5D4C'; ctx.fillRect(carpetX, 132, carpetW, canvas.height - 132);
    ctx.fillStyle = '#B9D9F6';
    ctx.fillRect(carpetX - 3, 132, 3, canvas.height - 132);
    ctx.fillRect(carpetX + carpetW, 132, 3, canvas.height - 132);

    ctx.fillStyle = 'rgba(185, 217, 246, 0.3)';
    ctx.beginPath(); ctx.arc(330, 85, 80, 0, Math.PI * 2); ctx.fill();

    ctx.fillStyle = '#374E5F'; ctx.fillRect(singleDoor.x, singleDoor.y, singleDoor.w, singleDoor.h);
    ctx.fillStyle = '#B9D9F6'; ctx.fillRect(singleDoor.x - 4, singleDoor.y - 4, singleDoor.w + 8, 8);
    ctx.fillStyle = '#AA5D4C'; ctx.fillRect(singleDoor.x + 8, singleDoor.y + 12, singleDoor.w - 16, singleDoor.h - 12);

    ctx.font = '34px Arial'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText(currentArtist.icon || '🎨', 330, singleDoor.y + 45);

    ctx.fillStyle = '#547791';
    ctx.fillRect(singleDoor.x - 14, singleDoor.y + singleDoor.h + 8, singleDoor.w + 28, 26);
    ctx.strokeStyle = '#B9D9F6'; ctx.lineWidth = 1.5;
    ctx.strokeRect(singleDoor.x - 14, singleDoor.y + singleDoor.h + 8, singleDoor.w + 28, 26);

    ctx.fillStyle = '#E2E1B5'; ctx.font = 'bold 13px serif';
    ctx.fillText(`【${currentArtist.matched_name}】展廳門`, 330, singleDoor.y + singleDoor.h + 24);
}

function drawPlayer() {
    ctx.fillStyle = 'rgba(0, 0, 0, 0.45)';
    ctx.beginPath(); ctx.ellipse(player.x, player.y + 10, 11, 5, 0, 0, Math.PI * 2); ctx.fill();

    const bob = Math.sin(player.walkFrame) * 2;

    ctx.fillStyle = '#25333E';
    ctx.fillRect(player.x - 6, player.y + 3 + bob, 5, 9);
    ctx.fillRect(player.x + 1, player.y + 3 + bob, 5, 9);

    ctx.fillStyle = '#547791'; ctx.fillRect(player.x - 7, player.y - 6 + bob, 14, 11);
    ctx.fillStyle = '#E2E1B5'; ctx.fillRect(player.x - 2, player.y - 6 + bob, 4, 6);
    ctx.fillStyle = '#AA5D4C'; ctx.fillRect(player.x - 2, player.y - 6 + bob, 4, 2);

    ctx.fillStyle = '#FED7AA'; ctx.fillRect(player.x - 5, player.y - 15 + bob, 10, 9);

    ctx.fillStyle = '#25333E';
    ctx.fillRect(player.x - 9, player.y - 18 + bob, 18, 3);
    ctx.fillRect(player.x - 6, player.y - 27 + bob, 12, 10);
    ctx.fillStyle = '#AA5D4C'; ctx.fillRect(player.x - 6, player.y - 20 + bob, 12, 2.5);

    ctx.fillStyle = '#1A120B';
    if (player.dir === 'down') {
        ctx.fillRect(player.x - 3, player.y - 11 + bob, 2, 2.5);
        ctx.fillRect(player.x + 1, player.y - 11 + bob, 2, 2.5);
    } else if (player.dir === 'left') {
        ctx.fillRect(player.x - 4, player.y - 11 + bob, 2, 2.5);
    } else if (player.dir === 'right') {
        ctx.fillRect(player.x + 2, player.y - 11 + bob, 2, 2.5);
    }
}

function loop() {
    update();
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    if (mode === "gallery") { drawGallery(); } else { drawLobby(); }
    drawPlayer();
    requestAnimationFrame(loop);
}
loop();
</script>
</body>
</html>
"""

game_html = (PIXEL_GAME_HTML
             .replace("__MODE__", mode_str)
             .replace("__ARTIST__", exhibit_json))

# 9. 主內容：左遊戲、右資訊
section_title("展廳漫遊", "用方向鍵或 WASD 移動，走到拱門前按空白鍵", anchor="gallery")

col_game, col_info = st.columns([3, 2], gap="large")

with col_game:
    if is_in_gallery:
        st.subheader(f"🏛️ 【{target_artist_data['matched_name']}】專屬古典展廳大門")
        st.caption("操縱紳士漫步至正前方古典拱門，按【空白鍵 (Space)】鑑賞真實館藏代表作！")
    else:
        st.subheader("🛋️ 古典接待大廳 (Grand Entrance Lobby)")
        st.caption("紳士漫步於古典大廳中；請於上方搜尋或點選名家標籤以開啟專屬展廊！")

    components.html(game_html, height=540)

with col_info:
    if is_in_gallery:
        st.subheader(f"🖼️ 【{target_artist_data['matched_name']}】代表作全覽")

        artworks = target_artist_data.get("artworks", [])
        if artworks:
            art_tabs = st.tabs([art["name"].split(' ')[0] for art in artworks])
            for i, tab in enumerate(art_tabs):
                with tab:
                    art = artworks[i]
                    st.markdown(
                        f'<div class="artwork-card"><img src="{art["final_src"]}" referrerpolicy="no-referrer">'
                        f'<div class="t">{art["name"]}</div><div class="d">{art["desc"]}</div></div>',
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
        st.info("💡 試著點擊上方標籤「**米開朗基羅**」、「**莫內**」或「**梵谷**」，立即開啟獨立專屬展廳！")

# 10. 頁尾
render_footer()
