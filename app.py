import streamlit as st
import folium
import clipboard

import subprocess
subprocess.run(["apt-get install xclip"]) 


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
col1, col2 = st.columns([0.8, 0.2])
with col1:
    m = folium.Map(location=[37.7749, -122.4194], zoom_start=10)
    folium.ClickForLatLng(format_str='"LATLNG" + lat + "," + lng', alert=False).add_to(m)
    folium.LatLngPopup().add_to(m)
    st.components.v1.html(folium.Figure().add_child(m).render(), height=400)
with col2:
    st.markdown('''
        Click on the map. Once you are satisfied, click on add coordinates.
        More text
        More text
        More text
        More text
        ''')
    st.button('Add coordinates', on_click=click_button)

    if st.session_state.clicked:

        pasted = clipboard.paste()
        st.session_state.clicked = False
        if "LATLNG" in pasted:
            st.session_state.coordinates = pasted[6:]
        else:
            st.session_state.coordinates = ""
            st.write("Click on the map first")
    if st.session_state.coordinates:
        st.write(st.session_state.coordinates)

submitted = st.button("Submit")
