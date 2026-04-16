import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="PFM ROI Simulator — RTS Edition", page_icon="💡", layout="wide")

PFM_PURPLE = "#762181"
PFM_RED = "#F04438"
PFM_AMBER = "#F59E0B"
PFM_ORANGE = "#FEAC76"
PFM_BLACK = "#0C111D"

BASE_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600;700;800&display=swap');

:root {{
  --pfm-purple: {PFM_PURPLE};
  --pfm-red: {PFM_RED};
  --pfm-orange: {PFM_ORANGE};
  --pfm-black: {PFM_BLACK};
}}

html, body, [class*="css"] {{
  font-family: 'Instrument Sans', sans-serif !important;
  background: #FFFFFF !important;
  color: #0C111D !important;
}}

body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stMain"] {{
  background: #FFFFFF !important;
  color: #0C111D !important;
}}

header {{
  visibility: hidden;
  height: 0 !important;
}}

.block-container {{
  padding-top: 1rem !important;
  padding-bottom: 2rem !important;
}}

.card {{
  border: 1px solid #eee;
  border-radius: 16px;
  padding: 14px 16px;
  background: #FFF7F2;
  box-shadow: 0 1px 2px rgba(0,0,0,0.05);
  min-height: 112px;
}}

.card-outline {{
  border: 1px solid #F5D7C0;
  border-radius: 16px;
  padding: 14px 16px;
  background: white;
  box-shadow: 0 1px 2px rgba(0,0,0,0.04);
  min-height: 112px;
}}

.kpi {{
  font-variant-numeric: tabular-nums;
  font-weight: 800;
  font-size: 1.45rem;
  color: #0C111D;
}}

.kpi-sub {{
  color: #667085;
}}

/* Align Apply preset button vertically */
div[data-testid="stButton"] {{
  margin-top: -24px !important;
}}

.stButton > button {{
  background-color: var(--pfm-red) !important;
  color: white !important;
  border: none !important;
  border-radius: 12px !important;
  font-weight: 700 !important;
  min-height: 44px;
}}

.stSlider [data-baseweb="slider"] > div > div:nth-child(1) {{
  background-color: #FAFAFA !important;
  height: 6px !important;
  border-radius: 3px !important;
}}

.stSlider [data-baseweb="slider"] > div > div:nth-child(2) {{
  background-color: var(--pfm-purple) !important;
  height: 6px !important;
  border-radius: 3px !important;
}}

.stSlider [data-baseweb="slider"] [role="slider"] {{
  background-color: var(--pfm-purple) !important;
  border: 2px solid white !important;
  width: 22px !important;
  height: 22px !important;
  border-radius: 50% !important;
}}

div[data-testid="stExpander"] {{
  border: 1px solid #F2F4F7 !important;
  border-radius: 16px !important;
}}

div[data-testid="stExpander"] details {{
  background: #FFFFFF !important;
  border-radius: 16px !important;
}}

div[data-testid="stExpander"] summary {{
  background: #FFFFFF !important;
  color: #0C111D !important;
  border-radius: 16px !important;
}}

div[data-testid="stExpander"] summary p {{
  color: #0C111D !important;
  -webkit-text-fill-color: #0C111D !important;
}}

div[data-testid="stWidgetLabel"] p {{
  color: #0C111D !important;
  -webkit-text-fill-color: #0C111D !important;
}}

/* Widget labels boven inputs/sliders */
div[data-testid="stWidgetLabel"] {{
  color: #0C111D !important;
}}

div[data-testid="stWidgetLabel"] p {{
  color: #0C111D !important;
  -webkit-text-fill-color: #0C111D !important;
  opacity: 1 !important;
}}

div[data-testid="stWidgetLabel"] label {{
  color: #0C111D !important;
  -webkit-text-fill-color: #0C111D !important;
  opacity: 1 !important;
}}

/* Slider labels en captions */
.stSlider label,
.stNumberInput label,
.stSelectbox label,
.stRadio label {{
  color: #0C111D !important;
  -webkit-text-fill-color: #0C111D !important;
  opacity: 1 !important;
}}

.stNumberInput > div > div > input,
.stTextInput > div > div > input,
div[data-baseweb="input"] input,
div[data-baseweb="base-input"] input {{
  background: #FFFFFF !important;
  color: #0C111D !important;
  -webkit-text-fill-color: #0C111D !important;
}}

.stNumberInput > div > div,
.stTextInput > div > div,
div[data-baseweb="input"],
div[data-baseweb="base-input"] {{
  background: #FFFFFF !important;
  border-radius: 12px !important;
}}

.stSelectbox div[data-baseweb="select"] > div {{
  background: #FFFFFF !important;
  color: #0C111D !important;
}}

.stSelectbox div[data-baseweb="select"] * {{
  color: #0C111D !important;
  -webkit-text-fill-color: #0C111D !important;
}}

.small-note {{
  color: #667085;
  font-size: 0.9rem;
}}
</style>
"""

st.markdown(BASE_CSS, unsafe_allow_html=True)

PRESETS = {
    "Fashion Retail": {
        "visitors_day": 150,
        "conv_pct": 0.16,
        "atv": 45.0,
        "open_days": 6,
        "gross_margin": 0.60,
        "footfall_uplift": 0.00,
        "conversion_uplift": 0.00,
        "atv_uplift": 0.00,
        "sat_share": 0.18,
        "sat_boost": 0.00,
        "desc": "General fashion scenario with moderate traffic and solid basket value.",
    },
    "Optics & Eyewear": {
        "visitors_day": 90,
        "conv_pct": 0.28,
        "atv": 160.0,
        "open_days": 6,
        "gross_margin": 0.68,
        "footfall_uplift": 0.00,
        "conversion_uplift": 0.00,
        "atv_uplift": 0.00,
        "sat_share": 0.17,
        "sat_boost": 0.00,
        "desc": "Higher-ticket retail where conversion and service quality drive the business case.",
    },
    "Sports & Outdoor": {
        "visitors_day": 220,
        "conv_pct": 0.21,
        "atv": 62.0,
        "open_days": 7,
        "gross_margin": 0.56,
        "footfall_uplift": 0.00,
        "conversion_uplift": 0.00,
        "atv_uplift": 0.00,
        "sat_share": 0.20,
        "sat_boost": 0.00,
        "desc": "Traffic-led retail where small uplifts compound quickly across the estate.",
    },
}

DEFAULTS = {
    "currency": "EUR",
    "num_stores": 50,
    "tco_years": 3,
    "visitors_day": 150,
    "conv_pct": 0.16,
    "atv": 45.0,
    "open_days": 6,
    "gross_margin": 0.60,
    "footfall_uplift": 0.00,
    "conversion_uplift": 0.00,
    "atv_uplift": 0.00,
    "sat_share": 0.18,
    "sat_boost": 0.00,
    "install_cost_store": 1500.0,
    "monthly_service_cost_store": 25.0,
    "preset_desc": PRESETS["Fashion Retail"]["desc"],
}

for key, value in DEFAULTS.items():
    st.session_state.setdefault(key, value)


def fmt_money(value: float, currency: str = "EUR", decimals: int = 0) -> str:
    symbol = "€" if currency == "EUR" else "£"
    rounded = round(float(value), decimals)
    if decimals == 0:
        integer_str = f"{int(round(rounded)):,}".replace(",", ".")
        return f"{symbol}{integer_str}"
    formatted = f"{rounded:,.{decimals}f}"
    formatted = formatted.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{symbol}{formatted}"


def fmt_pct(value: float, decimals: int = 1) -> str:
    return f"{value * 100:.{decimals}f}%".replace(".", ",")


def apply_preset(name: str) -> None:
    preset = PRESETS[name]
    for key in [
        "visitors_day",
        "conv_pct",
        "atv",
        "open_days",
        "gross_margin",
        "footfall_uplift",
        "conversion_uplift",
        "atv_uplift",
        "sat_share",
        "sat_boost",
    ]:
        st.session_state[key] = preset[key]
    st.session_state["preset_desc"] = preset["desc"]


st.title("PFM ROI Simulator — RTS Edition")
st.caption("Fast, event-ready ROI calculator for trade show and kiosk conversations.")

st.markdown("#### Preset & scope")
col1, col2, col3, col4 = st.columns([2.1, 0.9, 1.0, 1.1])

with col1:
    preset_name = st.selectbox(
        "Preset profile",
        list(PRESETS.keys()),
        index=0,
        label_visibility="collapsed",
    )

with col2:
    st.session_state["currency"] = st.radio(
        "Currency",
        ["EUR", "GBP"],
        horizontal=True,
        label_visibility="collapsed",
    )
    st.caption("Currency")

with col3:
    st.session_state["num_stores"] = st.number_input(
        "Number of stores",
        min_value=1,
        step=1,
        value=int(st.session_state["num_stores"]),
        label_visibility="collapsed",
    )
    st.caption("Number of stores")

with col4:
    st.markdown("<div style='height: 28px'></div>", unsafe_allow_html=True)
    if st.button("Apply preset", use_container_width=True):
        apply_preset(preset_name)
        st.rerun()

if st.session_state.get("preset_desc"):
    st.info(st.session_state["preset_desc"])

left, right = st.columns([1, 1])

with left:
    st.subheader("Inputs (per store)")
    st.session_state["visitors_day"] = st.number_input(
        "Visitors per day",
        min_value=0,
        step=10,
        value=int(st.session_state["visitors_day"]),
    )
    st.session_state["conv_pct"] = (
        st.slider(
            "Conversion rate (%)",
            min_value=0.0,
            max_value=100.0,
            value=float(round(st.session_state["conv_pct"] * 100, 1)),
            step=0.5,
        )
        / 100.0
    )
    st.session_state["atv"] = st.number_input(
        f"Average ticket value ({'€' if st.session_state['currency']=='EUR' else '£'})",
        min_value=0.0,
        step=1.0,
        value=float(st.session_state["atv"]),
    )
    st.session_state["open_days"] = st.slider(
        "Open days per week",
        min_value=1,
        max_value=7,
        value=int(st.session_state["open_days"]),
        step=1,
    )
    st.session_state["gross_margin"] = (
        st.slider(
            "Gross margin (%)",
            min_value=0,
            max_value=100,
            value=int(round(st.session_state["gross_margin"] * 100)),
            step=1,
        )
        / 100.0
    )
    st.session_state["tco_years"] = st.slider(
        "Contract term / TCO horizon (years)",
        min_value=1,
        max_value=10,
        value=int(st.session_state["tco_years"]),
        step=1,
    )

with right:
    st.subheader("What-if scenarios (apply to all stores)")
    st.session_state["footfall_uplift"] = (
        st.slider(
            "Footfall uplift (%)",
            min_value=0.0,
            max_value=20.0,
            value=float(round(st.session_state["footfall_uplift"] * 100, 1)),
            step=0.5,
        )
        / 100.0
    )
    st.session_state["conversion_uplift"] = (
        st.slider(
            "Conversion uplift (%)",
            min_value=0.0,
            max_value=20.0,
            value=float(round(st.session_state["conversion_uplift"] * 100, 1)),
            step=0.5,
        )
        / 100.0
    )
    st.session_state["atv_uplift"] = (
        st.slider(
            "ATV uplift (%)",
            min_value=0.0,
            max_value=20.0,
            value=float(round(st.session_state["atv_uplift"] * 100, 1)),
            step=0.5,
        )
        / 100.0
    )
    st.markdown('<div class="small-note">All uplift sliders start at 0 to keep the baseline clean and credible.</div>', unsafe_allow_html=True)

with st.expander("Optional Saturday scenario"):
    st.session_state["sat_share"] = (
        st.slider(
            "Share of turnover on Saturdays (%)",
            min_value=0.0,
            max_value=50.0,
            value=float(round(st.session_state["sat_share"] * 100, 1)),
            step=0.5,
        )
        / 100.0
    )
    st.session_state["sat_boost"] = (
        st.slider(
            "Extra conversion on Saturdays (%)",
            min_value=0.0,
            max_value=20.0,
            value=float(round(st.session_state["sat_boost"] * 100, 1)),
            step=0.5,
        )
        / 100.0
    )

with st.expander("Commercial assumptions"):
    st.caption("Visible here for flexibility, but out of the main pitch flow.")
    st.session_state["install_cost_store"] = st.number_input(
        f"One-off install cost per store ({'€' if st.session_state['currency']=='EUR' else '£'})",
        min_value=0.0,
        step=50.0,
        value=float(st.session_state["install_cost_store"]),
    )
    st.session_state["monthly_service_cost_store"] = st.number_input(
        f"Monthly subscription per store ({'€' if st.session_state['currency']=='EUR' else '£'})",
        min_value=0.0,
        step=50.0,
        value=float(st.session_state["monthly_service_cost_store"]),
    )

v = st.session_state
currency = v["currency"]
n_stores = int(v["num_stores"])
visitors_day = float(v["visitors_day"])
conv_pct = float(v["conv_pct"])
atv = float(v["atv"])
open_days = int(v["open_days"])
gross_margin = float(v["gross_margin"])
footfall_uplift = float(v["footfall_uplift"])
conversion_uplift = float(v["conversion_uplift"])
atv_uplift = float(v["atv_uplift"])
sat_share = float(v["sat_share"])
sat_boost = float(v["sat_boost"])
tco_years = int(v["tco_years"])
install_cost_store = float(v["install_cost_store"])
monthly_service_cost_store = float(v["monthly_service_cost_store"])

visitors_day_new = visitors_day * (1 + footfall_uplift)
conv_pct_new = conv_pct * (1 + conversion_uplift)
atv_new = atv * (1 + atv_uplift)

visitors_year_store = visitors_day * open_days * 52
visitors_year_store_new = visitors_day_new * open_days * 52

turnover_year_store = visitors_year_store * conv_pct * atv

non_sat_visitors_new = visitors_year_store_new * (1 - sat_share)
sat_visitors_new = visitors_year_store_new * sat_share
turnover_year_store_new = (
    non_sat_visitors_new * conv_pct_new * atv_new
    + sat_visitors_new * conv_pct_new * (1 + sat_boost) * atv_new
)

uplift_year_store = max(0.0, turnover_year_store_new - turnover_year_store)
extra_profit_year_store = uplift_year_store * gross_margin

turnover_year_total = turnover_year_store * n_stores
turnover_year_total_new = turnover_year_store_new * n_stores
uplift_year_total = uplift_year_store * n_stores
extra_profit_year_total = extra_profit_year_store * n_stores

tco_store = install_cost_store + monthly_service_cost_store * 12 * tco_years
tco_total = tco_store * n_stores
monthly_service_total = monthly_service_cost_store * n_stores
extra_profit_month_total = (uplift_year_total / 12.0) * gross_margin - monthly_service_total
net_value_horizon = extra_profit_year_total * tco_years - tco_total
roi_horizon = net_value_horizon / tco_total if tco_total > 0 else 0.0
payback_months = float("inf")
if extra_profit_month_total > 0:
    payback_months = (install_cost_store * n_stores) / extra_profit_month_total

conv_only_turnover_year_store = (
    non_sat_visitors_new * conv_pct_new * atv
    + sat_visitors_new * conv_pct_new * (1 + sat_boost) * atv
)
footfall_only_turnover_year_store = visitors_year_store_new * conv_pct * atv
atv_only_turnover_year_store = visitors_year_store * conv_pct * atv_new

conv_component = max(0.0, conv_only_turnover_year_store - turnover_year_store) * n_stores
footfall_component = max(0.0, footfall_only_turnover_year_store - turnover_year_store) * n_stores
atv_component = max(0.0, atv_only_turnover_year_store - turnover_year_store) * n_stores
component_sum = max(1e-9, conv_component + footfall_component + atv_component)

k1, k2, k3, k4 = st.columns(4)
with k1:
    st.markdown(
        f'<div class="card"><div><b>Revenue / year</b></div><div class="kpi">{fmt_money(turnover_year_total, currency)}</div><div class="kpi-sub">Baseline for {n_stores} stores</div></div>',
        unsafe_allow_html=True,
    )
with k2:
    st.markdown(
        f'<div class="card"><div><b>Uplift / year</b></div><div class="kpi">{fmt_money(uplift_year_total, currency)}</div><div class="kpi-sub">Scenario versus baseline</div></div>',
        unsafe_allow_html=True,
    )
with k3:
    st.markdown(
        f'<div class="card"><div><b>Extra profit / year</b></div><div class="kpi">{fmt_money(extra_profit_year_total, currency)}</div><div class="kpi-sub">At margin {fmt_pct(gross_margin)}</div></div>',
        unsafe_allow_html=True,
    )
with k4:
    st.markdown(
        f'<div class="card"><div><b>Total cost of ownership</b></div><div class="kpi">{fmt_money(tco_total, currency)}</div><div class="kpi-sub">{tco_years}-year contract horizon</div></div>',
        unsafe_allow_html=True,
    )

k5, k6 = st.columns(2)
with k5:
    payback_txt = "n/a" if payback_months == float("inf") else f"{payback_months:.1f}".replace(".", ",") + " mo"
    st.markdown(
        f'<div class="card-outline"><div><b>Payback time</b></div><div class="kpi">{payback_txt}</div><div class="kpi-sub">Based on monthly extra profit after subscription</div></div>',
        unsafe_allow_html=True,
    )
with k6:
    st.markdown(
        f'<div class="card-outline"><div><b>ROI over {tco_years} years</b></div><div class="kpi">{fmt_pct(roi_horizon)}</div><div class="kpi-sub">Net value: {fmt_money(net_value_horizon, currency)}</div></div>',
        unsafe_allow_html=True,
    )

st.markdown("### Visuals")

baseline_fmt = fmt_money(turnover_year_total, currency)
scenario_fmt = fmt_money(turnover_year_total_new, currency)

fig_bar = go.Figure()
fig_bar.add_trace(
    go.Bar(
        name="Baseline",
        x=["Annual revenue"],
        y=[turnover_year_total],
        marker_color=PFM_AMBER,
        text=[baseline_fmt],
        textposition="outside",
        customdata=[[baseline_fmt]],
        hovertemplate="Baseline: %{customdata[0]}<extra></extra>",
    )
)
fig_bar.add_trace(
    go.Bar(
        name="Scenario",
        x=["Annual revenue"],
        y=[turnover_year_total_new],
        marker_color=PFM_PURPLE,
        text=[scenario_fmt],
        textposition="outside",
        customdata=[[scenario_fmt]],
        hovertemplate="Scenario: %{customdata[0]}<extra></extra>",
    )
)
fig_bar.update_layout(
    barmode="group",
    height=420,
    margin=dict(l=20, r=20, t=10, b=10),
    legend=dict(orientation="h"),
)
st.plotly_chart(fig_bar, use_container_width=True)

fig_pie = go.Figure(
    data=[
        go.Pie(
            labels=["Footfall", "Conversion", "ATV"],
            values=[
                footfall_component / component_sum,
                conv_component / component_sum,
                atv_component / component_sum,
            ],
            hole=0.55,
            marker=dict(colors=[PFM_AMBER, PFM_RED, PFM_PURPLE]),
            textinfo="percent+label",
            customdata=[
                [fmt_money(footfall_component, currency)],
                [fmt_money(conv_component, currency)],
                [fmt_money(atv_component, currency)],
            ],
            hovertemplate="%{label}: %{percent} — uplift %{customdata[0]}<extra></extra>",
        )
    ]
)
fig_pie.update_layout(height=400, margin=dict(l=20, r=20, t=10, b=10), showlegend=True)
st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("### Recommended talk track")
recs = []
if uplift_year_total <= 0:
    recs.append("Start clean: keep all three uplifts at zero, then move one lever at a time.")
if conversion_uplift > 0 and conversion_uplift >= max(footfall_uplift, atv_uplift):
    recs.append("Conversion is the strongest story here. That lands well when you position PFM as improving store execution.")
if footfall_uplift > max(conversion_uplift, atv_uplift):
    recs.append("Footfall is doing most of the work. Good bridge into campaigns, events or local activation.")
if atv_uplift > max(footfall_uplift, conversion_uplift):
    recs.append("ATV is the main lever. Use that when the conversation is about cross-sell, upsell or service quality.")
if payback_years != float("inf") and payback_years < 1:
    recs.append("Payback under 12 months. That is exactly the kind of line people repeat after they leave the stand.")
if sat_boost > 0:
    recs.append("Saturday controls are active, but hidden by default. Sensible. Saturday is a side story, not the opening act.")
if not recs:
    recs.append("Use one metric change at a time. Cleaner story, stronger credibility.")

for rec in recs:
    st.write(f"- {rec}")
