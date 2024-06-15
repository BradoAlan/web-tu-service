import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title='Tu Service Especializado', page_icon='👨‍🔧', layout='wide')

#Carga de CSS
def css_load(css_file):
    with open(css_file) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

css_load("style/main.css")


#Carga de annimacion
url_animation = "https://lottie.host/ac98afd1-035f-4ae9-b031-acdb8f705806/0eBo1g3l7J.json"
url_animation2 = "https://lottie.host/ffa2ed6a-741f-44a3-b860-d5b94f3e8a86/LaxcXk4AEs.json"

def lottie_load(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
animation_1 = lottie_load(url_animation)
animation_2 = lottie_load(url_animation2)


#Intro
with st.container():
    st.header("Hola, soy Fernando")
    st.title('Técnico matriculado')
    st.write('Soy especialista en reparación de electrodomésticos de linea blanca y aires acondicionados')
    st.write('[Saber más >](https://service.com/)')

#Sobre nosotros
with st.container():
    st.write('---')
    text_column, animation_column = st.columns(2)
    with text_column:
        st.header('Sobre nosotros 👨‍🔧')
        st.write(
            """
            Soy técnico matriculado con más de 10 años de experiencia en reparación de electrodomésticos.

            -Lavarropas y lava secarropas

            -Heladeras

            -Aires acondicionados split y centralizados

            -Hornos electricos

            -Cavas de vino
            """)
        st.write('***Atendemos en todo el AMBA***')
    with animation_column:
        st_lottie(animation_1, height=400)

#Servicios
with st.container():
    st.write('---')
    st.header('Servicios 🔧')
    st.write('##')
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open('images/presupuesto.jpg')
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader('Presupuestos en el dia')
        st.write(
            """
                Luego de la consuslta, nos comprometemos en pasarte un presupuesto aproximado de la reparación
                en el dia.

            """
        )
        st.write('[Ver servicios >](https://service.com/)')


with st.container():
    st.write('---')
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open('images/camioneta.jpeg')
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader('Reparaciones a domicilio')
        st.write(
            """
                Nos acercamos hasta tu domicilio dentro de las 72hs para realizar el trabajo.

            """
        )
        st.write('[Ver servicios >](https://service.com/)')

with st.container():
    st.write('---')
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open('images/garantia.jpg')
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader('Garantia escrita de 3 meses')
        st.write(
            """
                Todos nuestros trabajos cuentan con garantía escrita de 3 meses.

            """
        )
        st.write('[Ver servicios >](https://service.com/)')

#Contacto
with st.container():
    st.write('---')
    st.header('Contacta con nosotros 📩')
    st.write('##')
    contact_form = """
        <form action="https://formsubmit.co/8db6ee048edf8780cff40b9c16f316c6" method="POST">
        <input type="hidden" name="_captcha" value="false">
            <label for="name">Nombre</label>
            <input type="text" id="name" name="firstname" placeholder="Tu nombre..." required>
            <label for="email">e-mail</label>
            <input type="email" id="email" name="email" placeholder="Tu email..." required>
            <label for="message">Mensaje</label>
            <textarea id="message" name="message" placeholder="Tu mensaje..." style="height:200px" required></textarea>
            <input type="submit" value="Enviar">
        </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st_lottie(animation_2, height=400)

        