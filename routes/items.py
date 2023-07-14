from typing import List

from fastapi import APIRouter, Body, HTTPException, status

from models.items import Item

item_router = APIRouter(tags=["Items"])

items = []


# 전체 item 불러오기
@item_router.get("/", response_model=List[Item])
async def retrieve_all_items() -> List[Item]:
    """전체 item 반환

    Returns:
        List[Item]: 전체 item
    """
    return items


# 특정 id를 가진 item 불러오기
@item_router.get("/{id}", response_model=Item)
async def retrieve_item(id: int) -> Item:
    """특정 id를 가진 item 반환

    Args:
        id (int): 찾고자 하는 item의 id

    Raises:
        HTTPException: 찾고자 하는 item이 없을 경우

    Returns:
        Item: 찾고자 하는 item 반환
    """
    for item in items:
        if item.id == id:
            return item
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="주어진 id에 해당하는 item이 없습니다."
    )


# 새로운 item 생성하기
# 현재, 중복된 id를 가진 제품을 넣을 수 있음. TBD
@item_router.post("/new")
async def create_item(body: Item) -> dict:
    """서버에 새로운 item 추가

    Args:
        body (Item): 추가하고자 하는 item

    Returns:
        dict: item 추가 성공 메시지 반환
    """
    items.append(body)
    return {"message": "성공적으로 item을 추가하였습니다."}


# 특정 id를 가진 item 삭제하기
@item_router.delete("/{id}")
async def delete_item(id: int) -> dict:
    """서버에 존재하는 특정 id를 가진 item 삭제

    Args:
        id (int): 삭제하고자 하는 item의 id

    Raises:
        HTTPException: 삭제하고자 하는 item이 없을 경우

    Returns:
        dict: item 삭제 성공 메시지 반환
    """
    for item in items:
        if item.id == id:
            items.remove(item)
            return {"message": "성공적으로 item을 삭제하였습니다."}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="주어진 id에 해당하는 item이 없습니다."
    )


# 전체 item 삭제하기
@item_router.delete("/")
async def delete_all_items() -> dict:
    """서버에 존재하는 모든 item 삭제

    Returns:
        dict: 삭제 성공 메시지 반환
    """
    items.clear()
    return {"message": "성공적으로 모든 item을 삭제하였습니다."}
