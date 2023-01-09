from .utils.helpers import _clear_payload
from datetime import datetime
from typing import NamedTuple

class CreateRaffleParams(NamedTuple):

    product_id: str
    spots: int
    pick_winners_at: datetime
    active: bool = None
    trial_period_days: int = None
    initial_fee_amount: int = None
    grouop_buy_guild: str = None

    def _build_payload(self) -> dict:

        payload = {
            "active": self.active,
            "trial_period_days": self.trial_period_days,
            "plan": self.product_id,
            "spots": self.spots,
            "initial_fee_amount": self.initial_fee_amount,
            "pick_winners_at": self.pick_winners_at.isoformat(),
            "group_buy_guild": self.grouop_buy_guild
        }
        
        return _clear_payload(payload=payload)
