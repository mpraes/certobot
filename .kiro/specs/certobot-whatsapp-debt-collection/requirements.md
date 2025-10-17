# Requirements Document

## Introduction

Certobot is a conversational AI system designed to help financial consulting firms automate debt collection and negotiation processes. The system addresses the bottleneck of managing thousands of individual debtors by providing an empathetic, human-like AI agent that can conduct negotiations via WhatsApp, validate debtor information, and integrate with CRM systems for outcome tracking.

## Glossary

- **Certobot_System**: The complete conversational AI platform for debt collection
- **WhatsApp_Integration**: The messaging interface component that handles WhatsApp communication
- **CRM_Connector**: The component that interfaces with customer relationship management systems
- **Debtor_Validator**: The component that validates debtor identity using CPF information
- **Negotiation_Engine**: The AI component that conducts debt negotiation conversations in Portuguese
- **Payment_Processor**: The component that generates and sends payment slips/invoices in Portuguese
- **CPF**: Brazilian individual taxpayer registry identification number
- **Mock_CRM_API**: Simulated CRM system for MVP testing and development
- **Portuguese_Language_Support**: All system interactions must be conducted in Brazilian Portuguese

## Requirements

### Requirement 1

**User Story:** As a debt collection operator, I want the AI system to automatically contact debtors via WhatsApp, so that I can handle more cases without manual intervention.

#### Acceptance Criteria

1. WHEN a debtor contact is initiated, THE Certobot_System SHALL send a WhatsApp message to the debtor's registered phone number
2. THE WhatsApp_Integration SHALL maintain conversation context throughout the entire negotiation session
3. WHILE a conversation is active, THE Certobot_System SHALL respond to debtor messages within 5 seconds
4. THE Negotiation_Engine SHALL use an empathetic and informal tone in Brazilian Portuguese appropriate for low-income clients
5. WHERE multiple conversations occur simultaneously, THE Certobot_System SHALL handle each conversation independently

### Requirement 2

**User Story:** As a debt collection manager, I want the system to validate debtor identity before proceeding with negotiations, so that we ensure we're speaking with the correct person.

#### Acceptance Criteria

1. WHEN a conversation begins, THE Debtor_Validator SHALL request the first three digits of the debtor's CPF
2. THE Debtor_Validator SHALL compare provided digits against the stored CPF information
3. IF the CPF validation fails, THEN THE Certobot_System SHALL terminate the conversation and log the failed attempt
4. THE Certobot_System SHALL allow a maximum of 3 CPF validation attempts per conversation session
5. WHEN CPF validation succeeds, THE Certobot_System SHALL proceed to debt negotiation phase

### Requirement 3

**User Story:** As a debtor, I want to have natural conversations about my debt situation, so that I can negotiate payment terms that work for my financial situation.

#### Acceptance Criteria

1. THE Negotiation_Engine SHALL conduct open-ended conversations in Brazilian Portuguese without restricting debtor responses to predefined options
2. WHEN a debtor mentions financial hardship, THE Negotiation_Engine SHALL respond with empathy and explore flexible payment options
3. THE Certobot_System SHALL access debtor information including CPF, name, phone number, total debt amount, and due date before initiating contact
4. WHILE negotiating, THE Negotiation_Engine SHALL offer appropriate discounts based on predefined parameters
5. THE Negotiation_Engine SHALL maintain conversation flow for up to 3 minutes per session

### Requirement 4

**User Story:** As a debt collection manager, I want successful negotiations to automatically generate payment documentation, so that debtors can immediately proceed with payment.

#### Acceptance Criteria

1. WHEN a payment agreement is reached, THE Payment_Processor SHALL generate an automatic invoice or payment slip
2. THE Payment_Processor SHALL send the payment documentation in Portuguese via WhatsApp to the debtor
3. THE Certobot_System SHALL capture payment terms including amount, due date, and any applied discounts
4. THE Payment_Processor SHALL include clear payment instructions and deadlines in Portuguese in all generated documents

### Requirement 5

**User Story:** As a debt collection manager, I want all conversation outcomes recorded in our CRM system, so that I can track negotiation results and follow up appropriately.

#### Acceptance Criteria

1. WHEN a conversation concludes, THE CRM_Connector SHALL update the CRM system with qualitative information about the contact outcome
2. THE CRM_Connector SHALL record whether the negotiation was successful, partially successful, or unsuccessful
3. THE CRM_Connector SHALL capture any payment agreements, discount amounts, and scheduled payment dates
4. WHERE payment documentation was generated, THE CRM_Connector SHALL link the payment slip reference to the debtor record
5. THE CRM_Connector SHALL timestamp all interactions for audit and follow-up purposes

### Requirement 6

**User Story:** As a Brazilian debt collection firm, I want all system interactions to be conducted in Portuguese, so that debtors can communicate naturally in their native language.

#### Acceptance Criteria

1. THE Certobot_System SHALL conduct all conversations exclusively in Brazilian Portuguese
2. THE Negotiation_Engine SHALL understand and respond to Brazilian Portuguese colloquialisms and informal expressions
3. THE Payment_Processor SHALL generate all payment documentation with Portuguese text and Brazilian currency formatting
4. THE Debtor_Validator SHALL provide CPF validation prompts and error messages in Portuguese
5. THE CRM_Connector SHALL store conversation logs and outcomes with Portuguese language metadata

### Requirement 7

**User Story:** As a system administrator, I want a mock CRM API for MVP testing, so that we can validate system functionality before integrating with the production CRM.

#### Acceptance Criteria

1. THE Mock_CRM_API SHALL simulate debtor data retrieval with realistic CPF, name, phone, debt amount, and due date information
2. THE Mock_CRM_API SHALL accept and store conversation outcome updates from the Certobot_System
3. THE Mock_CRM_API SHALL provide endpoints for creating, reading, updating debtor records
4. THE Mock_CRM_API SHALL return appropriate HTTP status codes and error messages for different scenarios
5. THE Mock_CRM_API SHALL support at least 100 mock debtor records for comprehensive testing