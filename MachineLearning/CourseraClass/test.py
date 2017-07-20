#coding=utf-8

import graphlab

products = graphlab.SFrame("amazon_baby.gl")

products["word_count"] = graphlab.text_analytics.count_words(products["review"])


def awesome_count(product_dict):
    if "awesome" in product_dict:
        return product_dict["awesome"]
    else:
        return 0

products["awesome"] = products["word_count"].apply(awesome_count)
# print products





diaper_baby_reviews["predicted_sentiment"] = sentiment_model.predict(diaper_baby_reviews, output_type="probablity")
diaper_baby_reviews.head()
diaper_baby_reviews = diaper_baby_reviews.sort("predicted_sentiment", ascending=False)
diaper_baby_reviews.head()
