import streamlit as st
from youtubesearchpython import ChannelsSearch, ResultMode, ChannelSearch, VideosSearch



@st.cache
def buscarCancion(param):
    videosSearch = VideosSearch(f'"karaoke"+"{param}"', limit = 40)
    resultados = videosSearch.result()
    resultados = [[i['title'],i['link'],i['richThumbnail']] for i in resultados['result']]
    res = []
    for i in resultados:
        if i[2] == None:
            pass
        else:
            res.append(i)
    resultados = res[0:12]
    del res
    for i in resultados:
        i[2] = i[2]['url']
    
    return resultados


def card(title, preview):
    return f"""
    <div class="card" style="margin: 1rem;">
        <img src="{preview}" class="card-img-top">
        <div class="card-body">
            <p class="card-text">{title}</p>
        </div>
    </div>
    """

st.set_page_config(
    page_title="KARAOKE FIESTA",
    page_icon="random",
    layout="wide",
    # initial_sidebar_state="expanded",
    # menu_items={
    #     'Get help': 'mailto:victorm.sanchezm@gmail.com',
    #     'Report a bug': None,
    #     'About': "# This is a header. This is an *extremely* cool app!"
    # }
)

st.markdown("""
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
""", unsafe_allow_html=True)

st.header('KAROAKE FIESTERO')


param = ''

param = st.text_input(
    "Escribe el nombre de una canción o artista",
    key='text'
)

def clear_text():
    st.session_state['text'] = ''

if st.button("Limpiar búsqueda", on_click=clear_text):
    param = ''

if param != '':
    resultados = buscarCancion(param)
    st.caption('Mostrando los 12 resultados principales')
    resultados = [resultados[j:j+3] for j in range(0,len(resultados),3)]

    col1, col2, col3 = st.columns(3)
    with col1:   
        for i in resultados[0]:
            st.video(i[1])
            st.subheader(i[0])
    with col2:
        for i in resultados[1]:
            st.video(i[1])
            st.subheader(i[0])
    with col3:
        for i in resultados[2]:
            st.video(i[1])
            st.subheader(i[0])
    # with col4:
    #     for i in resultados[3]:
    #         st.image(i[2])
    #         st.subheader(i[0])

st.markdown('v.tt.alpha.0.2')



##############################################################################
# versiones:
# v.tt.alpha.0.1
# prueba interna, primer release
# v.tt.alpha.0.2
# ahora limpia correctamente el input_text
##############################################################################
