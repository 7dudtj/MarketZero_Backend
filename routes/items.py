from typing import List
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status
from database.connection import Database
# from database.tmp_database import tmp_items  # 임시 설정
from models.items import Item, ItemUpdate

item_database = Database(Item)

item_router = APIRouter(tags=["Items"])


# 전체 item 불러오기
@item_router.get("/all", response_model=List[Item])
async def retrieve_all_items() -> List[Item]:
    """전체 item 반환

    Returns:
        List[Item]: 전체 item
    """
    items = await item_database.get_all()
    return items


# 신상(brand-new) item 불러오기
@item_router.get("/brand-new", response_model=List[Item])
async def retrieve_brand_new_items() -> List[Item]:
    """신상(brand-new) item 반환

    Returns:
        List[Item]: 신상(brand-new) item
    """
    brand_new_items = []
    items = await item_database.get_all()
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
    items = await item_database.get_all()
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
    items = await item_database.get_all()
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
    items = await item_database.get_all()
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
    items = await item_database.get_all()
    for item in items:
        if "zero-gluten" in item["tags"]:
            zero_gluten_items.append(item)
    return zero_gluten_items


# 제로카페인(zero-caffeine) item 불러오기
@item_router.get("/zero-caffeine", response_model=List[Item])
async def retrieve_zero_caffeine_items() -> List[Item]:
    """제로카페인(zero-caffeine) item 반환

    Returns:
        List[Item]: 제로카페인(zero-caffeine) item
    """
    zero_caffeine_items = []
    items = await item_database.get_all()
    for item in items:
        if "zero-caffeine" in item["tags"]:
            zero_caffeine_items.append(item)
    return zero_caffeine_items


# 논알콜(zero-alcohol) item 불러오기
@item_router.get("/zero-alcohol", response_model=List[Item])
async def retrieve_zero_alcohol_items() -> List[Item]:
    """논알콜(zero-alcohol) item 반환

    Returns:
        List[Item]: 논알콜(zero-alcohol) item
    """
    zero_alcohol_items = []
    items = await item_database.get_all()
    for item in items:
        if "zero-alcohol" in item["tags"]:
            zero_alcohol_items.append(item)
    return zero_alcohol_items


# 특정 id를 가진 item 불러오기
@item_router.get("/{id}", response_model=Item)
async def retrieve_item(id: PydanticObjectId) -> Item:
    """특정 id를 가진 item 반환

    Args:
        id (PydanticObjectId): 찾고자 하는 item의 id

    Raises:
        HTTPException: 찾고자 하는 item이 없을 경우

    Returns:
        Item: 찾고자 하는 item 반환
    """
    item = await item_database.get(id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item with supplied ID does not exist"
        )
    return item


# 새로운 item 생성하기
@item_router.post("/new")
async def create_item(body: Item) -> dict:
    """DB에 새로운 item 추가

    Args:
        body (Item): 추가하고자 하는 item

    Returns:
        dict: item 추가 성공 메시지 반환
    """
    await item_database.save(body)
    return{
        "message": "Item created successfully."
    }
    

# 특정 id를 가진 item 업데이트하기
@item_router.put("/{id}", response_model=Item)
async def update_item(id: PydanticObjectId, body: ItemUpdate) -> Item:
    """DB에 있는 item 업데이트

    Args:
        id (PydanticObjectId): 업데이트 하고자 하는 item의 id
        body (ItemUpdate): 업데이트 하고자 하는 내용

    Raises:
        HTTPException: 업데이트 하고자 하는 item이 없을 경우

    Returns:
        Item: 업데이트가 완료된 item 반환
    """
    updated_item = await item_database.update(id, body)
    if not updated_item:
        raise HTTPException(
            statud_code=status.HTTP_404_NOT_FOUND,
            detail="Item with supplied ID does not exist"
        )
    return updated_item


# 특정 id를 가진 item 삭제하기
@item_router.delete("/{id}")
async def delete_item(id: PydanticObjectId) -> dict:
    """DB에 존재하는 특정 id를 가진 item 삭제

    Args:
        id (PydanticObjectId): 삭제하고자 하는 item의 id

    Raises:
        HTTPException: 삭제하고자 하는 item이 없을 경우

    Returns:
        dict: item 삭제 성공 메시지 반환
    """
    item = await item_database.delete(id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item with supplied ID does not exist"
        )
    return{
        "message": "Item deleted successfully."
    }
