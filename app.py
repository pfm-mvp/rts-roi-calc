import streamlit as st

st.set_page_config(page_title="PFM ROI Simulator — RTS Edition", page_icon="💡", layout="wide")

st.title("PFM ROI Simulator — RTS Edition")
st.caption("Trade-show friendly ROI calculator for retail conversations.")

st.markdown(
    """
Use the navigation on the left to open the calculator.

### Included in this repo
- EUR / GBP toggle
- All uplift sliders default to 0
- Conversion uplift in 0.5% steps
- Saturday controls tucked into an expander
- TCO logic based on contract term
- Clean event-ready layout for kiosk and demo use

Open **RTS ROI Calculator** in the sidebar to start.
"""
)
