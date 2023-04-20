import streamlit as st
from excel_reader import read_xlsx
from csv_reader import read_csv
from word_reader import read_docx
import pandas as pd



hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

st.header("FastAlyze Chart app")

#adding a selectbox

choice = st.selectbox(

    'Select type of file',

    ('Excel' , 'Word' , 'CSV'))



#displaying the selected option

st.write('You have selected:', choice)

choice_2 = st.selectbox('Select Chart type' , ('Line Chart' , "Area Chart" , "Bar Chart"))
st.write('You have selected:', choice_2)

uploaded_file = st.file_uploader("Choose a file")

def btn_click():

 if uploaded_file is not None :
    aux = choice
    aux_2 = choice_2

    match aux:

        case "Excel":
         df = pd.read_excel(uploaded_file)
         match aux_2:
          case "Line Chart":
               st.line_chart(read_xlsx(df))
               st.table(df)
          case "Area Chart":
               st.area_chart(read_xlsx(df))
               st.table(df)
          case  "Bar Chart":
                st.bar_chart(read_xlsx(df))
                st.table(df)


        case "Word":
         data_frame=[]
         df = read_docx(uploaded_file)
         for i in range(0,len(df),1):
          for j in range(0,len(list(df[i]))):
               data_frame.append(list(df[i][j]))
              
               
         items_to_remove=[]
         for i in range(0,len(data_frame),1):
                   items_to_remove.append(data_frame[i][0])
               
         for item in items_to_remove:
                for i in range(len(data_frame)): 
                 if item in data_frame[i]:
                  data_frame[i].remove(item)
         df_1 = pd.DataFrame(data_frame , columns=items_to_remove)          
         match aux_2:
          case "Line Chart":
               st.line_chart(df_1)
               st.table(df_1)

          case "Area Chart":
               st.area_chart(df_1)
               st.table(df_1)
          case  "Bar Chart":
               st.bar_chart(df_1)
               st.table(df_1)
             

        case "CSV":
         df = pd.read_csv(uploaded_file)
         match aux_2:
          case "Line Chart":
               st.line_chart(read_csv(df))
               st.table(df)
          case "Area Chart":
               st.area_chart(read_csv(df))
               st.table(df)
          case  "Bar Chart":
                st.bar_chart(read_csv(df))
                st.table(df)


open_file_btn = st.button('See Results' , on_click=btn_click)


# folosesc switch statment urile pt fiecare tip de fisier si apoi in fiecare aux case voi face alt switch statement pt a selecta
# tipurile de grafice        

