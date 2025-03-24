import folium
from streamlit_folium import st_folium
import streamlit as st

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


m = folium.Map()
m.add_child(folium.LatLngPopup())
maps = st_folium(m, height=350, width=700)

if maps['last_clicked']:
    lat = maps['last_clicked']['lat']
    lng = maps['last_clicked']['lng']
    st.write(f'{lat}, {lng}')

submitted = st.button("Submit")

