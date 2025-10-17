-- Initialize Certobot database
-- This script runs when PostgreSQL container starts for the first time

-- Create extensions if needed
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create basic tables structure (will be managed by Alembic migrations later)
-- This is just to ensure the database is properly initialized

-- Grant permissions
GRANT ALL PRIVILEGES ON DATABASE certobot TO certobot_user;