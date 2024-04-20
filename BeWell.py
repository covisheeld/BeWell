# -*- coding: utf-8 -*-


import pickle
import random
import altair as alt 

import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
from altair.vegalite.api import Chart


# loading the saved models

# diabetes_model = pickle.load(open('C:/Heart-Disease Predictor/diabetes_model_1.sav','rb'))
# heart_disease_model = pickle.load(open('C:/Heart-Disease Predictor/heart_disease1.sav','rb'))

# diabetes_model = pickle.load(open('diabetes_model_1.sav','rb'))
heart_disease_model = pickle.load(open('heart_disease1.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('MVJCE', ['Home', 'Heart Disease Prediction', 'Team']
                           , icons=['activity', 'heart', 'person']
                           , default_index=0)
# diabetes prediction page


if (selected == 'Heart Disease Prediction'):
    # page title
    st.title('MVJCE Heart Disease Predictor')
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex [Male=0, Female=1]')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''
    types = ['Type 1 - CORONARY HEART DISEASE', 'Type 2 - STROKE', 'Type - 3 PERIPHERAL ARTERIAL DISEASE',
             'Type - 4 AORTIC DISEASE']
    randomvariable = random.choice(types)
    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if (heart_prediction[0] == 1):
            heart_diagnosis = ('The Person is having Heart-Disease and suffering from ' + randomvariable)

        else:
            heart_diagnosis = 'The Person does not have any Heart-Disease'

    st.success(heart_diagnosis)

if (selected == 'Team'):
    # page title
    st.title('Meet The Team:')
    st.subheader('G Ganesh Sai Prakash [1MJ20CS063] :)')
    st.subheader('G Naveen Kumar [1MJ20CS067] :)')
    st.subheader('H Pranav [1MJ20CS075] :)')
    st.subheader('Harshavardhan B [1MJ20CS080] :)')

if (selected == 'Home'):
    # page title
    st.title('Welcome to Cardio-Vascular Wellness Predictor')
    # st.image('https://res-rehab.com/wp-content/uploads/2021/08/HeartAttack_Infographic.png', width=650, )

    st.image('https://www.udmi.net/wp-content/uploads/2020/02/UDMI_Cardiovascular-Disease.png', width=650, )

    st.subheader(
        'A heart attack occurs when the flow of blood to the heart is severely reduced or blocked. The blockage is usually due to a buildup of fat, cholesterol and other substances in the heart (coronary) arteries. The fatty, cholesterol-containing deposits are called plaques.')

    st.image(
        'https://static.vecteezy.com/system/resources/thumbnails/034/487/737/small/gold-frame-page-divider-free-png.png',
        width=650, )

    st.subheader(
        'The dataset is a combination of 4 different databases, but the primary one is the UCI Cleveland dataset. This database consists of a total of 76 attributes but all published experiments refer to using a subset of only 14 features.!*) Therefore, we have used the already processed UCI Cleveland dataset available on the Kaggle website for our analysis.')

    st.image("WWW.png", width=650, )

#    st.subheader('A heart attack occurs when the flow of blood to the heart is severely reduced or blocked. The blockage is usually due to a buildup of fat, cholesterol and other substances in the heart (coronary) arteries. The fatty, cholesterol-containing deposits are called plaques.')
