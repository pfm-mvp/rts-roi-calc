# rts-roi-calc

Trade-show ready Streamlit ROI calculator for PFM.

This repo is a clean RTS-specific branch of the existing event ROI concept, created to avoid touching the currently live calculator before the Retail Technology Show.

## What is included

- EUR / GBP toggle
- uplift sliders default to `0`
- conversion uplift in `0.5%` steps
- Saturday controls inside an expander
- TCO based on contract term (`1–10 years`)
- clean event-style layout for kiosk/demo use
- separate page structure for future expansion

## Repo structure

```bash
rts-roi-calc/
├── .devcontainer/
│   └── devcontainer.json
├── .streamlit/
│   └── config.toml
├── pages/
│   └── 01_RTS_ROI_Calculator.py
├── README.md
├── app.py
├── requirements.txt
└── .gitignore
```

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the sidebar and select **RTS ROI Calculator**.

## Main logic

The calculator combines these retail levers:

- footfall
- conversion
- ATV
- gross margin
- contract term / TCO

The output focuses on:

- Revenue / year
- Uplift / year
- Extra profit / year
- Total cost of ownership
- Payback time
- ROI over selected term

## Notes for use at RTS

- Keep the baseline clean first: all uplift sliders start at `0`
- Move one lever at a time during the conversation
- Saturday controls are hidden by default because they are not part of the opening pitch
- Commercial assumptions are available in an expander, so the app stays commercially useful without cluttering the main screen

## Deployment

This repo is suitable for Streamlit Community Cloud.

Main entrypoint:

```text
app.py
```

## Suggested next steps after RTS

- add preset locking for kiosk mode
- add a UK-first default preset if the London version becomes permanent
- add export or screenshot-friendly summary block
- optionally split “expo” and “sales” modes
