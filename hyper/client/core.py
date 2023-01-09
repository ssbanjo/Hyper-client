from requests import Response
import requests
from ..exceptions import HyperAPIException


class Core:

    _base_url = "https://api.hyper.co/v6"

    def __init__(self, api_key: str) -> None:

        self._bearer = api_key

        self._headers = {
            "Authorization": "Bearer " + self._bearer,
            "accept": "application/json",
            "content-type": "application/json",
        }

    @staticmethod
    def _validate_response(res: Response):

        if res.status_code == 404:

            raise HyperAPIException("Not found")

        elif res.status_code not in (200, 202):

            error = res.json()["error"]["message"]

            raise HyperAPIException(error)

    def _call(self, method: str, path: str, params: dict = None, json: dict = None) -> Response:

        url = Core._base_url + path

        res = requests.request(method=method, url=url, headers=self._headers, params=params, json=json)

        self._validate_response(res)

        return res


    # ---- LICENSES CORE ------------------------------------------------------------------------------- #
    
    def _create_license_request(self, payload: dict) -> dict:

        path = "/licenses"

        return self._call(method="post", path=path, json=payload).json()

    def _retrieve_license_request(self, license_key: str) -> dict:

        path = "/licenses/" + license_key

        return self._call(method="get", path=path).json()
    
    def _update_license_request(self, license_key: str, payload: dict) -> dict:

        path = "/licenses/" + license_key

        return self._call(method="patch", path=path, json=payload).json()

    def _update_license_metadata_request(self, license_key: str, metadata: dict) -> dict:

        path = f"/licenses/{license_key}/metadata"

        return self._call(method="patch", path=path, json=metadata).json()

    def _delete_license_request(self, license_key: str) -> str:

        path = "/licenses/" + license_key

        return self._call(method="delete", path=path).text

    def _list_licenses_request(self, params: dict) -> dict:

        path = "/licenses"

        return self._call(method="get", path=path, params=params).json()

    # ---- PRODUCTS CORE ------------------------------------------------------------------------------- #
    
    def _create_product_request(self, payload: dict) -> dict:

        path = "/products"

        return self._call(method="post", path=path, json=payload).json()

    def _retrieve_product_request(self, product_id: str) -> dict:
        
        path = "/products/" + product_id
        
        return self._call("get", path=path).json()
    
    def _update_product_request(self, product_id: str, payload: dict) -> dict:
        
        path = "/products/" + product_id
        
        return self._call(method="patch", path=path, json=payload).json()
    
    def _list_products_request(self) -> dict:
        
        path = "/products"
        
        return self._call(method="get", path=path).json()

    # ---- LINKS CORE ---------------------------------------------------------------------------------- #
    
    def _create_link_request(self, payload: dict) -> dict:
        
        path = "/links"
        
        return self._call(method="post", path=path, json=payload).json()
    
    def _retrieve_link_request(self, link: str) -> dict:
        
        path = "/links/" + link
        
        return self._call(method="get", path=path).json() 
    
    def _update_link_request(self, link: str, payload: dict) -> dict:
        
        path = "/links/" + link
        
        return self._call(method="patch", path=path, json=payload).json()
    
    def _list_links_request(self) -> dict:
        
        path = "/links"
        
        return self._call(method="get", path=path).json()

    # ---- RAFFLES CORE -------------------------------------------------------------------------------- #
    
    def _create_raffle_request(self, payload: dict) -> dict:
        
        path = "/raffles"
        
        return self._call(method="post", path=path, json=payload).json()
    
    def _retrieve_raffle_request(self, raffle_id: str) -> dict:
        
        path = "/raffles/" + raffle_id
        
        return self._call(method="get", path=path).json()
    
    def _list_raffles_request(self, params: dict) -> dict:
        
        path = "/raffles"
        
        return self._call(method="get", path=path, params=params).json()

    # ---- WAITLIST CORE ------------------------------------------------------------------------------- #
    
    def _retrieve_waitlist_entry_request(self, entry_id: str) -> dict:
        
        path = "/waitlist/entries/" + entry_id
        
        return self._call(method="get", path=path).json()
    
    def _list_waitlist_entries_request(self) -> dict:
        
        path = "/waitlist/entries"
        
        return self._call(method="get", path=path).json()

    # ---- PAYMENTS CORE ------------------------------------------------------------------------------- #
    
    def _retrieve_payment_request(self, payment_id: str) -> dict:
        
        path = "/payments/" + payment_id
        
        return self._call(method="get", path=path).json()
    
    def _refund_payment_request(self, payment: str) -> dict:
        
        path = f"/payments/{payment}/refund"
        
        return self._call(method="post", path=path).text
    
    def _list_payments_request(self) -> dict:
        
        path = "/payments"
        
        return self._call(method="get", path=path).json()
    
    # ---- COUPONS CORE -------------------------------------------------------------------------------- #
    
    def _create_coupon_request(self, payload: dict) -> dict:
        
        path = "/coupons"
        
        return self._call(method="post", path=path, json=payload).json()
    
    def _retrieve_coupon_request(self, coupon_id: str) -> dict:
        
        path = "/coupons/" + coupon_id
        
        return self._call(method="get", path=path).json()
    
    def _list_coupons_request(self, params: dict) -> dict:
        
        path = "/coupons"
        
        return self._call(method="get", path=path, params=params).json()    