
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Elevate | Profit Intelligence",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>
.stApp {background-color: #f5f6f8;}
h1, h2, h3 {color: #15263d;}
[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border: 1px solid #e1e5eb;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("ELEVATE")
st.write("ECD dashboard is loading.")
st.subheader("PROFIT INTELLIGENCE")
st.caption("BUSINESS PERFORMANCE • FINANCIAL CLARITY • ACTION")

st.info(
    "Prototype version. Use fictional figures for testing. "
    "This tool provides indicative calculations, not audited financial advice."
)

with st.sidebar:
    st.header("Business profile")
    business = st.text_input("Business name", "Demo Business")
    industry = st.selectbox(
        "Industry",
        ["Retail", "Hospitality", "Professional services",
         "Construction", "Manufacturing", "Distribution", "Other"]
    )
    currency = st.selectbox(
        "Currency", ["USD", "EUR", "GBP", "XCD", "CAD", "JMD", "TTD", "BBD"]
    )
    period = st.selectbox(
        "Reporting period", ["Monthly", "Quarterly", "Annual"]
    )

    st.divider()
    st.caption("Enter figures for the same reporting period.")
    revenue = st.number_input("Revenue", min_value=0.0, value=100000.0, step=1000.0)
    direct_costs = st.number_input(
        "Direct / variable costs", min_value=0.0, value=40000.0, step=1000.0
    )
    operating_expenses = st.number_input(
        "Operating expenses", min_value=0.0, value=35000.0, step=1000.0
    )
    fixed_costs = st.number_input(
        "Estimated fixed costs included above",
        min_value=0.0, value=20000.0, step=1000.0
    )
    challenge = st.selectbox(
        "Main business challenge",
        ["Reducing costs", "Improving margins", "Cash flow",
         "Pricing", "Growth", "Operational efficiency", "Not sure yet"]
    )
    notes = st.text_area("Additional context (optional)")

if fixed_costs > operating_expenses:
    st.error("Fixed costs included above cannot exceed total operating expenses.")
    st.stop()

gross_profit = revenue - direct_costs
operating_profit = gross_profit - operating_expenses
gross_margin = gross_profit / revenue * 100 if revenue else 0
operating_margin = operating_profit / revenue * 100 if revenue else 0
direct_cost_share = direct_costs / revenue * 100 if revenue else 0
contribution_margin = (revenue - direct_costs) / revenue if revenue else 0

break_even = (
    fixed_costs / contribution_margin
    if contribution_margin > 0 else None
)

st.caption(f"{industry}  /  {period} analysis  /  {date.today().isoformat()}")
st.divider()

st.header("Executive performance overview")
st.write(f"**Business:** {business or 'Not specified'}")

c1, c2, c3 = st.columns(3)
c1.metric("Revenue", f"{currency} {revenue:,.2f}")
c2.metric("Gross profit", f"{currency} {gross_profit:,.2f}")
c3.metric("Operating profit", f"{currency} {operating_profit:,.2f}")

c4, c5, c6 = st.columns(3)
c4.metric("Gross margin", f"{gross_margin:.1f}%")
c5.metric("Operating margin", f"{operating_margin:.1f}%")
c6.metric("Direct costs / revenue", f"{direct_cost_share:.1f}%")

st.divider()
st.header("Profit intelligence")

if revenue == 0:
    st.warning("Enter revenue above zero to calculate meaningful margins.")
elif operating_profit < 0:
    st.warning(
        "Operating result is negative for this period. "
        "Review revenue, direct costs and operating expenses."
    )
elif operating_margin < 10:
    st.warning(
        "Operating margin is below 10%. Investigate pricing, cost structure "
        "and whether the result is normal for this industry."
    )
else:
    st.success(
        "Operating result is positive. Review performance across periods "
        "to determine whether this margin is sustainable."
    )

if direct_cost_share > 60:
    st.write(
        "• **Review direct costs:** Direct costs exceed 60% of revenue. "
        "Check supplier pricing, waste, purchasing and product mix. "
        "This is a review prompt, not proof of overspending."
    )

if operating_expenses > 0 and revenue > 0:
    expense_share = operating_expenses / revenue * 100
    st.write(
        f"• **Operating expenses:** {expense_share:.1f}% of revenue. "
        "Compare with prior periods and an appropriate industry benchmark."
    )

if break_even is not None:
    st.write(f"**Indicative break-even revenue:** {currency} {break_even:,.2f}")
    st.caption(
        "Estimate assumes direct costs vary proportionally with revenue "
        "and the fixed costs entered above remain constant. Other costs "
        "and real-world changes may affect the result."
    )
else:
    st.write("Break-even estimate unavailable: contribution margin must be positive.")

st.divider()
st.header("Recommended next actions")

actions = [
    "1. Validate the figures against accounting records.",
    "2. Compare margins and expenses with previous periods.",
    "3. Investigate the largest cost categories and supplier changes.",
    "4. Identify one measurable improvement and assign an owner.",
    "5. Recalculate results next period to assess progress."
]
for action in actions:
    st.write(action)

if notes.strip():
    st.subheader("Additional business context")
    st.write(notes)

report = f"""
ELEVATE CORPORATE DYNAMICS
PROFIT INTELLIGENCE — PRELIMINARY REPORT

Business: {business}
Industry: {industry}
Period: {period}
Report date: {date.today().isoformat()}
Currency: {currency}

FINANCIAL SUMMARY
Revenue: {currency} {revenue:,.2f}
Direct / variable costs: {currency} {direct_costs:,.2f}
Gross profit: {currency} {gross_profit:,.2f}
Operating expenses: {currency} {operating_expenses:,.2f}
Operating profit: {currency} {operating_profit:,.2f}
Gross margin: {gross_margin:.1f}%
Operating margin: {operating_margin:.1f}%
Direct costs as % of revenue: {direct_cost_share:.1f}%

Indicative break-even revenue:
{currency} {break_even:,.2f} if break_even is not None else "Unavailable"

Main challenge: {challenge}
Additional context: {notes or "None supplied"}

NEXT ACTIONS
- Validate figures against accounting records.
- Compare results across reporting periods.
- Investigate cost categories and supplier changes.
- Assign an owner and measure one improvement.
- Review results next period.

This is an indicative diagnostic, not an audit or a guarantee
of savings. Findings require validation by the business.
"""
report = report.replace(
    f"{currency} {break_even:,.2f} if break_even is not None else 'Unavailable'",
    f"{currency} {break_even:,.2f}" if break_even is not None else "Unavailable"
)

st.download_button(
    "Download preliminary report",
    data=report,
    file_name="elevate_profit_intelligence_report.txt",
    mime="text/plain"
)

st.divider()
st.caption(
    "ELEVATE CORPORATE DYNAMICS | Confidentiality must be established "
    "before entering real client data. This prototype does not provide "
    "secure client accounts or persistent financial-data storage."
)
