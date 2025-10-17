# Certobot Development Makefile
# Provides convenient commands for development, testing, and deployment

.PHONY: help install dev test clean docker-build docker-up docker-down docker-logs format lint type-check

# Default target
help:
	@echo "Certobot Development Commands"
	@echo "============================"
	@echo ""
	@echo "Setup Commands:"
	@echo "  install     Install dependencies and setup development environment"
	@echo "  dev         Start development environment with hot reload"
	@echo ""
	@echo "Docker Commands:"
	@echo "  docker-build    Build Docker images"
	@echo "  docker-up       Start all services with Docker Compose"
	@echo "  docker-down     Stop all Docker services"
	@echo "  docker-logs     Show Docker logs"
	@echo "  docker-clean    Clean Docker containers and volumes"
	@echo ""
	@echo "Development Commands:"
	@echo "  format      Format code with black and isort"
	@echo "  lint        Run linting with flake8"
	@echo "  type-check  Run type checking with mypy"
	@echo "  test        Run tests with pytest"
	@echo "  test-cov    Run tests with coverage report"
	@echo ""
	@echo "Database Commands:"
	@echo "  db-migrate  Create new database migration"
	@echo "  db-upgrade  Apply database migrations"
	@echo "  db-reset    Reset database (development only)"
	@echo ""
	@echo "Utility Commands:"
	@echo "  clean       Clean temporary files and caches"
	@echo "  shell       Start Python shell with app context"

# Setup Commands
install:
	@echo "📦 Installing dependencies..."
	pip install -e ".[dev]"
	@echo "✅ Dependencies installed"

dev:
	@echo "🚀 Starting development server..."
	uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload

# Docker Commands
docker-build:
	@echo "🐳 Building Docker images..."
	docker-compose build

docker-up:
	@echo "🐳 Starting Docker services..."
	docker-compose up -d
	@echo "✅ Services started:"
	@echo "  - Certobot API: http://localhost:8000"
	@echo "  - Mock CRM API: http://localhost:8001"
	@echo "  - PostgreSQL: localhost:5432"
	@echo "  - Redis: localhost:6379"

docker-down:
	@echo "🐳 Stopping Docker services..."
	docker-compose down

docker-logs:
	@echo "📋 Showing Docker logs..."
	docker-compose logs -f

docker-clean:
	@echo "🧹 Cleaning Docker containers and volumes..."
	docker-compose down -v --remove-orphans
	docker system prune -f

# Development Commands
format:
	@echo "🎨 Formatting code..."
	black backend/ mock_crm/
	isort backend/ mock_crm/
	@echo "✅ Code formatted"

lint:
	@echo "🔍 Running linter..."
	flake8 backend/ mock_crm/
	@echo "✅ Linting complete"

type-check:
	@echo "🔍 Running type checker..."
	mypy backend/ mock_crm/
	@echo "✅ Type checking complete"

test:
	@echo "🧪 Running tests..."
	pytest backend/tests/ -v

test-cov:
	@echo "🧪 Running tests with coverage..."
	pytest backend/tests/ --cov=backend --cov-report=html --cov-report=term-missing
	@echo "📊 Coverage report generated in htmlcov/"

# Database Commands
db-migrate:
	@echo "📊 Creating database migration..."
	alembic revision --autogenerate -m "$(msg)"

db-upgrade:
	@echo "📊 Applying database migrations..."
	alembic upgrade head

db-reset:
	@echo "⚠️  Resetting database (development only)..."
	@read -p "Are you sure? This will delete all data [y/N]: " confirm && [ "$$confirm" = "y" ]
	docker-compose exec postgres psql -U certobot_user -d certobot -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"
	alembic upgrade head

# Utility Commands
clean:
	@echo "🧹 Cleaning temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	@echo "✅ Cleanup complete"

shell:
	@echo "🐍 Starting Python shell..."
	python -c "from backend.main import app; from backend.core.settings import settings; print('Certobot shell ready. Available: app, settings')"

# Development workflow
dev-setup: install docker-up
	@echo "🎉 Development environment ready!"
	@echo "  - API Documentation: http://localhost:8000/docs"
	@echo "  - Mock CRM Documentation: http://localhost:8001/docs"

# Quality checks
check: format lint type-check test
	@echo "✅ All quality checks passed!"

# Production build
build: clean format lint type-check test docker-build
	@echo "🚀 Production build complete!"