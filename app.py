import streamlit as st
import pandas as pd

# 設定網頁版面配置與頁籤標題
st.set_page_config(page_title="銀行定存行銷轉換率分析專案", page_icon="🌙", layout="wide")

# ==================== 採用日系文青美學與精準對齊的 CSS ====================
st.markdown("""
    <style>
        /* 整體背景採用溫潤的米灰色 */
        .main {
            background-color: #f4f4f4;
        }

        /* 全域字體採用優雅的襯線字體 */
        html, body, [class*="css"] {
            font-family: "Noto Serif TC", serif;
            color: #4a4a4a;
        }

        /* 👑 關鍵修正：讓所有大標題在被點擊時，精準停在導覽列下方不被遮擋 */
        h2 {
            scroll-margin-top: 100px;
        }

        /* 頂部固定導覽列 (奶茶色系) */
        .fixed-nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background-color: #d9ccc3;
            padding: 15px 20px;
            display: flex;
            justify-content: center;
            gap: 30px;
            z-index: 999999;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }
        .fixed-nav a {
            text-decoration: none;
            color: #333333;
            font-weight: bold;
            font-size: 15px;
            transition: color 0.2s;
        }
        .fixed-nav a:hover {
            color: #6b4f4f;
        }

        /* 頂部 Header 風格 (柔和灰綠色) */
        .custom-header {
            background-color: #9da5a0;
            padding: 50px 20px;
            text-align: center;
            color: white;
            border-radius: 0 0 16px 16px;
            margin-top: 40px;
            margin-bottom: 40px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }
        .custom-header h1 {
            font-size: 2.3em;
            margin-bottom: 10px;
            color: white;
            font-weight: bold;
        }
        .custom-header p {
            font-size: 1.1em;
            color: #f9f9f9;
        }

        /* 白色圓角卡片式區塊容器 */
        .card-box {
            background-color: #ffffff;
            padding: 35px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.06);
            margin-bottom: 30px;
            border: 1px solid #eaeaea;
        }

        /* 區塊標題樣式 */
        h2 {
            color: #6b4f4f !important;
            font-size: 22px;
            margin-bottom: 20px;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
        }
    </style>

    <!-- 固定導覽列 -->
    <div class="fixed-nav">
        <a href="#section-top">🏠 頂端</a>
        <a href="#section-bg">商業背景</a>
        <a href="#section-data">資料概述</a>
        <a href="#section-insights">數據洞察</a>
        <a href="#section-strategy">策略與建議</a>
        <a href="#section-conclusion">結論</a>
    </div>
""", unsafe_allow_html=True)

# ==================== 網頁主內容 ====================
st.markdown('<div id="section-top"></div>', unsafe_allow_html=True)

st.markdown("""
    <div class="custom-header">
        <h1>📊 銀行定存行銷轉換率分析與決策最佳化專案</h1>
        <p>Celeste 蔡欣潔 ── 運用資料探勘與行為特徵，將行銷策略由亂槍打鳥化為精準對焦</p>
    </div>
""", unsafe_allow_html=True)

# 1. 商業背景
with st.container():
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.markdown('<h2 id="section-bg">一、 專案背景與商業價值</h2>', unsafe_allow_html=True)
    
    col_bg1, col_bg2 = st.columns(2)
    with col_bg1:
        st.subheader("商業痛點")
        st.write("定期存款為銀行穩健利息收入的核心來源。然而，傳統電話行銷高度依賴大量人工外撥，伴隨高昂的營運成本與資源浪費，缺乏精準的客戶分流機制。")
    with col_bg2:
        st.subheader("核心目標")
        st.success("透過資料探勘與行為分析，在行銷活動前識別高轉換潛力的客戶，將傳統亂槍打鳥轉化為精準鎖定，大幅降低獲客成本（CAC）並最大化轉換效率。")
    st.markdown('</div>', unsafe_allow_html=True)

# 2. 資料概述
with st.container():
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.markdown('<h2 id="section-data">二、 資料集說明</h2>', unsafe_allow_html=True)
    st.write("本專案使用葡萄牙銀行電話行銷歷史資料，特徵包含三大類：客戶基本資料、財務狀況、行銷與互動歷史。")
    st.info("💡 **重要考量**：包含 duration 可能導致資料外洩、pdays 包含特殊編碼值 (-1)、poutcome 具有高度預測力。")
    st.markdown('</div>', unsafe_allow_html=True)

# 3. 數據洞察與圖表展示
with st.container():
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.markdown('<h2 id="section-insights">三、 核心數據洞察與視覺化圖表</h2>', unsafe_allow_html=True)
    
    st.subheader("1. 先前行銷成效 (poutcome) 是最強預測指標")
    st.success("**核心發現**：在前一次行銷活動中成功申辦的客戶，本次轉換率高達 **64.7% (n=1,511)**，遠高於其他群體。")
    try:
        st.image("poutcome_chart.png", caption="依先前行銷活動結果劃分的轉換率", use_container_width=True)
    except:
        st.info("💡 提示：請將高畫質圖檔 `poutcome_chart.png` 上傳至 GitHub 倉庫中以顯示圖片。")

    st.markdown("---")

    st.subheader("2. 活動最佳行銷通話次數為 1 至 3 通")
    st.info("**核心發現**：單一活動撥打 1 至 3 通電話轉換率最高，第 4 通起邊際效益遞減，證實非以量制勝。")
    try:
        st.image("campaign_chart.png", caption="依通話頻次劃分的轉換率與樣本數", use_container_width=True)
    except:
        st.info("💡 提示：請將高畫質圖檔 `campaign_chart.png` 上傳至 GitHub 倉庫中以顯示圖片。")

    st.markdown("---")

    st.subheader("3. 黃金追蹤期落在 50 至 200 天")
    st.warning("**核心發現**：排除從未聯絡的客戶後，成功轉換高峰高度集中在距離上次接觸 50 至 200 天內。")
    try:
        st.image("pdays_chart.png", caption="黃金追蹤期 (pdays) 分佈密度圖", use_container_width=True)
    except:
        st.info("💡 提示：請將高畫質圖檔 `pdays_chart.png` 上傳至 GitHub 倉庫中以顯示圖片。")

    st.markdown("---")

    st.subheader("4. 行動電話 (cellular) 是最有效的行銷管道")
    st.success("**核心發現**：行動電話樣本數高達 29,285 筆，且轉換率達 **14.9%** 表現最佳。")
    try:
        st.image("contact_chart.png", caption="依聯絡管道劃分的轉換率", use_container_width=True)
    except:
        st.info("💡 提示：請將高畫質圖檔 `contact_chart.png` 上傳至 GitHub 倉庫中以顯示圖片。")
    
    st.markdown("---")
    st.subheader("5. 機器學習決策樹模型驗證")
    try:
        st.image("decision_tree.png", caption="銀行定存轉換率決策樹模型架構圖", use_container_width=True)
    except:
        st.info("💡 提示：請將高畫質圖檔 `decision_tree.png` 上傳至 GitHub 倉庫中以顯示圖片。")
    st.markdown('</div>', unsafe_allow_html=True)

# 4. 策略與建議
with st.container():
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.markdown('<h2 id="section-strategy">四、 具體營運策略與落地建議</h2>', unsafe_allow_html=True)
    st.markdown("""
    1. **建立 VIP 優先外撥名單（VIP Queue）**：
       * 將符合「前次行銷成功」且「無客訴紀錄」之舊客自動歸類，指派資深業務專員優先對接，確保優質體驗。
    2. **導入自動化停損機制（Automated Stop-Loss）**：
       * 當同一客戶在單次活動中被拒絕達 2 次（或超過最佳通話次數），系統自動將其移出外撥名單，改由成本較低的簡訊或網銀通知跟進。
    3. **客群細分與個人化行銷**：
       * 定期透過特徵工程更新標籤，依據年齡、資產分級與互動頻率，自動派送對應的溝通腳本。
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# 5. 結論
with st.container():
    st.markdown('<div class="card-box">', unsafe_allow_html=True)
    st.markdown('<h2 id="section-conclusion">五、 專案結論</h2>', unsafe_allow_html=True)
    st.write("本專案透過探索性數據分析證實，銀行定存行銷的成效取決於「精準鎖定高潛在舊客」與「嚴控外撥通數」，透過導入黃金追蹤期過濾與自動化停損機制，能有效解決邊際效益遞減並降低獲客成本。")
    st.markdown('</div>', unsafe_allow_html=True)

# 頁尾
st.markdown("---")
st.markdown("<div style='text-align: center; color: #7f8782; padding: 20px;'>🔗 <a href='https://colab.research.google.com/drive/1CZVOzrgRb-PzNwHQQsQw9RfnB5_xaiKo?usp=sharing' target='_blank' style='color: #6b4f4f; text-decoration: none;'>點此前往 Google Colab 完整分析筆記</a></div>", unsafe_allow_html=True)
