import streamlit as st
import pandas as pd

# 設定網頁版面配置
st.set_page_config(page_title="銀行定存行銷轉換率分析儀表板", layout="wide")

# ==================== 自訂 CSS：右上角固定導覽列 ====================
st.markdown("""
    <style>
        .fixed-nav {
            position: fixed;
            top: 15px;
            right: 30px;
            z-index: 999999;
            background-color: rgba(255, 255, 255, 0.95);
            padding: 8px 15px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            display: flex;
            gap: 15px;
        }
        .fixed-nav a {
            text-decoration: none;
            color: #2b6cb0;
            font-weight: bold;
            font-size: 14px;
        }
        .fixed-nav a:hover {
            color: #3182ce;
            text-decoration: underline;
        }
    </style>

    <div class="fixed-nav">
        <a href="#section-top">🏠 頂端</a>
        <a href="#section-bg">🎯 背景</a>
        <a href="#section-insights">📈 數據圖表</a>
        <a href="#section-tree">🌳 決策樹</a>
        <a href="#section-strategy">💡 策略</a>
    </div>
""", unsafe_allow_html=True)

# ==================== 網頁主內容 ====================
st.markdown('<div id="section-top"></div>', unsafe_allow_html=True)

st.title("📊 銀行定存行銷轉換率分析與決策最佳化專案")
st.markdown("> **專案定位**：基於行為特徵與互動歷史之銀行定存轉換率分析，透過 Python 探索性數據分析（EDA）與機器學習決策樹驗證，協助金融機構解決亂槍打鳥的高成本痛點，實現精準獲客。")
st.markdown("---")

# 1. 背景與價值
st.markdown('<div id="section-bg"></div>', unsafe_allow_html=True)
st.header("🎯 一、 專案背景與商業價值")
col_bg1, col_bg2 = st.columns(2)
with col_bg1:
    st.subheader("商業痛點")
    st.write("定期存款為銀行穩健利息收入的核心來源。然而，傳統電話行銷高度依賴大量人工外撥，伴隨高昂的營運成本與資源浪費。")
with col_bg2:
    st.subheader("核心目標")
    st.success("透過資料探勘與行為分析，在行銷活動前識別高轉換潛力的客戶，將亂槍打鳥轉化為精準鎖定，大幅降低獲客成本並最大化轉換效率。")

st.markdown("---")

# 2. 四大核心洞察與圖表展示
st.markdown('<div id="section-insights"></div>', unsafe_allow_html=True)
st.header("📈 二、 核心數據洞察與視覺化圖表")

# 洞察 1：先前行銷成效
st.subheader("1. 先前行銷成效 (poutcome) 是最強預測指標")
st.success("**核心發現**：在前一次行銷活動中成功申辦的客戶，本次轉換率高達 **64.7% (n=1,511)**，遠高於其他群體。")
try:
    st.image("poutcome_chart.png", caption="Conversion Rate by Previous Campaign Outcome (Poutcome)", use_container_width=True)
except:
    st.info("💡 提示：請上傳 `poutcome_chart.png` 圖檔至 GitHub 即可顯示此圖。")

st.markdown("---")

# 洞察 2：行銷通話頻次
st.subheader("2. 活動最佳行銷通話次數為 1 至 3 通")
st.info("**核心發現**：單一活動撥打 1 至 3 通電話轉換率最高，第 4 通起邊際效益遞減，證實非以量制勝。")
try:
    st.image("campaign_chart.png", caption="Conversion Rate and Sample Size by Campaign Contact Frequency", use_container_width=True)
except:
    st.info("💡 提示：請上傳 `campaign_chart.png` 圖檔至 GitHub 即可顯示此圖。")

st.markdown("---")

# 洞察 3：黃金追蹤期
st.subheader("3. 黃金追蹤期落在 50 至 200 天")
st.warning("**核心發現**：排除從未聯絡的客戶後，成功轉換高峰高度集中在距離上次接觸 50 至 200 天內。")
try:
    st.image("pdays_chart.png", caption="Density Distribution of pdays (Excluding First-time Contacts)", use_container_width=True)
except:
    st.info("💡 提示：請上傳 `pdays_chart.png` 圖檔至 GitHub 即可顯示此圖。")

st.markdown("---")

# 洞察 4：聯絡管道
st.subheader("4. 行動電話 (cellular) 是最有效的行銷管道")
st.success("**核心發現**：行動電話樣本數高達 29,285 筆，且轉換率達 **14.9%** 表現最佳。")
try:
    st.image("contact_chart.png", caption="Conversion Rate by Contact Method", use_container_width=True)
except:
    st.info("💡 提示：請上傳 `contact_chart.png` 圖檔至 GitHub 即可顯示此圖。")

st.markdown("---")

# 3. 決策樹模型
st.markdown('<div id="section-tree"></div>', unsafe_allow_html=True)
st.header("🌳 三、 機器學習決策樹模型驗證")
st.write("透過機器學習決策樹模型，在數學上印證上述特徵切分與收斂邏輯：")
try:
    st.image("decision_tree.png", caption="銀行定存轉換率決策樹模型架構圖", use_container_width=True)
except:
    st.info("💡 提示：請上傳 `decision_tree.png` 圖檔至 GitHub 即可顯示此圖。")

st.markdown("---")

# 4. 營運策略
st.markdown('<div id="section-strategy"></div>', unsafe_allow_html=True)
st.header("💡 四、 具體營運策略與落地建議")
st.markdown("""
1. **建立 VIP 優先外撥名單（VIP Queue）**：
   * 將符合「前次行銷成功」且「無客訴紀錄」之舊客自動歸類，指派資深業務專員優先對接，確保優質體驗。
2. **導入自動化停損機制（Automated Stop-Loss）**：
   * 當同一客戶在單次活動中被拒絕達 2 次（或超過最佳通話次數），系統自動將其移出外撥名單，改由成本較低的簡訊或網銀通知跟進。
3. **客群細分與個人化行銷**：
   * 定期透過特徵工程更新標籤，依據年齡、資產分級與互動頻率，自動派送對應的溝通腳本。
""")

st.markdown("---")
st.markdown("### 🔗 專案原始碼與完整筆記")
st.markdown("[👉 點此前往 Google Colab 完整分析筆記](https://colab.research.google.com/drive/1CZVOzrgRb-PzNwHQQsQw9RfnB5_xaiKo?usp=sharing)[cite: 1]")
