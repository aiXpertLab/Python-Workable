import streamlit as st


t = st.radio("Toggle to see font change", [True, False])

if t:
    st.markdown(
        """
        <style>
            @font-face {
            font-family: 'Tangerine';
            font-style: normal;
            font-weight: 100;
            src: url(https://fonts.gstatic.com/s/tangerine/v12/IurY6Y5j_oScZZow4VOxCZZM.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
            }

    html, body, [class*="css"]  {
    font-family: 'Tangerine';
    font-size: 48px;
    }
    </style>

    """,
        unsafe_allow_html=True,
    )

"# Hello"

"""This font will look different, based on your choice of radio button"""