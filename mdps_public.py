# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies',placeholder="Number of times pregnant",help="Number of times pregnant")
        
    with col2:
        Glucose = st.text_input('Glucose Level',placeholder="In Range(0-199)",help="Plasma glucose concentration a 2 hours in an oral glucose tolerance test")
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value',placeholder="eg.72(in mm Hg)",help="Diastolic blood pressure (mm Hg)")
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value',placeholder="In Range(0-99),in mm",help="Triceps skin fold thickness (mm)")
    
    with col2:
        Insulin = st.text_input('Insulin Level',placeholder="eg.210,in range(0-846)",help="2-Hour serum insulin (mu U/ml)")
    
    with col3:
        BMI = st.text_input('BMI value',placeholder="eg. 33.6",help="Body mass index (weight in kg/(height in m)^2)")
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value',placeholder="In Range(0.08-2.42)")
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
          st.error(diab_diagnosis)
          st.header("For healthy lief these 5 tips:")
          st.text("""1.Lose extra weight. Losing weight reduces the risk of diabetes.

2.Be more physically active. There are many benefits to regular physical activity.

3.Eat healthy plant foods. Plants provide vitamins, minerals and carbohydrates in your diet.

4.Eat healthy fats.

5.Skip fad diets and make healthier choices.""")
          
        else:
          diab_diagnosis = 'The person is not diabetic'
          st.success('The person is not diabetic')
          st.header("For stay away from the Diabetes,follow these 5 Tips:")
          st.text("""1.Lose extra weight. Losing weight reduces the risk of diabetes.

2.Be more physically active. There are many benefits to regular physical activity.

3.Eat healthy plant foods. Plants provide vitamins, minerals and carbohydrates in your diet.

4.Eat healthy fats.

5.Skip fad diets and make healthier choices.""")
        
    # st.error(diab_diagnosis)
    # st.success(diab_diagnosis)
    




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex',placeholder="(1 = male; 0 = female)")
        
    with col3:
        cp = st.text_input('Chest Pain types',placeholder="range(0-3)")
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure',placeholder="in range(94-200)",help="resting blood pressure (in mm Hg on admission to the hospital)")
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl',placeholder="eg 150 mg/dl",help="serum cholestoral in mg/dl")
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl',placeholder="(1 = true; 0 = false)",help="(fasting blood sugar &gt; 120 mg/dl) (1 = true; 0 = false)")
        
    with col1:
        restecg = st.text_input('RER',placeholder="values(0,1,2)",help="Resting Electrocardiographic Results")
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved',placeholder="Max heart rate",help="maximum heart rate achieved")
        
    with col3:
        exang = st.text_input('Exercise Induced Angina',placeholder="(1 = yes; 0 = no)")
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise',placeholder="",help="ST depression induced by exercise relative to rest")
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment',placeholder="0-6.2")
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy',placeholder="in range (0-3)")
        
    with col1:
        thal = st.text_input('thal',placeholder="eg 0,1,2",help="0=normal;1=fixed defect;2=reversable defect")
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
          st.error(heart_diagnosis)
          st.header("8 Steps to Prevent Heart Stroke")
          st.text("""
These key factors can help you live a longer, healthier life and reduce your risk of heart disease and stroke. Theyre part of an overall healthy lifestyle and prevention approach you can build with your health care team (doctors, nurses, pharmacists and other professionals). 


1.Know your risk. heart.org/ccccalculator
If you are 40-75 years old and have never had a heart attack or stroke, use our Check Change Control Calculator to estimate your risk of a cardiovascular event in the next 10 years. 
Certain factors can increase your risk, such as smoking, kidney disease or family history. Many risk factors can be improved with lifestyle changes.


2.Eat a healthy diet. heart.org/eatsmart
Center your eating plan around vegetables, fruits, whole grains, legumes, nuts, plant-based proteins, lean animal proteins and fish. 
Limit sweetened drinks, refined carbohydrates, added sugars, processed meats, sodium and saturated fats. Avoid trans fat.


3.Be physically active. heart.org/movemore
Adults should aim for at least 150 minutes of moderate-intensity aerobic activity or 75 minutes of vigorous activity each week.
If you are already active, increase your intensity for more benefits.
If you are not active now, get started by sitting less and moving more. 


4.Watch your weight. heart.org/weight
If you are overweight, lose weight by eating fewer calories and moving more.
Check your body mass index (BMI) online or talk to your team about a healthy weight for you.


5.Live tobacco-free. heart.org/tobacco
Don't smoke, vape or use tobacco products. 
If you don't think you can quit for good on your own, ask for help.
Avoid secondhand smoke, too.


6.Manage conditions. heart.org/conditions
Work closely with your health care team if you have high blood pressure (hypertension), high cholesterol, diabetes or other conditions that put you at greater risk. 
Many conditions can be prevented or managed by eating better, getting active, losing weight and not smoking.


7.Take your medicine
Your doctor may prescribe statins or other medications to help control cholesterol, blood sugar and blood pressure. Take all medications as directed.
Don't take daily aspirin unless your doctor tells you to. 


8.Be a team player.
Your health care team can help you build a prevention plan that works for you.
Make decisions together. Ask questions.

Talk about challenges in your life that may affect your health-like stress, sleep, mental health, family situations, tobacco use, food access, social support and more""")
        else:
          heart_diagnosis = 'The person does not have any heart disease'
          st.success(heart_diagnosis)
          st.header("8 Steps to Prevent Heart Disease ")
          
          
          st.text("""
These key factors can help you live a longer, healthier life and reduce your risk of heart disease and stroke. Theyre part of an overall healthy lifestyle and prevention approach you can build with your health care team (doctors, nurses, pharmacists and other professionals). 


1.Know your risk. heart.org/ccccalculator
If you are 40-75 years old and have never had a heart attack or stroke, use our Check Change Control Calculator to estimate your risk of a cardiovascular event in the next 10 years. 
Certain factors can increase your risk, such as smoking, kidney disease or family history. Many risk factors can be improved with lifestyle changes.


2.Eat a healthy diet. heart.org/eatsmart
Center your eating plan around vegetables, fruits, whole grains, legumes, nuts, plant-based proteins, lean animal proteins and fish. 
Limit sweetened drinks, refined carbohydrates, added sugars, processed meats, sodium and saturated fats. Avoid trans fat.


3.Be physically active. heart.org/movemore
Adults should aim for at least 150 minutes of moderate-intensity aerobic activity or 75 minutes of vigorous activity each week.
If you are already active, increase your intensity for more benefits.
If you are not active now, get started by sitting less and moving more. 


4.Watch your weight. heart.org/weight
If you are overweight, lose weight by eating fewer calories and moving more.
Check your body mass index (BMI) online or talk to your team about a healthy weight for you.


5.Live tobacco-free. heart.org/tobacco
Don't smoke, vape or use tobacco products. 
If you don't think you can quit for good on your own, ask for help.
Avoid secondhand smoke, too.


6.Manage conditions. heart.org/conditions
Work closely with your health care team if you have high blood pressure (hypertension), high cholesterol, diabetes or other conditions that put you at greater risk. 
Many conditions can be prevented or managed by eating better, getting active, losing weight and not smoking.


7.Take your medicine
Your doctor may prescribe statins or other medications to help control cholesterol, blood sugar and blood pressure. Take all medications as directed.
Don't take daily aspirin unless your doctor tells you to. 


8.Be a team player.
Your health care team can help you build a prevention plan that works for you.
Make decisions together. Ask questions.

Talk about challenges in your life that may affect your health-like stress, sleep, mental health, family situations, tobacco use, food access, social support and more""")
          
        
    # st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")

    a=st.button('Attribute Information:')
    if a:
        st.text("""Matrix column entries (attributes)
name - ASCII subject name and recording number
MDVP:Fo(Hz) - Average vocal fundamental frequency
MDVP:Fhi(Hz) - Maximum vocal fundamental frequency
MDVP:Flo(Hz) - Minimum vocal fundamental frequency
MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP - Several measures of variation in fundamental frequency
MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude
NHR,HNR - Two measures of ratio of noise to tonal components in the voice
status - Health status of the subject (one) - Parkinson's, (zero) - healthy
RPDE,D2 - Two nonlinear dynamical complexity measures
DFA - Signal fractal scaling exponent
spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation""")
    

    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')
        
    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
          st.error(parkinsons_diagnosis)
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
          st.success(parkinsons_diagnosis)
        
    # st.success(parkinsons_diagnosis)
















