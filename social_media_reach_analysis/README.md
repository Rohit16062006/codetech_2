# 📱 Social Media Reach Analysis

A data analytics project that analyzes post-level social media performance data to uncover reach trends, engagement patterns, and content strategy insights across multiple platforms. Built as part of a Data Analytics internship project submission for **CodeTech IT Solutions**.

---

## 📌 Project Overview

This project explores 18 months (Jan 2023 – Jun 2024) of simulated social media post data across five platforms to understand what drives reach and engagement. The goal is to demonstrate core data analytics skills: data wrangling, aggregation, trend analysis, and multi-dimensional visualization using Python.

**Key questions answered:**
- How does total reach trend over time?
- Which platform delivers the most reach and the best engagement rate?
- Which content/post type (Image, Video, Carousel, Text, Reel) performs best?
- How are followers growing across platforms?
- Are there weekday patterns in audience reach?
- How do reach, impressions, and engagement metrics correlate with each other?
- Which platform + post-type combination performs best?

---

## 🗂️ Project Structure

```
social_media_reach_analysis/
│
├── data/
│   └── social_media_data.csv          # Post-level performance dataset
│
├── outputs/
│   ├── 01_monthly_reach_trend.png
│   ├── 02_reach_by_platform.png
│   ├── 03_engagement_rate_by_platform.png
│   ├── 04_reach_by_posttype.png
│   ├── 05_platform_reach_trend.png
│   ├── 06_follower_growth.png
│   ├── 07_reach_by_weekday.png
│   ├── 08_correlation_heatmap.png
│   ├── 09_posttype_platform_heatmap.png
│   └── summary_report.txt             # Auto-generated text summary
│
├── generate_data.py                   # Script to generate the synthetic dataset
├── social_media_analysis.py           # Main analysis & visualization script
├── requirements.txt
└── README.md
```

---

## 🧰 Tech Stack

- **Python 3**
- **Pandas** — data manipulation & aggregation
- **Matplotlib** — chart rendering
- **Seaborn** — statistical visualization styling

---

## 📊 Dataset

The dataset (`data/social_media_data.csv`) contains ~1,000 post records with the following fields:

| Column | Description |
|---|---|
| `Date` | Date the post was published |
| `Platform` | Instagram, Twitter/X, Facebook, LinkedIn, or TikTok |
| `PostType` | Image, Video, Carousel, Text, or Reel/Short |
| `Followers` | Follower count of the account at time of posting |
| `Reach` | Number of unique accounts that saw the post |
| `Impressions` | Total number of times the post was displayed |
| `Likes`, `Comments`, `Shares` | Raw engagement counts |
| `Engagements` | Sum of likes, comments, and shares |
| `EngagementRate` | Engagements ÷ Reach |

> Note: The dataset is synthetically generated with realistic platform-specific behavior (e.g. TikTok has higher reach multipliers, video/Reel content outperforms static posts, weekends and holiday-season months see boosted reach) to simulate real-world social media performance. You can replace `data/social_media_data.csv` with exported analytics data from Instagram Insights, Meta Business Suite, etc. — just match the column names.

---

## ▶️ How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/social-media-reach-analysis.git
   cd social-media-reach-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Regenerate the dataset**
   ```bash
   python generate_data.py
   ```

4. **Run the analysis**
   ```bash
   python social_media_analysis.py
   ```

5. Check the `outputs/` folder for all generated charts and the summary report.

---

## 📈 Sample Visualizations

| Chart | Insight |
|---|---|
| Monthly Reach Trend | Shows overall reach growth/decline over time |
| Reach by Platform | Identifies which platform drives the most visibility |
| Engagement Rate by Platform | Shows which audience is most interactive |
| Reach by Post Type | Reveals which content format performs best |
| Platform Reach Trend | Tracks how each platform's reach evolves monthly |
| Follower Growth | Visualizes audience growth across platforms |
| Reach by Weekday | Highlights best days to post |
| Correlation Heatmap | Shows relationships between reach, impressions, and engagement metrics |
| Post Type × Platform Heatmap | Pinpoints the best content format for each platform |

---

## 🔍 Key Insights (from this dataset)

- **TikTok** generates the highest reach per post, driven by its strong algorithmic distribution.
- **Reel/Short** and **Video** content consistently outperform static Image and Text posts.
- Engagement rates are highest on **TikTok** and **Instagram**, while **Twitter/X** and **Facebook** lag behind.
- **Weekends** see a noticeable lift in average reach.
- Reach and Engagements show a strong positive correlation, confirming that wider distribution drives more interaction.
- November–December (holiday/campaign season) shows a clear reach spike across platforms.

---

## 🚀 Future Improvements

- Build an interactive dashboard (Plotly Dash / Power BI / Tableau)
- Add sentiment analysis on comments
- Predict optimal posting time using time-series forecasting
- Integrate live data via platform APIs (Meta Graph API, Twitter API, etc.)
- Add hashtag/caption performance analysis

---

## 👤 Author

Submitted as part of a Data Analytics Internship project at **CodeTech IT Solutions**.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
