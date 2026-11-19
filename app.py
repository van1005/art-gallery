"""web_style.py — 把 Streamlit 介面改造成「像一般網站」的外觀。
放在 app.py 同一個資料夾，然後在 app.py 裡 import 使用。
"""
import streamlit as st

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
[data-testid="stHorizontalBlock"] > [data-testid="stColumn"] > div[data-testid="stVerticalBlockBorderWrapper"],
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

/* 遊戲 iframe 圓角＋陰影 */
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
