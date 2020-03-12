from instapy import InstaPy
from instapy import smart_run

# get a session!
session = InstaPy(username='kawaiigalaxystor', password='azerty1234')

photo_comments = ['Nice shot! @{}',
    'I love your profile! @{}',
    'Your feed is an inspiration :thumbsup:',
    'Just incredible :open_mouth:',
    'What camera did you use @{}?',
    'Love your posts @{}',
    'Looks awesome @{}',
    'Getting inspired by you @{}',
    ':raised_hands: Yes!',
    'I can feel your passion @{} :muscle:']

# let's go! :>
with smart_run(session):
    # settings
    session.set_user_interact(amount=3, randomize=True, percentage=100,
                              media='Photo')
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=900,
                                    min_followers=50,
                                    min_following=50)
    session.set_simulation(enabled=False)
    session.set_do_like(enabled=True, percentage=100)
    session.set_ignore_users([])
    session.set_do_comment(enabled=True, percentage=35)
    session.set_do_follow(enabled=True, percentage=25, times=1)
    session.set_comments(photo_comments)
    session.set_ignore_if_contains([])
    session.set_action_delays(enabled=True, like=40)

    # activity
    session.interact_user_followers([], amount=340)

    session.join_pods(topic='fashion', engagement_mode='no_comments')
