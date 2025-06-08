import streamlit as st
import os

def resume_page():
    st.markdown("## 下载简历")
    
    # 简历PDF下载（需将你的简历命名为resume.pdf并放入static/docs/）
    pdf_path = os.path.join("static", "docs", "resume.pdf")
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            label="下载PDF简历",
            data=pdf_bytes,
            file_name="resume.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("简历文件未找到，请检查路径")
    
    st.markdown("---")
    st.markdown("## 简历概览")
    st.markdown("**专业技能**：数字化转型、市场调研、数据分析、Python/R/STATA")
    st.markdown("**实习经历**：德勤咨询（CRM数字化转型）、益普索（定量研究）")
    st.markdown("**教育背景**：香港中文大学（硕士在读）、华东理工大学（经济学学士）")