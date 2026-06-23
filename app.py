import streamlit as st
import pandas as pd

from states import US_STATES
from utils import generate_addresses

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Property Address Generator",
    page_icon="🏠",
    layout="wide"
)

# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.title("🏠 AI Property Address Generator")

st.write(
    "Generate realistic property addresses across all U.S. states for QA testing."
)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------
# Input Section
# ---------------------------------------------------

with st.container(border=True):

    col1, col2, col3 = st.columns([2, 1, 3])

    with col1:
        state = st.selectbox(
            "Select State",
            US_STATES
        )

    with col2:
        count = st.number_input(
            "Number of Addresses",
            min_value=1,
            max_value=100,
            value=10
        )

    st.markdown("<br>", unsafe_allow_html=True)

    generate = st.button(
        "🏠 Generate Addresses",
        type="primary"
    )

# ---------------------------------------------------
# Generate Addresses
# ---------------------------------------------------

if generate:

    with st.spinner("Generating addresses..."):

        try:

            addresses = generate_addresses(
                state,
                count
            )

            df = pd.DataFrame(addresses)

            st.success(
                f"{len(df)} addresses generated successfully."
            )

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            csv = df.to_csv(
                index=False
            )

            st.download_button(
                label="📥 Export CSV",
                data=csv,
                file_name=f"{state}_Addresses.csv",
                mime="text/csv"
            )

        except Exception as e:

            st.error(
                f"Error generating addresses: {str(e)}"
            )
