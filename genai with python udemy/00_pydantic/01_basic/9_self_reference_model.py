from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id : int
    content : str
    replies : Optional[List['Comment']] = None


Comment.model_rebuild()

comment = Comment(
    id=1,
    content='first comment',
    replies=[
        Comment(id=2, content='1st Reply'),
        Comment(id=3,content='2nd Reply',replies=[ 
                                            Comment(id=4, content='reply to second Comment') ]
                )
    ]
)