Yemeksepeti Order Analysis Project
## **Motivation**

The main motivation behind the project is to get an insight into my eating-out ordering habit and create some financial awareness. By analyzing my past orders from Yemeksepeti, I want to understand how my ordering behavior is influenced by using coupons, find patterns on when I order food delivery, and investigate the opportunities for cost savings by cooking my meals at home. Trend analysis over time will also be long-term behavioral insights.
---
 
## **Data Source**

The information herein wholly originates from my personal historical order data from Yemeksepeti. Data was hand-downloaded and cleaned off my Yemeksepeti account, including but not limited to order dates and times, costs, coupons used, and order contents. Similarly, I have manually obtained ingredient prices for various recipes for comparing the costs of cooking to that of ordering.
---
##
**
Techniques Applied
**
### **1. EDA**

#### Objective:

- Understand, clean, and extract initial insights from the data.
- Answer the following questions:
  - What times of the day do I place the most orders?
  - In which cases are coupons used more frequently?
  - What are my overall spending patterns?
#### Tools Used:

- **Pandas**: For data cleaning and manipulation.
- **Matplotlib and Seaborn**: For visualizing order times, coupon usage, and costs.
#### Example Analyses:

- Use bar charts to show order frequencies across different times of the day.
- Use box plots to visualize how coupon usage affects order costs.
---
 
### **2. Coupon Analysis**

#### Objective:
- Understand how coupon usage affects costs.
- Determine under what circumstances the usage of coupons is most beneficial.
#### Models Used:

- **Association Rule Mining (Apriori/FP-Growth)**:
  - To find associations between coupon usage and food categories.
- **Logistic Regression**:
-To model the factors that influence coupon usage.
---
 
### **3. Cooking vs Ordering Cost Analysis**

#### Objective:
- Estimate the savings potential of cooking meals at home compared to ordering.
- Compare the total cost of cooking recipes with the cost of similar orders.
#### Tools and Steps:

- **Data Collection**: Collect ingredient prices for recipes manually.
- **Comparative Analysis**:
  - Analyze the cost of recipes side by side with the cost of orders.
- **Time and Cost Model**
- Calculate the economic and temporal benefits of cooking at home.
---
 
### **4. Hourly Order Analysis**
 
#### Objective:
- Study hourly order distribution for insight into behavioral patterns
- Determine peak ordering hours.
#### Techniques Used:
- **Time Series Analysis**:
  - Understand order density for any given time.
- **Visualization**:
  - Plot line charts for order hourly trends.
---
 
### **5. Trend Analysis
 
#### Objective:
- Analyze the change in ordering habits and spending over time.
- Detect seasonal, monthly, or weekly variations.
#### Models Used:

- **Time Series Models (ARIMA, Prophet)**:
  - To forecast order trends.
- **Regression Analysis**:
  - To model how spending changes over time.
---

## **Findings and Insights**

1. Identification of categories and types of orders where coupon usage was most effective.
2. Computed that cooking meals at home could yield a high percentage of savings as compared to ordering.
3. Observed that my orders are mainly concentrated on weekday evenings, with higher coupon consumption during these times.
4. Saw an increase in spending habits over time, motivating me to develop a more structured food budget.
---
## **Limitations and Future Work**

- **Data limitation**: More data could provide better accuracy in modeling.
- **Cooking cost details**: More precise ingredient pricing could refine the cost analysis.
- **Future Goals**: Develop a recommendation system to suggest optimal meals and times for ordering or cooking based on historical data.
---

