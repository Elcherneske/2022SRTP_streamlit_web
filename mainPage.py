import streamlit as st
from dataBase import mDatabase
from user_module import userManagement
from baseParameter import parameters
from pageFile import *

#这个版本无法实现多并发访问服务器程序，因为不同客户端访问的都是同一个choice，也就是说前端交互程序是单独的
#实现通过不同账号访问不同database的功能
def main():
    db = mDatabase("localhost","root","fanggroup","srtp2022")
    parameter = parameters(db)
    users = userManagement(db)
    st.set_page_config(page_title="Fang group 2022 srtp project", layout="wide")

    choice = parameter.get_parameter("'choice'")

    if(st.sidebar.button("login")):
        parameter.change_parameter("'choice'", "'login'")
        choice = 'login'
    if(st.sidebar.button("sign up")):
        parameter.change_parameter("'choice'", "'sign up'")
        choice = 'sign up'
    if (st.sidebar.button("log out")):
        parameter.change_parameter("'choice'", "'logout'")
        choice = 'logout'


    if choice == "homepage":
        homepage()

    elif choice == "login":
        login_page(parameter, users)

    elif choice == "sign up":
        sign_up_page(parameter, users)

    elif choice == "main page":
        main_page(parameter,db)

    elif choice == "show data page":
        show_data_page(parameter,db)

    elif choice == "logout":
        parameter.change_parameter("'choice'", "'homepage'")
        st.success("登出成功")



main()