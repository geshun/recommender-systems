# reco/utils.py
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(profile1, profile2):
    """
    Calculate similarity between two user profiles.

    :param profile1: First user profile
    :param profile2: Second user profile
    :return: Similarity score
    """
    similarity = cosine_similarity(profile1.reshape(
        1, -1), profile2.reshape(1, -1))[0][0]
    return similarity
