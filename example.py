import os
from smm_wrapper import SMMPoliticians, SMMOrganizations


# Examples using the api directly
smm = SMMPoliticians()
smm2 = SMMOrganizations()
list_of_politicians = smm.api.get_all()
politician_search = smm.api.all_search(names_contain='merkel')
politician = smm.api.all_search(_id=2193)

#examples with organizations api
list_of_organizations = smm2.api.get_all()
org_tweets = smm2.api.tweets_by()
org_posts = smm2.api.posts_by()
posts_by_organization = smm2.api.posts_by(_id='2')

#organizations api, dataframes
df_organizations = smm2.dv.get_organizations()
df_all = smm2.dv.get_all()
if not df_organizations.equals(df_all[df_organizations.columns]):
    raise Exception('problem')

one = smm2.dv.get_one(240)
df_org_tweets = smm2.dv.tweets_by()
df_org_general_tweets = smm2.dv.general_tweets(text_contains='eu')
df_org_posts = smm2.dv.posts_by()
df_org_comments = smm2.dv.comments_by()
df_org_wikipedia = smm2.dv.wikipedia()

#twitter, aggregated tweets
all_tweets = smm.api.tweets_by(text_contains='eu')
tweets_by_politician = smm.api.tweets_by(_id='2190')
tweets_by_twitter = smm.api.tweets_by(twitter_user_id='389682667')
#twitter, aggregated replies
all_replies = smm.api.replies_to(text_contains='eu')
replies_by_politician = smm.api.replies_to(_id='2190')
replies_by_twitter_id = smm.api.replies_to(twitter_user_id='389682667')
#twitter, general public
general_tweets = smm.api.general_tweets(text_contains='eu')
general_tweets_id = smm.api.general_tweets(twitter_user_id='389682667', text_contains='eu')
#facebook, aggregated posts
all_posts = smm.api.posts_by(text_contains='eu')
posts_by_politician = smm.api.posts_by(_id='2193')
posts_by_facebook_id = smm.api.posts_by(facebook_user_id='1619528691651829')
#facebook, aggregated comments
all_comments = smm.api.comments_by(text_contains='eu')
comments_by_politician = smm.api.comments_by(_id='1')
comments_by_facebook_id = smm.api.comments_by(facebook_user_id='1619528691651829')
#wikipedia
all_chobs = smm.api.wikipedia()
chobs_by_politician = smm.api.wikipedia(_id='2')
chobs_by_wikipage = smm.api.wikipedia(wikipedia_page_id='4754538')
#dataframes
df_politicians = smm.dv.get_politicians()
df_all = smm.dv.get_all()
if not df_politicians.equals(df_all[df_politicians.columns]):
    raise Exception('problem')

one = smm.dv.get_one(240)
df_tweets = smm.dv.tweets_by(_id='2190')
df_general_tweets = smm.dv.general_tweets(text_contains='eu')
df_posts = smm.dv.posts_by(_id='27')
df_comments = smm.dv.comments_by(_id='27')
df_wikipedia = smm.dv.wikipedia(_id='27')

import ipdb; ipdb.set_trace()  # breakpoint 67efd4b1 //
