import streamlit as st
import folium
import clipboard

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

if 'coordinates' not in st.session_state:
    st.session_state.coordinates = ""

def click_button():
    st.session_state.clicked = True
    
st.title("POC")
value = st.number_input("Insert a number")
checkbox_val = st.checkbox("Form checkbox")
option = st.selectbox(
	"How would you like to be contacted?",
	("Email", "Home phone", "Mobile phone"),
)


# map   
import folium as fl
from streamlit_folium import st_folium
import streamlit as st

m = fl.Map()

m.add_child(fl.LatLngPopup())

maps = st_folium(m, height=350, width=700)

if maps['last_clicked']:
    lat = maps['last_clicked']['lat']
    lng = maps['last_clicked']['lng']
    st.write(f'{lat}, {lng}')

submitted = st.button("Submit")

