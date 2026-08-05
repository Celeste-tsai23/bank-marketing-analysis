import streamlit as st
import pandas as pd

# 設定網頁標題與基本樣式
st.set_page_config(page_title="銀行定存行銷轉換率分析儀表板", layout="wide")

st.title("📊 銀行定存行銷轉換率分析與決策最佳化專案")
st.markdown("> 運用 Python 探索性數據分析（EDA）與機器學習決策樹驗證，協助金融機構精準獲客。")

# 側邊欄導覽
st.sidebar.header("📌 專案導覽選單")
menu = st.sidebar.selectbox("選擇檢視主題", [
    "一、 專案背景與商業價值", 
    "二、 四大核心數據洞察", 
    "三、 機器學習決策樹收斂", 
    "四、 落地營運策略與建議"
])

if menu == "一、 專案背景與商業價值":
    st.subheader("商業背景與核心目標")
    st.write("定期存款為銀行穩健利息收入的核心來源。傳統電話行銷高度依賴大量人工外撥，伴隨高昂營運成本。")
    st.info("💡 **核心目標**：透過資料探勘與行為分析，在行銷活動前識別高轉換潛力的客戶，將亂槍打鳥轉化為精準鎖定，大幅降低獲客成本。")

elif menu == "二、 四大核心數據洞察":
    st.subheader("📈 關鍵數據發現 (Key Insights)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 1. 先前行銷成效 (`poutcome`)")
        st.success("成功舊客轉換率高達 **64.7%** (n=1,511)，遠高於其他群組，為最強預測指標。")
        
        st.markdown("### 2. 黃金追蹤期 (`pdays`)")
        st.warning("成功轉換高峰集中在距離上次接觸 **50 至 200 天** 內，超過 250 天大幅下滑。")
        
    with col2:
        st.markdown("### 3. 行銷通話頻次 (`campaign`)")
        st.info("最佳效益落在 **1 至 3 通**，第 4 通起顯著遞減，證實非以量制勝。")
        
        st.markdown("### 4. 聯絡管道選擇 (`contact`)")
        st.success("行動電話（`cellular`）轉換率達 **14.9%** 表現最佳，為最有效渠道。")

elif menu == "三、 機器學習決策樹收斂":
    st.subheader("🌳 決策樹特徵驗證模型")
    st.write("透過 3 層決策樹模型在數學上印證 EDA 洞察：")
    st.code("""
[根節點] poutcome_success (先前成功舊客群，轉換率 64.7%)
 ├── [第二層] gold_pdays (50-200天黃金追蹤期) & housing (房屋貸款狀況)
 │    └── [第三層] optimal_campaign (3通電話以內最佳化邊界)
    """, language="text")

elif menu == "四、 落地營運策略與建議":
    st.subheader("💡 具體營運建議")
    st.markdown("""
    1. **建立 VIP 優先外撥名單（VIP Queue）**：指派資深業務優先對接前次成功且無客訴之舊客。
    2. **導入自動化停損機制**：單次活動遭拒達指定次數時，自動移出外撥池，改由成本較低的簡訊或網銀跟進。
    3. **動態名單派送**：依據年齡、資產與互動頻率自動派送對應的溝通腳本。
    """)

st.markdown("---")
st.markdown("🔗 **原始碼與完整分析筆記**：[Google Colab 專案連結](https://colab.research.google.com/drive/1CZVOzrgRb-PzNwHQQsQw9RfnB5_xaiKo?usp=sharing)")
