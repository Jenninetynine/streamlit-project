import streamlit as st

def display_footer():
    footer = """
    <div class="footer">
        <p>© 2025 张硕 | <a href="mailto:zhangshuosophia@gmail.com" style="color: #2C3E50;">联系我</a> | 最后更新：2025年6月</p>
    </div>
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f8f9fa;
        color: #6c757d;
        text-align: center;
        padding: 10px;
        font-size: 0.8rem;
        border-top: 1px solid #dee2e6;
    }
    .footer a {
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """
    st.markdown(footer, unsafe_allow_html=True)