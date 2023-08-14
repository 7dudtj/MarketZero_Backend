from fastapi import APIRouter, HTTPException, status
from database.connection import Database
from models.users import User, UserSignIn

user_database = Database(User)

user_router = APIRouter(tags=["User"])


# 회원가입(사용자 등록)
@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
    """회원가입(사용자 등록)

    Args:
        user (User): 회원가입 하고자 하는 유저의 정보

    Raises:
        HTTPException: 이미 존재하는 이메일이 있는 경우

    Returns:
        dict: 회원가입 성공 메세지 반환
    """
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with email provided exists already"
        )
    await user_database.save(user)
    return{
        "message": "User created successfully."
    }


# 로그인
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    """로그인

    Args:
        user (UserSignIn): 로그인 하고자 하는 유저의 email, password

    Raises:
        HTTPException: 존재하지 않는 이메일일 때
        HTTPException: 비밀번호가 틀렸을 때


    Returns:
        dict: 로그인 성공 메시지 반환
    """
    user_exist = await User.find_one(User.email == user.email)
    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with email does not exist"
        )
    if user_exist.password == user.password:
        return{
            "message": "User signed in successfully."
        }
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid details passed"
    )
