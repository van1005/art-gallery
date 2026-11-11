import streamlit as st
import streamlit.components.v1 as components
import json

# 1. 頁面全域設定：寬版全螢幕模式
st.set_page_config(
    page_title="跨時代全球藝術家作品與生命歷程互動圖譜",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 結構化深度資料庫（透過全球無防盜鏈代理載入真正的博物館真跡）
ARTISTS_DATABASE = {
    "梵谷": {
        "title": "文森·梵谷 (Vincent van Gogh)",
        "period": "後印象派 (1853–1890)",
        "category": "油畫 / 後印象派表現主義",
        "identity": "現代表現主義先驅 ｜ 燃燒靈魂的悲劇巨匠",
        "work_name": "《星夜》 (The Starry Night)",
        "image": "https://wsrv.nl/?url=upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/640px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg",
        "color": "#FBBF24", "frame": "#B45309", "icon": "🌌",
        "quote": "「我夢想著繪畫，然後我畫下了我的夢想。」",
        "extract": (
            "### 📌 坎坷生平與創作狂熱\n\n"
            "梵谷出生於荷蘭南部，早年曾任藝術品店員、教師與傳教士，直到接近三十歲才正式投身繪畫。他一生飽受精神疾病、貧困與不被理解的孤獨折磨，但在其生命的最後十年間，以驚人的創作狂熱完成兩千餘幅作品，與弟弟西奧（Theo）之間真摯深刻的書信往返亦成為後世研究其心靈的重要文獻。\n\n"
            "### 🎨 厚塗旋渦與情感表現\n\n"
            "梵谷完全顛覆了傳統寫實色彩的用法，大膽採用鮮烈的高彩度原色、強烈旋渦狀的動態筆觸與厚塗技法（Impasto），將內心劇烈起伏的情感直接傾注於畫布之上，讓星空、麥田與向日葵呈現出震懾人心的生命張力，開啟了20世紀現代表現主義的大門。\n\n"
            "### 🌟 劃時代的藝術遺產\n\n"
            "生前僅售出極少數作品，逝世後其作品卻成為全球最受矚目與珍貴的藝術瑰寶，深刻啟發了野獸派與無數後代創作者，成為人類歷史上純粹藝術精神的永恆象徵。"
        ),
        "representative": (
            "* **《星夜》 (The Starry Night, 1889)**：紐約現代藝術博物館藏，以旋渦天體、柏樹與靜謐小鎮展現深層的精神掙扎與超凡想像。\n\n"
            "* **《向日葵》系列 (1888–1889)**：以高飽和度金黃色調歌頌陽光與生命力，為阿爾勒時期的顛峰之作。\n\n"
            "* **《麥田群鴉》 (1890)**：梵谷生命晚期的代表作，動盪壓抑的天空與四散的黑鴉展現深刻的孤寂與告別。\n\n"
            "* **《自畫像》系列**：透過旋轉筆觸真實記錄藝術家生命各時期的眼神轉折與精神風貌。"
        ),
        "link": "https://zh.wikipedia.org/wiki/文森特·梵高"
    },
    "達文西": {
        "title": "李奧納多·達文西 (Leonardo da Vinci)",
        "period": "文藝復興全盛期 (1452–1519)",
        "category": "油畫 / 跨學科手稿 / 解剖研究",
        "identity": "文藝復興三傑 ｜ 人類史上最偉大的全才博學大師",
        "work_name": "《蒙娜麗莎》 (Mona Lisa)",
        "image": "https://wsrv.nl/?url=upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/640px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg",
        "color": "#34D399", "frame": "#047857", "icon": "🖼️",
        "quote": "「簡約是細膩的極致。觀察是唯一的智慧泉源。」",
        "extract": (
            "### 📌 托斯卡尼的私生子與全方位的求知狂熱\n\n"
            "達文西出生於義大利佛羅倫斯附近的芬奇鎮，進入名師韋羅基奧畫坊學藝。他不僅是無可爭議的畫壇巨擘，更是跨越解剖學、工程學、流體力學、光學、建築與植物學的博學全才。他終生秉持「觀察是唯一的智慧泉源」，在數千頁的鏡像反寫手稿中記錄下對自然律動的精密洞察。\n\n"
            "### 🎨 革命性技法：暈塗法與空氣透視\n\n"
            "在繪畫技法上，達文西發明了劃時代的「暈塗法 (Sfumato)」——透過十多層極為輕薄微透明的顏料層層覆蓋，完全消除了人物邊緣生硬的勾勒輪廓線，使光影如煙霧般溫和融化於肌膚與空氣中；同時他首創「空氣透視法」，精確以冷色調與漸層模糊描摹遠方山巒，創造出無與倫比的立體深度與神秘氛圍。\n\n"
            "### 🌌 跨越五百年的精神高度\n\n"
            "達文西的作品數量極少卻無一不震撼世界，他完美代表了文藝復興時期「人文主義」的極致追求——以嚴謹的理性科學作為基石，開拓出震撼心靈的感性藝術巔峰。"
        ),
        "representative": (
            "* **《蒙娜麗莎》 (Mona Lisa, 約1503–1519，羅浮宮藏)**：暈塗法的巔峰之作，以深不可測的神秘微笑與多維視角聞名全球。\n\n"
            "* **《最後的晚餐》 (The Last Supper, 1495–1498)**：以嚴格單點透視與瞬間戲劇性張力，凝結耶穌宣布門徒叛徒時各人的心理反應。\n\n"
            "* **《維特魯威人》 (Vitruvian Man, 約1490)**：結合古羅馬建築黃金比例與人體解剖學的著名手稿圖標。\n\n"
            "* **《抱銀貂的女子》 (1489–1490)**：突破正面肖像傳統，以生動的三分之三轉身與光澤感展現宮廷女性的靈動高貴。"
        ),
        "link": "https://zh.wikipedia.org/wiki/列奥纳多·达·芬奇"
    },
    "米開朗基羅": {
        "title": "米開朗基羅 (Michelangelo Buonarroti)",
        "period": "文藝復興全盛期 (1475–1564)",
        "category": "大理石雕塑 / 濕壁畫 / 建築設計",
        "identity": "文藝復興三傑 ｜ 西方雕塑史的不朽神聖巨匠",
        "work_name": "《大衛像》 (David)",
        "image": "https://wsrv.nl/?url=upload.wikimedia.org/wikipedia/commons/thumb/8/80/Michelangelo%27s_David_-_waist_up.jpg/640px-Michelangelo%27s_David_-_waist_up.jpg",
        "color": "#E2E8F0", "frame": "#475569", "icon": "🗿",
        "quote": "「我看見天使在巨石裡，我雕刻直到使他重獲自由。」",
        "extract": (
            "### 📌 雕刻家的靈魂與對石材的虔誠\n\n"
            "米開朗基羅出生於卡普雷塞，深受佛羅倫斯美第奇家族的人文主義薰陶。他畢生自視為「純粹的雕刻家」，認為雕刻的真諦不是塑造形體，而是將隱藏並禁錮在沉重冷硬大理石中的靈魂釋放出來。他對人體結構與肌肉張力的掌握達到神聖無比的高度。\n\n"
            "### 🗿 雄渾震撼的英雄人體美學\n\n"
            "米開朗基羅的作品充滿了強大的男性力量美感與緊繃的內在張力（Terribilità）。在教皇朱利奧二世的委託下，他歷時四年仰頭在西斯汀禮拜堂天頂獨力創作出宏偉的《創世紀》濕壁畫，將神性創生與人類痛苦抗爭的龐大場面展現得淋漓盡致；其晚年設計的聖伯多祿大殿圓頂更奠定歐洲巴洛克與古典建築的典範。\n\n"
            "### 🏛️ 西方雕塑的極致象徵\n\n"
            "他將人體的解剖力學與靈魂深處的悲劇命運完美結合，被同時代人尊稱為「神聖的米開朗基羅（Il Divino）」，對西方美術史產生了無可撼動的深遠影響。"
        ),
        "representative": (
            "* **《大衛像》 (David, 1501–1504)**：文藝復興雕塑的絕對代表作，高達5公尺，精準捕捉迎戰巨人歌利亞前蓄勢待發的堅定眼神與肌理。\n\n"
            "* **《聖殤》 (Pietà, 1498–1499)**：聖伯多祿大殿鎮館之寶，以極致優雅的大理石褶皺展現聖母哀悼耶穌的靜謐與悲憫。\n\n"
            "* **《創世紀：創造亞當》 (1508–1512)**：西斯汀禮拜堂天頂壁畫核心，上帝與亞當即將觸碰的食指成為西方文明最具標誌性的構圖。\n\n"
            "* **《最後的審判》 (1536–1541)**：龐大宏偉的祭壇壁畫，以翻騰糾結的裸體群像刻劃末日審判的壯烈震撼。"
        ),
        "link": "https://zh.wikipedia.org/wiki/米开朗基罗"
    },
    "莫內": {
        "title": "克勞德·莫內 (Claude Monet)",
        "period": "印象派奠基人 (1840–1926)",
        "category": "油畫 / 外光派印象主義",
        "identity": "印象派之父 ｜ 追逐光影與剎那時間的色彩魔法師",
        "work_name": "《睡蓮》 (Water Lilies)",
        "image": "https://wsrv.nl/?url=upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Claude_Monet_-_Water_Lilies_-_Google_Art_Project.jpg/640px-Claude_Monet_-_Water_Lilies_-_Google_Art_Project.jpg",
        "color": "#60A5FA", "frame": "#1D4ED8", "icon": "🌸",
        "quote": "「世上沒有固定不變的色彩，只有特定瞬間的光線折射。」",
        "extract": (
            "### 📌 外光寫生革命與印象派誕生\n\n"
            "莫內出生於巴黎，自幼展露過人素描天賦，後師從尤金·布丹走出畫室，進入戶外大自然從事「外光寫生（En plein air）」。1874年，莫內與雷諾瓦等人舉辦獨立展覽，展出其名作《印象·日出》，遭受學院派保守藝評家嘲諷為「充其量不過是種模糊的印象」，這群革新者反而自豪地以「印象派」為名，正式掀起近代美術史最偉大的視覺革命。\n\n"
            "### 🎨 光影的瞬間性與連作系列\n\n"
            "莫內認為「世上沒有固定不變的色彩，只有特定瞬間的光線折射」。他突破了傳統繪畫以物體本身固有色上色的慣例，改用短促碎裂的純色筆觸直接並列在畫布上，讓色彩在觀者眼中自然混和；為研究不同光線下同一景物的細微轉變，他開創了著名的「連作」系列（如草垛、魯昂大教堂、睡蓮）。\n\n"
            "### 🌸 晚年吉維尼花園與抽象先聲\n\n"
            "晚年在吉維尼打造睡蓮水上花園，即使飽受白內障眼疾之苦，依然憑藉純粹的色彩直覺創作超大尺幅的《睡蓮》全景壁畫，消解了地平線與空間輪廓，直接啟蒙了後世的抽象表現主義。"
        ),
        "representative": (
            "* **《印象·日出》 (Impression, Sunrise, 1872)**：印象派定名之作，以迷濛晨霧與橙紅旭日顛覆傳統港口風景畫規範。\n\n"
            "* **《睡蓮》系列 (Water Lilies, 1897–1926)**：長達三十餘年對吉維尼池塘的極致凝視，橘園美術館典藏的巨幅環景壁畫名揚全球。\n\n"
            "* **《撐陽傘的女人》 (Woman with a Parasol, 1875)**：仰角捕捉妻子與兒子漫步草坡，微風與陽光在衣褶上流動的瞬間。\n\n"
            "* **《魯昂大教堂》系列 (1892–1894)**：連續記錄同一教堂正門在清晨、正午、黃昏等不同天氣下的光影熔鑄奇景。"
        ),
        "link": "https://zh.wikipedia.org/wiki/克洛德·莫奈"
    },
    "畢卡索": {
        "title": "巴勃羅·畢卡索 (Pablo Picasso)",
        "period": "現代立體派 (1881–1973)",
        "category": "油畫 / 拼貼 / 雕塑 / 現代主義",
        "identity": "立體主義創始人 ｜ 20世紀現代藝術最多產的天才巨擘",
        "work_name": "《格爾尼卡》 (Guernica)",
        "image": "https://wsrv.nl/?url=upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Guernica_reproduction_at_the_UN.jpg/640px-Guernica_reproduction_at_the_UN.jpg",
        "color": "#F472B6", "frame": "#BE185D", "icon": "🧩",
        "quote": "「每個孩子都是藝術家，問題在於長大後如何保持。」",
        "extract": (
            "### 📌 神童早慧與風格變奏\n\n"
            "畢卡索出生於西班牙馬拉加，自幼便展現驚人的古典寫實技藝，號稱「十多歲便畫得像拉斐爾一樣」。然而他隨後前往巴黎，歷經憂傷冷冽的「藍色時期」與溫馨浪漫的「粉紅時期」，不斷主動打碎已建立的成就，尋找全新的視覺表現途徑。\n\n"
            "### 🧩 立體主義革命：打破單一視角\n\n"
            "受到非洲原始木雕的純樸力量啟發，畢卡索在1907年創作出震驚藝壇的《亞維農的少女》，徹底打破自文藝復興以來統治西方五百年的單一焦點透視法。他將三度空間的物體解構、切碎、旋轉，並將正面與側面的視角同時壓縮並置在同一二維畫布上，與布拉克共同創立了影響整個現代藝術脈絡的「立體主義（Cubism）」。\n\n"
            "### 🕊️ 人文關懷與永恆傳奇\n\n"
            "畢卡索一生創作了上萬件作品，橫跨油畫、陶藝、拼貼與雕塑。他更以強烈的反戰精神創作出震撼世紀的《格爾尼卡》，抗議法西斯轟炸平民，展現藝術家作為時代良心的力量。"
        ),
        "representative": (
            "* **《格爾尼卡》 (Guernica, 1937)**：黑白灰純色調鋪陳的史詩級反戰名作，描繪西班牙內戰平民與動物慘遭轟炸的巨大悲鳴。\n\n"
            "* **《亞維農的少女》 (Les Demoiselles d'Avignon, 1907)**：立體主義開山之作，紐約現代藝術博物館鎮館之寶。\n\n"
            "* **《哭泣的女人》 (The Weeping Woman, 1937)**：以鋒利的立體色塊解構痛苦女性臉龐，展現深刻的精神崩潰感。\n\n"
            "* **《盲人的晚餐》 (1903)**：早期「藍色時期」代表作，呈現社會邊緣底層人物的蒼涼孤苦。"
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
    st.caption("數位像素美術館 ｜ 互動探索系統")
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
    * **未搜尋**：停留於接待大廳休憩。
    * **搜尋人名後**：系統只會開放**該名家的專屬展廳大門**，小人直接走向該門參觀！
    * **操作鍵位**：`↑` `↓` `←` `→` 或 `W / A / S / D` 移動；按 `空白鍵` 查看真跡大圖與名言。
    """)

# 5. 主標題樣式
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
        background: linear-gradient(135deg, #E0F7FA 0%, #29B6F6 40%, #0288D1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 4px 20px rgba(41, 182, 246, 0.35);
    }
    .custom-subtitle {
        font-family: 'Noto Serif TC', 'PingFang TC', 'Microsoft JhengHei', serif;
        font-size: 1.1rem;
        color: #B0BEC5;
        letter-spacing: 1.5px;
        margin-bottom: 1.2rem;
    }
    .cyan-accent { color: #29B6F6; font-weight: bold; }

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
        color: #64B5F6 !important;
        margin-top: 1.4rem !important;
        margin-bottom: 0.7rem !important;
    }
</style>

<div class="custom-main-title">跨時代全球藝術家作品與生命歷程互動圖譜</div>
<div class="custom-subtitle">痕跡與靈魂 <span class="cyan-accent">｜</span> 結合像素互動探索與多維生命脈絡之開放藝術平台</div>
""", unsafe_allow_html=True)

# 6. 搜尋與標籤區
col_search, col_tags = st.columns([2, 3])

with col_search:
    user_input = st.text_input(
        "🔍 搜尋藝術家（搜尋後只開放該名家專屬大門）：",
        value=st.session_state.current_artist,
        placeholder="請輸入藝術家姓名（例如：梵谷、達文西、米開朗基羅...）"
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

if is_in_gallery and not target_artist_data:
    target_artist_data = {
        "matched_name": current_query,
        "title": f"【{current_query}】主題特展",
        "period": "全球特展策劃中",
        "category": "跨媒材藝術創作",
        "identity": "當前特展焦點藝術家",
        "work_name": f"《{current_query} 特展創作》",
        "image": "https://wsrv.nl/?url=upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/640px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg",
        "color": "#A855F7",
        "frame": "#6B21A8",
        "icon": "✨",
        "quote": f"「為您特別開放：【{current_query}】專屬展門已就緒。」",
        "representative": "外部開放資料庫即時索引中",
        "extract": "系統正透過外部開放資料節點進行語義解析中...",
        "link": "https://zh.wikipedia.org"
    }

exhibit_json = json.dumps(target_artist_data, ensure_ascii=False) if target_artist_data else "{}"
mode_str = "gallery" if is_in_gallery else "lobby"

col_game, col_info = st.columns([3, 2], gap="large")

with col_game:
    if is_in_gallery:
        st.subheader(f"🕹️ 【{target_artist_data['matched_name']}】專屬展廳大門")
        st.caption("走進正前方專屬展位，按下【空白鍵 (Space)】欣賞該藝術家傳世真跡大圖！")
    else:
        st.subheader("🛋️ 美術館接待大廳 (Grand Entrance Lobby)")
        st.caption("小人目前在接待大廳中；請於上方搜尋或點選名家標籤以開啟專屬展廊！")

    pixel_game_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: #0B0F19;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden;
            user-select: none;
        }}
        #game-box {{
            position: relative;
            width: 660px;
            height: 520px;
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.9), 0 0 20px rgba(41, 182, 246, 0.3);
            border: 3px solid #1E293B;
            border-radius: 10px;
            overflow: hidden;
            background: #0F172A;
        }}
        canvas {{
            display: block;
            image-rendering: pixelated;
        }}
        #guide-bar {{
            position: absolute;
            top: 12px;
            left: 12px;
            background: rgba(15, 23, 42, 0.92);
            color: #38BDF8;
            padding: 6px 14px;
            border-radius: 6px;
            font-size: 12px;
            border: 1px solid #0284C7;
            pointer-events: none;
            letter-spacing: 0.5px;
        }}
        #interact-prompt {{
            position: absolute;
            display: none;
            color: #FACC15;
            background: rgba(15, 23, 42, 0.95);
            border: 1.5px solid #F59E0B;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            pointer-events: none;
            transform: translate(-50%, -100%);
            white-space: nowrap;
            box-shadow: 0 4px 12px rgba(0,0,0,0.6);
            animation: bounce 0.8s infinite alternate;
        }}
        @keyframes bounce {{
            from {{ margin-top: 0px; }}
            to {{ margin-top: -6px; }}
        }}
        /* 真實代表作彈跳卡片（左側真跡圖片 + 右側資訊） */
        #rpg-modal {{
            position: absolute;
            top: 52%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 550px;
            background: linear-gradient(145deg, #0F172A 0%, #1E293B 100%);
            border: 2px solid #38BDF8;
            box-shadow: 0 18px 45px rgba(0,0,0,0.9), 0 0 25px rgba(56, 189, 248, 0.4);
            border-radius: 12px;
            padding: 18px 20px;
            display: none;
            z-index: 100;
            color: #F8FAFC;
        }}
        .modal-body {{
            display: flex;
            gap: 16px;
            align-items: center;
        }}
        .modal-img-box {{
            flex: 0 0 190px;
            height: 230px;
            border-radius: 8px;
            overflow: hidden;
            border: 2px solid #475569;
            background: #000;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.6);
        }}
        .modal-img-box img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }}
        .modal-info {{
            flex: 1;
        }}
        .modal-info h3 {{
            margin: 0 0 4px 0;
            color: #38BDF8;
            font-size: 18px;
        }}
        .period-tag {{
            display: inline-block;
            background: #0369A1;
            color: #E0F2FE;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 11px;
            margin-bottom: 8px;
        }}
        .quote {{
            font-style: italic;
            color: #CBD5E1;
            font-size: 12.5px;
            line-height: 1.45;
            background: rgba(0, 0, 0, 0.35);
            border-left: 3px solid #F59E0B;
            padding: 6px 10px;
            margin: 6px 0 8px 0;
            border-radius: 0 4px 4px 0;
        }}
        .meta-list {{
            font-size: 12px;
            color: #94A3B8;
            line-height: 1.5;
        }}
        .close-hint {{
            margin-top: 10px;
            text-align: right;
            font-size: 11px;
            color: #64748B;
        }}
    </style>
    </head>
    <body>

    <div id="game-box">
        <canvas id="gameCanvas" width="660" height="520"></canvas>
        <div id="guide-bar">🚶 [WASD / 方向鍵] 移動</div>
        <div id="interact-prompt">❗ [空白鍵] 鑑賞代表作真跡</div>

        <div id="rpg-modal">
            <div class="modal-body">
                <div class="modal-img-box">
                    <img id="modal-img" src="" alt="真實代表作真跡">
                </div>
                <div class="modal-info">
                    <h3 id="modal-title">🎨 作品名稱</h3>
                    <span class="period-tag" id="modal-period">時代時期</span>
                    <div class="quote" id="modal-quote">經典名言</div>
                    <div class="meta-list" id="modal-meta">代表作列表</div>
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
        guide.innerHTML = `🚶 [WASD/方向鍵] 移動 ｜ 前方為【${{currentArtist.matched_name}}】專屬展門`;
    }} else {{
        guide.innerHTML = `🛋️ 接待大廳漫步 ｜ 請於上方搜尋或點選標籤開啟展門`;
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

    function toggleModal() {{
        if (isModalOpen) {{
            modal.style.display = 'none';
            isModalOpen = false;
        }} else {{
            document.getElementById('modal-title').innerHTML = `${{currentArtist.icon}} ${{currentArtist.work_name}}`;
            document.getElementById('modal-period').innerText = `【${{currentArtist.matched_name}}】${{currentArtist.period}}`;
            document.getElementById('modal-quote').innerText = currentArtist.quote;
            document.getElementById('modal-meta').innerHTML = `<b>代表作：</b>${{currentArtist.work_name}}<br><span style="color:#38BDF8; font-weight:bold; margin-top:4px; display:inline-block;">👉 右側已同步載入深度生平與完整傳世解析</span>`;
            
            // 透過無防盜鏈限制之開源 CDN 直發真實名作
            document.getElementById('modal-img').src = currentArtist.image;
            
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

    function drawLobby() {{
        ctx.fillStyle = '#0F172A';
        ctx.fillRect(0, 0, canvas.width, 160);

        ctx.fillStyle = '#1E293B';
        ctx.fillRect(0, 0, canvas.width, 18);
        ctx.fillStyle = '#334155';
        ctx.fillRect(0, 156, canvas.width, 4);

        const tileSize = 44;
        for (let x = 0; x < canvas.width; x += tileSize) {{
            for (let y = 160; y < canvas.height; y += tileSize) {{
                ctx.fillStyle = ((x / tileSize + y / tileSize) % 2 === 0) ? '#1E2433' : '#151A24';
                ctx.fillRect(x, y, tileSize, tileSize);
            }}
        }}

        ctx.fillStyle = '#78350F';
        ctx.fillRect(230, 80, 200, 48);
        ctx.fillStyle = '#B45309';
        ctx.fillRect(226, 76, 208, 10);
        ctx.fillStyle = '#FEF3C7';
        ctx.font = 'bold 13px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('🏛️ 美術館接待諮詢處', 330, 108);

        ctx.fillStyle = '#166534';
        ctx.beginPath();
        ctx.arc(80, 130, 24, 0, Math.PI * 2);
        ctx.arc(580, 130, 24, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#78350F';
        ctx.fillRect(70, 130, 20, 25);
        ctx.fillRect(570, 130, 20, 25);

        ctx.fillStyle = '#991B1B';
        ctx.fillRect(80, 260, 40, 90);
        ctx.fillRect(540, 260, 40, 90);

        ctx.fillStyle = 'rgba(2, 132, 199, 0.25)';
        ctx.fillRect(280, 160, 100, canvas.height - 160);

        ctx.fillStyle = '#38BDF8';
        ctx.font = 'bold 15px sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('✨ 請於上方輸入藝術家姓名，或點選名家標籤開啟專屬展門 ✨', 330, 220);
        ctx.fillStyle = '#94A3B8';
        ctx.font = '12px sans-serif';
        ctx.fillText('（小人目前在大廳休息，選定後將開啟該藝術家的單一專屬展廳）', 330, 245);
    }}

    function drawGallery() {{
        ctx.fillStyle = '#0F172A';
        ctx.fillRect(0, 0, canvas.width, 130);

        ctx.fillStyle = '#1E293B';
        ctx.fillRect(0, 0, canvas.width, 14);
        ctx.fillStyle = '#334155';
        ctx.fillRect(0, 126, canvas.width, 6);

        const tileSize = 40;
        for (let x = 0; x < canvas.width; x += tileSize) {{
            for (let y = 132; y < canvas.height; y += tileSize) {{
                ctx.fillStyle = ((x / tileSize + y / tileSize) % 2 === 0) ? '#1A202C' : '#141822';
                ctx.fillRect(x, y, tileSize, tileSize);
            }}
        }}

        const carpetW = 120;
        const carpetX = (canvas.width - carpetW) / 2;
        ctx.fillStyle = '#881337';
        ctx.fillRect(carpetX, 132, carpetW, canvas.height - 132);

        ctx.fillStyle = '#D97706';
        ctx.fillRect(carpetX - 2, 132, 2, canvas.height - 132);
        ctx.fillRect(carpetX + carpetW, 132, 2, canvas.height - 132);

        ctx.fillStyle = 'rgba(250, 204, 21, 0.28)';
        ctx.beginPath();
        ctx.arc(330, 85, 75, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#78350F';
        ctx.fillRect(singleDoor.x, singleDoor.y, singleDoor.w, singleDoor.h);
        ctx.fillStyle = '#D97706';
        ctx.fillRect(singleDoor.x - 4, singleDoor.y - 4, singleDoor.w + 8, 8);

        ctx.fillStyle = currentArtist.color || '#38BDF8';
        ctx.fillRect(singleDoor.x + 8, singleDoor.y + 12, singleDoor.w - 16, singleDoor.h - 12);

        ctx.font = '34px Arial';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(currentArtist.icon || '🎨', 330, singleDoor.y + 45);

        ctx.fillStyle = '#B45309';
        ctx.fillRect(singleDoor.x - 14, singleDoor.y + singleDoor.h + 8, singleDoor.w + 28, 26);
        ctx.fillStyle = '#FEF3C7';
        ctx.font = 'bold 13px sans-serif';
        ctx.fillText(`【${{currentArtist.matched_name}}】展廳門`, 330, singleDoor.y + singleDoor.h + 24);
    }}

    function drawPlayer() {{
        ctx.fillStyle = 'rgba(0, 0, 0, 0.45)';
        ctx.beginPath();
        ctx.ellipse(player.x, player.y + 10, 10, 5, 0, 0, Math.PI * 2);
        ctx.fill();

        const bob = Math.sin(player.walkFrame) * 2;

        ctx.fillStyle = '#0284C7';
        ctx.fillRect(player.x - 7, player.y - 4 + bob, 14, 13);

        ctx.fillStyle = '#FED7AA';
        ctx.fillRect(player.x - 6, player.y - 15 + bob, 12, 11);

        ctx.fillStyle = '#D97706';
        ctx.fillRect(player.x - 8, player.y - 19 + bob, 16, 5);
        ctx.fillRect(player.x - 5, player.y - 23 + bob, 10, 5);

        ctx.fillStyle = '#0F172A';
        if (player.dir === 'down') {{
            ctx.fillRect(player.x - 4, player.y - 11 + bob, 2, 3);
            ctx.fillRect(player.x + 2, player.y - 11 + bob, 2, 3);
        }} else if (player.dir === 'left') {{
            ctx.fillRect(player.x - 5, player.y - 11 + bob, 2, 3);
        }} else if (player.dir === 'right') {{
            ctx.fillRect(player.x + 3, player.y - 11 + bob, 2, 3);
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

# 8. 右側資訊卡片
with col_info:
    if is_in_gallery and target_artist_data:
        st.subheader("📖 藝術家脈絡與作品檔案")
        st.markdown(f"## {target_artist_data['title']}")
        st.info(f"🏷️ **身份地位：** {target_artist_data['identity']}")
        
        tab1, tab2 = st.tabs(["📜 深度生命脈絡與藝術轉折", "🖼️ 核心傳世代表作解析"])
        with tab1:
            st.markdown(target_artist_data["extract"])
            st.markdown(f"[🔗 前往維基百科閱讀權威典藏文獻]({target_artist_data['link']})")
        with tab2:
            st.image(target_artist_data["image"], caption=f"{target_artist_data['title']} 代表作：{target_artist_data['work_name']}", use_container_width=True)
            st.markdown(target_artist_data["representative"])
            st.divider()
            st.markdown(f"""
            ⏳ **活躍年代：** {target_artist_data['period']}  
            🎨 **主要媒材：** {target_artist_data.get('category', '油畫 / 雕塑')}
            """)
    else:
        st.subheader("🏛️ 美術館迎賓服務處")
        st.markdown("""
        ### 歡迎光臨數位像素美術館！
        本館典藏文藝復興、印象派至現代主義之劃時代藝術大師與雕塑家。
        
        #### 🎫 參觀動線說明：
        1. **領取展覽門票**：請於上方 **「搜尋藝術家」** 輸入人名，或直接點選 **「熱門名家標籤」**。
        2. **啟程漫遊專屬展廳**：領取門票後，左側畫面將只為您開啟該藝術家的**唯一專屬展廊大門**！
        3. **深度互動鑑賞**：操縱小人走至展門正前方並按下 **【空白鍵 (Space)】**，即可欣賞代表作真跡並同步解鎖其生平脈絡。
        """)
        st.info("💡 試著點擊上方標籤「**達文西**」、「**梵谷**」或「**米開朗基羅**」，立即開啟獨立專屬展廳！")
