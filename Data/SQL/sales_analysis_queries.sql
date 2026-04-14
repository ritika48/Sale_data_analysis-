-- =============================================================================
-- GLOBAL SUPERSTORE — SALES DATA ANALYSIS QUERIES
-- =============================================================================
-- Dataset : Global_Superstore2.csv  (51,290 rows | 2011–2014)
-- Table   : global_superstore
-- Purpose : Extract business insights on revenue, profitability, trends,
--           customer behavior, and operational efficiency.
-- =============================================================================


-- ─────────────────────────────────────────────────────────────────────────────
-- 1. KPI SUMMARY — Total Sales, Profit, Orders & Avg Discount by Year
-- Business Purpose: Quick executive snapshot of yearly performance.
-- ─────────────────────────────────────────────────────────────────────────────

SELECT
    YEAR([Order Date])                          AS [Year],
    COUNT(DISTINCT [Order ID])                  AS Total_Orders,
    ROUND(SUM(Sales), 2)                        AS Total_Sales,
    ROUND(SUM(Profit), 2)                       AS Total_Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2)  AS Profit_Margin_Pct,
    ROUND(AVG(Discount) * 100, 2)               AS Avg_Discount_Pct,
    ROUND(SUM([Shipping Cost]), 2)              AS Total_Shipping_Cost
FROM global_superstore
GROUP BY YEAR([Order Date])
ORDER BY [Year];


-- ─────────────────────────────────────────────────────────────────────────────
-- 2. TOP 10 PRODUCTS — By Total Revenue
-- Business Purpose: Identify best-selling products for inventory focus.
-- ─────────────────────────────────────────────────────────────────────────────

SELECT TOP 10
    [Product Name],
    Category,
    [Sub-Category],
    ROUND(SUM(Sales), 2)    AS Total_Revenue,
    ROUND(SUM(Profit), 2)   AS Total_Profit,
    SUM(Quantity)            AS Units_Sold
FROM global_superstore
GROUP BY [Product Name], Category, [Sub-Category]
ORDER BY Total_Revenue DESC;


-- ─────────────────────────────────────────────────────────────────────────────
-- 3. TOP 10 CUSTOMERS — By Total Spending
-- Business Purpose: Identify high-value customers for retention campaigns.
-- ─────────────────────────────────────────────────────────────────────────────

SELECT TOP 10
    [Customer ID],
    [Customer Name],
    Segment,
    COUNT(DISTINCT [Order ID])  AS Total_Orders,
    ROUND(SUM(Sales), 2)        AS Total_Spending,
    ROUND(SUM(Profit), 2)       AS Total_Profit
FROM global_superstore
GROUP BY [Customer ID], [Customer Name], Segment
ORDER BY Total_Spending DESC;


-- ─────────────────────────────────────────────────────────────────────────────
-- 4. CATEGORY PERFORMANCE — Sales, Profit & Margin by Category
-- Business Purpose: Evaluate which product categories drive profitability.
-- ─────────────────────────────────────────────────────────────────────────────

SELECT
    Category,
    COUNT(DISTINCT [Order ID])                          AS Total_Orders,
    ROUND(SUM(Sales), 2)                                AS Total_Sales,
    ROUND(SUM(Profit), 2)                               AS Total_Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin_Pct,
    ROUND(AVG(Discount) * 100, 2)                       AS Avg_Discount_Pct
FROM global_superstore
GROUP BY Category
ORDER BY Total_Sales DESC;


-- ─────────────────────────────────────────────────────────────────────────────
-- 5. SUB-CATEGORY RANKING — All 17 Sub-Categories by Profitability
-- Business Purpose: Pinpoint profitable & unprofitable sub-categories.
-- ─────────────────────────────────────────────────────────────────────────────

SELECT
    [Sub-Category],
    Category,
    ROUND(SUM(Sales), 2)                                AS Total_Sales,
    ROUND(SUM(Profit), 2)                               AS Total_Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin_Pct,
    SUM(Quantity)                                        AS Units_Sold,
    ROUND(AVG(Discount) * 100, 2)                       AS Avg_Discount_Pct
FROM global_superstore
GROUP BY [Sub-Category], Category
ORDER BY Total_Profit DESC;


-- ─────────────────────────────────────────────────────────────────────────────
-- 6. MARKET & REGION ANALYSIS — Revenue and Profit by Market / Region
-- Business Purpose: Identify strongest and weakest geographic markets.
-- ─────────────────────────────────────────────────────────────────────────────

-- 6a. By Market
SELECT
    Market,
    COUNT(DISTINCT [Order ID])                          AS Total_Orders,
    ROUND(SUM(Sales), 2)                                AS Total_Sales,
    ROUND(SUM(Profit), 2)                               AS Total_Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin_Pct
FROM global_superstore
GROUP BY Market
ORDER BY Total_Sales DESC;

-- 6b. By Region
SELECT
    Region,
    Market,
    ROUND(SUM(Sales), 2)                                AS Total_Sales,
    ROUND(SUM(Profit), 2)                               AS Total_Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin_Pct
FROM global_superstore
GROUP BY Region, Market
ORDER BY Total_Sales DESC;


-- ─────────────────────────────────────────────────────────────────────────────
-- 7. MONTHLY SALES TRENDS — Time-Series for Seasonality Detection
-- Business Purpose: Reveal seasonal patterns for demand forecasting.
-- ─────────────────────────────────────────────────────────────────────────────

SELECT
    YEAR([Order Date])                          AS [Year],
    MONTH([Order Date])                         AS [Month],
    ROUND(SUM(Sales), 2)                        AS Monthly_Sales,
    ROUND(SUM(Profit), 2)                       AS Monthly_Profit,
    COUNT(DISTINCT [Order ID])                  AS Monthly_Orders
FROM global_superstore
GROUP BY YEAR([Order Date]), MONTH([Order Date])
ORDER BY [Year], [Month];


-- ─────────────────────────────────────────────────────────────────────────────
-- 8. QUARTERLY PERFORMANCE — Year-over-Year Quarter Comparison
-- Business Purpose: Compare quarter-by-quarter growth across years.
-- ─────────────────────────────────────────────────────────────────────────────

SELECT
    YEAR([Order Date])                          AS [Year],
    DATEPART(QUARTER, [Order Date])             AS [Quarter],
    ROUND(SUM(Sales), 2)                        AS Quarterly_Sales,
    ROUND(SUM(Profit), 2)                       AS Quarterly_Profit,
    COUNT(DISTINCT [Order ID])                  AS Quarterly_Orders
FROM global_superstore
GROUP BY YEAR([Order Date]), DATEPART(QUARTER, [Order Date])
ORDER BY [Year], [Quarter];


-- ─────────────────────────────────────────────────────────────────────────────
-- 9. SHIPPING MODE ANALYSIS — Cost, Speed & Profitability per Mode
-- Business Purpose: Optimize shipping strategy for cost-effectiveness.
-- ─────────────────────────────────────────────────────────────────────────────

SELECT
    [Ship Mode],
    COUNT(DISTINCT [Order ID])                  AS Total_Orders,
    ROUND(SUM(Sales), 2)                        AS Total_Sales,
    ROUND(SUM(Profit), 2)                       AS Total_Profit,
    ROUND(SUM([Shipping Cost]), 2)              AS Total_Shipping_Cost,
    ROUND(AVG(DATEDIFF(DAY, [Order Date], [Ship Date])), 1)  AS Avg_Days_to_Ship,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2)     AS Profit_Margin_Pct
FROM global_superstore
GROUP BY [Ship Mode]
ORDER BY Total_Orders DESC;


-- ─────────────────────────────────────────────────────────────────────────────
-- 10. DISCOUNT IMPACT ON PROFIT — Discount Bands vs Profitability
-- Business Purpose: Determine the optimal discount level before margin erosion.
-- ─────────────────────────────────────────────────────────────────────────────

SELECT
    CASE
        WHEN Discount = 0       THEN '0% (No Discount)'
        WHEN Discount <= 0.10   THEN '1–10%'
        WHEN Discount <= 0.20   THEN '11–20%'
        WHEN Discount <= 0.30   THEN '21–30%'
        WHEN Discount <= 0.40   THEN '31–40%'
        ELSE '41%+'
    END                                          AS Discount_Band,
    COUNT(*)                                     AS Total_Rows,
    ROUND(SUM(Sales), 2)                         AS Total_Sales,
    ROUND(SUM(Profit), 2)                        AS Total_Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin_Pct,
    ROUND(AVG(Profit), 2)                        AS Avg_Profit_Per_Item
FROM global_superstore
GROUP BY
    CASE
        WHEN Discount = 0       THEN '0% (No Discount)'
        WHEN Discount <= 0.10   THEN '1–10%'
        WHEN Discount <= 0.20   THEN '11–20%'
        WHEN Discount <= 0.30   THEN '21–30%'
        WHEN Discount <= 0.40   THEN '31–40%'
        ELSE '41%+'
    END
ORDER BY Discount_Band;


-- ─────────────────────────────────────────────────────────────────────────────
-- 11. ORDER PRIORITY BREAKDOWN — Volume & Profit by Priority Level
-- Business Purpose: Assess whether high-priority orders yield better margins.
-- ─────────────────────────────────────────────────────────────────────────────

SELECT
    [Order Priority],
    COUNT(DISTINCT [Order ID])                          AS Total_Orders,
    ROUND(SUM(Sales), 2)                                AS Total_Sales,
    ROUND(SUM(Profit), 2)                               AS Total_Profit,
    ROUND(SUM(Profit) / NULLIF(SUM(Sales), 0) * 100, 2) AS Profit_Margin_Pct,
    ROUND(AVG(DATEDIFF(DAY, [Order Date], [Ship Date])), 1) AS Avg_Days_to_Ship
FROM global_superstore
GROUP BY [Order Priority]
ORDER BY Total_Orders DESC;


-- =============================================================================
-- END OF ANALYSIS QUERIES
-- =============================================================================
