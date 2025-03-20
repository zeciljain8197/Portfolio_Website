import streamlit as st
from constant import *
import pandas as pd
from streamlit_timeline import timeline
import plotly.graph_objects as go
import streamlit.components.v1 as components
from send_email import send_email
import webbrowser


st.set_page_config(page_title='Zecil Jain\'s Portfolio', layout="wide", page_icon='👨‍🔬',
                   initial_sidebar_state='collapsed')

st.markdown(""" 
<h1 style='text-align: center;'>Bonjour! 🖖 I'm Zecil</h1>
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> 
""", unsafe_allow_html=True)


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1448067686092-1f4f2070baae?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


add_bg_from_url()

st.markdown("<h2 style='text-align: center; color: white;'><u>Introduction</u> 🧑🏽‍💼</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: white;'>{info['Brief_1']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: white;'>{info['Brief_2']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: white;'>{info['Brief_3']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: white;'>{info['Brief_4']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: white;'>{info['Brief_5']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: white;'>{info['Brief_6']}</p>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: white;'>{info['Brief_']}</p>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: white;'><u>Career snapshot</u> 🎬</h2>", unsafe_allow_html=True)

with st.spinner(text="Building line"):
    with open('timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

st.markdown("<h2 style='text-align: center; color: white;'><u>Skills & Tools</u> ⚒</h2>", unsafe_allow_html=True)

skl1, skl2, skl3, skl4, skl5 = st.columns(5)

with skl1:
    st.markdown("""
    <p align="left"> 
        <a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="60" height="60"/> </a>
    </p>""", unsafe_allow_html=True)
    if st.button("HTML"):
        webbrowser.open_new_tab("https://www.w3.org/html/")

    st.markdown("""
    <p align="left"> 
             <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="60" height="60"/> </a>
    </p>""", unsafe_allow_html=True)
    if st.button("CSS"):
        webbrowser.open_new_tab("https://www.w3schools.com/css/")

    st.markdown("""
    <p align="left"> 
             <a href="https://www.python.org" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="60" height="60"/> </a>   
    </p>""", unsafe_allow_html=True)
    if st.button("Python"):
        webbrowser.open_new_tab("https://www.python.org")

    st.markdown("""
    <p align="left"> 
        <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("Django"):
        webbrowser.open_new_tab("https://www.djangoproject.com/")

    st.markdown("""
    <p align="left"> 
        <a href="https://www.tableau.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/tableau-software.svg" alt="tableau" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("Tableau"):
        webbrowser.open_new_tab("https://www.tableau.com/")

with skl2:
    st.markdown("""
    <p align="left"> 
        <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("GIT"):
        webbrowser.open_new_tab("https://git-scm.com/")

    st.markdown("""
    <p align="left">
        <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("MySQL"):
        webbrowser.open_new_tab("https://www.mysql.com/")

    st.markdown("""
    <p align="left">
        <a href="https://pandas.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/2ae2a900d2f041da66e950e4d48052658d850630/icons/pandas/pandas-original.svg" alt="pandas" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("PyData"):
        webbrowser.open_new_tab("https://pandas.pydata.org/")

    st.markdown("""
    <p align="left">
        <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("PostgreSQL"):
        webbrowser.open_new_tab("https://www.postgresql.org")

    st.markdown("""
    <p align="left">
        <a href="https://en.wikipedia.org/wiki/Natural_language_processing" target="_blank" rel="noreferrer"> <img src="https://cdn-icons-png.flaticon.com/512/3344/3344341.png" alt="nlp" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("NLP"):
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Natural_language_processing")

with skl3:
    st.markdown("""
    <p align="left">
        <a href="https://pytorch.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pytorch/pytorch-icon.svg" alt="pytorch" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("PyTorch"):
        webbrowser.open_new_tab("https://pytorch.org/")

    st.markdown("""
    <p align="left">
        <a href="https://scikit-learn.org/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="scikit_learn" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("Scikit-Learn"):
        webbrowser.open_new_tab("https://scikit-learn.org/")

    st.markdown("""
    <p align="left">
        <a href="https://seaborn.pydata.org/" target="_blank" rel="noreferrer"> <img src="https://seaborn.pydata.org/_images/logo-mark-lightbg.svg" alt="seaborn" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("Seaborn"):
        webbrowser.open_new_tab("https://seaborn.pydata.org/")

    st.markdown("""
    <p align="left">
        <a href="https://en.wikipedia.org/wiki/Machine_learning" target="_blank" rel="noreferrer"> <img src="https://cdn-icons-png.flaticon.com/512/4616/4616734.png" alt="machine_learning" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("Machine Learning"):
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Machine_learning")

    st.markdown("""
    <p align="left">
        <a href="https://en.wikipedia.org/wiki/Deep_learning" target="_blank" rel="noreferrer"> <img src="https://cdn-icons-png.flaticon.com/512/2103/2103787.png" alt="deep_learning" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("Deep Learning"):
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Deep_learning")

with skl4:
    st.markdown("""
    <p align="left">
        <a href="https://www.tensorflow.org" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/tensorflow/tensorflow-icon.svg" alt="tensorflow" width="60" height="60"/> </a>
    </p>""", unsafe_allow_html=True)
    if st.button("Tensorflow"):
        webbrowser.open_new_tab("https://www.tensorflow.org")

    st.markdown("""
    <p align="left">
        <a href="https://ubuntu.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/ubuntu/ubuntu-icon.svg" alt="Ubuntu" width="60" height="60"/> </a>
    </p>""", unsafe_allow_html=True)
    if st.button("Ubuntu"):
        webbrowser.open_new_tab("https://ubuntu.com/")

    st.markdown("""
    <p align="left">
        <a href="https://unity.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/unity3d/unity3d-icon.svg" alt="Unity" width="60" height="60"/> </a>
    </p>""", unsafe_allow_html=True)
    if st.button("Unity"):
        webbrowser.open_new_tab("https://unity.com/")

    st.markdown("""
    <p align="left">
        <a href="https://en.wikipedia.org/wiki/Data_science" target="_blank" rel="noreferrer"> <img src="https://cdn-icons-png.flaticon.com/512/2821/2821637.png" alt="data_science" width="60" height="60"/> </a>
    </p>""", unsafe_allow_html=True)
    if st.button("Data Science"):
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Data_science")

    st.markdown("""
    <p align="left">
        <a href="https://en.wikipedia.org/wiki/Data_and_information_visualization" target="_blank" rel="noreferrer"> <img src="https://cdn-icons-png.flaticon.com/512/4241/4241488.png" alt="data_vis" width="60" height="60"/> </a>
    </p>""", unsafe_allow_html=True)
    if st.button("Data Visualization"):
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Data_and_information_visualization")

with skl5:
    st.markdown("""
    <p align="left">
        <a href="https://wordpress.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/wordpress/wordpress-icon.svg" alt="Wordpress" width="60" height="60"/> </a> 
    </p>""", unsafe_allow_html=True)
    if st.button("Wordpress"):
        webbrowser.open_new_tab("https://wordpress.com/")

    st.markdown("""
    <p align="left">
        <a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="60" height="60"/> </a>
    </p>""", unsafe_allow_html=True)
    if st.button("OpenCV"):
        webbrowser.open_new_tab("https://opencv.org/")

    st.markdown("""
    <p align="left">
        <a href="https://jupyter.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/jupyter/jupyter-icon.svg" alt="jupyter" width="60" height="60"/> </a>
    </p>
    """, unsafe_allow_html=True)
    if st.button("Jupyter"):
        webbrowser.open_new_tab("https://jupyter.org/")

    st.markdown("""
    <p align="left">
        <a href="https://en.wikipedia.org/wiki/Data_analysis" target="_blank" rel="noreferrer"> <img src="https://cdn-icons-png.flaticon.com/512/294/294968.png" alt="data_analytics" width="60" height="60"/> </a>
    </p>
    """, unsafe_allow_html=True)
    if st.button("Data Analytics"):
        webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Data_analysis")

    st.markdown("""
    <p align="left">
        <a href="https://streamlit.io/" target="_blank" rel="noreferrer"> <img src="https://seeklogo.com/images/S/streamlit-logo-1A3B208AE4-seeklogo.com.png" alt="streamlit" width="60" height="60"/> </a>
    </p>
    """, unsafe_allow_html=True)
    if st.button("StreamLit"):
        webbrowser.open_new_tab("https://streamlit.io/")

with st.sidebar:
    st.markdown(
        '![Visitors](https://api.visitorbadge.io/api/visitors?path=https://portfolio8197.herokuapp.com/&'
        'label=Total-Visits&'
        'labelColor=%230e0a8a&'
        'countColor=%23d9e3f0&'
        'style=plastic&'
        'labelStyle=none)')

    st.subheader("Online Presence")

    components.html(embed_component['linkedin'], height=310)

    st.caption("some more...")

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.markdown(info['Github'], unsafe_allow_html=True)

    with col2:
        st.markdown(info['Kaggle'], unsafe_allow_html=True)

    with col3:
        st.markdown(info['Twitter'], unsafe_allow_html=True)

    with col4:
        st.markdown(info['Facebook'], unsafe_allow_html=True)

    with col5:
        st.markdown(info['Instagram'], unsafe_allow_html=True)

    with col6:
        st.markdown(info['Beacons.AI'], unsafe_allow_html=True)

    with st.expander("Want to connect?"):
        with st.form(key="email_forms"):
            user_email = st.text_input("Your email address")
            raw_message = st.text_area("Your message")
            message = f"""\
        Subject: New email from {user_email}
    
        From: {user_email}
        {raw_message}
        """
            button = st.form_submit_button()
            if button:
                send_email(message)
                st.info("Your email was sent successfully!")

    st.write("Need my resume?")
    pdfFileObj = open('Zecil_Jain_Resume.pdf', 'rb')
    st.download_button('Download', pdfFileObj, file_name='Zecil_Jain_Resume.pdf', mime='pdf')


st.markdown("<h2 style='text-align: center; color: white;'><u>Education</u> 📖</h2>", unsafe_allow_html=True)

layout = dict(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].keys()),
                fill_color='rgba(19, 23, 32, 0.9)',
                align='left', height=65, font_size=20),
    cells=dict(values=list(info['edu'].values()),
               fill_color='rgba(214, 67, 9, 0.9)',
               align='left', height=40, font_size=15))], layout=layout)

fig.update_layout(width=750, height=400)
st.plotly_chart(fig)

st.markdown("<h2 style='text-align: center; color: white;'><u>Projects</u> 💻</h2>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: white;'>Below you can find some of the projects I have built"
            " using various languages, frameworks and tools. Feel free to contact me!</p>",
            unsafe_allow_html=True)

df = pd.read_csv("data.csv", sep=";")

col1, col2, col3 = st.columns([0.5, 5.5, 0.5])

with col2:
    for index, row in df[:1].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

col4, empty_col, col5 = st.columns([1.5, 0.5, 1.5])

with col4:
    for index, row in df[1:7].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col5:
    for index, row in df[7:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
