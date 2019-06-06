import os
from smm_wrapper import SMM


# Examples using the api directly
smm = SMM()
smm2 = SMM(unit = "media")
list_of_politicians = smm.api.get_politicians()
politician_search = smm.api.politician_search(names_contain='merkel')
politician = smm.api.politician_search(politician_id=2193)

#testing media api
media_tweets = smm2.api.tweets_by()

#twitter, aggregated tweets
all_tweets = smm.api.tweets_by(text_contains='eu')
tweets_by_politician = smm.api.tweets_by(politician_id='2190')
tweets_by_twitter = smm.api.tweets_by(twitter_user_id='389682667')
#twitter, aggregated replies
all_replies = smm.api.replies_to(text_contains='eu')
replies_by_politician = smm.api.replies_to(politician_id='2190')
replies_by_twitter_id = smm.api.replies_to(twitter_user_id='389682667')
#facebook, aggregated posts
all_posts = smm.api.posts_by(text_contains='eu')
posts_by_politician = smm.api.posts_by(politician_id='2193')
posts_by_facebook_id = smm.api.posts_by(facebook_user_id='1619528691651829')
#facebook, aggregated comments
all_comments = smm.api.comments_by(text_contains='eu')
comments_by_politician = smm.api.comments_by(politician_id='1')
comments_by_facebook_id = smm.api.comments_by(facebook_user_id='1619528691651829')
#wikipedia
all_chobs = smm.api.wikipedia()
chobs_by_politician = smm.api.wikipedia(politician_id='2')
chobs_by_wikipage = smm.api.wikipedia(wikipedia_page_id='4754538')
#dataframes
df_politicians = smm.dv.get_politicians()
df_tweets = smm.dv.tweets_by(politician_id='2190')
df_posts = smm.dv.posts_by(politician_id='27')
df_comments = smm.dv.comments_by(politician_id='27')
df_wikipedia = smm.dv.wikipedia(politician_id='27')

import ipdb; ipdb.set_trace()  # breakpoint 67efd4b1 //
