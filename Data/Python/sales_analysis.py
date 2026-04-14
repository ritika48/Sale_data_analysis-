"""
=============================================================================
GLOBAL SUPERSTORE — SALES DATA ANALYSIS
=============================================================================
Dataset : Global_Superstore2.csv  (51,290 rows | 2011–2014)
Purpose : Generate publication-quality charts and print key business insights.
Output  : 10 PNG charts saved in the same directory as this script.
Run     : py -3.13 sales_analysis.py
=============================================================================
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import warnings

warnings.filterwarnings("ignore")

# ── Configuration ────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.dirname(SCRIPT_DIR)  # Sale_data_analysis/Data
CSV_PATH = os.path.join(DATA_DIR, "Global_Superstore2.csv")
OUTPUT_DIR = SCRIPT_DIR  # Save PNGs alongside this script

# Professional color palette
COLORS = {
    "primary": "#1B4F72",
    "secondary": "#2E86C1",
    "accent": "#F39C12",
    "positive": "#27AE60",
    "negative": "#E74C3C",
    "neutral": "#7F8C8D",
    "palette": ["#1B4F72", "#2E86C1", "#3498DB", "#1ABC9C", "#27AE60",
                "#F39C12", "#E67E22", "#E74C3C", "#9B59B6", "#34495E"],
    "cat3": ["#1B4F72", "#F39C12", "#27AE60"],
}

# Global plot style
plt.rcParams.update({
    "figure.facecolor": "#FAFAFA",
    "axes.facecolor": "#FAFAFA",
    "axes.edgecolor": "#CCCCCC",
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.color": "#CCCCCC",
    "font.family": "sans-serif",
    "font.size": 10,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.labelsize": 11,
})


# ── Helper Functions ─────────────────────────────────────────────────────────
def save_chart(fig, name):
    """Save chart as PNG and close figure."""
    path = os.path.join(OUTPUT_DIR, f"{name}.png")
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"  ✅ Saved: {name}.png")


def currency_fmt(x, _):
    """Format numbers as $XXXk or $X.XM."""
    if abs(x) >= 1_000_000:
        return f"${x / 1_000_000:.1f}M"
    elif abs(x) >= 1_000:
        return f"${x / 1_000:.0f}K"
    return f"${x:.0f}"


# ── Load & Prepare Data ─────────────────────────────────────────────────────
print("=" * 70)
print("GLOBAL SUPERSTORE — SALES DATA ANALYSIS")
print("=" * 70)
print(f"\nLoading data from: {CSV_PATH}")

df = pd.read_csv(CSV_PATH, encoding="latin1")
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)
df["Ship Date"] = pd.to_datetime(df["Ship Date"], dayfirst=True)
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
df["Quarter"] = df["Order Date"].dt.quarter
df["YearMonth"] = df["Order Date"].dt.to_period("M")
df["Profit Margin"] = df["Profit"] / df["Sales"] * 100

print(f"Loaded {len(df):,} rows  |  {df['Year'].min()}–{df['Year'].max()}")
print(f"Markets: {df['Market'].nunique()}  |  Regions: {df['Region'].nunique()}")
print(f"Categories: {df['Category'].nunique()}  |  Sub-Categories: {df['Sub-Category'].nunique()}")
print()


# ══════════════════════════════════════════════════════════════════════════════
# CHART 1 — Yearly Sales & Profit Trend
# ══════════════════════════════════════════════════════════════════════════════
print("── Chart 1: Yearly Sales & Profit Trend ──")
yearly = df.groupby("Year").agg({"Sales": "sum", "Profit": "sum"}).reset_index()

fig, ax1 = plt.subplots(figsize=(9, 5))
x = yearly["Year"]
bar_w = 0.35
ax1.bar(x - bar_w / 2, yearly["Sales"], bar_w, label="Sales", color=COLORS["primary"])
ax1.bar(x + bar_w / 2, yearly["Profit"], bar_w, label="Profit", color=COLORS["accent"])
ax1.set_xlabel("Year")
ax1.set_ylabel("Amount ($)")
ax1.set_title("Yearly Sales & Profit Trend (2011–2014)")
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(currency_fmt))
ax1.set_xticks(x)
ax1.legend()

# Add value labels
for i, row in yearly.iterrows():
    ax1.text(row["Year"] - bar_w / 2, row["Sales"] + 50000, f"${row['Sales']:,.0f}",
             ha="center", va="bottom", fontsize=7, fontweight="bold")
    ax1.text(row["Year"] + bar_w / 2, row["Profit"] + 50000, f"${row['Profit']:,.0f}",
             ha="center", va="bottom", fontsize=7, fontweight="bold")

fig.tight_layout()
save_chart(fig, "01_yearly_sales_profit_trend")

yoy_growth = yearly["Sales"].pct_change().dropna().values
print(f"  📊 Total Revenue (4 years): ${yearly['Sales'].sum():,.0f}")
print(f"  📊 Total Profit  (4 years): ${yearly['Profit'].sum():,.0f}")
if len(yoy_growth) > 0:
    print(f"  📊 YoY Sales Growth: {', '.join([f'{g:.1%}' for g in yoy_growth])}")
print()


# ══════════════════════════════════════════════════════════════════════════════
# CHART 2 — Monthly Sales Trend (Seasonality)
# ══════════════════════════════════════════════════════════════════════════════
print("── Chart 2: Monthly Sales Trend ──")
monthly = df.groupby("YearMonth").agg({"Sales": "sum"}).reset_index()
monthly["YearMonth"] = monthly["YearMonth"].astype(str)

fig, ax = plt.subplots(figsize=(14, 5))
ax.plot(range(len(monthly)), monthly["Sales"], color=COLORS["secondary"], linewidth=1.5)
ax.fill_between(range(len(monthly)), monthly["Sales"], alpha=0.15, color=COLORS["secondary"])
ax.set_title("Monthly Sales Trend — Seasonality Analysis (2011–2014)")
ax.set_ylabel("Sales ($)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(currency_fmt))

# Show every 6th label to avoid clutter
tick_positions = list(range(0, len(monthly), 6))
ax.set_xticks(tick_positions)
ax.set_xticklabels([monthly["YearMonth"].iloc[i] for i in tick_positions], rotation=45, ha="right")
fig.tight_layout()
save_chart(fig, "02_monthly_sales_trend")

# Find peak months
avg_by_month = df.groupby("Month")["Sales"].sum().sort_values(ascending=False)
peak_months = avg_by_month.head(3).index.tolist()
month_names = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
               7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
print(f"  📊 Peak Sales Months: {', '.join([month_names[m] for m in peak_months])}")
print(f"  📊 Slowest Month: {month_names[avg_by_month.idxmin()]}")
print()


# ══════════════════════════════════════════════════════════════════════════════
# CHART 3 — Category-wise Sales & Profit
# ══════════════════════════════════════════════════════════════════════════════
print("── Chart 3: Category-wise Sales & Profit ──")
cat = df.groupby("Category").agg({"Sales": "sum", "Profit": "sum"}).reset_index()
cat = cat.sort_values("Sales", ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
x_pos = range(len(cat))
bar_w = 0.35
bars1 = ax.bar([p - bar_w / 2 for p in x_pos], cat["Sales"], bar_w,
               label="Sales", color=COLORS["cat3"])
bars2 = ax.bar([p + bar_w / 2 for p in x_pos], cat["Profit"], bar_w,
               label="Profit", color=[COLORS["accent"]] * len(cat))

ax.set_title("Category-wise Sales & Profit")
ax.set_ylabel("Amount ($)")
ax.set_xticks(x_pos)
ax.set_xticklabels(cat["Category"])
ax.yaxis.set_major_formatter(mticker.FuncFormatter(currency_fmt))
ax.legend()

for bar, val in zip(bars1, cat["Sales"]):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 20000,
            f"${val:,.0f}", ha="center", va="bottom", fontsize=8, fontweight="bold")

fig.tight_layout()
save_chart(fig, "03_category_sales_profit")

for _, row in cat.iterrows():
    margin = row["Profit"] / row["Sales"] * 100
    print(f"  📊 {row['Category']}: Sales=${row['Sales']:,.0f}, "
          f"Profit=${row['Profit']:,.0f}, Margin={margin:.1f}%")
print()


# ══════════════════════════════════════════════════════════════════════════════
# CHART 4 — Top 10 Sub-Categories by Profit
# ══════════════════════════════════════════════════════════════════════════════
print("── Chart 4: Top 10 Sub-Categories by Profit ──")
subcat = df.groupby("Sub-Category").agg({"Profit": "sum"}).reset_index()
subcat = subcat.sort_values("Profit", ascending=True)

fig, ax = plt.subplots(figsize=(10, 6))
colors_bar = [COLORS["positive"] if p > 0 else COLORS["negative"] for p in subcat["Profit"]]
ax.barh(subcat["Sub-Category"], subcat["Profit"], color=colors_bar)
ax.set_title("Sub-Category Profitability (All 17 Sub-Categories)")
ax.set_xlabel("Total Profit ($)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(currency_fmt))
ax.axvline(x=0, color="gray", linewidth=0.8)

for i, (val, name) in enumerate(zip(subcat["Profit"], subcat["Sub-Category"])):
    offset = 3000 if val >= 0 else -3000
    ax.text(val + offset, i, f"${val:,.0f}", va="center", fontsize=7.5)

fig.tight_layout()
save_chart(fig, "04_subcategory_profitability")

loss_cats = subcat[subcat["Profit"] < 0]
if not loss_cats.empty:
    print(f"  ⚠️  Loss-making sub-categories: {', '.join(loss_cats['Sub-Category'].tolist())}")
top3 = subcat.tail(3)
print(f"  📊 Most profitable: {', '.join(top3['Sub-Category'].tolist())}")
print()


# ══════════════════════════════════════════════════════════════════════════════
# CHART 5 — Market-wise Revenue
# ══════════════════════════════════════════════════════════════════════════════
print("── Chart 5: Market-wise Revenue ──")
market = df.groupby("Market").agg({"Sales": "sum", "Profit": "sum"}).reset_index()
market = market.sort_values("Sales", ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(market["Market"], market["Sales"], color=COLORS["palette"][:len(market)])
ax.set_title("Revenue by Market")
ax.set_ylabel("Total Sales ($)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(currency_fmt))

for bar, val in zip(bars, market["Sales"]):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 20000,
            f"${val:,.0f}", ha="center", va="bottom", fontsize=8, fontweight="bold")

fig.tight_layout()
save_chart(fig, "05_market_revenue")

total_sales = market["Sales"].sum()
for _, row in market.iterrows():
    share = row["Sales"] / total_sales * 100
    print(f"  📊 {row['Market']}: ${row['Sales']:,.0f} ({share:.1f}% share)")
print()


# ══════════════════════════════════════════════════════════════════════════════
# CHART 6 — Segment-wise Sales Distribution (Donut Chart)
# ══════════════════════════════════════════════════════════════════════════════
print("── Chart 6: Segment-wise Sales ──")
seg = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(7, 7))
wedges, texts, autotexts = ax.pie(
    seg, labels=seg.index, autopct="%1.1f%%",
    colors=[COLORS["primary"], COLORS["accent"], COLORS["positive"]],
    startangle=140, pctdistance=0.82, wedgeprops=dict(width=0.45, edgecolor="white"))
for t in autotexts:
    t.set_fontsize(11)
    t.set_fontweight("bold")
ax.set_title("Sales Distribution by Customer Segment")
fig.tight_layout()
save_chart(fig, "06_segment_distribution")

for name, val in seg.items():
    print(f"  📊 {name}: ${val:,.0f} ({val / total_sales * 100:.1f}%)")
print()


# ══════════════════════════════════════════════════════════════════════════════
# CHART 7 — Discount vs Profit Scatter Plot
# ══════════════════════════════════════════════════════════════════════════════
print("── Chart 7: Discount vs Profit ──")
fig, ax = plt.subplots(figsize=(10, 6))
sample = df.sample(min(5000, len(df)), random_state=42)
scatter = ax.scatter(sample["Discount"], sample["Profit"],
                     alpha=0.35, s=12, c=sample["Profit"],
                     cmap="RdYlGn", edgecolors="none")
ax.set_title("Discount vs. Profit — Impact Analysis")
ax.set_xlabel("Discount (%)")
ax.set_ylabel("Profit ($)")
ax.axhline(y=0, color="red", linestyle="--", linewidth=0.8, alpha=0.6)
plt.colorbar(scatter, ax=ax, label="Profit ($)", shrink=0.8)
fig.tight_layout()
save_chart(fig, "07_discount_vs_profit")

no_disc = df[df["Discount"] == 0]["Profit"].mean()
hi_disc = df[df["Discount"] > 0.3]["Profit"].mean()
print(f"  📊 Avg Profit (No Discount): ${no_disc:,.2f}")
print(f"  📊 Avg Profit (>30% Discount): ${hi_disc:,.2f}")
corr = df["Discount"].corr(df["Profit"])
print(f"  📊 Correlation (Discount vs Profit): {corr:.3f}")
print()


# ══════════════════════════════════════════════════════════════════════════════
# CHART 8 — Shipping Mode Analysis
# ══════════════════════════════════════════════════════════════════════════════
print("── Chart 8: Shipping Mode Analysis ──")
ship = df.groupby("Ship Mode").agg({
    "Sales": "sum", "Profit": "sum", "Shipping Cost": "sum"
}).reset_index()
ship = ship.sort_values("Sales", ascending=False)

fig, ax = plt.subplots(figsize=(9, 5))
x_pos = range(len(ship))
bar_w = 0.25
ax.bar([p - bar_w for p in x_pos], ship["Sales"], bar_w,
       label="Sales", color=COLORS["primary"])
ax.bar(x_pos, ship["Profit"], bar_w,
       label="Profit", color=COLORS["positive"])
ax.bar([p + bar_w for p in x_pos], ship["Shipping Cost"], bar_w,
       label="Shipping Cost", color=COLORS["negative"])

ax.set_title("Shipping Mode — Sales, Profit & Cost Comparison")
ax.set_ylabel("Amount ($)")
ax.set_xticks(x_pos)
ax.set_xticklabels(ship["Ship Mode"])
ax.yaxis.set_major_formatter(mticker.FuncFormatter(currency_fmt))
ax.legend()
fig.tight_layout()
save_chart(fig, "08_shipping_mode_analysis")

for _, row in ship.iterrows():
    margin = row["Profit"] / row["Sales"] * 100
    print(f"  📊 {row['Ship Mode']}: Sales=${row['Sales']:,.0f}, "
          f"Profit Margin={margin:.1f}%, Ship Cost=${row['Shipping Cost']:,.0f}")
print()


# ══════════════════════════════════════════════════════════════════════════════
# CHART 9 — Top 10 Customers by Revenue
# ══════════════════════════════════════════════════════════════════════════════
print("── Chart 9: Top 10 Customers by Revenue ──")
cust = df.groupby("Customer Name").agg({"Sales": "sum", "Profit": "sum"}).reset_index()
top_cust = cust.sort_values("Sales", ascending=True).tail(10)

fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(top_cust["Customer Name"], top_cust["Sales"], color=COLORS["secondary"])
ax.set_title("Top 10 Customers by Revenue")
ax.set_xlabel("Total Revenue ($)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(currency_fmt))

for i, (val, name) in enumerate(zip(top_cust["Sales"], top_cust["Customer Name"])):
    ax.text(val + 500, i, f"${val:,.0f}", va="center", fontsize=8)

fig.tight_layout()
save_chart(fig, "09_top10_customers")

print(f"  📊 #1 Customer: {top_cust.iloc[-1]['Customer Name']} "
      f"(${top_cust.iloc[-1]['Sales']:,.0f})")
print()


# ══════════════════════════════════════════════════════════════════════════════
# CHART 10 — Top 10 Products by Revenue
# ══════════════════════════════════════════════════════════════════════════════
print("── Chart 10: Top 10 Products by Revenue ──")
prod = df.groupby("Product Name").agg({"Sales": "sum", "Profit": "sum"}).reset_index()
top_prod = prod.sort_values("Sales", ascending=True).tail(10)

# Shorten long product names for display
top_prod["Short Name"] = top_prod["Product Name"].apply(
    lambda x: x[:45] + "..." if len(x) > 45 else x)

fig, ax = plt.subplots(figsize=(12, 6))
colors_bar = [COLORS["positive"] if p > 0 else COLORS["negative"]
              for p in top_prod["Profit"]]
ax.barh(top_prod["Short Name"], top_prod["Sales"], color=colors_bar)
ax.set_title("Top 10 Products by Revenue")
ax.set_xlabel("Total Revenue ($)")
ax.xaxis.set_major_formatter(mticker.FuncFormatter(currency_fmt))

for i, val in enumerate(top_prod["Sales"]):
    ax.text(val + 500, i, f"${val:,.0f}", va="center", fontsize=8)

fig.tight_layout()
save_chart(fig, "10_top10_products")

print(f"  📊 #1 Product: {top_prod.iloc[-1]['Product Name'][:50]}")
print(f"     Revenue: ${top_prod.iloc[-1]['Sales']:,.0f}")
print()


# ══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════════════════════
print("=" * 70)
print("KEY BUSINESS INSIGHTS SUMMARY")
print("=" * 70)

# Overall KPIs
total_revenue = df["Sales"].sum()
total_profit = df["Profit"].sum()
overall_margin = total_profit / total_revenue * 100
total_orders = df["Order ID"].nunique()
total_customers = df["Customer Name"].nunique()

print(f"\n  💰 Total Revenue (2011–2014): ${total_revenue:,.0f}")
print(f"  💰 Total Profit: ${total_profit:,.0f} ({overall_margin:.1f}% margin)")
print(f"  📦 Total Unique Orders: {total_orders:,}")
print(f"  👤 Total Unique Customers: {total_customers:,}")

# Growth
rev_2011 = df[df["Year"] == 2011]["Sales"].sum()
rev_2014 = df[df["Year"] == 2014]["Sales"].sum()
growth = (rev_2014 - rev_2011) / rev_2011 * 100
print(f"  📈 Revenue Growth 2011→2014: {growth:.1f}%")

# Best performing
best_cat = cat.iloc[0]
print(f"  🏆 Highest Revenue Category: {best_cat['Category']} (${best_cat['Sales']:,.0f})")

best_market = market.iloc[0]
print(f"  🌍 Largest Market: {best_market['Market']} (${best_market['Sales']:,.0f})")

# Risk insights
print(f"  ⚠️  Discount-Profit Correlation: {corr:.3f} (negative = higher discounts hurt profit)")

print(f"\n  ✅ All 10 charts saved to: {OUTPUT_DIR}")
print("=" * 70)
