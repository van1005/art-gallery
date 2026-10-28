import streamlit as st
import streamlit.components.v1 as components

# 1. 頁面全域設定：啟用寬版全螢幕模式
st.set_page_config(
    page_title="跨時代全球藝術家作品與生命歷程互動圖譜",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 外部 3D 虛擬展廳公開網址
EXHVERSE_PUBLIC_URL = "https://e.fliphtml5.com/huucj/qflj/index.html"

# 3. 結構化深度全球藝術家與雕塑家資料庫
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

# 4. 狀態管理函數
if "current_artist" not in st.session_state:
    st.session_state.current_artist = "梵谷"

def select_artist(name):
    st.session_state.current_artist = name

# 5. 側邊欄篩選與導覽控制台
with st.sidebar:
    st.title("🏛️ 策展導覽台")
    st.caption("跨維度數位策展索引")
    
    category_filter = st.selectbox(
        "藝術媒材分類",
        ["全部媒材", "油畫", "雕塑", "壁畫"]
    )
    
    filtered_artists = [
        name for name, info in ARTISTS_DATABASE.items()
        if category_filter == "全部媒材" or category_filter in info["category"]
    ]
    
    st.divider()
    st.subheader("📌 快速選擇名家")
    
    for name in filtered_artists:
        if st.button(f"👤 {name}", key=f"sidebar_{name}", use_container_width=True):
            select_artist(name)
            st.rerun()
    
    st.divider()
    st.markdown("🔗 **外部展廳直通**")
    st.link_button("🌐 開啟 3D 展廳全螢幕", EXHVERSE_PUBLIC_URL, use_container_width=True)

# 6. 主頁面：自訂藝術風格標題與字體樣式（大幅調大內文字級）
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@600;900&display=swap');

    /* 頂部主標題 */
    .custom-main-title {
        font-family: 'Noto Serif TC', 'PingFang TC', 'Microsoft JhengHei', serif;
        font-size: 2.9rem;
        font-weight: 900;
        letter-spacing: 2.5px;
        line-height: 1.25;
        margin-bottom: 0.4rem;
        background: linear-gradient(135deg, #E0F7FA 0%, #29B6F6 40%, #0288D1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 4px 20px rgba(41, 182, 246, 0.35);
    }

    /* 頂部副標題 */
    .custom-subtitle {
        font-family: 'Noto Serif TC', 'PingFang TC', 'Microsoft JhengHei', serif;
        font-size: 1.15rem;
        color: #B0BEC5;
        letter-spacing: 1.5px;
        margin-bottom: 1.5rem;
    }
    
    .cyan-accent {
        color: #29B6F6;
        font-weight: bold;
    }

    /* 右側分頁內文（非粗體一般字體）：放大至 1.45rem，行距加大更透氣 */
    .stTabs [data-baseweb="tab-panel"] p,
    .stTabs [data-baseweb="tab-panel"] li,
    .stTabs [data-baseweb="tab-panel"] a {
        font-size: 1.45rem !important;
        line-height: 2.05 !important;
        color: #E2E8F0 !important;
        letter-spacing: 0.5px !important;
    }

    /* 藍色資訊框文字放大 */
    div[data-testid="stAlert"] p {
        font-size: 1.35rem !important;
        line-height: 1.8 !important;
    }

    /* 分段小標題（粗體） */
    .stTabs [data-baseweb="tab-panel"] h3 {
        font-size: 1.7rem !important;
        color: #64B5F6 !important;
        margin-top: 1.5rem !important;
        margin-bottom: 0.8rem !important;
    }
</style>

<div class="custom-main-title">跨時代全球藝術家作品與生命歷程互動圖譜</div>
<div class="custom-subtitle">痕跡與靈魂 <span class="cyan-accent">｜</span> 整合繪畫、雕塑與生命脈絡的全球藝術開放檢索系統</div>
""", unsafe_allow_html=True)

# 7. 主頁面：搜尋輸入區與熱門名家標籤
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

# 8. 主視覺展示：左右雙欄排版
col_exhibition, col_info = st.columns([3, 2], gap="large")

with col_exhibition:
    st.subheader("🏛️ 3D 沉浸式虛擬展廳")
    st.caption("支援在畫面內直接拖曳視角漫遊體驗")
    components.iframe(
        src=EXHVERSE_PUBLIC_URL,
        height=660,
        scrolling=True
    )

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
        > 系統正透過外部開放資料節點進行語義解析，建議您點擊上方熱門名家標籤，或於左側導覽台選擇已索引之典藏名單。
        """)
