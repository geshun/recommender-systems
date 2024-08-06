# reco/recommender.py

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd


class RecommendationEngine:
    def __init__(self, data):
        self.data = data
        self.user_profiles = self.create_user_profiles()

    def create_user_profiles(self):
        """
        Create user profiles based on their interactions.

        :return: DataFrame containing user profiles
        """
        user_profiles = self.data.pivot_table(
            index='user_id', columns='course_id', values='interaction_value', fill_value=0)
        return user_profiles

    def recommend(self, user_id, top_n=5):
        """
        Recommend top N courses for a given user.

        :param user_id: ID of the user
        :param top_n: Number of recommendations to return
        :return: List of recommended course IDs
        """
        user_profile = self.user_profiles.loc[user_id].values.reshape(1, -1)
        similarities = cosine_similarity(user_profile, self.user_profiles)[0]
        similar_users = self.user_profiles.index[similarities.argsort()[::-1]]
        # Exclude the user themselves
        similar_users = similar_users[similar_users != user_id]

        recommendations = pd.Series(dtype='float64')
        for similar_user in similar_users:
            user_courses = self.user_profiles.loc[similar_user]
            recommendations = pd.concat([recommendations, user_courses])

        recommendations = recommendations.groupby(recommendations.index).mean()
        recommendations = recommendations.sort_values(
            ascending=False).head(top_n)
        return recommendations.index.tolist()
