import streamlit as st
import pandas as pd

st.set_page_config(page_title="S-OIL OA Simulator", page_icon="🛢️", layout="wide")

# =========================================================
# 1) EMBEDDED DATA
# =========================================================
# 아래 UNIT_DATA에 엑셀의 각 유닛 row를 그대로 넣으면,
# 이후에는 엑셀 파일 없이도 앱이 동작합니다.
#
# 각 row 형식:
# {
#   "plant": "정유/윤활/아로공장",
#   "unit_code": "U-1100",
#   "unit_name": "#1 CDU",
#   "unit_desc": "설명",
#   "all": {
#       "Refinery": -0.010,
#       "#1Complex": -0.012,
#       "정유/윤활/아로공장": -0.015,
#       "HYC공장": 0.0,
#       "RFCC1공장": 0.0,
#       "#2Complex": 0.0,
#       "RFCC2공장": 0.0,
#       "아로마틱2공장": 0.0,
#       "폴리머공장": 0.0,
#   },
#   "major": {
#       "Refinery": -0.020,
#       "#1Complex": -0.022,
#       "정유/윤활/아로공장": -0.030,
#       "HYC공장": 0.0,
#       "RFCC1공장": 0.0,
#       "#2Complex": 0.0,
#       "RFCC2공장": 0.0,
#       "아로마틱2공장": 0.0,
#       "폴리머공장": 0.0,
#   }
# }

UNIT_DATA = [
    {
        "plant": "정유/윤활/아로공장",
        "unit_code": "U-1100",
        "unit_name": "#1 CDU",
        "unit_desc": "Sample",
        "all": {
            "Refinery": -0.010,
            "#1Complex": -0.012,
            "정유/윤활/아로공장": -0.015,
            "HYC공장": 0.0,
            "RFCC1공장": 0.0,
            "#2Complex": 0.0,
            "RFCC2공장": 0.0,
            "아로마틱2공장": 0.0,
            "폴리머공장": 0.0,
        },
        "major": {
            "Refinery": -0.020,
            "#1Complex": -0.022,
            "정유/윤활/아로공장": -0.030,
            "HYC공장": 0.0,
            "RFCC1공장": 0.0,
            "#2Complex": 0.0,
            "RFCC2공장": 0.0,
            "아로마틱2공장": 0.0,
            "폴리머공장": 0.0,
        },
    },
    {
        "plant": "HYC공장",
        "unit_code": "U-2100",
        "unit_name": "#1 HDS",
        "unit_desc": "Sample",
        "all": {
            "Refinery": -0.008,
            "#1Complex": -0.010,
            "정유/윤활/아로공장": 0.0,
            "HYC공장": -0.020,
            "RFCC1공장": 0.0,
            "#2Complex": 0.0,
            "RFCC2공장": 0.0,
            "아로마틱2공장": 0.0,
            "폴리머공장": 0.0,
        },
        "major": {
            "Refinery": -0.015,
            "#1Complex": -0.018,
            "정유/윤활/아로공장": 0.0,
            "HYC공장": -0.035,
            "RFCC1공장": 0.0,
            "#2Complex": 0.0,
            "RFCC2공장": 0.0,
            "아로마틱2공장": 0.0,
            "폴리머공장": 0.0,
        },
    },
    {
        "plant": "RFCC1공장",
        "unit_code": "U-3100",
        "unit_name": "PO",
        "unit_desc": "Sample",
        "all": {
            "Refinery": -0.012,
            "#1Complex": -0.014,
            "정유/윤활/아로공장": 0.0,
            "HYC공장": 0.0,
            "RFCC1공장": -0.030,
            "#2Complex": 0.0,
            "RFCC2공장": 0.0,
            "아로마틱2공장": 0.0,
            "폴리머공장": 0.0,
        },
        "major": {
            "Refinery": -0.024,
            "#1Complex": -0.028,
            "정유/윤활/아로공장": 0.0,
            "HYC공장": 0.0,
            "RFCC1공장": -0.050,
            "#2Complex": 0.0,
            "RFCC2공장": 0.0,
            "아로마틱2공장": 0.0,
            "폴리머공장": 0.0,
        },
    },
]

PLANT_OPTIONS = [
    "정유/윤활/아로공장",
    "HYC공장",
    "RFCC1공장",
    "RFCC2공장",
    "아로마틱2공장",
    "폴리머공장",
]

SUMMARY_ORDER = [
    "Refinery",
    "#1Complex",
    "정유/윤활/아로공장",
    "HYC공장",
    "RFCC1공장",
    "#2Complex",
    "RFCC2공장",
    "아로마틱2공장",
    "폴리머공장",
]

# =========================================================
# 2) TARGET / CURRENT
# =========================================================
TARGET_MAJOR = {
    "Refinery": 95.6,
    "#1Complex": 96.2,
    "정유/윤활/아로공장": 96.7,
    "HYC공장": 96.4,
    "RFCC1공장": 94.9,
    "#2Complex": 95.1,
    "RFCC2공장": 94.3,
    "아로마틱2공장": 96.7,
    "폴리머공장": 95.2,
}

TARGET_ALL = {
    "Refinery": 96.1,
    "#1Complex": 96.5,
    "정유/윤활/아로공장": 96.7,
    "HYC공장": 97.0,
    "RFCC1공장": 95.9,
    "#2Complex": 95.5,
    "RFCC2공장": 94.6,
    "아로마틱2공장": 96.6,
    "폴리머공장": 95.0,
}

CURRENT_MAJOR = {k: round(v + 0.3, 1) for k, v in TARGET_MAJOR.items()}
CURRENT_ALL = {k: round(v + 0.3, 1) for k, v in TARGET_ALL.items()}

DEFAULT_TARGET = 96.0
DEFAULT_CURRENT = 96.3

# =========================================================
# 3) UI
# =========================================================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #f5f7fb 0%, #eef2f7 100%);
    }

    .block-container {
        max-width: 1400px;
        padding-top: 0.7rem;
        padding-bottom: 1rem;
    }

    .hero-box {
        background: rgba(255,255,255,0.92);
        border: 1px solid #e5e7eb;
        border-radius: 24px;
        padding: 20px 24px;
        box-shadow: 0 8px 24px rgba(15,23,42,0.05);
        margin-bottom: 14px;
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 850;
        color: #0f172a;
        margin: 0;
        letter-spacing: -0.04em;
        line-height: 1.05;
    }

    .hero-subtitle {
        font-size: 0.92rem;
        color: #64748b;
        margin-top: 8px;
        line-height: 1.45;
    }

    .section-card {
        background: rgba(255,255,255,0.90);
        border: 1px solid #e7ebf0;
        border-radius: 20px;
        padding: 14px 16px;
        box-shadow: 0 8px 20px rgba(15,23,42,0.04);
        margin-bottom: 14px;
    }

    .section-title {
        font-size: 1rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 4px;
    }

    .section-note {
        font-size: 0.84rem;
        color: #64748b;
        margin-bottom: 10px;
    }

    .metric-box {
        background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
        border: 1px solid #fdba74;
        border-radius: 18px;
        padding: 14px 16px;
        box-shadow: 0 6px 16px rgba(249,115,22,0.06);
        min-height: 96px;
    }

    .metric-label {
        font-size: 0.84rem;
        font-weight: 700;
        color: #9a3412;
        margin-bottom: 8px;
    }

    .metric-number {
        font-size: 2.05rem;
        font-weight: 850;
        color: #0f172a;
        letter-spacing: -0.04em;
        line-height: 1.0;
    }

    .table-title {
        font-size: 1rem;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 8px;
    }

    div.stButton > button {
        border-radius: 12px !important;
        font-weight: 700 !important;
        height: 2.25rem !important;
        border: 1px solid #d9e0e8 !important;
        background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%) !important;
        color: #0f172a !important;
        box-shadow: 0 2px 8px rgba(15,23,42,0.04);
        font-size: 0.86rem !important;
    }

    div[data-baseweb="select"] > div {
        border-radius: 12px !important;
        min-height: 40px !important;
        border-color: #d7dee7 !important;
        background: rgba(255,255,255,0.99) !important;
        color: #111827 !important;
        box-shadow: none !important;
    }

    div[data-baseweb="input"] > div {
        border-radius: 12px !important;
        min-height: 40px !important;
        border-color: #d7dee7 !important;
        background: rgba(255,255,255,0.99) !important;
        color: #111827 !important;
        box-shadow: none !important;
    }

    input {
        color: #111827 !important;
        font-size: 0.93rem !important;
    }

    div[data-testid="stVerticalBlock"] > div:empty {
        display: none !important;
    }

    hr {
        display: none !important;
    }

    [data-testid="stMetricDelta"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-box">
        <div class="hero-title">S-OIL OA Simulator</div>
        <div class="hero-subtitle">공장 선택 후 해당 Unit과 설명을 선택하고, 정지 일수 및 T&I / Non-T&I 조건에 따라 All / Major 영향을 계산합니다.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================================================
# 4) HELPERS
# =========================================================
def units_by_plant(plant: str) -> list[str]:
    subset = [row for row in UNIT_DATA if row["plant"] == plant]
    return [
        f'{row["unit_code"]} | {row["unit_name"]} | {row["unit_desc"]}'
        for row in subset
        if str(row["unit_code"]).strip()
    ]

def row_by_unit_display(unit_display: str):
    for row in UNIT_DATA:
        display = f'{row["unit_code"]} | {row["unit_name"]} | {row["unit_desc"]}'
        if display == unit_display:
            return row
    return None

def new_row():
    default_plant = PLANT_OPTIONS[0]
    unit_opts = units_by_plant(default_plant)
    default_unit = unit_opts[0] if unit_opts else ""
    return {"plant": default_plant, "unit": default_unit, "days": 1.0, "mode": "Non-T&I"}

def get_ti_factor(plant_name: str, unit_name: str, mode: str) -> float:
    if mode == "Non-T&I":
        return 1.0
    if plant_name in {"RFCC1공장", "RFCC2공장"}:
        return 1.0 / 3.0
    if unit_name.strip().upper() == "PO":
        return 1.0 / 3.0
    return 1.0 / 4.0

def get_target(label: str, mode: str) -> float:
    if mode == "all":
        return float(TARGET_ALL.get(label, DEFAULT_TARGET))
    return float(TARGET_MAJOR.get(label, DEFAULT_TARGET))

def get_current(label: str, mode: str) -> float:
    if mode == "all":
        return float(CURRENT_ALL.get(label, DEFAULT_CURRENT))
    return float(CURRENT_MAJOR.get(label, DEFAULT_CURRENT))

def prettify_label(label: str) -> str:
    if label == "Refinery":
        return "Refinery"
    if "Complex" in label:
        return "   " + label
    return "      • " + label

def build_summary_df(headers, impact_map, mode: str):
    rows = []
    for h in headers:
        target = get_target(h, mode=mode)
        current = get_current(h, mode=mode)
        impact = float(impact_map.get(h, 0.0))
        forecast = current + impact
        signal = "🔴" if forecast < target else "🟢"
        rows.append({
            "구분": prettify_label(h),
            "Target": f"{target:.1f}",
            "현재 추정": f"{current:.1f}",
            "Forecast Impact": "" if abs(impact) < 1e-12 else f"{impact:,.3f}",
            "변동": f"{forecast:,.2f} {signal}",
            "__raw__": h,
        })
    return pd.DataFrame(rows)

def style_summary_df(df: pd.DataFrame):
    raw_labels = df["__raw__"].tolist()
    display_df = df.drop(columns=["__raw__"]).copy()

    def highlight_rows(row):
        raw_label = raw_labels[row.name]
        if raw_label == "Refinery":
            return ["border:2px solid black; font-weight:700; background-color:#f8fafc"] * len(row)
        return [""] * len(row)

    return (
        display_df.style
        .hide(axis="index")
        .apply(highlight_rows, axis=1)
        .set_table_styles([
            {
                "selector": "table",
                "props": [
                    ("border-collapse", "collapse"),
                    ("width", "100%"),
                    ("font-size", "15px"),
                    ("background-color", "#ffffff"),
                    ("color", "#111827"),
                ],
            },
            {
                "selector": "thead th",
                "props": [
                    ("background-color", "#dfe7f2"),
                    ("color", "#111827"),
                    ("font-size", "15px"),
                    ("font-weight", "700"),
                    ("padding", "10px 10px"),
                    ("text-align", "center"),
                    ("border", "1px solid #cfd8e3"),
                ],
            },
            {
                "selector": "tbody td",
                "props": [
                    ("font-size", "15px"),
                    ("color", "#111827"),
                    ("padding", "9px 10px"),
                    ("border", "1px solid #d7dde6"),
                    ("background-color", "#ffffff"),
                ],
            },
            {
                "selector": "tbody tr:nth-child(even) td",
                "props": [("background-color", "#fafcff")],
            },
        ])
    )

# =========================================================
# 5) SESSION STATE
# =========================================================
if "rows_main" not in st.session_state:
    st.session_state.rows_main = [new_row()]

# =========================================================
# 6) INPUT
# =========================================================
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">입력</div>', unsafe_allow_html=True)
st.markdown('<div class="section-note">공장을 먼저 선택한 뒤, 오른쪽 Unit 목록에서 해당 공장의 Unit과 설명을 선택하세요.</div>', unsafe_allow_html=True)

top_btn_col, _ = st.columns([0.14, 0.86])
with top_btn_col:
    if st.button("행 추가", use_container_width=True):
        st.session_state.rows_main.append(new_row())
        st.rerun()

delete_idx = None
updated_rows = []

for i, row in enumerate(st.session_state.rows_main):
    c1, c2, c3, c4, c5 = st.columns([0.45, 1.0, 1.8, 0.9, 0.8], gap="small")

    with c1:
        if len(st.session_state.rows_main) > 1:
            if st.button("삭제", key=f"del_{i}", use_container_width=True):
                delete_idx = i

    with c2:
        plant = st.selectbox(
            f"공장 {i+1}",
            PLANT_OPTIONS,
            index=PLANT_OPTIONS.index(row["plant"]) if row["plant"] in PLANT_OPTIONS else 0,
            key=f"plant_{i}",
        )

    unit_options = units_by_plant(plant)
    current_unit = row["unit"] if row["unit"] in unit_options else (unit_options[0] if unit_options else "")

    with c3:
        unit = st.selectbox(
            f"Unit {i+1}",
            unit_options,
            index=unit_options.index(current_unit) if current_unit in unit_options and unit_options else 0,
            key=f"unit_{i}",
        )

    with c4:
        mode = st.selectbox(
            f"구분 {i+1}",
            ["Non-T&I", "T&I"],
            index=["Non-T&I", "T&I"].index(row["mode"]) if row["mode"] in ["Non-T&I", "T&I"] else 0,
            key=f"mode_{i}",
        )

    with c5:
        days = st.number_input(
            f"정지 일수 {i+1}",
            min_value=0.0,
            step=0.1,
            value=float(row["days"]),
            format="%.1f",
            key=f"days_{i}",
        )

    updated_rows.append({
        "plant": plant,
        "unit": unit,
        "days": float(days),
        "mode": mode,
    })

if delete_idx is not None:
    updated_rows.pop(delete_idx)
    st.session_state.rows_main = updated_rows if updated_rows else [new_row()]
    st.rerun()
else:
    st.session_state.rows_main = updated_rows

st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# 7) CALCULATION
# =========================================================
all_impact_map = {h: 0.0 for h in SUMMARY_ORDER}
major_impact_map = {h: 0.0 for h in SUMMARY_ORDER}

for row in st.session_state.rows_main:
    matched_row = row_by_unit_display(row["unit"])
    if matched_row is None:
        continue

    plant_name = str(matched_row["plant"]).strip()
    unit_name = str(matched_row["unit_name"]).strip()
    factor = get_ti_factor(plant_name, unit_name, row["mode"])

    for h in SUMMARY_ORDER:
        all_impact_map[h] += float(matched_row["all"].get(h, 0.0)) * row["days"] * factor
        major_impact_map[h] += float(matched_row["major"].get(h, 0.0)) * row["days"] * factor

major_refinery = float(major_impact_map.get("Refinery", 0.0))
all_refinery = float(all_impact_map.get("Refinery", 0.0))

# =========================================================
# 8) SUMMARY
# =========================================================
st.subheader("요약")

m1, m2 = st.columns(2, gap="large")
with m1:
    st.markdown(
        f"""
        <div class="metric-box">
            <div class="metric-label">Major Refinery Impact</div>
            <div class="metric-number">{major_refinery:,.3f}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with m2:
    st.markdown(
        f"""
        <div class="metric-box">
            <div class="metric-label">All Refinery Impact</div>
            <div class="metric-number">{all_refinery:,.3f}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

major_df = build_summary_df(SUMMARY_ORDER, major_impact_map, mode="major")
all_df = build_summary_df(SUMMARY_ORDER, all_impact_map, mode="all")

t1, t2 = st.columns(2, gap="large")
with t1:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="table-title">Major</div>', unsafe_allow_html=True)
    st.dataframe(style_summary_df(major_df), use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with t2:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="table-title">All Unit</div>', unsafe_allow_html=True)
    st.dataframe(style_summary_df(all_df), use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)