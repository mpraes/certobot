# Implementation Plan

- [x] 1. Set up project structure and core dependencies






  - Create Docker Compose configuration for PostgreSQL and Redis
  - Set up Python project with FastAPI, PydanticAI, and required dependencies
  - Configure environment variables and settings management
  - Create basic project structure with modules for WhatsApp, negotiation, validation, payment, and CRM integration
  - _Requirements: 6.1, 6.2, 6.3, 6.4, 6.5_

- [ ] 2. Implement database models and core data structures
  - [ ] 2.1 Create PostgreSQL database schema and models
    - Design and implement Debtor, Debt, Conversation, Message, and Outcome models using SQLAlchemy
    - Set up database migrations with Alembic
    - Create database connection and session management
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5_
  
  - [ ] 2.2 Implement Pydantic models for API contracts
    - Create Pydantic models for all data structures (DebtorInfo, ConversationOutcome, PaymentAgreement, etc.)
    - Implement validation rules for CPF format and Brazilian data standards
    - Add Portuguese language support for validation error messages
    - _Requirements: 2.1, 2.2, 6.1, 6.2, 6.3_

- [ ] 3. Build Mock CRM API system
  - [ ] 3.1 Create Mock CRM FastAPI application
    - Set up separate FastAPI application for Mock CRM
    - Implement debtor data management endpoints (GET, POST /api/debtors)
    - Create mock debtor database with realistic Brazilian test data
    - _Requirements: 7.1, 7.2, 7.3, 7.4, 7.5_
  
  - [ ] 3.2 Implement negotiation results API
    - Create endpoint to receive negotiation outcomes from Certobot
    - Store conversation results and outcomes in database
    - Implement result retrieval endpoints for monitoring
    - _Requirements: 5.1, 5.2, 5.3, 5.5_
  
  - [ ] 3.3 Build boleto generation system
    - Implement boleto generation endpoint with Brazilian payment standards
    - Create boleto PDF generation with proper formatting and Portuguese text
    - Set up automatic WhatsApp delivery of boletos to debtors
    - Store boleto metadata and payment tracking information
    - _Requirements: 4.1, 4.2, 4.3, 4.4_

- [ ] 4. Implement WhatsApp Business API integration
  - [ ] 4.1 Set up WhatsApp webhook handling
    - Create FastAPI endpoints to receive WhatsApp webhooks
    - Implement message parsing and validation
    - Set up webhook verification for WhatsApp Business API
    - _Requirements: 1.1, 1.2_
  
  - [ ] 4.2 Build WhatsApp message sending functionality
    - Implement WhatsApp Business API client for sending messages
    - Create message formatting for Portuguese language
    - Add support for sending documents (boletos) via WhatsApp
    - Implement message delivery status tracking
    - _Requirements: 1.1, 1.3, 4.2_
  
  - [ ] 4.3 Implement conversation session management
    - Create Redis-based session storage for active conversations
    - Implement session lifecycle management (start, active, completed, failed)
    - Add conversation timeout and cleanup mechanisms
    - _Requirements: 1.2, 1.5_

- [ ] 5. Build CPF validation and identity verification
  - [ ] 5.1 Implement CPF validation logic
    - Create CPF format validation and digit verification algorithms
    - Implement challenge-response system for identity confirmation
    - Add support for Portuguese language prompts and error messages
    - _Requirements: 2.1, 2.2, 6.4_
  
  - [ ] 5.2 Build validation attempt management
    - Implement maximum attempt limits (3 attempts per session)
    - Create validation failure handling and conversation termination
    - Add audit logging for validation attempts and outcomes
    - _Requirements: 2.3, 2.4, 2.5_

- [ ] 6. Create PydanticAI negotiation agents
  - [ ] 6.1 Set up Groq API integration
    - Configure Groq API client with proper authentication
    - Set up model selection and configuration for Portuguese conversations
    - Implement API error handling and fallback mechanisms
    - _Requirements: 3.1, 3.5, 6.1, 6.2_
  
  - [ ] 6.2 Build negotiation agent with PydanticAI
    - Create PydanticAI agent for debt negotiation conversations
    - Implement custom prompts for empathetic, informal Brazilian Portuguese tone
    - Add structured output validation for negotiation responses
    - Configure agent with negotiation parameters (discounts, installments, etc.)
    - _Requirements: 3.1, 3.2, 3.4, 6.1, 6.2, 6.3_
  
  - [ ] 6.3 Implement conversation flow management
    - Create conversation state machine (validation → negotiation → agreement → completion)
    - Implement context management and conversation history tracking
    - Add empathy detection and appropriate response generation
    - Handle conversation timeouts and session management
    - _Requirements: 3.1, 3.2, 3.3, 3.5_

- [ ] 7. Build CRM integration module
  - [ ] 7.1 Create CRM API client
    - Implement HTTP client for communicating with Mock CRM API
    - Add authentication, rate limiting, and error handling
    - Create retry logic and circuit breaker patterns for reliability
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_
  
  - [ ] 7.2 Implement debtor data retrieval
    - Create functions to fetch debtor information from CRM API
    - Add caching layer using Redis for frequently accessed debtor data
    - Implement error handling for missing or invalid debtor records
    - _Requirements: 3.3, 5.1_
  
  - [ ] 7.3 Build outcome reporting system
    - Create functions to send negotiation results to CRM API
    - Implement structured outcome data formatting
    - Add automatic boleto generation triggering for successful negotiations
    - _Requirements: 5.1, 5.2, 5.3, 5.4, 5.5_

- [ ] 8. Integrate all components and implement main conversation flow
  - [ ] 8.1 Build main conversation orchestrator
    - Create main conversation handler that coordinates all modules
    - Implement complete flow: WhatsApp message → CPF validation → negotiation → outcome → CRM update
    - Add proper error handling and graceful degradation throughout the flow
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 2.1, 2.2, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 3.4, 3.5_
  
  - [ ] 8.2 Implement conversation monitoring and logging
    - Add comprehensive logging for all conversation steps and outcomes
    - Create monitoring endpoints for system health and conversation metrics
    - Implement conversation analytics and reporting features
    - _Requirements: 5.5_
  
  - [ ] 8.3 Add Docker deployment configuration
    - Create production-ready Docker Compose configuration
    - Set up proper environment variable management
    - Configure health checks and service dependencies
    - Add database initialization and migration scripts
    - _Requirements: 6.5_

- [ ] 9. Testing and validation
  - [ ] 9.1 Create unit tests for core functionality
    - Write unit tests for CPF validation, negotiation logic, and API clients
    - Test PydanticAI agent responses and conversation flow
    - Validate Portuguese language processing and response generation
    - _Requirements: All requirements_
  
  - [ ] 9.2 Build integration tests
    - Create end-to-end tests for complete conversation flows
    - Test WhatsApp webhook integration and message sending
    - Validate CRM API integration and data synchronization
    - _Requirements: All requirements_
  
  - [ ] 9.3 Set up load testing and performance validation
    - Create load tests for concurrent conversation handling
    - Validate system performance under realistic usage scenarios
    - Test database and Redis performance with multiple sessions
    - _Requirements: 1.3, 1.5_