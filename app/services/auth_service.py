from app.security import issue_token

class AuthService:
    def login(self, email: str) -> dict[str, str]:
        return {"accessToken": issue_token(email)}
