import streamlit as st
import streamlit.components.v1 as components

# 1. 頁面全域設定：啟用寬版全螢幕模式
st.set_page_config(
    page_title="跨時代全球藝術家作品與生命歷程互動圖譜",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 結構化深度全球藝術家與雕塑家資料庫
ARTISTS_DATABASE = {
    "梵谷": {
        "title": "文森·梵谷 (Vincent van Gogh)",
        "period": "後印象派 (1853–1890)",
        "category": "油畫 / 後印象派表現主義",
        "identity": "現代表現主義先驅 ｜ 燃燒靈魂的悲劇巨匠",
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

# 3. 狀態管理函數
if "current_artist" not in st.session_state:
    st.session_state.current_artist = "梵谷"

def select_artist(name):
    st.session_state.current_artist = name

# 4. 側邊欄：展覽系統說明與導覽指南
with st.sidebar:
    st.title("🏛️ 策展導覽台")
    st.caption("數位像素美術館 ｜ 互動探索系統")
    
    st.divider()
    st.subheader("🎮 像素小遊戲操控")
    st.markdown("""
    * **方向鍵**（`↑` `↓` `←` `→`）或 **W / A / S / D**：控制像素小人自由移動
    * **接近展品**：走到牆上的名畫或雕像展位前
    * **互動查看**：碰觸展品時會顯示名畫資訊，點擊右方標籤可查看完整人生脈絡
    """)
    
    st.divider()
    st.subheader("📐 系統設計架構")
    st.markdown("""
    * **遊戲引擎**：HTML5 Canvas 2D 像素渲染
    * **知識架構**：開放藝術歷史語義圖譜
    * **UI 框架**：Streamlit 響應式佈局
    """)

# 5. 主頁面：自訂藝術風格標題與字級樣式
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@600;900&display=swap');

    .custom-main-title {
        font-family: 'Noto Serif TC', 'PingFang TC', 'Microsoft JhengHei', serif;
        font-size: 2.8rem;
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
        font-size: 1.15rem;
        color: #B0BEC5;
        letter-spacing: 1.5px;
        margin-bottom: 1.2rem;
    }
    
    .cyan-accent {
        color: #29B6F6;
        font-weight: bold;
    }

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

# 6. 主頁面：搜尋輸入區與熱門名家標籤
col_search, col_tags = st.columns([2, 3])

with col_search:
    user_input = st.text_input(
        "🔍 搜尋藝術家（支援中英文）：",
        value=st.session_state.current_artist,
        placeholder="例如：梵谷、達文西、米開朗基羅、莫內..."
    )
    if user_input != st.session_state.current_artist:
        st.session_state.current_artist = user_input

with col_tags:
    st.write("✨ **熱門名家標籤：**")
    tag_cols = st.columns(len(ARTISTS_DATABASE))
    for i, name in enumerate(ARTISTS_DATABASE.keys()):
        if tag_cols[i].button(name, key=f"tag_btn_{name}", use_container_width=True):
            select_artist(name)
            st.rerun()

st.markdown("---")

# 7. 主視覺展示：左側像素美術館小遊戲；右側藝術家檔案
col_game, col_info = st.columns([3, 2], gap="large")

with col_game:
    st.subheader("🕹️ 像素時空美術館 (Pixel Art Museum)")
    st.caption("點擊下方遊戲畫面獲取焦點，使用 方向鍵 或 W/A/S/D 漫步參觀展廳！")

    # 內嵌 HTML5 Canvas 像素遊戲
    pixel_game_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #0E1117;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Courier New', Courier, monospace;
            overflow: hidden;
            user-select: none;
        }
        #game-container {
            position: relative;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.8), 0 0 15px rgba(41, 182, 246, 0.4);
            border: 3px solid #1E293B;
            border-radius: 8px;
            overflow: hidden;
        }
        canvas {
            display: block;
            image-rendering: pixelated;
        }
        #hud {
            position: absolute;
            top: 10px;
            left: 10px;
            background: rgba(15, 23, 42, 0.85);
            color: #38BDF8;
            padding: 6px 14px;
            border-radius: 4px;
            font-size: 13px;
            border: 1px solid #38BDF8;
            letter-spacing: 1px;
            pointer-events: none;
        }
        #dialog {
            position: absolute;
            bottom: 12px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(15, 23, 42, 0.95);
            color: #F8FAFC;
            padding: 10px 20px;
            border-radius: 6px;
            font-size: 14px;
            border: 2px solid #F59E0B;
            display: none;
            box-shadow: 0 4px 15px rgba(0,0,0,0.6);
            text-align: center;
            white-space: nowrap;
        }
    </style>
    </head>
    <body>

    <div id="game-container">
        <canvas id="canvas" width="600" height="540"></canvas>
        <div id="hud">🚶 鍵盤 [↑↓←→] 或 [WASD] 移動探索</div>
        <div id="dialog">💡 走近展品觸發對話</div>
    </div>

    <script>
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');
    const dialog = document.getElementById('dialog');

    // 玩家像素小人
    const player = {
        x: 300,
        y: 420,
        size: 20,
        speed: 3.5,
        color: '#38BDF8',
        dir: 'down'
    };

    // 展廳中的展品節點（對應五大名家）
    const exhibits = [
        { name: "梵谷", title: "《星夜》展位", color: "#FBBF24", frameColor: "#B45309", x: 100, y: 100, w: 50, h: 60, icon: "🌌" },
        { name: "達文西", title: "《蒙娜麗莎》展位", color: "#34D399", frameColor: "#047857", x: 230, y: 90, w: 50, h: 60, icon: "🖼️" },
        { name: "米開朗基羅", title: "《大衛像》展位", color: "#E2E8F0", frameColor: "#64748B", x: 370, y: 90, w: 46, h: 70, icon: "🗿" },
        { name: "莫內", title: "《睡蓮》展位", color: "#60A5FA", frameColor: "#1D4ED8", x: 500, y: 100, w: 50, h: 60, icon: "🌸" },
        { name: "畢卡索", title: "《格爾尼卡》立體展位", color: "#F472B6", frameColor: "#BE185D", x: 290, y: 250, w: 60, h: 50, icon: "🧩" }
    ];

    const keys = {};

    window.addEventListener('keydown', (e) => {
        if(["ArrowUp","ArrowDown","ArrowLeft","ArrowRight"," "].includes(e.key)) {
            e.preventDefault();
        }
        keys[e.key.toLowerCase()] = true;
    });

    window.addEventListener('keyup', (e) => {
        keys[e.key.toLowerCase()] = false;
    });

    function update() {
        if (keys['arrowup'] || keys['w']) { player.y -= player.speed; player.dir = 'up'; }
        if (keys['arrowdown'] || keys['s']) { player.y += player.speed; player.dir = 'down'; }
        if (keys['arrowleft'] || keys['a']) { player.x -= player.speed; player.dir = 'left'; }
        if (keys['arrowright'] || keys['d']) { player.x += player.speed; player.dir = 'right'; }

        // 牆壁碰撞邊界
        player.x = Math.max(35, Math.min(canvas.width - 35, player.x));
        player.y = Math.max(160, Math.min(canvas.height - 40, player.y));

        // 偵測是否走到展品附近
        let nearExhibit = null;
        for (let ex of exhibits) {
            let dist = Math.hypot((player.x) - (ex.x + ex.w / 2), (player.y) - (ex.y + ex.h / 2));
            if (dist < 55) {
                nearExhibit = ex;
                break;
            }
        }

        if (nearExhibit) {
            dialog.style.display = 'block';
            dialog.innerHTML = `✨ 正在欣賞：<b>【${nearExhibit.name}】${nearExhibit.title}</b><br><span style="color:#94A3B8; font-size:12px;">👉 點擊右側標籤可檢索生平與傳世全集</span>`;
        } else {
            dialog.style.display = 'none';
        }
    }

    function drawFloor() {
        // 復古方格地板
        const tileSize = 40;
        for (let x = 0; x < canvas.width; x += tileSize) {
            for (let y = 140; y < canvas.height; y += tileSize) {
                ctx.fillStyle = ((x / tileSize + y / tileSize) % 2 === 0) ? '#1E2430' : '#171B24';
                ctx.fillRect(x, y, tileSize, tileSize);
            }
        }

        // 後牆展覽壁面
        ctx.fillStyle = '#0F172A';
        ctx.fillRect(0, 0, canvas.width, 140);

        // 踢腳線與紅地毯走道
        ctx.fillStyle = '#475569';
        ctx.fillRect(0, 136, canvas.width, 4);

        // 紅地毯走道
        ctx.fillStyle = '#991B1B';
        ctx.fillRect(260, 140, 80, canvas.height - 140);
        ctx.fillStyle = '#F59E0B';
        ctx.fillRect(258, 140, 2, canvas.height - 140);
        ctx.fillRect(340, 140, 2, canvas.height - 140);
    }

    function drawExhibits() {
        for (let ex of exhibits) {
            // 畫框陰影
            ctx.fillStyle = 'rgba(0, 0, 0, 0.4)';
            ctx.fillRect(ex.x + 4, ex.y + 4, ex.w, ex.h);

            // 畫框
            ctx.fillStyle = ex.frameColor;
            ctx.fillRect(ex.x, ex.y, ex.w, ex.h);

            // 畫布內容
            ctx.fillStyle = ex.color;
            ctx.fillRect(ex.x + 4, ex.y + 4, ex.w - 8, ex.h - 8);

            // 展品圖示
            ctx.font = '20px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(ex.icon, ex.x + ex.w / 2, ex.y + ex.h / 2);

            // 銘牌說明
            ctx.fillStyle = '#F8FAFC';
            ctx.font = 'bold 11px sans-serif';
            ctx.fillText(ex.name, ex.x + ex.w / 2, ex.y + ex.h + 14);
        }
    }

    function drawPlayer() {
        // 像素小人陰影
        ctx.fillStyle = 'rgba(0, 0, 0, 0.35)';
        ctx.beginPath();
        ctx.ellipse(player.x, player.y + 12, 10, 5, 0, 0, Math.PI * 2);
        ctx.fill();

        // 像素小人主體（復古像素風格小法師 / 探險家）
        // 身體 (披風)
        ctx.fillStyle = player.color;
        ctx.fillRect(player.x - 7, player.y - 2, 14, 14);

        // 頭部
        ctx.fillStyle = '#FDE68A';
        ctx.fillRect(player.x - 6, player.y - 14, 12, 12);

        // 帽子 / 頭飾
        ctx.fillStyle = '#1D4ED8';
        ctx.fillRect(player.x - 8, player.y - 18, 16, 5);
        ctx.fillRect(player.x - 4, player.y - 23, 8, 5);

        // 眼睛
        ctx.fillStyle = '#0F172A';
        if (player.dir === 'down') {
            ctx.fillRect(player.x - 4, player.y - 10, 2, 3);
            ctx.fillRect(player.x + 2, player.y - 10, 2, 3);
        } else if (player.dir === 'left') {
            ctx.fillRect(player.x - 5, player.y - 10, 2, 3);
        } else if (player.dir === 'right') {
            ctx.fillRect(player.x + 3, player.y - 10, 2, 3);
        }
    }

    function loop() {
        update();
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawFloor();
        drawExhibits();
        drawPlayer();
        requestAnimationFrame(loop);
    }

    loop();
    </script>
    </body>
    </html>
    """

    components.html(pixel_game_html, height=560)

with col_info:
    st.subheader("📖 藝術家脈絡與作品檔案")
    
    search_keyword = st.session_state.current_artist.strip().lower()
    target_data = None
    
    if search_keyword:
        for name, data in ARTISTS_DATABASE.items():
            if search_keyword in name.lower() or search_keyword in data["title"].lower():
                target_data = data
                break
    
    if target_data:
        st.markdown(f"## {target_data['title']}")
        st.info(f"🏷️ **身份地位：** {target_data['identity']}")
        
        tab1, tab2 = st.tabs(["📜 深度生命脈絡與藝術轉折", "🖼️ 核心傳世代表作解析"])
        with tab1:
            st.markdown(target_data["extract"])
            st.markdown(f"[🔗 前往維基百科閱讀權威典藏文獻]({target_data['link']})")
        with tab2:
            st.markdown(target_data["representative"])
            st.divider()
            st.markdown(f"""
            ⏳ **活躍年代：** {target_data['period']}  
            🎨 **主要媒材：** {target_data['category']}
            """)
    else:
        st.warning(f"目前資料庫中未直接收錄「{st.session_state.current_artist}」")
        st.markdown("""
        > **系統動態檢索機制已啟動：**  
        > 建議您點擊上方熱門名家標籤，或在左側像素小遊戲中靠近名家展位進行探索。
        """)
        
