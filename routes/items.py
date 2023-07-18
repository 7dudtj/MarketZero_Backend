from typing import List

from fastapi import APIRouter, Body, HTTPException, status

from database.tmp_database import items  # 임시 설정
from models.items import Item

item_router = APIRouter(tags=["Items"])

# items = []


# 전체 item 불러오기
@item_router.get("/all", response_model=List[Item])
async def retrieve_all_items() -> List[Item]:
    """전체 item 반환

    Returns:
        List[Item]: 전체 item
    """
    return items


# 신상(brand-new) item 불러오기
@item_router.get("/brand-new", response_model=List[Item])
async def retrieve_brand_new_items() -> List[Item]:
    """신상(brand-new) item 반환

    Returns:
        List[Item]: 신상(brand-new) item
    """
    brand_new_items = []
    for item in items:
        if "brand-new" in item["tags"]:
            brand_new_items.append(item)
    return brand_new_items


# 추천(recommend) item 불러오기
@item_router.get("/recommend", response_model=List[Item])
async def retrieve_recommend_items() -> List[Item]:
    """추천(recommend) item 반환

    Returns:
        List[Item]: 추천(recommend) item
    """
    recommend_items = []
    for item in items:
        if "recommend" in item["tags"]:
            recommend_items.append(item)
    return recommend_items


# 무설탕(zero-sugar) item 불러오기
@item_router.get("/zero-sugar", response_model=List[Item])
async def retrieve_zero_sugar_items() -> List[Item]:
    """무설탕(zero-sugar) item 반환

    Returns:
        List[Item]: 무설탕(zero-sugar) item
    """
    zero_sugar_items = []
    for item in items:
        if "zero-sugar" in item["tags"]:
            zero_sugar_items.append(item)
    return zero_sugar_items


# 제로칼로리(zero-kcal) item 불러오기
@item_router.get("/zero-kcal", response_model=List[Item])
async def retrieve_zero_kcal_items() -> List[Item]:
    """제로칼로리(zero-kcal) item 반환

    Returns:
        List[Item]: 제로칼로리(zero-kcal) item
    """
    zero_kcal_items = []
    for item in items:
        if "zero-kcal" in item["tags"]:
            zero_kcal_items.append(item)
    return zero_kcal_items


# 제로글루텐(zero-gluten) item 불러오기
@item_router.get("/zero-gluten", response_model=List[Item])
async def retrieve_zero_gluten_items() -> List[Item]:
    """제로글루텐(zero-gluten) item 반환

    Returns:
        List[Item]: 제로글루텐(zero-gluten) item
    """
    zero_gluten_items = []
    for item in items:
        if "zero-gluten" in item["tags"]:
            zero_gluten_items.append(item)
    return zero_gluten_items


# 제로카페인(zero-caffeine) item 불러오기
@item_router.get("/zero-caffeine", response_model=List[Item])
async def retrieve_zero_caffeine_items() -> List[Item]:
    zero_caffeine_items = []
    for item in items:
        if "zero-caffeine" in item["tags"]:
            zero_caffeine_items.append(item)
    return zero_caffeine_items


# 논알콜(zero-alcohol) item 불러오기
@item_router.get("/zero-alcohol", response_model=List[Item])
async def retrieve_zero_alcohol_items() -> List[Item]:
    zero_alcohol_items = []
    for item in items:
        if "zero-alcohol" in item["tags"]:
            zero_alcohol_items.append(item)
    return zero_alcohol_items


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


# 새로운 item 생성하기 -> TBD
# @item_router.post("/new")
# async def create_item(body: Item) -> dict:
#     """서버에 새로운 item 추가

#     Args:
#         body (Item): 추가하고자 하는 item

#     Returns:
#         dict: item 추가 성공 메시지 반환
#     """
#     items.append(body)
#     return {"message": "성공적으로 item을 추가하였습니다."}


# 특정 id를 가진 item 삭제하기 -> TBD
# @item_router.delete("/{id}")
# async def delete_item(id: int) -> dict:
#     """서버에 존재하는 특정 id를 가진 item 삭제

#     Args:
#         id (int): 삭제하고자 하는 item의 id

#     Raises:
#         HTTPException: 삭제하고자 하는 item이 없을 경우

#     Returns:
#         dict: item 삭제 성공 메시지 반환
#     """
#     for item in items:
#         if item.id == id:
#             items.remove(item)
#             return {"message": "성공적으로 item을 삭제하였습니다."}
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND, detail="주어진 id에 해당하는 item이 없습니다."
#     )


# 전체 item 삭제하기 -> TBD
# @item_router.delete("/")
# async def delete_all_items() -> dict:
#     """서버에 존재하는 모든 item 삭제

#     Returns:
#         dict: 삭제 성공 메시지 반환
#     """
#     items.clear()
#     return {"message": "성공적으로 모든 item을 삭제하였습니다."}
