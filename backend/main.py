"""
Main FastAPI application for Certobot.
Conversational AI system for debt collection via WhatsApp in Brazilian Portuguese.
"""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.core.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan manager."""
    # Startup
    print(f"🚀 Starting Certobot API in {settings.environment} mode")
    print(f"📊 Database: {settings.database_url.split('@')[-1] if '@' in settings.database_url else 'Not configured'}")
    print(f"🔄 Redis: {settings.redis_url}")
    print(f"🌍 Language: {settings.default_language}")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down Certobot API")


# Create FastAPI application
app = FastAPI(
    title="Certobot API",
    description="Conversational AI system for debt collection via WhatsApp in Brazilian Portuguese",
    version="0.1.0",
    docs_url="/docs" if settings.is_development else None,
    redoc_url="/redoc" if settings.is_development else None,
    lifespan=lifespan,
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.is_development else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Certobot API - Sistema de Cobrança Conversacional",
        "version": "0.1.0",
        "environment": settings.environment,
        "language": settings.default_language,
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint for Docker and monitoring."""
    return {
        "status": "healthy",
        "environment": settings.environment,
        "version": "0.1.0"
    }


# TODO: Add API routers for different modules
# from backend.api.v1.whatsapp import router as whatsapp_router
# from backend.api.v1.negotiation import router as negotiation_router
# from backend.api.v1.validation import router as validation_router
# from backend.api.v1.payment import router as payment_router
# from backend.api.v1.crm import router as crm_router

# app.include_router(whatsapp_router, prefix="/api/v1/whatsapp", tags=["WhatsApp"])
# app.include_router(negotiation_router, prefix="/api/v1/negotiation", tags=["Negotiation"])
# app.include_router(validation_router, prefix="/api/v1/validation", tags=["Validation"])
# app.include_router(payment_router, prefix="/api/v1/payment", tags=["Payment"])
# app.include_router(crm_router, prefix="/api/v1/crm", tags=["CRM"])


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "backend.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.is_development,
        log_level=settings.log_level.lower(),
    )