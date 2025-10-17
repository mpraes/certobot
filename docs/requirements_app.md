# Certobot: A project of conversational AI to help people negotiate and finish their financial debts.

Context: there was a client who requested a need to deal with the 'bottleneck' he has:
- Product for consulting to sell and apply to physical clients. Partners have a billing base with an low average ticket and too much individual clients to deal with.
- More effective for outstanding credit is a call (operator) contacting the person, trying to reach someone available for collection assistance. The examples of amount of people in debt is huge (25 thousand CPFs estimated).
- It depends on too many operators (thousands of CPFs per day for an operator to handle) to deal with.
- What does the consulting firm want to propose to deal with this bottleneck problem? Voice AI model (WhatsApp as an alternative). Preference for voice to achieve efficiency.
- There is information about the debtor (debtor's CPF, how much is owed, how many days overdue). Depending on the situation, there may be a discount.
- Parameters set for the agent's trading base, to act as if it were human. For verification.

## Questions about the project:
Q1: What is the sole goal of success (e.g., confirming the last 4 digits of the CPF, closing a payment proposal)?
R1: Successfully completing the negotiation could even include sending an automatic invoice. Transfer it to the CRM system where management is done.

Q2: Is the conversation guided (decision tree with few options) or open (the debtor can ask whatever they want)? (The 'open' is the higher risk and cost).
R2: It can be more open (as human as possible). Even to generate empathy. Example of unemployed person, empathy, and improving the conversation.

Q3: Does the agent need to access debtor data during the call (e.g., outstanding balance, installment offers) from a database or API? What is the maximum latency for this query?
R3: No, since the agent collect the data before the contact (cpf, name, phone number, total amount debt and due date)

Q4: What is the final action after the call (e.g., update the CRM, send an SMS/email with the invoice)?
R4: The aim would be to feed a specific CRM system with qualitative information about the outcome of the contact. If so, provide the payment slip.

Q5: What is the tone and personality of the voice (formal, friendly, neutral)? Will it be a standard Azure AI Speech voice or a custom neural voice?
R5: Very empathetic and informal, most of the clients are low-income.

Ps.: Collection advisory for mass credit. Audio is ideal, but the cost may make it unfeasible. There needs to be follow-up on this. The agent must contact directly by phone. WhatsApp can be an alternative, considering this aspect. Voice via WhatsApp. The CPF validator must be included (confirm the first three digits with me).

Client wants a Preliminary calculation for a 3-minute estimative conversation call. Create an infrastructure and architecture as well and allow them to have access. Support on Azure. They are used to it.

The Infrastructure and later support will be all on client administration. All in Azure.

From all the story above, I want to create an mvp version of it, first in integration with whatsapp. Also create an CRM simluation with mock data API to the main system access it before start to make contact