from modelo import Modelo
import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title='Tail - Análise de Sentimento', 
                   page_icon=None, 
                   layout='centered', 
                   initial_sidebar_state='auto'
                   )

st.markdown("""
            <style>
            body {
                color: #000;
                background-color: #ccc;
            }
            </style>
                """, unsafe_allow_html=True)

paginas = st.sidebar.radio('Selecione a página',
            ['IO', 'Sobre', 'Código', 'Participantes'])

df = pd.read_csv('https://raw.githubusercontent.com/humbertonc/CSV_tripadvisor/main/tripadvisor_hotel_reviews.csv', encoding='utf8')

st.title('Análise de Sentimento TripAdvisor')

### Página Principal

if paginas == "IO":
    st.subheader("Entrada")

    review = st.text_area('Coloque o texto a ser analisado na área abaixo: (Em Inglês)')
    st.info('O resultado é mais acurado se o comentário for longo')

    st.subheader("Resultado")
    mod = Modelo()

    if review :
        with st.spinner('Rodando o código...') :
            resultado = mod.predict(review)[0]
        st.code(review, language='html')
        if resultado == 0 :
            st.error('A revisão foi ruim')
        elif resultado == 1 :
            st.warning('A revisão foi neutra')       
        else :
            st.success('A revisão foi boa')

### Página Sobre

elif paginas == 'Sobre':

    st.subheader("Sobre")
    st.markdown(''' A Technology and Artificial Intelligence League (TAIL) é uma liga acadêmica da UFPB ligada ao Laboratório de Aplicações em Inteligência Artificial (ARIA) do Centro de Informática (CI). Ela é composta por cinco diretorias, sendo uma delas a Diretoria de Projetos, que é responsável pela Análise de Sentimento TripAdvisor.
                  O objetivo desse projeto é analisar comentários e tentar inferir se neles foi feita uma avaliação boa, neutra ou ruim. Para isso, foi utilizada uma base de dados em inglês de comentários avaliativos do site de viagens TripAdvisor e técnica de análise de sentimentos.
                  ''')

    st.subheader("O dataset")

    'Tripadvisor_hotel_reviews.csv: \n', df
    st.write('Comentário e Nota dada por cada usuário')

### Página do código

elif paginas == 'Código':

    st.subheader("O Código")
    code = open('assets/modelo.txt').read()
    st.write()
    st.code(code, language='python')

    st.subheader("Resultados")
    rt = open('assets/resultados.txt').read()
    st.write()
    st.code(rt, language='html')
    ### O texto em diferentes etapas?
    ### O Modelo?
    ### Os resultados?

### Participantes

elif paginas == 'Participantes':

    st.subheader("Diretores")
    diretor_1, diretor_2, diretor_3, diretor_4 = st.beta_columns(4)

    jw = Image.open('assets/authors/wallace.jpg')
    fh = Image.open('assets/authors/felipe.png')

    with diretor_2:
        st.markdown('João Wallace')
        st.image(jw, use_column_width=True)
        st.markdown('Github: **[joallace](https://github.com/joallace)**')

    with diretor_3:
        st.markdown('Felipe Honorato')
        st.image(fh, use_column_width=True)
        st.markdown('Github: **[Felipehonorato1](https://github.com/Felipehonorato1)**')

    st.subheader("Grupo")
    participante_1, participante_2, participante_3, participante_4 = st.beta_columns(4)

    ah = Image.open('assets/authors/andre.jpg')
    hn = Image.open('assets/authors/humberto.jpg')
    yn = Image.open('assets/authors/yann.jpg')
    ll = Image.open('assets/authors/larissa.jpg')

    with participante_1:
        st.markdown('André Hugo')
        st.image(ah, use_column_width=True)
        st.markdown('Github: **[hugo451](https://www.github.com/hugo451)**')

    with participante_2:
        st.markdown('Humberto Navarro')
        st.image(hn, use_column_width=True)
        st.markdown('Github: **[humbertonc](https://github.com/humbertonc)**')

    with participante_3:
        st.markdown('Yann Nicholas')
        st.image(yn, use_column_width=True)
        st.markdown('Github: **[Yannngn](https://github.com/Yannngn)**')

    with participante_4:
        st.markdown('Larissa Lucena')
        st.image(ll, use_column_width=True)
        st.markdown('Github: **[LucenaLarissa](https://github.com/LucenaLarissa)**')