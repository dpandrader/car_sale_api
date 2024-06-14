import pandas as pd
import plotly.express as px
import streamlit as st
      
      
st.header("Car Analysis")
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

hist_button = st.button('Build Histogram') # crear un botón
        
if hist_button: # al hacer clic en el botón
         
    st.write('Creating a Histogram for the Car Sales Advertisements Dataset')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
    
 

scatter_button = st.button('Build Scatter Plot') # crear un botón
        
if scatter_button: # al hacer clic en el botón
           
    st.write('Creating a Scatter Plot for the Car Sales Advertisements Dataset')
            
    # crear gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión

        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)  
    
    
     
    
build_boxplot = st.checkbox('Build boxplot') # crear un botón

if build_boxplot: # al hacer clic en el checkbox
           
    st.write('Creating a boxPlot for the Car Sales Advertisements Dataset') 
    
    fig = px.box(car_data, x="condition", y="price", color="fuel") 
    
    st.plotly_chart(fig, use_container_width=True)   
    