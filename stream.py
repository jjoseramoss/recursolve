import streamlit as st
import numpy as np
from solver import linear_recurrence

st.title("Recursolve")
st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    c1 = st.number_input("First Constant:", 0, 10)

with col2:
    c2 = st.number_input("Second Constant:", 0, 10)

with col3:
    c3 = st.number_input("Base Case:", 0, 100)


st.write("Recurrence Relation: ")
st.latex("a_n = "+str(c1)+"a_{n-1}"+"+ " +str(c2))
st.markdown(f"<div style='text-align: center'>Base Case: {c3}</div> ", unsafe_allow_html=True)
#create equation
eq1 = linear_recurrence(c1, c2, c3)

if st.button("Solve", type="primary"):
    st.write(eq1.solve_recurrence(20))


