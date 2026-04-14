# Case Study: Revenue Growth Strategy for Global Superstore
### A Business Analyst's Data-Driven Approach to Increasing Revenue

---

**Prepared by:** Ritika | Entry-Level Business Analyst  
**Date:** April 2026  
**Tools Used:** SQL · Python (Pandas, Matplotlib) · Power BI  
**Dataset:** Global Superstore — 51,290 orders across 7 markets (2011–2014)

---

##  Executive Summary

Global Superstore, a multinational retail company, experienced strong revenue growth of **90.3%** over four years (2011–2014), growing from **$2.26M to $4.30M**. However, profitability remained constrained at an overall **11.6% margin** due to aggressive discounting practices, underperforming product lines, and untapped market potential.

This case study identifies **five strategic opportunities** that, if implemented, could increase annual revenue by an estimated **15–25%** while simultaneously improving profit margins. The recommendations are backed by analysis of 51,290 transactions using SQL, Python, and Power BI.

---

##  Table of Contents

1. [Business Context & Problem Statement](#1-business-context--problem-statement)
2. [Methodology & Approach](#2-methodology--approach)
3. [Current State Analysis](#3-current-state-analysis)
4. [Key Findings & Revenue Opportunities](#4-key-findings--revenue-opportunities)
5. [Strategic Recommendations](#5-strategic-recommendations)
6. [Implementation Roadmap](#6-implementation-roadmap)
7. [Expected Financial Impact](#7-expected-financial-impact)
8. [Risks & Mitigation](#8-risks--mitigation)
9. [Conclusion](#9-conclusion)

---

## 1. Business Context & Problem Statement

### Background

Global Superstore operates across **7 international markets** (Asia-Pacific, EU, US, Latin America, Africa, EMEA, and Canada), selling products in three categories — **Technology, Furniture, and Office Supplies** — to three customer segments: Consumer, Corporate, and Home Office.

### The Problem

While overall revenue was growing, the company was facing multiple challenges:

- **Profit margins were inconsistent** across product categories (ranging from 6.9% to 14.0%)
- **Certain product lines were operating at a loss** despite generating significant revenue
- **Discounting practices were eroding profits** with no clear policy in place
- **Geographic expansion opportunities were being missed** in high-potential markets
- **Seasonal demand fluctuations were not being leveraged** for maximum revenue capture

### Objective

> Analyze 4 years of sales data to identify **actionable strategies to increase revenue** while improving or maintaining profit margins.

---

## 2. Methodology & Approach

### Data Pipeline

```
Raw CSV Data (51,290 rows)
    │
    ├── SQL Analysis (11 queries)
    │   └── Aggregations, trend analysis, discount impact, top performers
    │
    ├── Python Analysis (10 visualizations)
    │   └── Pandas for cleaning & aggregation
    │   └── Matplotlib for publication-quality charts
    │
    └── Power BI Dashboard (3-page interactive report)
        └── Executive, Product, and Regional views
```

### Analytical Framework

I structured the analysis around **five revenue levers** commonly used in retail analytics:

| Revenue Lever | Question Answered |
|---------------|-------------------|
| **Price Optimization** | Are discounts helping or hurting revenue? |
| **Product Mix** | Which products generate the most revenue per unit? |
| **Market Expansion** | Where are the untapped growth opportunities? |
| **Customer Retention** | Who are our high-value customers and how do we keep them? |
| **Seasonal Strategy** | Are we maximizing revenue during peak demand periods? |

---

## 3. Current State Analysis

### 3.1 Revenue Overview (2011–2014)

| Metric | Value |
|--------|-------|
| **Total Revenue** | $12,642,905 |
| **Total Profit** | $1,467,457 |
| **Overall Profit Margin** | 11.6% |
| **Total Unique Orders** | 25,035 |
| **Total Unique Customers** | 1,590 |
| **Average Order Value** | ~$505 |

### 3.2 Year-over-Year Growth

| Year | Revenue | YoY Growth |
|------|---------|------------|
| 2011 | $2,259,451 | — |
| 2012 | $2,677,440 | +18.5% |
| 2013 | $3,405,747 | +27.2% |
| 2014 | $4,300,267 | +26.3% |

**Insight:** Growth is strong and accelerating. The company nearly **doubled its revenue** in 4 years. The challenge is not growth itself — it's ensuring that growth is *profitable*.

### 3.3 Category Performance

| Category | Revenue | Profit | Margin |
|----------|---------|--------|--------|
| Technology | $4,744,557 | $663,776 | 14.0% |
| Furniture | $4,110,880 | $283,576 | 6.9% |
| Office Supplies | $3,787,493 | $518,847 | 13.7% |

**Critical Observation:** Furniture generates **$4.1M in revenue** but only a **6.9% margin** — nearly half the margin of Technology and Office Supplies. This is a major revenue optimization opportunity.

### 3.4 Market Distribution

| Market | Revenue | Share | Role |
|--------|---------|-------|------|
| Asia-Pacific (APAC) | $3,585,837 | 28.4% | **Growth Engine** |
| European Union (EU) | $2,938,151 | 23.2% | **Stable Core** |
| United States (US) | $2,297,201 | 18.2% | **Mature Market** |
| Latin America (LATAM) | $2,164,691 | 17.1% | **Emerging** |
| EMEA | $833,658 | 6.6% | **Emerging** |
| Africa | $755,992 | 6.0% | **Emerging** |
| Canada | $67,375 | 0.5% | **Underperforming** |

---

## 4. Key Findings & Revenue Opportunities

### Finding #1: Discounts Over 30% Are Destroying Revenue AND Profit

This is the **most critical and immediately actionable finding**.

| Discount Level | Avg Profit Per Order | Impact |
|----------------|----------------------|--------|
| No Discount (0%) | **+$61.04** | Healthy profit |
| 1–20% | Moderate positive | Acceptable |
| 21–30% | Near break-even | Warning zone |
| >30% | **−$76.59** | Net loss per order |

- **Correlation between discount and profit: −0.316** (statistically significant negative relationship)
- The company is literally **paying customers to take products** when discounts exceed 30%
- **Revenue Impact:** Every order with >30% discount loses an average of $76.59 — this directly erodes top-line revenue potential

> **Revenue Opportunity:** By capping discounts at 20% and converting deep-discount customers to moderate-discount offers, the company could recover an estimated **$200K–$400K in annual profit** that is currently being given away.

---

### Finding #2: Tables Sub-Category Is a Revenue Black Hole

Out of 17 sub-categories, **Tables is the only one generating a net loss**.

| Sub-Category | Revenue | Profit | Status |
|--------------|---------|--------|--------|
| Copiers | High | **Highest profit** | Star performer |
| Phones | High | High profit | Star performer |
| Accessories | Moderate | Good profit | Healthy |
| **Tables** | Moderate | **Negative** | Loss-making |

- Tables are cannibalizing the Furniture category's profitability
- The Furniture category would have a **~10% margin** (instead of 6.9%) if Tables were either fixed or discontinued
- **Root Cause (Likely):** Combination of high shipping costs (heavy items), excessive discounting, and possibly unfavorable supplier pricing

> **Revenue Opportunity:** Fixing the Tables pricing strategy or reallocating marketing spend to profitable sub-categories like Copiers and Phones could add **$100K–$200K** in annual profit without requiring additional revenue.

---

### Finding #3: Seasonal Peaks Are Underutilized

| Peak Months | Slow Months |
|-------------|-------------|
| September, November, December (Q4) | January, February (Q1) |

- **Q4 generates 35–40% more revenue** than Q1
- The company is likely not adjusting inventory, staffing, or marketing budgets to match this seasonality
- **February is the weakest month** — a known retail pattern that could be addressed with targeted campaigns

> **Revenue Opportunity:** Increasing marketing spend by **20% during Q4** and running strategic clearance events in Jan–Feb could capture an additional **$300K–$500K** in annual revenue.

---

### Finding #4: APAC Is Underinvested Despite Being the Largest Market

- APAC represents **28.4% of total revenue** ($3.59M) — the single largest market
- Yet marketing and operational investment may not reflect this dominance
- In contrast, **Canada produces only $67K** (0.5%) — questioning the ROI of maintaining operations there

> **Revenue Opportunity:** Redirecting even **5% of the Canada/EMEA budget to APAC** and expanding the Technology product line in that region could generate an additional **$200K–$400K** in revenue.

---

### Finding #5: Consumer Segment Drives 51.5% of Revenue — But Are We Retaining Them?

| Segment | Revenue Share |
|---------|---------------|
| Consumer | 51.5% |
| Corporate | 30.3% |
| Home Office | 18.3% |

- Over half the revenue comes from individual consumers
- **Top 10 customers contribute disproportionately** to total revenue
- There is no evidence of a loyalty or retention program to protect this revenue base

> **Revenue Opportunity:** Implementing a **customer loyalty program** targeting the top 20% of customers (by revenue) could increase retention by 10–15%, protecting approximately **$500K–$750K** in at-risk annual revenue.

---

## 5. Strategic Recommendations

### Recommendation 1: Implement a Smart Discount Policy
**Priority:** Critical | **Timeline:** Immediate (0–30 days)

| Action | Detail |
|--------|--------|
| Cap maximum discount | **20% hard cap** across all categories |
| Replace blanket discounts | Use **targeted promotions** based on customer segment and purchase history |
| Implement tiered pricing | Volume-based discounts (e.g., 5% for 10+ units, 10% for 50+ units) |
| Monitor weekly | Create a **discount monitoring dashboard** in Power BI to track compliance |

**Why it works:** The data shows a clear break-even point around 20% discount. Every percentage point above that destroys profit. This single change has the **highest ROI with the lowest cost to implement**.

---

### Recommendation 2: Restructure the Tables Product Line
**Priority:** Critical | **Timeline:** 30–60 days

| Action | Detail |
|--------|--------|
| Audit supplier pricing | Renegotiate contracts or find alternative suppliers |
| Review shipping costs | Tables are heavy — explore flat-rate or regional shipping |
| Reduce discounts on Tables | Tables likely receive excessive discounts; enforce the 20% cap |
| Consider premium positioning | Reposition Tables as a premium/designer product with higher prices |

**Fallback:** If Tables remain unprofitable after 90 days, consider **discontinuing the lowest-selling Table SKUs** and reallocating shelf/warehouse space to Copiers and Phones.

---

### Recommendation 3: Launch a Seasonal Revenue Maximization Program
**Priority:** High | **Timeline:** Before Q4 each year

| Season | Strategy |
|--------|----------|
| **Q4 (Sep–Dec)** | ↑ 20% inventory for Technology & Office Supplies. ↑ Marketing spend. Launch holiday bundles. |
| **Q1 (Jan–Feb)** | Clearance sales for slow-moving Furniture. New Year "office refresh" campaign for Corporate segment. |
| **Q2–Q3** | Standard operations. Build inventory for Q4. Run "Back to Business" campaign in September. |

---

### Recommendation 4: Double Down on APAC Market
**Priority:** High | **Timeline:** 60–90 days

| Action | Detail |
|--------|--------|
| Increase APAC marketing budget | Reallocate **5–10% from underperforming markets (Canada, Africa)** |
| Expand Technology offerings in APAC | Technology has the highest margin (14%) — push it in the biggest market |
| Localize promotions | Tailor campaigns to APAC-specific shopping seasons and preferences |
| Evaluate Canada operations | At $67K revenue, assess whether the market justifies operational costs |

---

### Recommendation 5: Build a Customer Retention Engine
**Priority:**  Medium | **Timeline:** 90–120 days

| Action | Detail |
|--------|--------|
| Identify top 20% customers | Use SQL/Python to calculate customer lifetime value (CLV) |
| Launch loyalty program | Tiered rewards based on annual spending (Silver/Gold/Platinum) |
| Prevent churn | Flag customers whose order frequency drops and trigger re-engagement campaigns |
| Corporate partnerships | Offer dedicated pricing for Corporate segment to increase B2B revenue (30.3% of sales) |

---

## 6. Implementation Roadmap

```
PHASE 1 — Quick Wins (Month 1)
├── Implement 20% discount cap policy
├── Create discount monitoring dashboard in Power BI
└── Audit Tables sub-category pricing

PHASE 2 — Revenue Optimization (Month 2–3)
├── Restructure Tables product line
├── Reallocate marketing budget to APAC
├── Build seasonal inventory plan for Q4
└── Develop customer segmentation model (RFM analysis)

PHASE 3 — Growth Engine (Month 3–6)
├── Launch customer loyalty program
├── Expand Technology product line in APAC
├── Implement targeted promotional campaigns
├── Build predictive demand forecasting model
└── Create automated revenue dashboards for leadership

PHASE 4 — Scale & Monitor (Month 6+)
├── Monthly revenue performance reviews
├── A/B test discount strategies
├── Evaluate new market entry opportunities
└── Continuous dashboard optimization
```

---

## 7. Expected Financial Impact

### Conservative Estimates (Annual)

| Initiative | Revenue Impact | Profit Impact | Confidence |
|------------|---------------|---------------|------------|
| Smart Discount Policy | +$150K–$300K | +$200K–$400K | High |
| Fix Tables Sub-Category | +$50K–$100K | +$100K–$200K | High |
| Seasonal Maximization | +$300K–$500K | +$90K–$150K | Medium |
| APAC Market Investment | +$200K–$400K | +$80K–$160K | Medium |
| Customer Retention | +$500K–$750K (protected) | +$60K–$90K | Medium |
| **TOTAL** | **+$1.2M–$2.0M** | **+$530K–$1.0M** | — |

> Based on 2014 revenue of $4.3M, these initiatives could increase annual revenue by **28–47%** and nearly **double the profit** from ~$600K to $1.1–$1.6M.

---

## 8. Risks & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Discount cap causes customer churn | Medium | High | Phase in gradually; offer loyalty rewards as an alternative |
| APAC investment doesn't yield returns | Low | Medium | Start with a small pilot; measure ROI after 90 days |
| Tables restructuring disrupts Furniture sales | Low | Medium | Maintain bestsellers; only discontinue bottom performers |
| Seasonal forecasting errors | Medium | Medium | Use 4-year historical data for predictions; build buffer stock |
| Competitor response to pricing changes | Medium | Medium | Monitor competitor pricing quarterly; maintain value proposition |

---

## 9. Conclusion

Global Superstore is a company with **strong revenue momentum** — growing 90.3% over four years — but with **significant profitability leaks** that limit its full potential. The data tells a clear story:

1. **Stop giving away profits** — discounts over 30% cost more than they earn
2. **Fix what's broken** — Tables is a loss-maker hiding inside a $4.1M Furniture category
3. **Go where the money is** — APAC is the largest market and Technology has the highest margins
4. **Sell more when customers are buying** — Q4 seasonality is predictable and exploitable
5. **Keep your best customers** — the top 20% drive the majority of revenue

These are not theoretical suggestions — they are **data-backed strategies derived from analysis of 51,290 real transactions**. The estimated impact of **$1.2M–$2.0M in additional annual revenue** is achievable within 6–12 months with focused execution.

---

### 📎 Supporting Materials

| Document | Description |
|----------|-------------|
| `Python/sales_analysis.py` | Complete Python analysis script with 10 visualizations |
| `SQL/sales_analysis_queries.sql` | 11 SQL queries covering all business dimensions |
| `Dashboard/PBQuery.pbix` | Interactive Power BI dashboard (3 pages) |
| `Dashboard/PowerBI_Dashboard_Guide.md` | Step-by-step guide to build the dashboard |
| `Python/*.png` | 10 analysis charts (trends, categories, markets, discounts, etc.) |

---

*This case study was prepared as part of a portfolio project demonstrating business analysis skills including data analysis (SQL, Python), visualization (Matplotlib, Power BI), and strategic recommendation development.*
