# Installation

```
pip install hyperco-client
```

# Introduction

With this client you can interact with the Hyper.co API withou needing to prepare the requests yourself.
It provides a clean and easy way to build client calls.

The client will raise an exception if the Hyper.co API returns an error response.

# Example

```python
from hyper.client import Client
from hyper.links import CreateLinkParams


api_key = "YOUR_HYPER_API_KEY"

client = Client(api_key=api_key)


# ---- Get all business licenses  ---------------------- #

licenses = client.list_licenses(page=2, limit=10)

print(licenses)

# ------------------------------------------------------ #


# ---- Create a new product link  ---------------------- #

params = CreateLinkParams(
    product_id="product_id",
    password="link_password",
    trial_period_days=7,
    group_buy_guild="0000000000000000",
    enable_bot_protection=True,
    max_usages=50,
    start_date=datetime.fromtimestamp(1683577538),
    initial_fee_amount=10
)

link = client.create_link(params=params)

print(link)

# ------------------------------------------------------ #


# ---- Authorize a license  ---------------------------- #

valid_license = client.authorize(license_key="license_key")

print(valid_license)

# ------------------------------------------------------ #
```