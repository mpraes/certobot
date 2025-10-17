"""
Logging configuration for Certobot.
Provides structured logging with Brazilian Portuguese support.
"""

import logging
import sys
from typing import Any, Dict

import structlog
from rich.console import Console
from rich.logging import RichHandler

from backend.core.settings import settings

# Configure console for rich output
console = Console()


def configure_logging():
    """Configure application logging."""
    
    # Configure structlog
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer() if settings.log_format == "json" else structlog.dev.ConsoleRenderer(),
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
    
    # Configure standard library logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, settings.log_level.upper()),
        handlers=[
            RichHandler(console=console, rich_tracebacks=True)
            if settings.is_development and settings.log_format != "json"
            else logging.StreamHandler(sys.stdout)
        ],
    )
    
    # Set specific logger levels
    logging.getLogger("uvicorn").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy.engine").setLevel(
        logging.INFO if settings.is_development else logging.WARNING
    )


def get_logger(name: str) -> structlog.stdlib.BoundLogger:
    """Get a structured logger instance."""
    return structlog.get_logger(name)


class LoggerMixin:
    """Mixin class to add logging capabilities to any class."""
    
    @property
    def logger(self) -> structlog.stdlib.BoundLogger:
        """Get logger for this class."""
        return get_logger(self.__class__.__name__)
    
    def log_info(self, message: str, **kwargs: Any):
        """Log info message with context."""
        self.logger.info(message, **kwargs)
    
    def log_error(self, message: str, **kwargs: Any):
        """Log error message with context."""
        self.logger.error(message, **kwargs)
    
    def log_warning(self, message: str, **kwargs: Any):
        """Log warning message with context."""
        self.logger.warning(message, **kwargs)
    
    def log_debug(self, message: str, **kwargs: Any):
        """Log debug message with context."""
        self.logger.debug(message, **kwargs)


# Portuguese language log messages
LOG_MESSAGES = {
    "conversation_started": "Conversa iniciada com devedor",
    "cpf_validation_requested": "Validação de CPF solicitada",
    "cpf_validation_failed": "Falha na validação do CPF",
    "cpf_validation_success": "CPF validado com sucesso",
    "negotiation_started": "Negociação iniciada",
    "negotiation_completed": "Negociação concluída",
    "payment_agreement_reached": "Acordo de pagamento estabelecido",
    "boleto_generated": "Boleto gerado com sucesso",
    "conversation_timeout": "Conversa expirou por timeout",
    "system_error": "Erro do sistema",
    "whatsapp_message_sent": "Mensagem WhatsApp enviada",
    "whatsapp_message_received": "Mensagem WhatsApp recebida",
    "crm_update_success": "CRM atualizado com sucesso",
    "crm_update_failed": "Falha ao atualizar CRM",
}


def log_conversation_event(
    event: str,
    session_id: str,
    debtor_cpf: str = None,
    **context: Any
) -> None:
    """Log conversation-related events with standard format."""
    logger = get_logger("conversation")
    
    log_data = {
        "event": event,
        "session_id": session_id,
        "language": settings.default_language,
        **context
    }
    
    if debtor_cpf:
        # Mask CPF for privacy (show only first 3 and last 2 digits)
        masked_cpf = f"{debtor_cpf[:3]}****{debtor_cpf[-2:]}" if len(debtor_cpf) >= 5 else "***"
        log_data["debtor_cpf"] = masked_cpf
    
    message = LOG_MESSAGES.get(event, event)
    logger.info(message, **log_data)