op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0]) 
