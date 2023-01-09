from .utils.helpers import _clear_payload
from enum import StrEnum
from typing import NamedTuple


class CouponDuration(StrEnum):

    Forever = "forever"
    Once = "once"
    Repeating = "repeating"


class CreateCouponParams(NamedTuple):

    code: str
    product_id: str = None
    active: bool = None
    amount_off: int = None
    percent_off: int = None
    currency: str = None
    duration: CouponDuration = None
    max_redemptions: int = None

    def _build_payload(self) -> dict:

        payload = {
            "active": self.active,
            "duration": self.duration.value,
            "name": self.code,
            "product": self.product_id,
            "amount_off": self.amount_off,
            "percent_off": self.percent_off,
            "currency": self.currency,
            "max_redemptions": self.max_redemptions
        }

        return _clear_payload(payload=payload)
