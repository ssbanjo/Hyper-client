from datetime import datetime
from typing import NamedTuple
from .utils.helpers import _clear_payload


class LicenseSubscription(NamedTuple):

    cancel_at_period_end: bool = None
    current_period_end: datetime = None
    pause_collection: bool = None


class CreateLicenseParams(NamedTuple):

    product_id: str
    email: str
    key: str = None
    metadata: dict = None

    def _build_payload(self) -> dict:

        payload = {
            "plan": self.product_id,
            "email": self.email,
            "key": self.key,
            "metadata": self.metadata
        }

        return _clear_payload(payload=payload)


class UpdateLicenseParams(NamedTuple):

    email: str = None
    key: str = None
    unlocked: bool = None
    metadata: dict = None
    subscription: LicenseSubscription = None

    def _build_payload(self) -> dict:

        payload = {
            "email": self.email,
            "key": self.key,
            "unlocked": self.unlocked,
            "subscription": {
                "cancel_at_period_end": self.subscription.cancel_at_period_end,
                "current_period_end": self.subscription.current_period_end.isoformat(),
                "pause_collection": self.subscription.pause_collection
            } if self.subscription else None
        }

        return _clear_payload(payload=payload)
