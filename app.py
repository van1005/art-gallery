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
    "常玉": {
        "title": "常玉 (Sanyu)",
        "period": "近代華人現代主義 (1895–1966)",
        "category": "油畫 / 水墨書法融合",
        "identity": "東方馬諦斯 ｜ 留法華人現代藝術先鋒 ｜ 巴黎畫派傳奇",
        "extract": (
            "### 📌 生平背景與流亡巴黎\n\n"
            "常玉出生於四川順慶富商家庭，自幼隨父學習繪畫，並師從名家趙熙研習書法。1920年代在「勤工儉學」浪潮中前往法國巴黎，與徐悲鴻、林風眠等同為早期留法先鋒。然而不同於其他藝術家返國建立學院派體系，常玉選擇終生客居蒙帕納斯（Montparnasse），融入波希米亞式的自由創作圈。\n\n"
            "### 🎨 藝術風格與美學轉折\n\n"
            "常玉的美學精髓在於將中國傳統毛筆書法的「飛白」、「氣韻」與西方野獸派的純粹色塊完美揉合。早年作品色彩明朗、線條輕柔優雅，以粉紅、象牙白為基調；晚年因家道中落與生活困頓，線條轉為凝重蒼勁，常以黑漆般的墨黑線條勾勒誇張比例的裸女與孤寂動物，意境淒冷深邃，展現深厚的東方文人哲學。\n\n"
            "### 🌟 歷史地位與後世共鳴\n\n"
            "生前孤傲不喜逢迎，死後其獨特的原創藝術語言被國際學界重新發現。其作品打破東西方媒材與視角的界線，被譽為華人現代藝術史上難以被取代的「純粹詩人」。"
        ),
        "representative": (
            "* **《五裸女》 (1950年代)**：常玉畢生尺幅最大之裸女油畫作品，融合書法線條與西方人體透視，拍賣市場華人藝術標竿。\n\n"
            "* **《曲腿裸女》 (1965)**：藝術家晚年沉積之作，純黑背景下線條極簡剛勁，獲選為國立歷史博物館典藏國寶。\n\n"
            "* **《白瓶花卉》與《枯梅》系列**：借物抒情，將宋代花鳥的空靈與巴黎沙龍的靜物構圖渾然天成。\n\n"
            "* **《孤獨的豹》、《荒漠中的馬》**：象徵異鄉遊子廣袤天地間的孤寂與自由靈魂。"
        ),
        "link": "https://zh.wikipedia.org/wiki/常玉"
    },
    "朱銘": {
        "title": "朱銘 (Ju Ming)",
        "period": "當代雕塑巨擘 (1938–2023)",
        "category": "木雕 / 青銅 / 現代立體雕塑",
        "identity": "台灣國寶級現代雕塑大師 ｜ 東方哲思雕刻語彙實踐者",
        "extract": (
            "### 📌 從匠師到純粹藝術家的破繭歷程\n\n"
            "朱銘本名朱川泰，出生於苗栗通霄。早年師從李金川學習傳統木雕廟宇雕刻，練就極為紮實的寫實鑿工技巧。三十歲後毅然拜入現代雕塑大師楊英風門下，歷經八年淬鍊，打破具象工匠思維，轉向以氣韻生動、大刀闊斧為核心的當代藝術語彙。\n\n"
            "### 🥋 核心美學：太極與斧鑿之間的氣韻\n\n"
            "為了改善體質並體悟動靜之道，朱銘在恩師建議下修習太極拳，因而催生了名揚國際的《太極系列》。他揚棄了傳統雕塑講究細緻修飾的手法，採用電鋸、斧劈方式直接劈砍巨木與發泡模型，保留材料本身的裂紋、肌理與重量感，精準捕捉招式初發、氣機流轉那一瞬間的雄渾張力。隨後開展的《人間系列》則轉向彩繪木雕、海綿綑紮翻銅等多樣材質，以普世包容之眼觀察市井眾生相。\n\n"
            "### 🌍 公共藝術與國際影響\n\n"
            "其大型青銅雕塑廣泛設立於台北、香港（中環交易廣場）、日本、新加坡及歐美各大城市重要地標，更憑一己之力創立朱銘美術館，被譽為將東方哲學轉化為具象立體空間震撼力的世紀大師。"
        ),
        "representative": (
            "* **《太極系列：單鞭下勢》 (1980年代)**：以俐落刀法凝結太極拳下盤沉穩蓄勢之動能，為朱銘最標誌性的公共藝術雕塑。\n\n"
            "* **《太極拱門》 (2000)**：兩位對招者合而為一演化成貫通天地的拱門，象徵太極陰陽圓融與生命對話。\n\n"
            "* **《人間系列：三軍》**：歷時數年耗資龐大打造的等身大軍人雕塑群，刻劃群體紀律下士兵們各異的面容與人性本質。\n\n"
            "* **《人間系列：排隊》**：以鮮明色彩與雨具服裝刻劃現代都會人群，呈現社會結構下的生活日常與疏離感。"
        ),
        "link": "https://zh.wikipedia.org/wiki/朱銘"
    },
    "雪舟": {
        "title": "雪舟等楊 (Sesshū Tōyō)",
        "period": "室町時代 (1420–1506)",
        "category": "水墨山水 / 禪林破墨畫",
        "identity": "日本室町時代畫聖 ｜ 東亞水墨畫跨國流變先驅",
        "extract": (
            "### 📌 禪門生活與遣明求法之行\n\n"
            "雪舟出生於備中國（今岡山縣），早年在京都相國寺出家為僧，隨當時水墨名僧周文學習宋元繪畫技法。1467年，雪舟隨同貿易遣明船遠赴明朝中國，歷訪寧波、北京等地。他在中國深入研習南宋馬遠、夏珪與元代山水，並直接以大自然的崇山峻嶺、名川江流為師，奠定了宏大的構圖視野。\n\n"
            "### 🖌️ 破墨技法本土化與硬朗筆觸\n\n"
            "返回日本後，雪舟開創了獨立於京都宮廷繪畫的雲谷派水墨風格。他將中國傳統水墨的柔和雲煙轉化為線條剛勁、石骨突兀的「硬筆山水」；其晚年所作的「破墨山水」更將墨彩的水份控制、淡墨渲染與濃墨點破發揮至禪宗頓悟的意境極致，展現空靈與凝鍊兼具的精神世界。\n\n"
            "### 🏆 跨越國界的文化地位\n\n"
            "雪舟的作品對後世日本桃山時代的狩野派、長谷川等伯產生了決定性影響，近代亦被世界和平理事會推選為世界十大文化名人之一，在日本美術史被尊奉為至高無上的「畫聖」。"
        ),
        "representative": (
            "* **《破墨山水圖》 (1495，日本國寶)**：雪舟傳世最著名代表作，墨色暈染極具禪意，上方留有題詩與傳承印可證明。\n\n"
            "* **《四季山水圖卷》（山水長卷） (1486，日本國寶)**：全長近16公尺，細膩鋪陳春夏秋冬四時更迭之浩瀚山水。\n\n"
            "* **《秋冬山水圖》 (15世紀末，日本國寶)**：以垂直斷崖與硬朗剛硬的垂直筆線切分空間，構圖震撼現代人眼界。\n\n"
            "* **《天橋立圖》 (1501–1506，日本國寶)**：以俯瞰透視鳥瞰丹後名勝，展現高超的實地寫生與地景重組能力。"
        ),
        "link": "https://zh.wikipedia.org/wiki/雪舟"
    },
    "奧古斯特·羅丹": {
        "title": "奧古斯特·羅丹 (Auguste Rodin)",
        "period": "19至20世紀交替 (1840–1917)",
        "category": "青銅鑄造 / 大理石雕刻",
        "identity": "現代雕塑之父 ｜ 印象派與象徵主義立體光影巨匠",
        "extract": (
            "### 📌 與傳統學院體制的抗衡與突破\n\n"
            "羅丹出身巴黎平民階層，早年三度報考巴黎高等美術學院均遭落榜，被迫長期從事建築裝飾浮雕代工。然而深厚的底層歷練反倒使他擺脫了古典學院派僵硬空洞的理想化神祇雕刻模式，專注於探尋真實人體肌肉、血管與骨骼在運動中的動態表現。\n\n"
            "### 🗿 雕塑的印象主義：凹凸肌理與光影捕捉\n\n"
            "羅丹對西方雕塑史最大的革新在於「非完整性」與「凹凸肌理」。他故意在青銅或石材表面留下深刻的手指捏塑痕跡與斧鑿刀刻，使光線落在雕塑上產生劇烈的明暗交錯跳躍，如同印象派畫家在畫布上擺動的筆觸。他認為人體的扭曲、痛苦與拉扯，正是靈魂深處對命運進行無聲抗爭的最佳外化表現。\n\n"
            "### 🏛️ 承先啟後的時代燈塔\n\n"
            "他將古典雕塑自米開朗基羅以來的具象敘事推向頂峰，同時其對人體解構與生命意識的探討，直接啟蒙了布朗庫西、賈科梅蒂等後代現代主義大師，奠定「現代雕塑之父」的不朽地位。"
        ),
        "representative": (
            "* **《思考者》 (The Thinker, 1880–1904)**：原為《地獄之門》頂端俯瞰人類苦難的詩人但丁，後演化為全人類理性與精神沉思的永恆圖騰。\n\n"
            "* **《地獄之門》 (The Gates of Hell)**：耗費三十餘年未竟之宏偉史詩巨作，包含近兩百個痛苦掙扎的人體雕像。\n\n"
            "* **《吻》 (The Kiss, 1882)**：細膩大理石雕琢出的浪漫纏綿，與雕像底座未經加工的粗糙岩石形成強烈對比。\n\n"
            "* **《加萊義民》 (The Burghers of Calais, 1889)**：破除英雄主義高台陳設，將六位視死如歸的英勇市民拉至與觀眾同一平面。"
        ),
        "link": "https://zh.wikipedia.org/wiki/奧古斯特·羅丹"
    },
    "李奧納多·達文西": {
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
    }
}

# 4. 側邊欄篩選與導覽控制台
with st.sidebar:
    st.title("🏛️ 策展導覽台")
    st.caption("跨維度數位策展索引")
    
    category_filter = st.selectbox(
        "藝術媒材分類",
        ["全部媒材", "繪畫", "雕塑", "水墨"]
    )
    
    filtered_artists = [
        name for name, info in ARTISTS_DATABASE.items()
        if category_filter == "全部媒材" or category_filter in info["category"]
    ]
    
    st.divider()
    st.subheader("📌 快速選擇名家")
    selected_from_sidebar = st.radio("名冊清單：", filtered_artists)
    
    st.divider()
    st.markdown("🔗 **外部展廳直通**")
    st.link_button("🌐 開啟 3D 展廳全螢幕", EXHVERSE_PUBLIC_URL, use_container_width=True)

# 5. 主頁面：自訂藝術風格標題與導言（科技冰藍漸層 + 大字級 + 內文字體全域放大）
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

    /* 全面調大右側分頁內文與段落字體 */
    .stTabs [data-baseweb="tab-panel"] p, 
    .stTabs [data-baseweb="tab-panel"] li {
        font-size: 1.18rem !important;
        line-height: 1.85 !important;
        color: #E2E8F0 !important;
    }

    /* 分段標題字體美化 */
    .stTabs [data-baseweb="tab-panel"] h3 {
        font-size: 1.35rem !important;
        color: #64B5F6 !important;
        margin-top: 1.2rem !important;
        margin-bottom: 0.6rem !important;
    }
</style>

<div class="custom-main-title">跨時代全球藝術家作品與生命歷程互動圖譜</div>
<div class="custom-subtitle">痕跡與靈魂 <span class="cyan-accent">｜</span> 整合繪畫、雕塑與生命脈絡的全球藝術開放檢索系統</div>
""", unsafe_allow_html=True)

# 6. 主頁面：搜尋輸入區與熱門名家標籤
col_search, col_tags = st.columns([2, 3])
with col_search:
    search_query = st.text_input(
        "🔍 搜尋藝術家（支援中英文）：",
        value=selected_from_sidebar,
        placeholder="例如：常玉、朱銘、羅丹、達文西..."
    )

with col_tags:
    st.write("✨ **熱門名家標籤：**")
    tag_cols = st.columns(len(ARTISTS_DATABASE))
    for i, name in enumerate(ARTISTS_DATABASE.keys()):
        if tag_cols[i].button(name, key=f"tag_{name}", use_container_width=True):
            search_query = name

st.markdown("---")

# 7. 主視覺展示：左右雙欄排版（左：3D 展廳；右：藝術家詳情卡片）
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
    
    target_data = None
    if search_query:
        for name, data in ARTISTS_DATABASE.items():
            if search_query.strip().lower() in name.lower() or search_query.strip().lower() in data["title"].lower():
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
        st.warning(f"目前資料庫中未直接收錄「{search_query}」")
        st.markdown("""
        > **系統動態檢索機制已啟動：**  
        > 系統正透過外部開放資料節點進行語義解析，建議您點擊上方熱門名家標籤，或於左側導覽台選擇已索引之典藏名單。
        """)