import random
from instapy import InstaPy
from instapy import smart_run

insta_username = 'kawaiigalaxystore'
insta_password = 'azerty1234'

dont_likes = ['sex', 'nude', 'naked', 'beef', 'pork', 'seafood',
              'egg', 'chicken', 'cheese', 'sausage', 'lobster',
              'fisch', 'schwein', 'lamm', 'rind', 'kuh', 'meeresfrüchte',
              'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
              'meal', 'food', 'eat', 'pancake', 'cake', 'dessert',
              'protein', 'essen', 'mahl', 'breakfast', 'lunch',
              'dinner', 'turkey', 'truthahn', 'plate', 'bacon',
              'sushi', 'burger', 'salmon', 'shrimp', 'steak',
              'schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
              'breakfast', 'dinner', 'lunch']

friends = ['list of friends I do not want to interact with']

like_tag_list = ['oldfashion', 'ullzang', 'pinkfashion', 'kawaiilifestyle',
                 'kawaiithings', 'kawaii', 'kawaiistore', 'kawaiishop', 'kawaiipink', 'pastel',
                 'aesthetic', 'girlsstuff', 'cutegirls', 'kawaiicute', 'cutestyle', 'harajukugirls',
                 'harajukustyle', 'kawaiioftheday', 'kawaiianime', 'softaesthetic', 'yumekawaii',
                 'fairykei', 'cutestuff', 'kawaiioutfit', 'cute', 'cutecute', 'softgirls'
                 ]
list_locations = ['US/united-states/', 'JP/japan/', 'CA/']
ignore_list = ['naked', 'nude', 'sex']

accounts = ['my_kawaiiwish', 'kawaiiwishstore', 'kawaiiteeshop',
            'thekawaiistory', 'kawaii.kz', 'kawaiigirlshop', 'kawaiitherapy']

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=1.34,
                                    delimit_by_numbers=True,
                                    max_followers=300,
                                    max_following=200,
                                    min_followers=50,
                                    min_following=56,
                                    min_posts=10,
                                    max_posts=50)
    session.set_action_delays(
        enabled=True, like=2, randomize=True, random_range_from=70, random_range_to=140)
    session.comment_by_locations(list_locations, amount=100)
    session.follow_by_locations(list_locations, amount=100)
    session.follow_user_following(
        accounts, amount=10, randomize=False, sleep_delay=90)

    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 3),
                         amount=random.randint(50, 100), interact=True)
    session.follow_by_tags(like_tag_list, amount=10)
    session.set_delimit_liking(enabled=True, max_likes=500, min_likes=20)
    session.set_delimit_commenting(
        enabled=True, max_comments=32, min_comments=0)

    session.unfollow_users(amount=random.randint(75, 150),
                           InstapyFollowed=(True, "all"), style="FIFO",
                           unfollow_after=90 * 60 * 60, sleep_delay=501)
    session.set_skip_users(skip_private=True,
                           private_percentage=100,
                           skip_no_profile_pic=False,
                           no_profile_pic_percentage=100,
                           skip_business=False,
                           skip_non_business=False,
                           business_percentage=100,
                           skip_business_categories=[],
                           dont_skip_business_categories=[])

    photo_comments = ['Nice shot! @{}',
                      'I love your profile! @{}',
                      'Wonderful :thumbsup:',
                      'Just incredible :open_mouth:',
                      'What camera did you use @{}?',
                      'Love your posts @{}',
                      'Looks awesome @{}',
                      'Getting inspired by you @{}',
                      ':raised_hands: Yes!',
                      'I can feel your passion @{} :muscle:']

    session.set_do_comment(enabled=True, percentage=95)
    session.set_comments(photo_comments, media='Photo')
    session.join_pods(topic='fashion')
