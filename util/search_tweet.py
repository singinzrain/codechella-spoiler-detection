from typing import List

from TwitterSearch import TwitterSearchOrder, TwitterSearch, TwitterSearchException


def search(keywords: List[str]):
    try:
        tso = TwitterSearchOrder()
        tso.set_count(10)
        tso.set_keywords(keywords)

        ts = TwitterSearch(
            consumer_key='a',
            consumer_secret='b',
            access_token='c',
            access_token_secret='d'
        )

        # https://twittersearch.readthedocs.io/en/latest/advanced_usage_ts.html#twittersearch-without-automatic-iteration
        response = ts.search_tweets(tso)
        return response['content']

    except TwitterSearchException as e:
        print(e)


if __name__ == "__main__":
    search(["weather"])
