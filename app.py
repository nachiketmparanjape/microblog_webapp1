from models.post import Post
from database import Database

Database.initialize()

post = Post(blog_id='123',
            title = "Another great post",
            content = 'This is some sample content',
            author = 'Jose')

post.save_to_mongo()