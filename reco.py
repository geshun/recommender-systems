from reco import load_data, preprocess_data, RecommendationEngine

df = load_data('data/user_interactions.csv')
df = preprocess_data(df)

recommender = RecommendationEngine(df)

user_id = 1
recommendations = recommender.recommend(user_id, top_n=5)
print(recommendations)
