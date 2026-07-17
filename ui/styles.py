"""
Shared Streamlit styling helpers.
"""

import streamlit as st


def load_css():

    st.markdown(
        """
<style>

/*==================================================
Google Font
==================================================*/

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');


/*==================================================
Global
==================================================*/

html,
body,
[class*="css"]{

    font-family:'Inter',sans-serif;
    color:#2D3A4A;

}


/*==================================================
Background
==================================================*/

.stApp{

background:
radial-gradient(circle at top left,#EAF8FF 0%,transparent 35%),
radial-gradient(circle at top right,#BEE9FF 0%,transparent 30%),
linear-gradient(
135deg,
#F7FCFF,
#E8F8FF,
#D4F1FF,
#C4EAFF,
#E9F8FF,
#FCFEFF);

background-attachment:fixed;

}


/*==================================================
Main Container
==================================================*/

.block-container{

padding-top:2rem;
padding-bottom:2rem;
max-width:1400px;

}


/*==================================================
Headings
==================================================*/

h1{

font-size:42px;

font-weight:800;

color:#1565C0;

letter-spacing:-1px;

}

h2{

font-size:30px;

font-weight:700;

color:#1976D2;

}

h3{

font-size:22px;

font-weight:600;

color:#1E88E5;

}

p{

font-size:16px;

line-height:1.7;

color:#546E7A;

}


/*==================================================
Hero Banner
==================================================*/

.hero{

background:rgba(255,255,255,.85);

backdrop-filter:blur(18px);

padding:42px;

border-radius:24px;

border:1px solid rgba(255,255,255,.55);

box-shadow:

0 15px 40px rgba(21,101,192,.08);

margin-bottom:35px;

text-align:center;

}


/*==================================================
Cards
==================================================*/

.card{

background:white;

padding:28px;

border-radius:22px;

border:1px solid #DCEFFF;

box-shadow:

0 8px 25px rgba(30,80,120,.08);

transition:.3s;

margin-bottom:20px;

}

.card:hover{

transform:translateY(-5px);

box-shadow:

0 18px 35px rgba(30,120,200,.15);

}


/*==================================================
Buttons
==================================================*/

.stButton>button{

width:100%;

height:58px;

font-size:18px;

font-weight:700;

border-radius:14px;

background:

linear-gradient(
90deg,
#1FAFFF,
#63D3FF);

color:white;

border:none;

transition:.3s;

}

.stButton>button:hover{

transform:translateY(-2px);

box-shadow:

0 12px 25px rgba(31,175,255,.35);

}


/*==================================================
Text Areas
==================================================*/

div[data-baseweb="textarea"]{

border-radius:15px;

border:1px solid #D7EBFA;

background:#FCFEFF;

}


/*==================================================
Text Inputs
==================================================*/

input{

border-radius:12px !important;

}


/*==================================================
Select Boxes
==================================================*/

div[data-baseweb="select"]{

border-radius:12px;

}


/*==================================================
Metrics
==================================================*/

[data-testid="stMetric"]{

background:white;

padding:15px;

border-radius:16px;

border:1px solid #DCEFFF;

box-shadow:

0 5px 15px rgba(0,0,0,.05);

}


/*==================================================
Sidebar
==================================================*/

[data-testid="stSidebar"]{

background:

linear-gradient(
180deg,
#F9FDFF,
#EAF8FF);

border-right:1px solid #D7EBFA;

padding-top:20px;

}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3{

color:#1976D2;

font-weight:700;

}


/*==================================================
File Uploader
==================================================*/

[data-testid="stFileUploader"]{

background:white;

padding:20px;

border-radius:18px;

border:2px dashed #78CFFF;

transition:.3s;

}

[data-testid="stFileUploader"]:hover{

background:#F8FDFF;

}


/*==================================================
Alerts
==================================================*/

.stSuccess{

border-radius:14px;

border-left:6px solid #2ECC71;

}

.stWarning{

border-radius:14px;

border-left:6px solid #F39C12;

}

.stError{

border-radius:14px;

border-left:6px solid #E74C3C;

}


/*==================================================
Spinner
==================================================*/

[data-testid="stSpinner"]{

color:#1E88E5;

font-weight:700;

}


/*==================================================
Horizontal Divider
==================================================*/

hr{

border:none;

height:1px;

background:#D6ECFF;

margin:35px 0;

}


/*==================================================
Audio Player
==================================================*/

audio{

width:100%;

border-radius:14px;

}


/*==================================================
Scrollbar
==================================================*/

::-webkit-scrollbar{

width:10px;

}

::-webkit-scrollbar-thumb{

background:#8FD7FF;

border-radius:20px;

}

::-webkit-scrollbar-track{

background:#F4FBFF;

}


/*==================================================
Transitions
==================================================*/

*{

transition:all .2s ease;

}

</style>
""",
        unsafe_allow_html=True,
    )