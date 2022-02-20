from instapy import InstaPy
from instapy import smart_run

my_username = 'iamkartikeyrathore'
my_password = 'Indian@123'

session = InstaPy(username = my_username, password = my_password, headless_browser = False)

with smart_run(session):
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=500, min_followers=50) 
    session.like_by_tags(['meme', 'funny'], amount = 10)
    session.set_dont_like(['pakistan', 'china'])

