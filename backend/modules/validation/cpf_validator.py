"""
CPF validation utilities for Brazilian documents.
Uses validate-docbr library for accurate CPF validation.
"""

from typing import Optional

from validate_docbr import CPF

from backend.core.logging import LoggerMixin


class CPFValidator(LoggerMixin):
    """CPF validation service for Brazilian documents."""
    
    def __init__(self):
        self.cpf_validator = CPF()
    
    def validate(self, cpf: str) -> bool:
        """
        Validate a CPF number.
        
        Args:
            cpf: CPF string to validate (can include formatting)
            
        Returns:
            True if CPF is valid, False otherwise
        """
        if not cpf:
            return False
        
        try:
            # The validate_docbr library handles formatting automatically
            is_valid = self.cpf_validator.validate(cpf)
            
            self.log_debug(
                "CPF validation performed",
                cpf_masked=self._mask_cpf(cpf),
                is_valid=is_valid
            )
            
            return is_valid
            
        except Exception as e:
            self.log_error(
                "Error during CPF validation",
                cpf_masked=self._mask_cpf(cpf),
                error=str(e)
            )
            return False
    
    def format(self, cpf: str) -> Optional[str]:
        """
        Format a CPF number with standard Brazilian formatting.
        
        Args:
            cpf: CPF string to format
            
        Returns:
            Formatted CPF (XXX.XXX.XXX-XX) or None if invalid
        """
        if not self.validate(cpf):
            return None
        
        # Remove any existing formatting
        clean_cpf = self._clean_cpf(cpf)
        
        # Apply standard formatting
        if len(clean_cpf) == 11:
            return f"{clean_cpf[:3]}.{clean_cpf[3:6]}.{clean_cpf[6:9]}-{clean_cpf[9:]}"
        
        return None
    
    def _clean_cpf(self, cpf: str) -> str:
        """Remove all non-digit characters from CPF."""
        return ''.join(filter(str.isdigit, cpf))
    
    def _mask_cpf(self, cpf: str) -> str:
        """Mask CPF for logging (show only first 3 and last 2 digits)."""
        clean_cpf = self._clean_cpf(cpf)
        if len(clean_cpf) >= 5:
            return f"{clean_cpf[:3]}****{clean_cpf[-2:]}"
        return "***"


# Global validator instance
cpf_validator = CPFValidator()