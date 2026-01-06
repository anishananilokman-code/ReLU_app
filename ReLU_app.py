import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Minimal ReLU Visualization")

x = np.linspace(-10, 10, 100)
y = np.maximum(0, x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('ReLU(x)')
plt.title('ReLU Activation Function')
st.pyplot(plt)