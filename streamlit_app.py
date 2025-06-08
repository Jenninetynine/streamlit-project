import streamlit as st
from page_content.home import home_page
from page_content.education import education_page
from page_content.experience import experience_page
from page_content.contact import contact_page
from page_content.resume import resume_page
from components.footer import display_footer
from components.style import load_css

class MultiApp:
    def __init__(self):
        self.apps = []
    
    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})
    
    def run(self):
        st.set_page_config(page_title="张硕个人网站", layout="wide")  # 设置页面配置
        load_css()  # 加载CSS样式
        st.sidebar.markdown("# 导航菜单")
        # 通过侧边栏单选框切换页面
        app = st.sidebar.radio("选择页面", self.apps, format_func=lambda x: x["title"])
        app["function"]()
        display_footer()  # 显示页脚

# 初始化应用并添加页面
if __name__ == "__main__":
    app = MultiApp()
    app.add_app("个人主页", home_page)
    app.add_app("教育背景", education_page)
    app.add_app("个人经历", experience_page)
    app.add_app("请联系我", contact_page)
    app.add_app("下载简历", resume_page)
    app.run()