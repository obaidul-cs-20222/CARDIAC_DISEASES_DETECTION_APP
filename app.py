import numpy as np
import pandas as pd
import streamlit as st
from backend import prediction
from streamlit_option_menu import option_menu



def predictHeartDisease(input_data):
    input_data=np.asarray(input_data).reshape(1,-1)

    returned_value=prediction(input_data)
    answer=int(returned_value)
    if answer==1:
            st.error("__POSSIBLE CARDIAC DISEASE DETECTED.__")
    else: 
            st.success("__YOUR CONDITION SEEMS FINE. BUT FEEL FREE TO CONSULT A PHYSICIAN IF YOU ARE FELLING UNWELL.__")

    return answer


if __name__ == '__main__':

    with st.sidebar:
    
        selected = option_menu('Cardiac Disease Prediction App',
                          
                          ['Predict Heart Health',
                           'Our Prediction Records',
                           'About Us'],
                          icons=['heart','book','info'],
                          default_index=0)
    
    if selected == "Predict Heart Health":
        st.markdown("<h1 style='text-align: center;'>CARDIAC DISEASE PREDICTION APP</h1>", unsafe_allow_html=True)
        st.markdown("____")
        st.markdown("<p style='text-align: center;'><b><i>Select normal values for ★ marked fields if you don't know the exact values</b></i></p>", unsafe_allow_html=True)
        st.markdown("____")
        age = st.number_input("__ENTER YOUR AGE__",min_value=0, max_value=110, value=0, step =1)

        sex = st.radio(
            "__YOUR GENDER__",
            ('MALE', 'FEMALE'))

        cp = st.radio(
            "__ARE YOU HAVING CHEST PAIN?__",
            ('SEVERE PAIN','CHEST PAIN WITH TIGHTNESS','MILD CHEST PAIN WITH DISCOMFORT','NO')
            )

        trestbps = st.number_input("__ENTER YOUR CURRENT SYSTOLIC BLOOD PRESSURE__",min_value=0, max_value=300, value=0,step =1)

        chol = st.number_input("__ENTER YOUR SERUM CHOLESTEROL LEVEL__",min_value=0, max_value=700, value=0,step =1)

        fbs = st.radio("__ARE YOU DIABETIC?__",
                    ('YES (if FastingBS > 120 mg/dl)', 'NO (if FastingBS < 120 mg/dl)')
                    )

        restecg = st.radio("__RESTING ELECTROCARDIOGRAM RESULT ★__",
                        ('NORMAL','ST-T ABNORMALITY','LEFT VENTRICULAR HYPERTROPHY')
                        )

        thalach = st.number_input("__ENTER YOUR HIGHEST HEART RATE IN LAST 5 MIN__",min_value=0, max_value=250, value=0,step =1)

        exang = st.radio("__DO YOU HAVE CHEST PAIN DURING PHYSICAL ACTIVITIES?__",
                    ('YES','NO')
                    )

        oldpeak = st.number_input("__NUMERIC VALUE MEASURED IN ST DEPRESSION (NORMAL VALUE IS < 0.5) ★__",min_value=0.0, max_value=10.0, value=0.0,step =0.1,format="%.1f")

        slope = st.radio("__THE SLOPE OF THE PEAK EXERCISE ST SEGMENT ★__",
                    ('UPSLOPING (NORMAL CONDITION)','FLAT (SLIGHT ABNORMALITY)','DOWNSLOPING (SEVERE ABNORMALITY)')
                    )
        st.markdown("____")

        if sex == "MALE":
            sex = 1
        else:
            sex =  0


        if cp == "SEVERE PAIN":
            cp = 1
        elif cp == "CHEST PAIN WITH TIGHTNESS":
            cp = 2
        elif cp == "MILD CHEST PAIN WITH DISCOMFORT":
            cp = 3
        else:
            cp = 4


        if fbs == "YES (if FastingBS > 120 mg/dl)":
            fbs = 1
        else:
            fbs = 0

        if restecg == "NORMAL":
            restecg = 0
        elif restecg == "ST-T ABNORMALITY":
            restecg = 1
        else:
            restecg = 2


        if exang == "YES":
            exang = 1
        else:
            exang = 0


        if slope == "UPSLOPING (NORMAL CONDITION)":
            slope = 1
        elif slope == "FLAT (SLIGHT ABNORMALITY)":
            slope = 2
        else:
            slope = 3
        
        
    

        if st.button("__PREDICT HEART HEALTH__"):
            target = predictHeartDisease([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope])
            f = open("user_records.txt", "a")
            f.write("\n")
            new_data = str([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, target])
            leng = len(new_data)
            f.write(new_data[1:leng-1]) 
            f.close()


        
    if selected == "Our Prediction Records":
        st.markdown("<h3 style='text-align: center;'>PREDICTION RECORDS OF OUR PREVIOUS USERS</h3>", unsafe_allow_html=True)
        f = pd.read_csv("user_records.txt")
        st.table(f)
        st.markdown("____")
        st.markdown("<p style='text-align: center;'><i>All the records are stored only for academic and research purpose & will not be used for any other means.</i></p>", unsafe_allow_html=True)

    
    if selected == "About Us":
        st.markdown("<h2 style='text-align: center;'>ABOUT US</h2>", unsafe_allow_html=True)
        st.markdown("____")
        st.markdown("<p style='text-align: center;'>This is an academic project made by B.Sc Computer Science (Honours) final year students. This project is an ambitious academic endeavor aimed at exploring and advancing knowledge in the field of Machine Learning & Artifical Intelligence. As a team of passionate students, our goal is to delve into the intricacies of Machine Learning & Artifical Intelligence and contribute valuable insights to the existing body of knowledge.</p>", unsafe_allow_html=True)
        st.markdown("____")
        st.markdown("<h4 style='text-align: center;'>Developed and maintained by</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><b>Md Obaidul Islam</b></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><b>Swapnil Basu Choudhury</b</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><b>Sneha Rana</b></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><b>Pritam Mondal</b></p>", unsafe_allow_html=True)
        st.markdown("____")
        
        