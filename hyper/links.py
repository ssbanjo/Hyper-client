from .utils.helpers import _clear_payload
from datetime import datetime
from typing import NamedTuple

class CreateLinkParams(NamedTuple):

    product_id: str
    password: str = None
    trial_period_days: int = None
    group_buy_guild: str = None
    enable_bot_protection: bool = None
    max_usages: int = None
    start_date: datetime = None
    initial_fee_amount: float = None

    def _build_payload(self) -> dict:

        payload = {
            "plan": self.product_id,
            "password": self.password,
            "trial_period_days": self.trial_period_days,
            "group_buy_guild": self.group_buy_guild,
            "enable_bot_protection": self.enable_bot_protection,
            "max_usages": self.max_usages,
            "start_date": int(self.start_date.timestamp()),
            "initial_fee_amount": self.initial_fee_amount
        }
        
        return _clear_payload(payload=payload)

class UpdateLinkParams(NamedTuple):
    
    active: bool
    remaining_stock: int = None
    
    def _build_payload(self) -> dict:
        
        payload = {
            "active": self.active,
            "remaining_stock": self.remaining_stock
        }
        
        return _clear_payload(payload=payload)