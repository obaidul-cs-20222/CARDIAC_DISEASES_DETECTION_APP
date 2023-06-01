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
    # give a title to our app
    with st.sidebar:
    
        selected = option_menu('Cardiac Disease Prediction App',
                          
                          ['Predict Heart Health',
                           'Our Prediction Records',
                           'About Us'],
                          icons=['heart','book','info'],
                          default_index=0)
    
    if selected == "Predict Heart Health":
        st.title('CARDIAC DISEASE PREDICTION APP')
        st.markdown("____")
        st.markdown("__Select normal values for ★ marked fields if you don't know the exact value__")
        st.markdown("____")
        age=st.number_input("ENTER YOUR AGE",min_value=0, max_value=9999, value=0,step =1)

        sex = st.radio(
            "YOUR GENDER",
            ('MALE', 'FEMALE'))

        cp = st.radio(
            "ARE YOU HAVING CHEST PAIN?",
            ('SEVERE PAIN','CHEST PAIN WITH TIGHTNESS','MILD CHEST PAIN WITH DISCOMFORT','NO')
            )

        trestbps=st.number_input("ENTER YOUR CURRENT SYSTOLIC BLOOD PRESSURE",min_value=0, max_value=9999, value=0,step =1)

        chol=st.number_input("ENTER YOUR SERUM CHOLESTEROL LEVEL",min_value=0, max_value=9999, value=0,step =1)

        fbs=st.radio("ARE YOU DIABETIC?",
                    ('YES (if FastingBS > 120 mg/dl)', 'NO (if FastingBS < 120 mg/dl)')
                    )

        restecg=st.radio("RESTING ELECTROCARDIOGRAM RESULT ★",
                        ('NORMAL','ST-T ABNORMALITY','LEFT VENTRICULAR HYPERTROPHY')
                        )

        thalach=st.number_input("ENTER YOUR HIGHEST HEART RATE IN LAST 5 MIN",min_value=0, max_value=9999, value=0,step =1)

        exang=st.radio("DO YOU HAVE CHEST PAIN DURING PHYSICAL ACTIVITIES?",
                    ('YES','NO')
                    )

        oldpeak=st.number_input("NUMERIC VALUE MEASURED IN ST DEPRESSION (NORMAL VALUE IS < 0.5) ★",min_value=0.0, max_value=9999.0, value=0.0,step =0.1,format="%.1f")

        slope=st.radio("THE SLOPE OF THE PEAK EXERCISE ST SEGMENT ★",
                    ('UPSLOPING (NORMAL CONDITION)','FLAT (SLIGHT ABNORMALITY)','DOWNSLOPING (SEVERE ABNORMALITY)')
                    )
        st.markdown("____")

        if sex =="MALE":
            sex=1
        else:
            sex=0


        if cp=="SEVERE PAIN":
            cp=1
        elif cp=="CHEST PAIN WITH TIGHTNESS":
            cp=2
        elif cp=="MILD CHEST PAIN WITH DISCOMFORT":
            cp=3
        else:
            cp=4


        if fbs=="YES (if FastingBS > 120 mg/dl)":
            fbs=1
        else:
            fbs=0

        if restecg=="NORMAL":
            restecg=0
        elif restecg=="ST-T ABNORMALITY":
            restecg=1
        else:
            restecg=2


        if exang =="YES":
            exang=1
        else:
            exang=0


        if slope=="UPSLOPING (NORMAL CONDITION)":
            slope=1
        elif slope=="FLAT (SLIGHT ABNORMALITY)":
            slope=2
        else:
            slope=3
        
        
    

        if st.button("PREDICT HEART HEALTH"):
            target = predictHeartDisease([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope])
            f = open("user_records.txt", "a")
            f.write("\n")
            new_data = str([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, target])
            leng = len(new_data)
            f.write(new_data[1:leng-1]) 
            f.close()
            

        
    if selected == "Our Prediction Records":
        st.markdown("<h3 style='text-align: center;'>PREDICTION RECORDS OF OUR PREVIOUS USERS</h1>", unsafe_allow_html=True)
        f = pd.read_csv("user_records.txt")
        st.table(f)
        st.markdown("____")
        st.write("All the records are stored only for academic and research purpose & will not be used for any other means.")

    
    if selected == "About Us":
        st.markdown("<h2 style='text-align: center;'>ABOUT US</h2>", unsafe_allow_html=True)
        st.markdown("____")
        st.markdown("<p style='text-align: center;'>This is an academic project made by B.Sc Computer Science (Honors) final year students. This project is an ambitious academic endeavor aimed at exploring and advancing knowledge in the field of Machine Learning & Artifical Intelligence. As a team of passionate students, our goal is to delve into the intricacies of Machine Learning & Artifical Intelligence and contribute valuable insights to the existing body of knowledge.</p>", unsafe_allow_html=True)
        st.markdown("____")
        st.markdown("<h4 style='text-align: center;'>Developed and maintained by</h4>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Md Obaidul Islam</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Swapnil Basu Choudhury</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Sneha Rana</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Pritam Mondal</p>", unsafe_allow_html=True)
        st.markdown("____")
        
        