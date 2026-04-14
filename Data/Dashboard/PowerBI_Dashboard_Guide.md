# Power BI Dashboard Guide — Global Superstore Sales Analysis

A step-by-step guide to building a professional, interactive Power BI dashboard for the Global Superstore dataset.

---

## 1. Data Import & Transformation

### Import the Data
1. Open **Power BI Desktop** → **Home** → **Get Data** → **Text/CSV**
2. Browse to `Global_Superstore2.csv` and click **Open**
3. In the preview, set **File Origin** to `1252: Western European` (handles special characters)
4. Click **Transform Data** to open Power Query Editor

### Apply Transformations in Power Query
| Step | Column | Action |
|------|--------|--------|
| 1 | `Order Date` | Change type → **Date** (Format: DD/MM/YYYY) |
| 2 | `Ship Date` | Change type → **Date** |
| 3 | `Sales`, `Profit`, `Shipping Cost` | Change type → **Decimal Number** |
| 4 | `Discount` | Change type → **Decimal Number** |
| 5 | `Quantity` | Change type → **Whole Number** |
| 6 | `Postal Code` | Change type → **Text** (keep nulls — expected for non-US) |

### Add Custom Columns (Add Column → Custom Column)
```
Year = Date.Year([Order Date])
Month = Date.Month([Order Date])
Quarter = "Q" & Text.From(Date.QuarterOfYear([Order Date]))
Month Name = Date.MonthName([Order Date])
Profit Margin % = [Profit] / [Sales] * 100
```

Click **Close & Apply**.

---

## 2. DAX Measures

Create these measures in the **Modeling** tab → **New Measure**:

```dax
// Core KPIs
Total Sales = SUM('global_superstore'[Sales])
Total Profit = SUM('global_superstore'[Profit])
Total Orders = DISTINCTCOUNT('global_superstore'[Order ID])
Total Customers = DISTINCTCOUNT('global_superstore'[Customer Name])
Avg Discount = AVERAGE('global_superstore'[Discount]) * 100
Total Shipping Cost = SUM('global_superstore'[Shipping Cost])

// Calculated Metrics
Profit Margin % = DIVIDE([Total Profit], [Total Sales], 0) * 100
Avg Order Value = DIVIDE([Total Sales], [Total Orders], 0)

// Year-over-Year Growth
Sales YoY Growth % =
    VAR CurrentYearSales = [Total Sales]
    VAR PreviousYearSales =
        CALCULATE([Total Sales],
            DATEADD('global_superstore'[Order Date], -1, YEAR))
    RETURN
        DIVIDE(CurrentYearSales - PreviousYearSales, PreviousYearSales, 0) * 100

Profit YoY Growth % =
    VAR CurrentYearProfit = [Total Profit]
    VAR PreviousYearProfit =
        CALCULATE([Total Profit],
            DATEADD('global_superstore'[Order Date], -1, YEAR))
    RETURN
        DIVIDE(CurrentYearProfit - PreviousYearProfit, PreviousYearProfit, 0) * 100
```

---

## 3. Color Palette & Theme

Use this professional dark-blue theme throughout:

| Element | Color | Hex Code |
|---------|-------|----------|
| Primary (Headers, KPI) | Dark Navy | `#1B4F72` |
| Secondary (Bars, Lines) | Blue | `#2E86C1` |
| Accent (Highlights) | Amber | `#F39C12` |
| Positive (Profit) | Green | `#27AE60` |
| Negative (Loss) | Red | `#E74C3C` |
| Background | Light Gray | `#F5F6FA` |
| Card Background | White | `#FFFFFF` |
| Text Primary | Dark Gray | `#2C3E50` |
| Text Secondary | Medium Gray | `#7F8C8D` |

### Apply Theme
1. Go to **View** → **Themes** → **Customize Current Theme**
2. Set the data colors to the palette above
3. Set background colors and text as specified

---

## 4. Dashboard Layout — 3 Pages

### PAGE 1: Executive Overview

**Canvas Size**: 1280 × 720 px (16:9)

#### Row 1 — KPI Cards (Top Banner)
Place **6 KPI Cards** across the top in a single row:

| Card | Measure | Font Size | Font Color | Background | Value Format |
|------|---------|-----------|------------|------------|--------------|
| Total Sales | `[Total Sales]` | 28pt Bold | `#1B4F72` | White | `$0.00M` |
| Total Profit | `[Total Profit]` | 28pt Bold | `#27AE60` | White | `$0.00M` |
| Profit Margin | `[Profit Margin %]` | 28pt Bold | `#2E86C1` | White | `0.0%` |
| Total Orders | `[Total Orders]` | 28pt Bold | `#F39C12` | White | `#,##0` |
| Total Customers | `[Total Customers]` | 28pt Bold | `#1B4F72` | White | `#,##0` |
| YoY Growth | `[Sales YoY Growth %]` | 28pt Bold | `#27AE60` | White | `0.0%` |

**Card formatting**: Round corners (10px), subtle shadow, 1px border `#E0E0E0`

#### Row 2 — Charts (Left + Right)

| Position | Chart Type | Fields | Colors |
|----------|-----------|--------|--------|
| Left (60% width) | **Line Chart** | X: `Month Name`, Y: `[Total Sales]`, Legend: `Year` | Blue palette |
| Right (40% width) | **Donut Chart** | Legend: `Category`, Values: `[Total Sales]` | Navy, Amber, Green |

#### Row 3 — Secondary Charts

| Position | Chart Type | Fields | Colors |
|----------|-----------|--------|--------|
| Left (50%) | **Clustered Bar** | Y: `Market`, X: `[Total Sales]` | `#2E86C1` |
| Right (50%) | **Stacked Bar** | Y: `Segment`, X: `[Total Sales]`, Legend: `Category` | Theme colors |

---

### PAGE 2: Product & Category Deep Dive

#### Row 1 — Sub-Category Performance
| Chart | Type | Fields | Notes |
|-------|------|--------|-------|
| Full Width | **Bar Chart** | Y: `Sub-Category`, X: `[Total Profit]` | Conditional formatting: Green for profit, Red for loss |

#### Row 2

| Position | Chart | Fields |
|----------|-------|--------|
| Left (50%) | **Treemap** | Group: `Category` → `Sub-Category`, Values: `[Total Sales]` |
| Right (50%) | **Table** | `Product Name`, `[Total Sales]`, `[Total Profit]`, `[Profit Margin %]` — Top 10 by Sales |

#### Row 3

| Position | Chart | Fields |
|----------|-------|--------|
| Left (50%) | **Scatter Plot** | X: `Discount`, Y: `[Total Profit]`, Size: `[Total Sales]`, Color: `Category` |
| Right (50%) | **Clustered Column** | X: `Ship Mode`, Y: `[Total Sales]` and `[Total Profit]` |

---

### PAGE 3: Regional & Trend Analysis

#### Row 1

| Position | Chart | Fields |
|----------|-------|--------|
| Left (50%) | **Filled Map** | Location: `Country`, Values: `[Total Sales]`, Color: Blue gradient |
| Right (50%) | **Matrix** | Rows: `Market` → `Region`, Values: `[Total Sales]`, `[Total Profit]`, `[Profit Margin %]` |

#### Row 2

| Position | Chart | Fields |
|----------|-------|--------|
| Full Width | **Area Chart** | X: `Order Date` (Monthly), Y: `[Total Sales]`, Legend: `Category` |

#### Row 3

| Position | Chart | Fields |
|----------|-------|--------|
| Left (50%) | **Clustered Column** | X: `Quarter`, Y: `[Total Sales]`, Legend: `Year` |
| Right (50%) | **KPI Visual** | Indicator: `[Total Sales]`, Trend: `Order Date`, Target: Previous Year Sales |

---

## 5. Slicer / Filter Setup

Add these slicers to **every page** (place in a consistent position — top-right or sidebar):

| Slicer | Field | Style | Settings |
|--------|-------|-------|----------|
| Year | `Year` | **Dropdown** or **Buttons** | Multi-select ON |
| Market | `Market` | **Dropdown** | Multi-select ON |
| Category | `Category` | **Buttons** | Single-select |
| Segment | `Segment` | **Buttons** | Single-select |

**Sync slicers across pages**: Select slicer → **View** → **Sync Slicers** → Check all pages.

---

## 6. Interactivity Settings

1. **Cross-filtering**: Go to **Format** → **Edit Interactions** for each chart. Set related charts to **Filter** mode, not **Highlight**
2. **Drill-through**: On the Product page, enable drill-through on `Product Name` so users can right-click any product from Page 1 to see its details
3. **Tooltips**: Add `[Total Sales]`, `[Total Profit]`, `[Profit Margin %]` as tooltip fields on all charts
4. **Bookmarks** (optional): Create bookmarks for "Technology Focus", "Furniture Focus", "Full View" for quick navigation

---

## 7. Final Polish

1. **Page titles**: Use text boxes with 20pt bold font in `#1B4F72`
2. **Alignment**: Use **Format** → **Align** to keep visuals neatly arranged
3. **Borders**: Use rounded borders (5px) with `#E0E0E0` on all cards and charts
4. **Page navigator**: Add buttons at the bottom to switch between the 3 pages
5. **Logo/Branding**: Add a small company logo in the top-left if desired

---

## Quick Start Checklist

- [ ] Import CSV and apply transformations
- [ ] Create all DAX measures
- [ ] Apply the color theme
- [ ] Build Page 1 (Executive Overview)
- [ ] Build Page 2 (Product & Category Deep Dive)
- [ ] Build Page 3 (Regional & Trend Analysis)
- [ ] Add and sync slicers
- [ ] Configure cross-filtering and drill-through
- [ ] Final alignment and polish
