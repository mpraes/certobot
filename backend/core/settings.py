"""
Application settings and configuration management.
Handles environment variables and application configuration.
"""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )
    
    # Application Settings
    environment: Literal["development", "staging", "production"] = "development"
    debug: bool = True
    secret_key: str = Field(..., description="Secret key for JWT and encryption")
    
    # Database Configuration
    database_url: str = Field(..., description="PostgreSQL database URL")
    
    # Redis Configuration
    redis_url: str = Field(..., description="Redis connection URL")
    
    # WhatsApp Business API Configuration
    whatsapp_api_url: str = Field(
        default="https://graph.facebook.com/v18.0",
        description="WhatsApp Business API base URL"
    )
    whatsapp_access_token: str = Field(..., description="WhatsApp API access token")
    whatsapp_phone_number_id: str = Field(..., description="WhatsApp phone number ID")
    whatsapp_webhook_verify_token: str = Field(..., description="Webhook verification token")
    
    # Groq API Configuration
    groq_api_key: str = Field(..., description="Groq API key for AI processing")
    groq_model: str = Field(
        default="llama-3.1-70b-versatile",
        description="Groq model to use for conversations"
    )
    
    # Mock CRM Configuration
    mock_crm_url: str = Field(
        default="http://localhost:8001",
        description="Mock CRM API base URL"
    )
    mock_crm_api_key: str = Field(
        default="mock-api-key-for-testing",
        description="Mock CRM API key"
    )
    
    # Logging Configuration
    log_level: str = Field(default="INFO", description="Logging level")
    log_format: Literal["json", "text"] = Field(default="json", description="Log format")
    
    # Brazilian Localization
    default_language: str = Field(default="pt-BR", description="Default language")
    default_timezone: str = Field(default="America/Sao_Paulo", description="Default timezone")
    default_currency: str = Field(default="BRL", description="Default currency")
    
    # Security Settings
    jwt_secret_key: str = Field(..., description="JWT secret key")
    jwt_algorithm: str = Field(default="HS256", description="JWT algorithm")
    jwt_expire_minutes: int = Field(default=30, description="JWT expiration time in minutes")
    
    # Session Configuration
    session_timeout_minutes: int = Field(
        default=3,
        description="Maximum conversation session duration in minutes"
    )
    max_cpf_validation_attempts: int = Field(
        default=3,
        description="Maximum CPF validation attempts per session"
    )
    max_conversation_duration_minutes: int = Field(
        default=3,
        description="Maximum conversation duration in minutes"
    )
    
    # Payment Configuration
    boleto_expiration_days: int = Field(
        default=7,
        description="Boleto expiration time in days"
    )
    max_discount_percentage: float = Field(
        default=50.0,
        description="Maximum discount percentage allowed"
    )
    min_payment_amount: float = Field(
        default=10.00,
        description="Minimum payment amount in BRL"
    )
    
    @property
    def is_development(self) -> bool:
        """Check if running in development environment."""
        return self.environment == "development"
    
    @property
    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.environment == "production"


@lru_cache()
def get_settings() -> Settings:
    """Get cached application settings."""
    return Settings()


# Global settings instance
settings = get_settings()