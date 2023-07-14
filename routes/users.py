from fastapi import APIRouter, HTTPException, status

from models.users import User, UserSignIn

user_router = APIRouter(tags=["User"])

users = {}  # key: email, value: User


# 회원가입
@user_router.post("/signup")
async def sign_new_user(data: User) -> dict:
    """회원가입 함수

    Args:
        data (User): 회원가입 하고자 하는 유저의 정보

    Raises:
        HTTPException: 이미 존재하는 이메일이 있는 경우

    Returns:
        dict: 회원가입 성공 메시지 반환
    """
    if data.email in users:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="이미 존재하는 회원입니다."
        )
    users[data.email] = data
    return {"message": "성공적으로 회원가입이 완료되었습니다."}


# 로그인
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    """로그인 함수

    Args:
        user (UserSignIn): 로그인 하고자 하는 유저의 email, password

    Raises:
        HTTPException: 존재하지 않는 이메일일 때
        HTTPException: 비밀번호가 틀렸을 때

    Returns:
        dict: 로그인 성공 메시지 반환
    """
    if user.email not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="존재하지 않는 회원입니다."
        )
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="비밀번호가 일치하지 않습니다."
        )
    return {"message": "성공적으로 로그인이 완료되었습니다."}
