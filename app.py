import streamlit as st
import pandas as pd

# 設定網頁版面配置
st.set_page_config(page_title="銀行定存行銷轉換率分析", layout="wide")

# ==================== 自訂 CSS：右上角固定導覽列 ====================
st.markdown("""
    <style>
        .fixed-nav {
            position: fixed;
            top: 15px;
            right: 30px;
            z-index: 999999;
            background-color: #f4f4f4;
            padding: 8px 15px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            display: flex;
            gap: 15px;
        }
        .fixed-nav a {
            text-decoration: none;
            color: #4a4a4a;
            font-weight: bold;
            font-size: 14px;
        }
        .fixed-nav a:hover {
            color: #3182ce;
            text-decoration: underline;
        }
    </style>

    <div class="fixed-nav">
        <a href="#section-top">商業背景</a>
        <a href="#section-bg">資料概述</a>
        <a href="#section-insights">數據洞察</a>
        <a href="#section-tree">策略與建議</a>
        <a href="#section-strategy">結論</a>
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
st.header("一、 專案背景與商業價值")
col_bg1, col_bg2 = st.columns(2)
with col_bg1:
    st.subheader("商業痛點")
@@ -62,7 +62,7 @@

# 2. 四大核心洞察與圖表展示
st.markdown('<div id="section-insights"></div>', unsafe_allow_html=True)
st.header("📈 二、 核心數據洞察與視覺化圖表")
st.header("二、 核心數據洞察與視覺化圖表")

# 洞察 1：先前行銷成效
st.subheader("1. 先前行銷成效（poutcome）是轉換率的最強預測指標")
@@ -106,7 +106,7 @@

# 3. 決策樹模型
st.markdown('<div id="section-tree"></div>', unsafe_allow_html=True)
st.header("🌳 三、 機器學習決策樹模型驗證")
st.header(" 三、 機器學習決策樹模型驗證")
st.write("透過機器學習決策樹模型，在數學上印證上述特徵切分與收斂邏輯：")
try:
    st.image("decision_tree.png", caption="銀行定存轉換率決策樹模型架構圖", use_container_width=True)
@@ -117,7 +117,7 @@

# 4. 營運策略
st.markdown('<div id="section-strategy"></div>', unsafe_allow_html=True)
st.header("💡 四、 具體營運策略與落地建議")
st.header("四、 具體營運策略與落地建議")
st.markdown("""
1. **建立 VIP 優先外撥名單（VIP Queue）**：
   * 將符合「前次行銷成功」且「無客訴紀錄」之舊客自動歸類，指派資深業務專員優先對接，確保優質體驗。
@@ -128,5 +128,5 @@
""")

st.markdown("---")
st.markdown("### 🔗 專案原始碼與完整筆記")
st.markdown("### 🔗 專案程式碼")
st.markdown("[👉 點此前往 Google Colab 完整分析筆記](https://colab.research.google.com/drive/1CZVOzrgRb-PzNwHQQsQw9RfnB5_xaiKo?usp=sharing)")
