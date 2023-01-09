from enum import StrEnum
import json
from typing import NamedTuple
from .utils.helpers import _clear_payload


class ProductType(StrEnum):

    Lifetime = "lifetime"
    Recurring = "recurring"
    Free = "free"
    Rental = "rental"


class RecurringInterval(StrEnum):

    Day = "day"
    Week = "week"
    Month = "month"
    Year = "year"


class DiscordCancelAction(StrEnum):

    Kick = "kick"
    RemovePlanRoles = "remove_plan_roles"
    RemoveAllRoles = "remove_all_roles"
    Nothing = "none"


class TelegramCancelAction(StrEnum):

    Kick = "kick"
    Nothing = "none"


class ProductLink(NamedTuple):

    title: str
    href: str


class ProductRecurring(NamedTuple):

    interval: RecurringInterval
    interval_count: int


class ProductTransfers(NamedTuple):

    enabled: bool
    cooldown_days: int


class IntegrationDiscord(NamedTuple):

    guild: str
    roles: list[str]
    cancel_action: DiscordCancelAction


class IntegrationTelegram(NamedTuple):

    chat: str
    cancel_action: TelegramCancelAction


class ProductIntegrations(NamedTuple):

    discord: IntegrationDiscord = None
    telegram: IntegrationTelegram = None


class CreateProductParams(NamedTuple):

    name: str
    type: ProductType
    amount: float
    currency: str
    image: str = None
    description: str = None
    rental_period_days: int = None
    links: list[ProductLink] = None
    recurring: ProductRecurring = None
    transfers: ProductTransfers = None
    integrations: ProductIntegrations = None

    def _build_payload(self) -> dict:

        payload = {
            "links": [{"title": l.title, "href": l.href} for l in self.links] if self.links else None,
            "recurring": {
                "interval": json.dumps(self.recurring.interval),
                "interval_count": self.recurring.interval_count
            } if self.recurring else None,
            "transfers": {
                "enabled": self.transfers.enabled,
                "cooldown_days": self.transfers.cooldown_days
            } if self.transfers else None,
            "integrations": {
                "discord": {
                    "roles": self.integrations.discord.roles,
                    "cancel_action": json.dumps(self.integrations.discord.cancel_action),
                    "guild": self.integrations.discord.guild
                } if self.integrations.discord else None,
                "telegram": {
                    "cancel_action": json.dumps(self.integrations.telegram.cancel_action),
                    "chat": self.integrations.telegram.chat
                } if self.integrations.telegram else None
            } if self.integrations else None,
            "name": self.name,
            "type": json.dumps(self.type),
            "amount": self.amount,
            "currency": self.currency,
            "image": self.image,
            "description": self.description,
            "rental_period_days": self.rental_period_days
        }

        return _clear_payload(payload=payload)


class UpdateProductParams(NamedTuple):

    product_id: str
    image: str = None
    description: str = None
    rental_period_days: int = None
    links: list[ProductLink] = None
    transfers: ProductTransfers = None
    integrations: ProductIntegrations = None

    def _build_payload(self) -> dict:

        payload = {
            "name": self.product_id,
            "image": self.image,
            "description": self.description,
            "rental_period_days": self.rental_period_days,
            "links": [{"title": l.title, "href": l.href} for l in self.links] if self.links else None,
            "transfers": {
                "enabled": self.transfers.enabled,
                "cooldown_days": self.transfers.cooldown_days
            } if self.transfers else None,
            "integrations": {
                "discord": {
                    "roles": self.integrations.discord.roles,
                    "cancel_action": json.dumps(self.integrations.discord.cancel_action),
                    "guild": self.integrations.discord.guild
                } if self.integrations.discord else None,
                "telegram": {
                    "cancel_action": json.dumps(self.integrations.telegram.cancel_action),
                } if self.integrations.telegram else None
            } if self.integrations else None,
        }
        
        return _clear_payload(payload=payload)
