"""
Mock CRM FastAPI application.
Provides REST API endpoints to simulate CRM functionality for Certobot testing.
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
    print(f"🏢 Starting Mock CRM API in {settings.environment} mode")
    print(f"📊 Database: {settings.database_url.split('@')[-1] if '@' in settings.database_url else 'Not configured'}")
    print(f"🌍 Language: {settings.default_language}")
    
    yield
    
    # Shutdown
    print("🛑 Shutting down Mock CRM API")


# Create FastAPI application
app = FastAPI(
    title="Mock CRM API",
    description="Mock CRM system for Certobot testing with realistic Brazilian debtor data",
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
        "message": "Mock CRM API - Sistema de CRM Simulado",
        "version": "0.1.0",
        "environment": settings.environment,
        "language": settings.default_language,
        "status": "running",
        "mock_debtors_available": 100
    }


@app.get("/health")
async def health_check():
    """Health check endpoint for Docker and monitoring."""
    return {
        "status": "healthy",
        "environment": settings.environment,
        "version": "0.1.0",
        "service": "mock-crm"
    }


# TODO: Add API routers for Mock CRM functionality
# from mock_crm.api.debtors import router as debtors_router
# from mock_crm.api.negotiations import router as negotiations_router
# from mock_crm.api.boletos import router as boletos_router

# app.include_router(debtors_router, prefix="/api/debtors", tags=["Debtors"])
# app.include_router(negotiations_router, prefix="/api/negotiations", tags=["Negotiations"])
# app.include_router(boletos_router, prefix="/api/boletos", tags=["Boletos"])


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "mock_crm.main:app",
        host="0.0.0.0",
        port=8001,
        reload=settings.is_development,
        log_level=settings.log_level.lower(),
    )