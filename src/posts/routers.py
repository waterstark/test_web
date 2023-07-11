from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from posts.models import Post
from auth.models import User
from posts.schemas import ReadAllPosts, CreatePost, EditPost


from database import get_async_session


router = APIRouter(prefix="/posts", tags=["Post"])


@router.get("/", response_model=ReadAllPosts, status_code=status.HTTP_200_OK)
async def get_posts(session: AsyncSession = Depends(get_async_session)):
    query = select(Post).limit(10)
    result = await session.execute(query)
    posts = result.scalars().all()
    return {"data": posts}


@router.post("/", response_model=CreatePost, status_code=status.HTTP_201_CREATED)
async def upload_post(
    new_post: CreatePost, session: AsyncSession = Depends(get_async_session)
):
    query = select(Post).where(Post.id == new_post.data.id)
    post = await session.execute(query)
    if post.scalar():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    print(new_post.data.dict())
    # stmt = insert(Post).values(**new_post.data.dict(), owner_id=User.id)
    # await session.execute(stmt)
    # await session.commit()
    return {"data": new_post.data}


@router.put("/{post_id}", response_model=EditPost, status_code=status.HTTP_200_OK)
async def edit_post(
    post_id: int,
    updated_post: EditPost,
    session: AsyncSession = Depends(get_async_session),
):
    query = select(Post).where(Post.id == post_id)
    post = await session.execute(query)
    if post.scalar() == None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    stmt = update(Post).values(**updated_post.dict()).where(Post.id == post_id)
    await session.execute(stmt)
    await session.commit()
    return {"data": updated_post}


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def upload_post(post_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Post).where(post_id == Post.id)
    await session.execute(stmt)
    await session.commit()
