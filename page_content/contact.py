import streamlit as st

def contact_page():
    st.markdown("## 联系我")
    
    st.markdown("### 联系方式")
    st.markdown("- **邮箱**：zhangshuosophia@gmail.com")
    st.markdown("- **电话**：+86 59560186")
    st.markdown("- **地址**：中国香港")
    
    st.markdown("### 发送消息")
    with st.form("contact_form"):
        name = st.text_input("姓名", placeholder="请输入姓名")
        email = st.text_input("邮箱", placeholder="请输入邮箱")
        message = st.text_area("留言", placeholder="请输入留言内容", height=150)
        submitted = st.form_submit_button("提交")
        if submitted:
            st.success("消息已收到，我会尽快回复！")
    
    st.markdown("---")
    st.markdown("### 社交链接")
    st.markdown("- [LinkedIn](https://www.linkedin.com/in/shuo-zhang-sophia/)")