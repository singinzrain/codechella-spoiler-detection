from tweepy import Status, User


class Tweet:
    id: str
    user_id: str
    text: str
    username: str
    screen_name: str
    profile_image_url: str
    created_at: str

    @staticmethod
    def parse_from_status(t: Status):
        tweet = Tweet()
        tweet.id = t.id_str
        author: User = t.author
        tweet.user_id = author.id_str
        tweet.text = t.text
        tweet.username = author.name
        tweet.screen_name = author.screen_name
        tweet.profile_image_url = author.profile_image_url
        tweet.created_at = t.created_at
        return tweet