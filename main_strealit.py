import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image



st.title('Consultar puntaje de crédito')

st.markdown('## ¿Qué es el Scorecad?')
st.markdown('Uno de los principales actividades de los bancos es el prestamo de dinero.Saber a quién prestar es un problema porque deben saber si el dinero si se les va a regresar.Por esta razón se desarolló un puntaje de crédito, el cual es un número que representa la probabilidad que el prestatario regrese el dinero al banco a tiempo')

image = Image.open('credit.png')
st.image(image)

st.markdown('La anterior imagen es un ejemplo de el Scorecard, el cual son unos intervalos que indican que tan bueno es prestar dinero según el puntaje que adquiera ')

st.markdown('## ¿Por qué es importante?')

st.markdown('Este número también le proporciona unade ideacomo estaría su bienestar financiero. Es decir como su situación financiera y decisiones monetarias le proporcionan seguridad y libertad en sus decisiones.')

st.markdown('### Consulte su puntaje de crédito')
st.markdown('Con el siguiente formulario puede consultar su puntaje de crédito. Además podrá comparar su puntaje con el resto de la población ')

image3 = Image.open('desarrollo2.png')
with st.sidebar:
    
    st.image(image3,width=80)
    st.markdown("#### Desarrollado por:")
    st.markdown("- Jose Daniel Bustamante Arango.")
    st.markdown("   jobustamantea@unal.edu.co")
    st.markdown("- Daniel Santiago Cadavid Montoya.")
    st.markdown("   dcadavid@unal.edu.co")
    st.markdown("- Ronald Gabriel Palencia.")
    st.markdown("   ropalencia@unal.edu.co")
    st.markdown("- Marlon Calle Areiza.")
    st.markdown("   mcalle@unal.edu.co")
    st.markdown("- Daniel Daza Macías.")
    st.markdown("   dadazam@unal.edu.co")


with st.form("my_form"):
    option_purpose = st.selectbox(
    '¿Cuál es el propósito del crédito?',
    ('tarjeta de crédito','Otro'))

    option_verification_status = st.selectbox(
    '¿Fueron los ingresos verificados?',
    ('No','Si'))

    option_home_ownership = st.selectbox(
    '¿Posee casa?',
    ('No','Si'))


    option_tot_cur_bal = st.text_input('Saldo actual total de todas las cuentas')
    
    option_dti = st.selectbox(
    'dti del prestatario',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_inq_last_6mths = st.selectbox(
    '¿El número de consultas en los últimos 6 meses?',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_out_prncp = st.selectbox(
    'Capital restante pendiente por el monto total financiado',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_int_rate = st.selectbox(
    '¿Qué importancia tiene para usted que la universidad tenga gran porcentaje de titulos otorgados en el campo de las matemáticas?',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_termfda = st.selectbox(
    'ddfds',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_annual_inc = st.selectbox(
    '¿Cuáles son sus ingresos anuales?',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_revol_util = st.selectbox(
    '¿hola?',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_grade = st.selectbox(
    '¿Grado de préstamo asignado en la carta de crédito?',
    (1,2,3,4,5))

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.markdown("### Su puntaje de crédito es:" + 'no tiene' + "\U0001F600" )

        
st.write("Outside the form")