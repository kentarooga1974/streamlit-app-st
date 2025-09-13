import streamlit as st
import psycopg2
from datetime import date

# DB接続設定（環境に合わせて変更）
conn = psycopg2.connect(
    host="localhost",
    dbname="kentaro_db",
    user="postgres",
    password="16231623",
    port="5432"
)
cur = conn.cursor()

st.title("業務報告デモアプリ")

# 入力フォーム
task = st.text_input("タスク名")
person = st.text_input("担当者")
report_date = st.date_input("報告日", value=date.today())

if st.button("登録"):
    if task and person:
        cur.execute(
            "INSERT INTO reports (task_name, person, report_date) VALUES (%s, %s, %s)",
            (task, person, report_date)
        )
        conn.commit()
        st.success("登録しました！")
    else:
        st.warning("すべての項目を入力してください")


# データ表示
st.subheader(" 登録済み報告一覧")
cur.execute("SELECT task_name, person, report_date FROM reports ORDER BY report_date DESC")
rows = cur.fetchall()

for row in rows:
    st.write(f" {row[0]} |  {row[1]} |  {row[2]}")

cur.close()
conn.close()

