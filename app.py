
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Elevate | Profit Intelligence",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f4f6fa;
}
.block-container {
    padding-top: 2rem;
}
h1, h2, h3 {
    color: #15263d;
}
[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border: 1px solid #dfe5ee;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title("ELEVATE CORPORATE DYNAMICS")
st.subheader("PROFIT INTELLIGENCE")
st.caption("BUSINESS PERFORMANCE | FINANCIAL CLARITY | ACTION")
st.write("Executive financial diagnostic")

with st.sidebar:
    st.header("Business profile")

    business = st.text_input("Business name", "Demo Business")
    industry = st.selectbox(
        "Industry",
        ["Retail", "Hospitality", "Professional services",
         "Construction", "Manufacturing", "Distribution", "Other"]
    )
    currency = st.selectbox(
        "Currency", ["EUR", "USD", "GBP", "XCD", "CAD"]
    )
    period = st.selectbox(
        "Reporting period", ["Monthly", "Quarterly", "Annual"]
    )

    st.divider()
    st.caption("Use figures from the same reporting period.")

    revenue = st.number_input(
        "Revenue", min_value=0.0, value=100000.0, step=1000.0
    )
    direct_costs = st.number_input(
        "Direct costs", min_value=0.0, value=40000.0, step=1000.0
    )
    operating_expenses = st.number_input(
        "Operating expenses", min_value=0.0, value=35000.0, step=1000.0
    )
    fixed_costs = st.number_input(
        "Fixed costs included in operating expenses",
        min_value=0.0, value=20000.0, step=1000.0
    )
    challenge = st.selectbox(
        "Main challenge",
        ["Reducing costs", "Improving margins", "Cash flow",
         "Pricing", "Growth", "Operational efficiency", "Not sure"]
    )

if fixed_costs > operating_expenses:
    st.error("Fixed costs cannot exceed operating expenses.")
    st.stop()

gross_profit = revenue - direct_costs
operating_profit = gross_profit - operating_expenses

gross_margin = gross_profit / revenue * 100 if revenue else 0
operating_margin = operating_profit / revenue * 100 if revenue else 0
direct_cost_share = direct_costs / revenue * 100 if revenue else 0

contribution_margin = (
    (revenue - direct_costs) / revenue if revenue else 0
)
break_even = (
    fixed_costs / contribution_margin
    if contribution_margin > 0 else None
)

st.caption(
    f"{industry} | {period} | Report date: {date.today().isoformat()}"
)
st.divider()

st.header("Executive performance overview")
st.write(f"**Business:** {business or 'Not specified'}")

col1, col2, col3 = st.columns(3)
col1.metric("Revenue", f"{currency} {revenue:,.2f}")
col2.metric("Gross profit", f"{currency} {gross_profit:,.2f}")
col3.metric("Operating profit", f"{currency} {operating_profit:,.2f}")

col4, col5, col6 = st.columns(3)
col4.metric("Gross margin", f"{gross_margin:.1f}%")
col5.metric("Operating margin", f"{operating_margin:.1f}%")
col6.metric("Direct costs / revenue", f"{direct_cost_share:.1f}%")

st.divider()
st.header("Profit intelligence")

if revenue == 0:
    st.warning("Enter revenue above zero for meaningful calculations.")
elif operating_profit < 0:
    st.warning(
        "The operating result is negative. Review revenue, direct costs "
        "and operating expenses."
    )
elif operating_margin < 10:
    st.warning(
        "Operating margin is below 10%. Investigate pricing and costs, "
        "and compare against a suitable industry benchmark."
    )
else:
    st.success(
        "The operating result is positive. Compare several periods "
        "before judging whether performance is sustainable."
    )

if direct_cost_share > 60:
    st.write(
        "**Review direct costs:** They exceed 60% of revenue. "
        "Investigate purchasing, waste, supplier prices and product mix. "
        "This is a warning indicator, not proof of waste."
    )

if revenue > 0:
    expense_share = operating_expenses / revenue * 100
    st.write(f"Operating expenses represent {expense_share:.1f}% of revenue.")

if break_even is not None:
    st.write(
        f"**Indicative break-even revenue:** {currency} {break_even:,.2f}"
    )
    st.caption(
        "Estimate assumes direct costs vary with revenue and fixed costs "
        "remain constant. Actual results may differ."
    )
else:
    st.write("Break-even estimate unavailable with the current figures.")

st.divider()
st.header("Recommended next actions")

for action in [
    "Validate the figures against accounting records.",
    "Compare results with previous reporting periods.",
    "Investigate the largest expense categories.",
    "Choose one measurable improvement.",
    "Review the result next period."
]:
    st.write(f"• {action}")

report = f"""
ELEVATE CORPORATE DYNAMICS
PROFIT INTELLIGENCE — PRELIMINARY REPORT

Business: {business}
Industry: {industry}
Reporting period: {period}
Date: {date.today().isoformat()}
Currency: {currency}

Revenue: {revenue:,.2f}
Direct costs: {direct_costs:,.2f}
Gross profit: {gross_profit:,.2f}
Operating expenses: {operating_expenses:,.2f}
Operating profit: {operating_profit:,.2f}
Gross margin: {gross_margin:.1f}%
Operating margin: {operating_margin:.1f}%
Direct costs / revenue: {direct_cost_share:.1f}%
Break-even revenue: {
    f"{break_even:,.2f}" if break_even is not None else "Unavailable"
}
Main challenge: {challenge}

Recommended actions:
- Validate the financial figures.
- Compare results across periods.
- Investigate major cost categories.
- Measure one improvement.

This is an indicative diagnostic, not an audit or a guarantee of savings.
"""

st.download_button(
    "Download preliminary report",
    data=report,
    file_name="elevate_profit_intelligence_report.txt",
    mime="text/plain"
)

st.divider()
st.caption(
    "ECD | Preliminary diagnostic. Do not enter confidential client "
    "financial data into this prototype."
)
