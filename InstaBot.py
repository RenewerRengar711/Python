from instapy import InstaPy
from instapy import smart_run


insta_username = 'dogsbevibin'
insta_password = '1jacques'


session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)
session.login()

with smart_run(session):
    session.set_quota_supervisor(enabled=True, sleep_after=["likes", "follows", "unfollows"],
                                 sleepyhead=True, stochastic_flow=True, notify_me=True,
                                 peak_likes_hourly=50,
                                 peak_likes_daily=500,
                                 peak_follows_hourly=20,
                                 peak_follows_daily=200,
                                 peak_unfollows_hourly=16,
                                 peak_unfollows_daily=164)
    session.set_skip_users(skip_no_profile_pic=True,
                           no_profile_pic_percentage=100,
                           skip_business=True,
                           business_percentage=50)
    session.set_relationship_bounds(enabled=True,
                                    max_followers=2000,
                                    min_followers=100)
    session.set_action_delays(enabled=True,
                              like=1,
                              follow=2,
                              unfollow=2)

    session.like_by_tags(['#dogs', '#dog'])
    session.follow_likers(['doggyunity', 'dog_trending'], photos_grab_amount=2, follow_likers_per_photo=15,
                          randomize=True,
                          sleep_delay=600, interact=True)
    session.unfollow_users(amount=40, allFollowing=True, style="LIFO", unfollow_after=48 * 60 * 60, sleep_delay=450)


session.end()
