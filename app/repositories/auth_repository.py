class AuthRepository:
    async def find_user_by_email(self, email: str) -> dict[str, str] | None:
        return {"email": email}
