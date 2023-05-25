import streamlit as st
import numpy as np
import pandas as pd
import os

def homepage():
    st.subheader("首页")
    st.markdown('''Streamlit文档的地址是：https://docs.streamlit.io/''')
    c1, c2 = st.columns(2)
    with c1:
        st.success("success 1")
        # st.image()
    with c2:
        st.success("success 2")
        # st.image()


def login_page(para, users):
    st.subheader("登录区域")
    username = "'" + st.text_input("用户名") + "'"
    password = "'" + st.text_input("密码", type="password") + "'"
    if st.button("开始登录"):
        login_result = users.login_user(username,password)
        if(login_result == True):
            para.change_parameter("'choice'", "'main page'")
            st.success("登录成功，请再次点击进入主页")
        else:
            st.error("账号密码输入错误")


def sign_up_page(para, users):
    st.subheader("注册区域")
    username = "'" + st.text_input("用户名") + "'"
    password = "'" + st.text_input("密码", type="password") + "'"
    if st.button("注册"):
        sign_result = users.add_userdata(username, password)
        if(sign_result == False):
            st.error("此账号已注册，请使用其他用户名")
        else:
            st.success("注册成功,请点击左方按钮登录")


def main_page(para, db):
    st.subheader("主页")
    temp = db.select_all_value("tablenametable")
    tables = temp[::-1]
    table_number = len(tables)

    if(table_number < 20):
        present_tables = tables
        for i in range(len(present_tables)):
            present_tables[i] = present_tables[i][0]
        choice = st.radio("choose the data", tables)
        para.add_parameter("'data_choice'", '"' + choice +'"')
    else:
        present_tables = tables[0:20:1]
        for i in range(len(present_tables)):
            present_tables[i] = present_tables[i][0]
        choice = st.radio("choose the data", present_tables)
        para.add_parameter("'data_choice'", '"' + choice + '"')
    if st.button("选择"):
        para.add_parameter("'choice'", "'show data page'")
        st.success("登录成功，请再次点击进入")

def show_data_page(para,db):
    st.subheader("数据展示")
    data_choice = para.get_parameter("'data_choice'")
    datas = db.select_all_value(data_choice)
    num = len(datas)
    present_array = np.zeros(num)
    present_time = np.zeros(num)
    for i in range(num):
        present_array[i] = datas[i][1]
        present_time[i] = datas[i][0]


    # 其中df定义的位置，并不影响最后的输出位置！
    chart_data = pd.DataFrame(
        present_array,
        columns=['value'])
    st.line_chart(chart_data)


    if st.button("show data"):
        st.write(pd.DataFrame({
            'time': present_time,
            'value': present_array
        }))


    filename = st.text_input("输入文件名称") + ".csv"
    path = "..\\DataBase\\" + filename
    if os.path.exists(path):
        with open(path, "rb") as file:
            btn = st.download_button(
                label="下载实时交互脚本",
                data=file,
                file_name=filename,
            )
    else:
        st.error("file not exist")