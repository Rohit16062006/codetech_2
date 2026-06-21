"""
Social Media Reach Analysis
----------------------------
Analyzes post-level social media performance data across platforms
to uncover reach trends, engagement patterns, and content performance.

Output charts are saved as PNG files in the 'outputs' folder.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 110

DATA_PATH = "data/social_media_data.csv"
OUT_DIR = "outputs"

# ---------------------------------------------------------
# 1. Load and prepare data
# ---------------------------------------------------------
df = pd.read_csv(DATA_PATH, parse_dates=["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)
df["Weekday"] = df["Date"].dt.day_name()

print("Dataset shape:", df.shape)
print(df.head())
print("\nReach summary:\n", df["Reach"].describe())

# ---------------------------------------------------------
# 2. Monthly Reach Trend (Line Chart)
# ---------------------------------------------------------
monthly_reach = df.groupby("Month")["Reach"].sum().reset_index()

plt.figure(figsize=(12, 5))
plt.plot(monthly_reach["Month"], monthly_reach["Reach"], marker="o", color="#E63946")
plt.title("Monthly Total Reach Trend", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Total Reach")
plt.xticks(rotation=60, fontsize=8)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/01_monthly_reach_trend.png")
plt.close()

# ---------------------------------------------------------
# 3. Reach by Platform (Bar Chart)
# ---------------------------------------------------------
platform_reach = df.groupby("Platform")["Reach"].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=platform_reach, x="Reach", y="Platform", hue="Platform", palette="rocket", legend=False)
plt.title("Total Reach by Platform", fontsize=14, fontweight="bold")
plt.xlabel("Total Reach")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/02_reach_by_platform.png")
plt.close()

# ---------------------------------------------------------
# 4. Average Engagement Rate by Platform (Bar Chart)
# ---------------------------------------------------------
platform_engagement = df.groupby("Platform")["EngagementRate"].mean().sort_values(ascending=False).reset_index()
platform_engagement["EngagementRate"] = (platform_engagement["EngagementRate"] * 100).round(2)

plt.figure(figsize=(8, 5))
sns.barplot(data=platform_engagement, x="EngagementRate", y="Platform", hue="Platform", palette="crest", legend=False)
plt.title("Average Engagement Rate by Platform (%)", fontsize=14, fontweight="bold")
plt.xlabel("Engagement Rate (%)")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/03_engagement_rate_by_platform.png")
plt.close()

# ---------------------------------------------------------
# 5. Reach by Post Type (Bar Chart)
# ---------------------------------------------------------
posttype_reach = df.groupby("PostType")["Reach"].mean().sort_values(ascending=False).reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(data=posttype_reach, x="Reach", y="PostType", hue="PostType", palette="flare", legend=False)
plt.title("Average Reach by Post Type", fontsize=14, fontweight="bold")
plt.xlabel("Average Reach")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/04_reach_by_posttype.png")
plt.close()

# ---------------------------------------------------------
# 6. Platform Reach Trend Over Time (Multi-line Chart)
# ---------------------------------------------------------
platform_month = df.groupby(["Month", "Platform"])["Reach"].sum().reset_index()
pivot_platform = platform_month.pivot(index="Month", columns="Platform", values="Reach").fillna(0)

plt.figure(figsize=(13, 6))
for col in pivot_platform.columns:
    plt.plot(pivot_platform.index, pivot_platform[col], marker="o", markersize=3, label=col)
plt.title("Monthly Reach Trend by Platform", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Reach")
plt.xticks(rotation=60, fontsize=7)
plt.legend(title="Platform", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/05_platform_reach_trend.png")
plt.close()

# ---------------------------------------------------------
# 7. Follower Growth Over Time (Line Chart)
# ---------------------------------------------------------
follower_trend = df.groupby(["Month", "Platform"])["Followers"].max().reset_index()
pivot_followers = follower_trend.pivot(index="Month", columns="Platform", values="Followers")

plt.figure(figsize=(13, 6))
for col in pivot_followers.columns:
    plt.plot(pivot_followers.index, pivot_followers[col], marker="o", markersize=3, label=col)
plt.title("Follower Growth Over Time by Platform", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Followers")
plt.xticks(rotation=60, fontsize=7)
plt.legend(title="Platform", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/06_follower_growth.png")
plt.close()

# ---------------------------------------------------------
# 8. Reach by Day of Week (Bar Chart)
# ---------------------------------------------------------
weekday_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
weekday_reach = df.groupby("Weekday")["Reach"].mean().reindex(weekday_order).reset_index()

plt.figure(figsize=(9, 5))
sns.barplot(data=weekday_reach, x="Weekday", y="Reach", hue="Weekday", palette="mako", legend=False)
plt.title("Average Reach by Day of Week", fontsize=14, fontweight="bold")
plt.ylabel("Average Reach")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/07_reach_by_weekday.png")
plt.close()

# ---------------------------------------------------------
# 9. Correlation Heatmap (Reach, Impressions, Engagements, etc.)
# ---------------------------------------------------------
corr_cols = ["Followers", "Reach", "Impressions", "Likes", "Comments", "Shares", "Engagements", "EngagementRate"]
corr_matrix = df[corr_cols].corr()

plt.figure(figsize=(9, 7))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Performance Metrics", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/08_correlation_heatmap.png")
plt.close()

# ---------------------------------------------------------
# 10. Platform vs Post Type Reach Heatmap
# ---------------------------------------------------------
heat_data = df.pivot_table(values="Reach", index="PostType", columns="Platform", aggfunc="mean")

plt.figure(figsize=(9, 6))
sns.heatmap(heat_data, annot=True, fmt=".0f", cmap="YlOrRd", linewidths=0.5)
plt.title("Average Reach: Post Type vs Platform", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig(f"{OUT_DIR}/09_posttype_platform_heatmap.png")
plt.close()

# ---------------------------------------------------------
# 11. Save a summary report (text)
# ---------------------------------------------------------
with open(f"{OUT_DIR}/summary_report.txt", "w") as f:
    f.write("SOCIAL MEDIA REACH ANALYSIS - SUMMARY REPORT\n")
    f.write("=" * 48 + "\n\n")
    f.write(f"Total posts analyzed: {len(df):,}\n")
    f.write(f"Date range: {df['Date'].min().date()} to {df['Date'].max().date()}\n")
    f.write(f"Total reach: {df['Reach'].sum():,}\n")
    f.write(f"Total impressions: {df['Impressions'].sum():,}\n")
    f.write(f"Total engagements: {df['Engagements'].sum():,}\n")
    f.write(f"Overall average engagement rate: {df['EngagementRate'].mean()*100:.2f}%\n\n")

    f.write("Reach by Platform:\n")
    f.write(platform_reach.to_string(index=False) + "\n\n")

    f.write("Average Engagement Rate by Platform (%):\n")
    f.write(platform_engagement.to_string(index=False) + "\n\n")

    f.write("Average Reach by Post Type:\n")
    f.write(posttype_reach.to_string(index=False) + "\n\n")

    best_month = monthly_reach.loc[monthly_reach["Reach"].idxmax()]
    f.write(f"Best performing month (reach): {best_month['Month']} ({best_month['Reach']:,})\n")

    best_weekday = weekday_reach.loc[weekday_reach["Reach"].idxmax()]
    f.write(f"Best performing weekday (avg reach): {best_weekday['Weekday']} ({best_weekday['Reach']:.0f})\n")

    top_platform = platform_reach.iloc[0]
    f.write(f"Top platform by total reach: {top_platform['Platform']} ({top_platform['Reach']:,})\n")

print("\nAll charts and summary report saved to the 'outputs' folder.")
