import folium
from streamlit_folium import st_folium
import streamlit as st
from PIL import Image
from google.oauth2 import service_account
from googleapiclient.discovery import build

from googleapiclient.http import MediaIoBaseUpload
import io
import os



service_account_info = {
    "type": st.secrets["type"],
    "project_id": st.secrets["project_id"],
    "private_key_id": st.secrets["private_key_id"],
    "private_key": st.secrets["private_key"].replace('\\n', '\n') if st.secrets["private_key"] else None,
    "client_email": st.secrets["client_email"],
    "client_id": st.secrets["client_id"],
    "auth_uri": st.secrets["auth_uri"],
    "token_uri": st.secrets["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["client_x509_cert_url"],
    "universe_domain": st.secrets["universe_domain"]
}

# Ensure private_key is properly formatted
if not service_account_info["private_key"]:
    raise ValueError("Missing or improperly formatted private key")

creds = service_account.Credentials.from_service_account_info(service_account_info)

service = build('drive', 'v3', credentials=creds)

st.markdown(
    """
    <style>
        footer {display: none}
        [data-testid="stHeader"] {display: none}
        body { 
  color: blue;
}
    </style>
    """, unsafe_allow_html = True
)

st.write("hh")
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


img_file_buffer = st.file_uploader('Upload a PNG image', type='png')

submitted = st.button("Submit")

if img_file_buffer and submitted:
    # Convert file buffer to a binary stream
    img_bytes = io.BytesIO(img_file_buffer.getvalue())
    
    media = MediaIoBaseUpload(img_bytes, mimetype='image/png', resumable=True)
    request = service.files().create(
        media_body=media,
        body={'name': img_file_buffer.name, 'parents': ['1p_MOQsdzhW3bRCwRTsyeydHOz0LvfeVq']}
    )
    
    file = request.execute()
