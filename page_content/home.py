import streamlit as st
from PIL import Image
import os

def home_page():
    # 左右分栏：左侧文字，右侧头像
    left_col, right_col = st.columns([3, 2])
    with left_col:
        st.markdown(
            """
            <h1>张硕  ZHANG Shuo, Sophia</h1>
            <p>香港中文大学 市场营销硕士（大数据方向）</p>
            <p>📧 zhangshuosophia@gmail.com | ☎️ +852 59560186</p>
            <p>地址：中国香港</p>
            """,
            unsafe_allow_html=True
        )
        st.markdown("## 个人简介")
        st.markdown("""
        香港中文大学市场营销硕士（大数据方向）在读，具备经济学本科背景，擅长数据分析与市场策略制定。曾在德勤咨询、益普索等企业实习，参与数字化转型、市场调研等项目，熟练使用Python、R、STATA等工具，具备较强的跨团队协作与问题解决能力。
        """)
        st.markdown("## 核心技能")
        st.markdown("- 数据分析：Python、R、STATA、SQL")
        st.markdown("- 市场策略：数字化转型、CRM优化、用户增长")
        st.markdown("- 工具：Excel（VLOOKUP/数据透视表）、Tableau、Power BI")
    
    with right_col:
        # 加载头像（需将你的照片命名为profile.png并放入static/images/）
        image_path = os.path.join("static", "images", "profile.jpg")
        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption="张硕", width=200)
        else:
            st.warning("头像文件未找到，请检查路径")
    
    st.markdown("---")  # 分隔线