from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # API
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Sistema de Gestão de Precatórios"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "API para gestão de Precatórios e transações"
    DATABASE_URL: str = "sqlite:///./warranty.db"
    SECRET_KEY: str = 'your-secret-key-here'
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:8080", "http://127.0.0.1:8080"
    ]
    ALLOWED_METHODS: list[str] = ["GET", "POST", "PUT", "DELETE"]
    ALLOWED_HEADERS: list[str] = [
        "Authorization",
        "Content-Type",
        "Accept",
        "Origin",
        "X-Requested-With",
    ]
    DEFAULT_PAGE_SIZE: int = 100
    MAX_PAGE_SIZE: int = 1000
    REDIS_URL: str | None = None
    CACHE_EXPIRE_MINUTES: int = 60
    LOG_LEVEL: str = "INFO"
    SWAGGER_UI_OAUTH2_REDIRECT_URL: str | None = None

    class Config:
        env_file = ".env"
        case_sensitive = True
        env_example = {
            "DATABASE_URL": "sqlite:///./warranty.db",
            "SECRET_KEY": "your-secret-key-here",
            "ALGORITHM": "HS256",
            "ACCESS_TOKEN_EXPIRE_MINUTES": "30",
        }

        @field_validator("SECRET_KEY")
        @classmethod
        def validate_secret_key(cls, v):
            if len(v.encode()) < 32:
                raise ValueError("SECRET_KEY deve ter pelo menos 32 bytes")
            return v


settings = Settings()