from pydantic import BaseModel


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    post_id: int


class CommentIn(BaseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    comment_id: int


class UserPostWithComment(BaseModel):
    post: UserPost
    comments: list[Comment]
