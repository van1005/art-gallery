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
# 網站外觀（樣式、導覽列、主視覺、頁尾）
# ============================================================
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;600;700;900&family=Noto+Sans+TC:wght@400;500;700&family=LXGW+WenKai+TC:wght@300;400;700&display=swap');

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
.artwork-card { text-align: center; margin-bottom: 14px; }
.artwork-card img {
  max-width: 100%; border-radius: 10px; border: 1px solid rgba(185,217,246,.3);
  box-shadow: 0 10px 30px rgba(0,0,0,.55); transition: transform .35s;
}
.artwork-card img:hover { transform: scale(1.025); }
.artwork-card .t { font-weight: 700; color: var(--cream); margin-top: 10px; }
.artwork-card .d { font-size: .95rem; color: var(--sky); margin-top: 4px; line-height: 1.7; }

/* ---------- 7. 分頁、提示框 ---------- */
.stTabs [data-baseweb="tab-list"] { gap: 6px; border-bottom: 1px solid rgba(185,217,246,.2); }
.stTabs [data-baseweb="tab"] { color: var(--cream); border-radius: 10px 10px 0 0; padding: 8px 16px; }
.stTabs [aria-selected="true"] { color: var(--sky) !important; background: rgba(84,119,145,.25); }
.stTabs [data-baseweb="tab-highlight"] { background-color: var(--rust) !important; }
.stTabs [data-baseweb="tab-panel"] a { color: var(--sky) !important; }
div[data-testid="stAlert"] {
  background: rgba(84,119,145,.22); border: 1px solid rgba(185,217,246,.25); border-radius: 12px;
}
hr { border-color: rgba(185,217,246,.14) !important; }
iframe { border-radius: 14px; }

/* ---------- 8. 頁尾 ---------- */
.site-footer {
  margin: 50px -28px -40px -28px; padding: 34px 32px; text-align: center;
  background: #10171D; border-top: 1px solid rgba(185,217,246,.14);
  color: var(--gold); font-size: .88rem; letter-spacing: 1.5px; line-height: 2;
}
.site-footer b { color: var(--sky); font-family: 'Noto Serif TC', serif; }

/* ---------- 9. 字體（內文：霞鶩文楷；標題：思源宋體） ---------- */
.stMarkdown, .stMarkdown p, .stMarkdown li, [data-testid="stCaptionContainer"],
.stTextInput label p, .stTextInput input, .stButton button p,
div[data-testid="stAlert"] p, .stTabs [data-baseweb="tab"] p,
.stTabs [data-baseweb="tab-panel"] p, .stTabs [data-baseweb="tab-panel"] li {
  font-family: 'LXGW WenKai TC', 'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', sans-serif !important;
  letter-spacing: .05em;
}
.stMarkdown p, .stMarkdown li { font-size: 1.1rem; line-height: 1.95; color: #E6E3C8; }
.stTabs [data-baseweb="tab-panel"] p, .stTabs [data-baseweb="tab-panel"] li {
  font-size: 1.15rem !important; line-height: 1.95 !important; color: #E6E3C8 !important;
}
div[data-testid="stAlert"] p { font-size: 1.05rem !important; line-height: 1.8 !important; color: var(--cream) !important; }
.stMarkdown strong, .stTabs [data-baseweb="tab-panel"] strong { font-weight: 700; color: #F3E7B8; }
[data-testid="stCaptionContainer"] p { font-size: .95rem !important; color: #B7B082 !important; }

h1, h2, h3, h4, [data-testid="stHeading"] h3 {
  font-family: 'Noto Serif TC', serif !important; font-weight: 600 !important;
  letter-spacing: .08em; color: var(--sky) !important;
}
[data-testid="stHeading"] h3 { font-size: 1.4rem !important; }
.stMarkdown h3, .stTabs [data-baseweb="tab-panel"] h3 { font-size: 1.3rem !important; margin: 1.2rem 0 .6rem !important; }
.stMarkdown h4 { font-size: 1.12rem !important; color: #B7B082 !important; }

/* ---------- 10. 手機版 ---------- */
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
        '操作說明：方向鍵 / WASD 移動（或直接點擊地面），走近掛畫按空白鍵鑑賞真跡<br>'
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

# 8. 擬真展廳遊戲（透視地板、燈光、掛畫、可點擊移動）
PIXEL_GAME_HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="referrer" content="no-referrer">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@500;700&family=LXGW+WenKai+TC:wght@400;700&display=swap" rel="stylesheet">
<style>
    body { margin:0; padding:0; background:transparent; display:flex; justify-content:center; align-items:center;
           font-family:'LXGW WenKai TC','Noto Serif TC',serif; overflow:hidden; user-select:none; outline:none; }
    #game-box { position:relative; width:660px; height:520px; border-radius:14px; overflow:hidden;
                border:1px solid rgba(185,217,246,.45); background:#1b2630; cursor:pointer;
                box-shadow:0 18px 50px rgba(0,0,0,.8), 0 0 0 4px rgba(84,119,145,.25); }
    canvas { display:block; }
    #guide-bar { position:absolute; top:12px; left:12px; background:rgba(20,28,35,.72); color:#E2E1B5;
                 padding:6px 14px; border-radius:20px; font-size:12.5px; border:1px solid rgba(185,217,246,.4);
                 pointer-events:none; letter-spacing:.5px; backdrop-filter:blur(6px); }
    #interact-prompt { position:absolute; display:none; color:#fff; background:rgba(170,93,76,.95);
                       border:1.5px solid #f1e3b0; padding:5px 14px; border-radius:20px; font-size:12.5px;
                       pointer-events:none; transform:translate(-50%,-100%); white-space:nowrap;
                       box-shadow:0 6px 18px rgba(0,0,0,.6); animation:bounce .8s infinite alternate; }
    @keyframes bounce { from { margin-top:0; } to { margin-top:-6px; } }
    @keyframes pop { from { opacity:0; transform:translate(-50%,-46%) scale(.94); } to { opacity:1; transform:translate(-50%,-50%) scale(1); } }
    #rpg-modal { position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); width:570px;
                 background:linear-gradient(145deg,rgba(47,62,74,.97),rgba(27,38,48,.97));
                 border:1px solid #d8b86a; border-radius:16px; padding:18px 22px; display:none; z-index:100;
                 color:#E2E1B5; box-shadow:0 24px 60px rgba(0,0,0,.9); animation:pop .25s ease-out; }
    .modal-body { display:flex; gap:18px; align-items:center; }
    .modal-img-box { flex:0 0 215px; height:255px; border-radius:6px; overflow:hidden; background:#10171d;
                     border:6px solid #c9a85c; box-shadow:0 8px 22px rgba(0,0,0,.7); display:flex;
                     align-items:center; justify-content:center; }
    .modal-img-box img { width:100%; height:100%; object-fit:contain; display:block; }
    .modal-info { flex:1; }
    .modal-info h3 { margin:0 0 6px 0; color:#B9D9F6; font-size:18px; font-family:'Noto Serif TC',serif; font-weight:700; line-height:1.4; }
    .period-tag { display:inline-block; background:#AA5D4C; color:#fff; padding:2px 10px; border-radius:20px;
                  font-size:11.5px; margin-bottom:8px; }
    .quote { font-size:13.5px; line-height:1.7; color:#E2E1B5; border-left:3px solid #AA5D4C;
             padding:4px 0 4px 12px; margin:6px 0 8px 0; }
    #modal-desc { font-size:13px; color:#c9c39a; line-height:1.75; }
    .nav-dots { display:flex; gap:6px; margin-top:10px; flex-wrap:wrap; }
    .nav-btn { background:transparent; color:#E2E1B5; border:1px solid rgba(185,217,246,.5); padding:3px 12px;
               font-size:12px; border-radius:20px; cursor:pointer; font-family:inherit; }
    .nav-btn.on, .nav-btn:hover { background:#AA5D4C; border-color:#AA5D4C; color:#fff; }
    .close-hint { margin-top:12px; text-align:right; font-size:11.5px; color:#B7B082; }
</style>
</head>
<body tabindex="0">
<div id="game-box">
    <canvas id="gameCanvas"></canvas>
    <div id="guide-bar"></div>
    <div id="interact-prompt"></div>
    <div id="rpg-modal">
        <div class="modal-body">
            <div class="modal-img-box"><img id="modal-img" src="" alt="作品" referrerpolicy="no-referrer"></div>
            <div class="modal-info">
                <h3 id="modal-title"></h3>
                <span class="period-tag" id="modal-period"></span>
                <div class="quote" id="modal-quote"></div>
                <div id="modal-desc"></div>
                <div class="nav-dots" id="modal-nav"></div>
            </div>
        </div>
        <div class="close-hint">按 [空白鍵] 或 移動角色 關閉視窗</div>
    </div>
</div>

<script>
const W = 660, H = 520, WALL = 190, VPY = 60;
const canvas = document.getElementById('gameCanvas');
const dpr = Math.min(window.devicePixelRatio || 1, 2);
canvas.width = W * dpr; canvas.height = H * dpr;
canvas.style.width = W + 'px'; canvas.style.height = H + 'px';
const ctx = canvas.getContext('2d');
ctx.scale(dpr, dpr);
ctx.imageSmoothingQuality = 'high';

const promptEl = document.getElementById('interact-prompt');
const modal = document.getElementById('rpg-modal');
const guide = document.getElementById('guide-bar');
const SERIF = '"Noto Serif TC","LXGW WenKai TC",serif';

const mode = "__MODE__";
const currentArtist = __ARTIST__;
const arts = currentArtist.artworks || [];
const imgs = arts.map(a => { const im = new Image(); im.referrerPolicy = 'no-referrer'; im.src = a.final_src; return im; });

const T = mode === 'gallery'
  ? { wallTop:'#3a5063', wallBot:'#263847', panel:'#1e2d39', floorA:'#80593a', floorB:'#6d4b32', rug:['#8a3232','#5c2025'] }
  : { wallTop:'#557590', wallBot:'#3a566d', panel:'#2d4458', floorA:'#ebe5cb', floorB:'#bdb798', rug:['#a24f40','#6f2f2b'] };

guide.innerHTML = mode === 'gallery'
  ? '🚶 方向鍵 / WASD 或點擊地面移動 ｜ 走近掛畫按空白鍵'
  : '🏛️ 接待大廳 ｜ 請於上方搜尋或點選名家（先點一下畫面）';

const player = { x: 330, y: mode === 'gallery' ? 440 : 400, speed: 3.2, dir: 'up', walkFrame: 0, moving: false };
const keys = {};
let target = null, nearIdx = -1, isModalOpen = false;

/* ---------- 小工具 ---------- */
function rr(x, y, w, h, r) {
  ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath();
}
function lg(x0, y0, x1, y1, stops) {
  const g = ctx.createLinearGradient(x0, y0, x1, y1);
  stops.forEach(s => g.addColorStop(s[0], s[1])); return g;
}
function ell(x, y, rx, ry, color) {
  ctx.fillStyle = color; ctx.beginPath(); ctx.ellipse(x, y, rx, ry, 0, 0, Math.PI * 2); ctx.fill();
}
function P(y, bx) { return 330 + (bx - 330) * (y - VPY) / (H - VPY); }
function hash(n) { const s = Math.sin(n * 12.9898) * 43758.5453; return s - Math.floor(s); }

/* ---------- 牆面 ---------- */
function drawWall() {
  ctx.fillStyle = lg(0, 0, 0, WALL, [[0, T.wallTop], [1, T.wallBot]]); ctx.fillRect(0, 0, W, WALL);
  ctx.fillStyle = 'rgba(255,255,255,.035)';
  for (let x = 0; x < W; x += 44) { ctx.fillRect(x, 20, 2, 140); ctx.beginPath(); ctx.arc(x + 22, 90, 5, 0, 7); ctx.fill(); }
  ctx.fillStyle = lg(0, 0, 0, 18, [[0, '#14202a'], [1, '#2a3d4b']]); ctx.fillRect(0, 0, W, 18);
  ctx.fillStyle = lg(0, 18, 0, 22, [[0, '#e6c97a'], [1, '#8a6f35']]); ctx.fillRect(0, 18, W, 4);
  ctx.fillStyle = T.panel; ctx.fillRect(0, 160, W, 30);
  ctx.fillStyle = lg(0, 158, 0, 162, [[0, '#e6c97a'], [1, '#8a6f35']]); ctx.fillRect(0, 158, W, 4);
  ctx.strokeStyle = 'rgba(230,201,122,.28)'; ctx.lineWidth = 1;
  for (let x = 14; x < W; x += 110) ctx.strokeRect(x, 168, 94, 12);
  ctx.fillStyle = lg(0, 180, 0, 190, [[0, '#10181f'], [1, '#222f3a']]); ctx.fillRect(0, 180, W, 10);
}

/* ---------- 地板 ---------- */
function quad(y1, y2, bx1, bx2, fill) {
  ctx.beginPath(); ctx.moveTo(P(y1, bx1), y1); ctx.lineTo(P(y1, bx2), y1);
  ctx.lineTo(P(y2, bx2), y2); ctx.lineTo(P(y2, bx1), y2); ctx.closePath(); ctx.fillStyle = fill; ctx.fill();
}
function drawFloor() {
  const n = 9, step = 110;
  for (let i = 0; i < n; i++) {
    const y1 = WALL + (H - WALL) * Math.pow(i / n, 1.6), y2 = WALL + (H - WALL) * Math.pow((i + 1) / n, 1.6);
    for (let k = -5; k < 5; k++) {
      const base = mode === 'gallery' ? (k & 1 ? T.floorA : T.floorB) : (((i + k) & 1) ? T.floorA : T.floorB);
      quad(y1, y2, 330 + k * step, 330 + (k + 1) * step, base);
      quad(y1, y2, 330 + k * step, 330 + (k + 1) * step, 'rgba(0,0,0,' + (hash(i * 11 + k * 7) * 0.1) + ')');
      ctx.strokeStyle = 'rgba(0,0,0,.14)'; ctx.lineWidth = .6; ctx.stroke();
    }
  }
  ctx.fillStyle = lg(0, WALL, 0, WALL + 130, [[0, 'rgba(0,0,0,.4)'], [1, 'rgba(0,0,0,0)']]); ctx.fillRect(0, WALL, W, 130);
  const g = ctx.createRadialGradient(330, 330, 20, 330, 330, 280);
  g.addColorStop(0, 'rgba(255,244,210,.22)'); g.addColorStop(1, 'rgba(255,244,210,0)');
  ctx.fillStyle = g; ctx.fillRect(0, WALL, W, H - WALL);
}
function drawRug() {
  const y1 = WALL, y2 = H, half = 74;
  const path = h => { ctx.beginPath(); ctx.moveTo(P(y1, 330 - h), y1); ctx.lineTo(P(y1, 330 + h), y1);
    ctx.lineTo(P(y2, 330 + h), y2); ctx.lineTo(P(y2, 330 - h), y2); ctx.closePath(); };
  path(half); ctx.fillStyle = lg(0, y1, 0, y2, [[0, T.rug[1]], [1, T.rug[0]]]); ctx.fill();
  ctx.strokeStyle = '#d4b46a'; ctx.lineWidth = 3; ctx.stroke();
  path(half - 12); ctx.strokeStyle = 'rgba(212,180,106,.55)'; ctx.lineWidth = 1.2; ctx.stroke();
  [0.22, 0.5, 0.82].forEach(t => {
    const y = y1 + (y2 - y1) * Math.pow(t, 1.5), s = (y - VPY) / (H - VPY);
    ctx.strokeStyle = 'rgba(212,180,106,.5)'; ctx.lineWidth = 1.2;
    ctx.beginPath(); ctx.ellipse(330, y, 38 * s, 12 * s, 0, 0, Math.PI * 2); ctx.stroke();
    ell(330, y, 8 * s, 3 * s, 'rgba(212,180,106,.5)');
  });
}

/* ---------- 擺設 ---------- */
function column(cx) {
  const w = 40, top = 26, bot = 186;
  ell(cx + 8, bot + 10, 36, 8, 'rgba(0,0,0,.3)');
  ctx.fillStyle = lg(cx - w / 2, 0, cx + w / 2, 0, [[0, '#9c9577'], [.35, '#f1ebd1'], [.7, '#cfc8a8'], [1, '#7e775d']]);
  ctx.fillRect(cx - w / 2, top, w, bot - top);
  ctx.fillStyle = 'rgba(0,0,0,.07)';
  for (let i = 1; i < 4; i++) ctx.fillRect(cx - w / 2 + i * w / 4 - 1, top, 2, bot - top);
  ctx.fillStyle = lg(0, top - 10, 0, top + 2, [[0, '#efe8cc'], [1, '#bdb694']]); rr(cx - w / 2 - 7, top - 10, w + 14, 13, 3); ctx.fill();
  ctx.fillStyle = lg(0, bot - 4, 0, bot + 9, [[0, '#d8d2b2'], [1, '#9d967a']]); rr(cx - w / 2 - 9, bot - 4, w + 18, 13, 3); ctx.fill();
}
function plant(x, y) {
  ell(x, y + 4, 24, 6, 'rgba(0,0,0,.3)');
  for (let i = 0; i < 9; i++) {
    const a = (-80 + i * 20) * Math.PI / 180, len = 32 + hash(i + x) * 22;
    ctx.save(); ctx.translate(x, y - 30); ctx.rotate(a);
    ctx.fillStyle = lg(0, 0, 0, -len, [[0, '#1f5a3a'], [1, '#4f9a5c']]);
    ctx.beginPath(); ctx.ellipse(0, -len / 2, 7, len / 2, 0, 0, Math.PI * 2); ctx.fill(); ctx.restore();
  }
  ctx.fillStyle = lg(x - 16, 0, x + 16, 0, [[0, '#7a3f2e'], [.5, '#c97a5c'], [1, '#6b3526']]);
  ctx.beginPath(); ctx.moveTo(x - 15, y - 28); ctx.lineTo(x + 15, y - 28); ctx.lineTo(x + 10, y + 3); ctx.lineTo(x - 10, y + 3); ctx.closePath(); ctx.fill();
  ctx.fillStyle = '#d99a7a'; rr(x - 17, y - 32, 34, 7, 3); ctx.fill();
}
function frameBox(cx, cy, w, h, drawInner) {
  ctx.save(); ctx.shadowColor = 'rgba(0,0,0,.6)'; ctx.shadowBlur = 16; ctx.shadowOffsetY = 7;
  ctx.fillStyle = lg(cx - w / 2 - 8, cy - h / 2 - 8, cx + w / 2 + 8, cy + h / 2 + 8, [[0, '#f0d78a'], [.5, '#a98a42'], [1, '#e6c97a']]);
  ctx.fillRect(cx - w / 2 - 8, cy - h / 2 - 8, w + 16, h + 16); ctx.restore();
  ctx.fillStyle = '#16100a'; ctx.fillRect(cx - w / 2 - 3, cy - h / 2 - 3, w + 6, h + 6);
  ctx.save(); ctx.beginPath(); ctx.rect(cx - w / 2, cy - h / 2, w, h); ctx.clip();
  drawInner(cx - w / 2, cy - h / 2, w, h);
  ctx.fillStyle = lg(cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2, [[0, 'rgba(255,255,255,.13)'], [.4, 'rgba(255,255,255,0)'], [1, 'rgba(0,0,0,.12)']]);
  ctx.fillRect(cx - w / 2, cy - h / 2, w, h); ctx.restore();
}
function pictureLight(cx, topY, w) {
  const g = ctx.createLinearGradient(0, topY, 0, topY + 90);
  g.addColorStop(0, 'rgba(255,236,170,.28)'); g.addColorStop(1, 'rgba(255,236,170,0)');
  ctx.fillStyle = g; ctx.beginPath(); ctx.moveTo(cx - 14, topY); ctx.lineTo(cx + 14, topY);
  ctx.lineTo(cx + w / 2 + 14, topY + 90); ctx.lineTo(cx - w / 2 - 14, topY + 90); ctx.closePath(); ctx.fill();
  ctx.fillStyle = lg(0, topY - 5, 0, topY + 1, [[0, '#f0d78a'], [1, '#8a6f35']]); rr(cx - 22, topY - 5, 44, 6, 3); ctx.fill();
  ctx.fillStyle = '#8a6f35'; ctx.fillRect(cx - 1.5, topY - 12, 3, 8);
}
function plaque(cx, y, text) {
  ctx.font = '11px ' + SERIF;
  const w = Math.max(80, ctx.measureText(text).width + 22);
  ctx.fillStyle = '#17120c'; rr(cx - w / 2, y, w, 17, 3); ctx.fill();
  ctx.strokeStyle = '#c9a85c'; ctx.lineWidth = 1; ctx.stroke();
  ctx.fillStyle = '#ecdcab'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillText(text, cx, y + 9);
}
function shortName(n) { return n.split(' (')[0].split('(')[0]; }

function artSlots() {
  const n = arts.length; return arts.map((a, i) => 330 + (i - (n - 1) / 2) * 175);
}
function drawGalleryWall() {
  ctx.fillStyle = 'rgba(8,14,20,.6)'; rr(230, 28, 200, 24, 12); ctx.fill();
  ctx.strokeStyle = '#d4b46a'; ctx.lineWidth = 1; ctx.stroke();
  ctx.fillStyle = '#ecdcab'; ctx.font = 'bold 14px ' + SERIF; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  ctx.fillText((currentArtist.icon || '') + ' 【' + currentArtist.matched_name + '】專屬展廳', 330, 41);
  const cs = artSlots();
  arts.forEach((a, i) => {
    const im = imgs[i], ok = im.complete && im.naturalWidth > 0;
    let w = 120, h = 84;
    if (ok) { const r = im.naturalWidth / im.naturalHeight; if (r > 128 / 88) { w = 128; h = 128 / r; } else { h = 88; w = 88 * r; } }
    pictureLight(cs[i], 40, w);
    frameBox(cs[i], 104, w, h, (x, y, ww, hh) => {
      if (ok) ctx.drawImage(im, x, y, ww, hh);
      else { ctx.fillStyle = lg(x, y, x + ww, y + hh, [[0, '#5a7a92'], [1, '#2a3a48']]); ctx.fillRect(x, y, ww, hh); }
    });
    plaque(cs[i], 163, shortName(a.name));
    const pool = ctx.createRadialGradient(cs[i], 235, 4, cs[i], 235, 85);
    pool.addColorStop(0, 'rgba(255,238,180,.16)'); pool.addColorStop(1, 'rgba(255,238,180,0)');
    ctx.save(); ctx.translate(0, 0); ctx.fillStyle = pool; ctx.fillRect(cs[i] - 90, 195, 180, 80); ctx.restore();
  });
}
function drawLobbyWall() {
  frameBox(135, 100, 84, 62, (x, y, w, h) => {
    ctx.fillStyle = lg(x, y, x, y + h, [[0, '#f2b36b'], [.55, '#c8604a'], [1, '#2f3e5c']]); ctx.fillRect(x, y, w, h);
    ell(x + w * .5, y + h * .5, 14, 14, 'rgba(255,240,200,.85)');
  });
  frameBox(525, 100, 84, 62, (x, y, w, h) => {
    ctx.fillStyle = lg(x, y, x + w, y + h, [[0, '#1f3b5c'], [.5, '#4f86a8'], [1, '#b9d9f6']]); ctx.fillRect(x, y, w, h);
    ctx.fillStyle = 'rgba(255,255,255,.35)'; ctx.fillRect(x, y + h * .62, w, 3); ctx.fillRect(x, y + h * .74, w, 2);
  });
  pictureLight(135, 44, 84); pictureLight(525, 44, 84);
}
function desk() {
  const x = 215, w = 230, top = 124, bot = 190;
  ell(330, bot + 5, 128, 8, 'rgba(0,0,0,.35)');
  ctx.fillStyle = lg(0, top, 0, bot, [[0, '#7d5638'], [1, '#442b1d']]); ctx.fillRect(x, top, w, bot - top);
  ctx.strokeStyle = 'rgba(230,201,122,.5)'; ctx.lineWidth = 1;
  for (let i = 0; i < 3; i++) ctx.strokeRect(x + 10 + i * 74, top + 12, 62, bot - top - 22);
  ctx.fillStyle = lg(0, top - 9, 0, top + 2, [[0, '#dcb583'], [1, '#a67c52']]); rr(x - 9, top - 9, w + 18, 11, 3); ctx.fill();
  ctx.fillStyle = '#e6c97a'; ctx.font = 'bold 15px ' + SERIF; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  ctx.fillText('接待諮詢處', 330, top + 34);
  ctx.fillStyle = '#3a2a1a'; ctx.fillRect(x + 28, top - 14, 4, 6);
  ctx.fillStyle = '#2f6b4f'; ctx.beginPath(); ctx.moveTo(x + 18, top - 14); ctx.lineTo(x + 42, top - 14); ctx.lineTo(x + 36, top - 28); ctx.lineTo(x + 24, top - 28); ctx.closePath(); ctx.fill();
  const g = ctx.createRadialGradient(x + 30, top - 12, 2, x + 30, top - 12, 46);
  g.addColorStop(0, 'rgba(255,236,170,.4)'); g.addColorStop(1, 'rgba(255,236,170,0)'); ctx.fillStyle = g; ctx.fillRect(x - 20, top - 60, 100, 90);
  ctx.fillStyle = '#e8e2c8'; ctx.fillRect(x + w - 62, top - 13, 34, 4); ctx.fillStyle = '#AA5D4C'; ctx.fillRect(x + w - 60, top - 17, 30, 4);
}
function chandelier(t) {
  const fl = 0.9 + 0.1 * Math.sin(t / 280);
  ctx.strokeStyle = '#8a7a4a'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(330, 0); ctx.lineTo(330, 44); ctx.stroke();
  ctx.save(); ctx.globalCompositeOperation = 'lighter';
  const g = ctx.createRadialGradient(330, 58, 6, 330, 58, 190);
  g.addColorStop(0, 'rgba(255,226,150,' + (0.34 * fl) + ')'); g.addColorStop(1, 'rgba(255,226,150,0)');
  ctx.fillStyle = g; ctx.fillRect(100, 0, 460, 300); ctx.restore();
  ctx.strokeStyle = '#e0bf6c'; ctx.lineWidth = 4; ctx.beginPath(); ctx.ellipse(330, 58, 54, 11, 0, 0, Math.PI * 2); ctx.stroke();
  for (let a = 0; a < 8; a++) {
    const x = 330 + Math.cos(a * Math.PI / 4) * 54, y = 58 + Math.sin(a * Math.PI / 4) * 11;
    ctx.strokeStyle = 'rgba(255,255,255,.55)'; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x, y + 12); ctx.stroke();
    ell(x, y - 3, 3.4, 3.4, '#fff6cf'); ell(x, y + 13, 2, 2.6, 'rgba(210,235,255,.85)');
  }
  ell(330, 72, 5, 6, '#e0bf6c');
}

/* ---------- 紳士 ---------- */
function drawPlayer() {
  const s = (0.7 + 0.4 * (player.y - 215) / (H - 215)) * 1.2;
  const sw = player.moving ? Math.sin(player.walkFrame) : 0;
  ctx.save(); ctx.translate(player.x, player.y); ctx.scale(s, s);
  ell(0, 2, 16, 5, 'rgba(0,0,0,.4)');
  ctx.fillStyle = '#1c2630'; rr(-8, -14 + Math.max(0, sw) * -2, 6, 15, 2); ctx.fill(); rr(2, -14 + Math.max(0, -sw) * -2, 6, 15, 2); ctx.fill();
  ctx.fillStyle = '#0d1218'; rr(-9, -2 + Math.max(0, sw) * -2, 8, 4, 2); ctx.fill(); rr(1, -2 + Math.max(0, -sw) * -2, 8, 4, 2); ctx.fill();
  if (player.dir === 'right' || player.dir === 'left') { const d = player.dir === 'right' ? 1 : -1;
    ctx.strokeStyle = '#d4b46a'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(d * 12, -22 + sw * 2); ctx.lineTo(d * 16, 0); ctx.stroke(); }
  ctx.fillStyle = lg(-10, 0, 10, 0, [[0, '#2f4a61'], [.5, '#5b86a6'], [1, '#2a4257']]); rr(-10, -36, 20, 24, 5); ctx.fill();
  ctx.fillStyle = '#f1ead2'; ctx.beginPath(); ctx.moveTo(-3.5, -36); ctx.lineTo(3.5, -36); ctx.lineTo(0, -22); ctx.closePath(); ctx.fill();
  ctx.fillStyle = '#AA5D4C'; ctx.fillRect(-3, -35, 6, 3);
  ctx.fillStyle = '#2f4a61'; rr(-14, -35 + sw * 2, 5, 17, 2.5); ctx.fill(); rr(9, -35 - sw * 2, 5, 17, 2.5); ctx.fill();
  ctx.fillStyle = '#f3d3b0'; ctx.beginPath(); ctx.arc(0, -43, 8, 0, 7); ctx.fill();
  ctx.fillStyle = '#1b1f27'; ctx.beginPath(); ctx.ellipse(0, -49, 13, 3.2, 0, 0, 7); ctx.fill(); rr(-7.5, -64, 15, 16, 2); ctx.fill();
  ctx.fillStyle = '#AA5D4C'; ctx.fillRect(-7.5, -54, 15, 3.5);
  ctx.fillStyle = '#1a120b';
  if (player.dir === 'down') { ell(-3, -42, 1.2, 1.6, '#1a120b'); ell(3, -42, 1.2, 1.6, '#1a120b'); }
  else if (player.dir === 'left') ell(-4, -42, 1.2, 1.6, '#1a120b');
  else if (player.dir === 'right') ell(4, -42, 1.2, 1.6, '#1a120b');
  ctx.restore();
}

/* ---------- 灰塵光點、暗角、提示 ---------- */
const dust = Array.from({ length: 30 }, (_, i) => ({ x: hash(i) * W, y: hash(i + 50) * 400, v: 0.1 + hash(i + 9) * 0.25, r: 0.8 + hash(i + 3) * 1.4 }));
function drawDust() {
  dust.forEach(d => { d.y += d.v * 0.3; d.x += Math.sin((d.y + d.r * 50) / 40) * 0.15; if (d.y > 480) d.y = 20;
    ctx.fillStyle = 'rgba(255,244,210,' + (0.18 + d.r * 0.08) + ')'; ctx.beginPath(); ctx.arc(d.x, d.y, d.r, 0, 7); ctx.fill(); });
}
function vignette() {
  const g = ctx.createRadialGradient(330, 270, 170, 330, 270, 440);
  g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(1, 'rgba(0,0,0,.5)'); ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
}
function lobbyHud() {
  ctx.fillStyle = 'rgba(14,20,26,.72)'; rr(95, 482, 470, 26, 13); ctx.fill();
  ctx.strokeStyle = 'rgba(212,180,106,.7)'; ctx.lineWidth = 1; ctx.stroke();
  ctx.fillStyle = '#ecdcab'; ctx.font = '13px ' + SERIF; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  ctx.fillText('✨ 請於上方搜尋藝術家，或點選名家標籤開啟專屬展廳 ✨', 330, 495);
}

/* ---------- 互動 ---------- */
function showArt(i) {
  const a = arts[i];
  document.getElementById('modal-img').src = a.final_src;
  document.getElementById('modal-title').innerHTML = (currentArtist.icon || '') + ' ' + a.name;
  document.getElementById('modal-desc').innerText = a.desc;
  document.querySelectorAll('.nav-btn').forEach((b, j) => b.classList.toggle('on', j === i));
}
function openModal(i) {
  document.getElementById('modal-period').innerText = '【' + currentArtist.matched_name + '】' + currentArtist.period;
  document.getElementById('modal-quote').innerText = currentArtist.quote;
  const nav = document.getElementById('modal-nav'); nav.innerHTML = '';
  if (arts.length > 1) arts.forEach((a, j) => { const b = document.createElement('button'); b.className = 'nav-btn';
    b.innerText = '作品 ' + (j + 1); b.onclick = e => { e.stopPropagation(); showArt(j); }; nav.appendChild(b); });
  showArt(i); modal.style.display = 'block'; isModalOpen = true;
}
function closeModal() { modal.style.display = 'none'; isModalOpen = false; }

window.addEventListener('keydown', e => {
  if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', ' '].includes(e.key)) e.preventDefault();
  keys[e.key.toLowerCase()] = true;
  if ((e.key === ' ' || e.key === 'Enter') && mode === 'gallery') {
    if (isModalOpen) closeModal(); else if (nearIdx >= 0) openModal(nearIdx);
  }
});
window.addEventListener('keyup', e => { keys[e.key.toLowerCase()] = false; });
document.getElementById('game-box').addEventListener('mousedown', e => {
  window.focus(); document.body.focus();
  if (e.target.closest('#rpg-modal')) return;
  const r = canvas.getBoundingClientRect();
  target = { x: Math.max(30, Math.min(W - 30, e.clientX - r.left)), y: Math.max(215, Math.min(470, e.clientY - r.top)) };
});

function update() {
  let dx = 0, dy = 0;
  if (keys['arrowup'] || keys['w']) dy -= 1; if (keys['arrowdown'] || keys['s']) dy += 1;
  if (keys['arrowleft'] || keys['a']) dx -= 1; if (keys['arrowright'] || keys['d']) dx += 1;
  if (dx || dy) target = null;
  else if (target) { const vx = target.x - player.x, vy = target.y - player.y, d = Math.hypot(vx, vy);
    if (d < 4) target = null; else { dx = vx / d; dy = vy / d; } }
  player.moving = !!(dx || dy);
  if (player.moving) {
    const len = Math.hypot(dx, dy) || 1;
    player.x += dx / len * player.speed; player.y += dy / len * player.speed;
    player.dir = Math.abs(dx) > Math.abs(dy) ? (dx < 0 ? 'left' : 'right') : (dy < 0 ? 'up' : 'down');
    player.walkFrame += 0.28; if (isModalOpen) closeModal();
  }
  player.x = Math.max(30, Math.min(W - 30, player.x));
  player.y = Math.max(215, Math.min(470, player.y));

  nearIdx = -1;
  if (mode === 'gallery') {
    const cs = artSlots(); let best = 75;
    cs.forEach((cx, i) => { const d = Math.abs(player.x - cx); if (d < best && player.y < 300) { best = d; nearIdx = i; } });
  }
  if (nearIdx >= 0 && !isModalOpen) {
    promptEl.style.display = 'block'; promptEl.style.left = player.x + 'px';
    promptEl.style.top = (player.y - 90) + 'px';
    promptEl.innerText = '❗ [空白鍵] 鑑賞 ' + shortName(arts[nearIdx].name);
  } else promptEl.style.display = 'none';
}

function loop(t) {
  update(); ctx.clearRect(0, 0, W, H);
  drawWall();
  if (mode === 'gallery') drawGalleryWall(); else drawLobbyWall();
  drawFloor(); drawRug();
  if (mode === 'lobby') desk();
  column(48); column(612);
  if (mode === 'lobby') chandelier(t || 0);
  const items = [{ y: player.y, f: drawPlayer }];
  if (mode === 'lobby') { items.push({ y: 255, f: () => plant(92, 255) }); items.push({ y: 255, f: () => plant(568, 255) }); }
  else { items.push({ y: 250, f: () => plant(100, 250) }); items.push({ y: 250, f: () => plant(560, 250) }); }
  items.sort((a, b) => a.y - b.y).forEach(o => o.f());
  drawDust(); vignette();
  if (mode === 'lobby') lobbyHud();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
</script>
</body>
</html>
"""

game_html = (PIXEL_GAME_HTML
             .replace("__MODE__", mode_str)
             .replace("__ARTIST__", exhibit_json))

# 9. 主內容：左遊戲、右資訊
section_title("展廳漫遊", "用方向鍵或 WASD 移動（也可直接點擊地面），走近掛畫按空白鍵", anchor="gallery")

col_game, col_info = st.columns([3, 2], gap="large")

with col_game:
    if is_in_gallery:
        st.subheader(f"🏛️ 【{target_artist_data['matched_name']}】專屬古典展廳")
        st.caption("漫步於展廳中，走近牆上的掛畫，按【空白鍵 (Space)】鑑賞真實館藏代表作！")
    else:
        st.subheader("🛋️ 古典接待大廳 (Grand Entrance Lobby)")
        st.caption("紳士漫步於古典大廳中；請於上方搜尋或點選名家標籤以開啟專屬展廳！")

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
2. **啟程漫遊專屬展廳**：領取門票後，左側畫面將開啟該藝術家的**專屬展廳**，牆上掛滿他的代表作！
3. **深度互動鑑賞**：操縱紳士走近掛畫並按下 **【空白鍵 (Space)】**，即可放大鑑賞作品並同步解鎖其生平脈絡。
""")
        st.info("💡 試著點擊上方標籤「**米開朗基羅**」、「**莫內**」或「**梵谷**」，立即開啟專屬展廳！")

# 10. 頁尾
render_footer()

