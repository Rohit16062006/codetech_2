"""
Generates a synthetic social media performance dataset
covering posts across multiple platforms over 18 months.
"""

import pandas as pd
import numpy as np

np.random.seed(7)

start_date = "2023-01-01"
end_date = "2024-06-30"
dates = pd.date_range(start_date, end_date, freq="D")

platforms = ["Instagram", "Twitter/X", "Facebook", "LinkedIn", "TikTok"]
post_types = ["Image", "Video", "Carousel", "Text", "Reel/Short"]

# Base follower counts per platform (growing over time)
base_followers = {
    "Instagram": 12000, "Twitter/X": 8000, "Facebook": 15000,
    "LinkedIn": 5000, "TikTok": 6000
}

# Platform-specific reach multiplier and engagement tendency
platform_profile = {
    "Instagram": {"reach_mult": 1.3, "engagement_rate": 0.045},
    "Twitter/X": {"reach_mult": 0.9, "engagement_rate": 0.018},
    "Facebook": {"reach_mult": 0.7, "engagement_rate": 0.022},
    "LinkedIn": {"reach_mult": 0.6, "engagement_rate": 0.032},
    "TikTok": {"reach_mult": 2.1, "engagement_rate": 0.065},
}

post_type_boost = {
    "Image": 1.0, "Video": 1.4, "Carousel": 1.2, "Text": 0.6, "Reel/Short": 1.8
}

rows = []
follower_state = base_followers.copy()

for date in dates:
    day_index = (date - dates[0]).days
    # gradual follower growth
    for p in platforms:
        growth_rate = 1 + np.random.uniform(0.0003, 0.0012)
        follower_state[p] = follower_state[p] * growth_rate

    n_posts_today = np.random.poisson(2)
    for _ in range(n_posts_today):
        platform = np.random.choice(platforms)
        post_type = np.random.choice(post_types, p=[0.25, 0.25, 0.15, 0.1, 0.25])

        profile = platform_profile[platform]
        followers = follower_state[platform]

        # weekend/evening boost simulated via weekday factor
        weekday_factor = 1.25 if date.dayofweek >= 5 else 1.0

        # seasonal campaign boost (e.g. festive months)
        month_factor = 1.4 if date.month in [11, 12] else 1.0

        reach = followers * profile["reach_mult"] * post_type_boost[post_type] \
                * weekday_factor * month_factor * np.random.uniform(0.4, 1.3)
        impressions = reach * np.random.uniform(1.1, 1.6)

        engagement_rate = profile["engagement_rate"] * post_type_boost[post_type] * np.random.uniform(0.6, 1.4)
        likes = reach * engagement_rate * np.random.uniform(0.6, 0.85)
        comments = reach * engagement_rate * np.random.uniform(0.05, 0.15)
        shares = reach * engagement_rate * np.random.uniform(0.05, 0.2)
        engagements = likes + comments + shares

        rows.append({
            "Date": date,
            "Platform": platform,
            "PostType": post_type,
            "Followers": int(followers),
            "Reach": int(reach),
            "Impressions": int(impressions),
            "Likes": int(likes),
            "Comments": int(comments),
            "Shares": int(shares),
            "Engagements": int(engagements),
            "EngagementRate": round(engagements / reach, 4) if reach > 0 else 0,
        })

df = pd.DataFrame(rows)
df.sort_values("Date", inplace=True)
df.to_csv("data/social_media_data.csv", index=False)
print(df.shape)
print(df.head())
