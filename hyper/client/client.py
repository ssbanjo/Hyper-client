import re
import uuid
from ..coupons import CreateCouponParams
from ..links import CreateLinkParams, UpdateLinkParams
from ..products import CreateProductParams, UpdateProductParams
from ..raffles import CreateRaffleParams
from ..licenses import CreateLicenseParams, UpdateLicenseParams
from .core import Core


class Client(Core):

    def __init__(self, api_key: str) -> None:
        """
        Hyper.co dashboard client that interacts with the Hyper API.
        * https://docs.hyper.co/reference/getting-started

        Args:
            api_key: the business API key.
        """

        super().__init__(api_key)

    # ---- LICENSES CLIENT ------------------------------------------------------------------------------ #

    def create_license(self, params: CreateLicenseParams) -> dict:
        """
        Creates a license.
        * https://docs.hyper.co/reference/create-license

        Args:
            params: the create license params.

        Returns:
            The created license data.
        """
        payload = params._build_payload()

        return self._create_license_request(payload=payload)

    def retrieve_license(self, license_key: str) -> dict:
        """
        Retrieves a license data.
        * https://docs.hyper.co/reference/retrieve-license

        Args:
            license_key: the license key.

        Returns:
            The license data.
        """

        return self._retrieve_license_request(license_key=license_key)

    def update_license(self, license_key: str, params: UpdateLicenseParams) -> dict:
        """
        Updates a license data.
        * https://docs.hyper.co/reference/update-license

        Args:
            license_key: the license key.
            params: the update license params.

        Returns:
            The updated license.
        """

        payload = params._build_payload()

        return self._update_license_request(license_key=license_key, payload=payload)

    def update_license_metadata(self, license_key: str, metadata: dict) -> dict:
        """
        Updates a license metadata.
        * https://docs.hyper.co/reference/update-license-metadata

        Args:
            license_key: the license key.
            metadata: the new metadata.

        Returns:
            The updated license metadata.
        """

        return self._update_license_metadata_request(license_key=license_key, metadata=metadata)

    def delete_license(self, license_key: str) -> str:
        """
        Deletes a license.
        * https://docs.hyper.co/reference/delete-license

        Args:
            license_key: the license key.

        Returns:
            "Accepted" if the license was deleted successfuly.
        """

        return self._delete_license_request(license_key=license_key)

    def list_licenses(self, page: int = 1, limit: int = 20) -> dict:
        """
        Retrieves all the licenses.
        * https://docs.hyper.co/reference/list-licenses

        Args:
            page: the page number. Defaults to 1.
            limit: limit of licenses to retrieve. Defaults to 20.

        Returns:
            The licenses list and the pagination data.
        """

        params = {"page": page, "limit": limit}

        return self._list_licenses_request(params=params)

    # ---- PRODUCTS CLIENT ------------------------------------------------------------------------------ #

    def create_product(self, params: CreateProductParams) -> dict:
        """
        Creates a product.
        * https://docs.hyper.co/reference/create-product

        Args:
            params: the create product params.

        Returns:
            The created product data.
        """

        payload = params._build_payload()

        return self._create_product_request(payload=payload)

    def retreive_product(self, product_id: str) -> dict:
        """
        Retrieves a product data.
        * https://docs.hyper.co/reference/retrieve-product

        Args:
            product_id: the product id.

        Returns:
            The product data
        """

        return self._retrieve_product_request(product_id=product_id)

    def update_product(self, product_id: str, params: UpdateProductParams) -> dict:
        """
        Updates a product data.
        * https://docs.hyper.co/reference/update-product

        Args:
            product_id: the product id.
            params: the update product params.

        Returns:
            The updated product.
        """

        payload = params._build_payload()

        return self._update_product_request(product_id=product_id, payload=payload)

    def list_products(self) -> dict:
        """
        Retrieves all the products.
        * https://docs.hyper.co/reference/list-products

        Returns:
            The products list and the pagination data.
        """

        return self._list_products_request()

    # ---- LINKS CLIENT ------------------------------------------------------------------------------ #

    def create_link(self, params: CreateLinkParams) -> dict:
        """
        Creates a link for a product.
        * https://docs.hyper.co/reference/create-link

        Args:
            params: the create link params.

        Returns:
            The created link data.
        """

        payload = params._build_payload()

        return self._create_link_request(payload=payload)

    def retrieve_link(self, link: str) -> dict:
        """
        Retrieves a link data.
        * https://docs.hyper.co/reference/retrieve-link

        Args:
            link: the link.

        Returns:
            The link data.
        """

        return self._retrieve_link_request(link=link)

    def update_link(self, link: str, params: UpdateLinkParams) -> dict:
        """
        Updates a link data.
        * https://docs.hyper.co/reference/update-link

        Args:
            link: the link.
            params: the update link params.

        Returns:
            The updated link.
        """

        payload = params._build_payload()

        return self._update_link_request(link=link, payload=payload)

    def list_links(self) -> dict:
        """
        Retrieves all the links.
        * https://docs.hyper.co/reference/list-links

        Returns:
            The links list and the pagination data.
        """

        return self._list_links_request()

    # ---- RAFFLES CLIENT ------------------------------------------------------------------------------ #

    def create_raffle(self, params: CreateRaffleParams) -> dict:
        """
        Creates a raffle.
        * https://docs.hyper.co/reference/create-a-raffle

        Args:
            params: the create raffle params.

        Returns:
            The created raffle data.
        """

        payload = params._build_payload()

        return self._create_raffle_request(payload=payload)

    def retrieve_raffle(self, raffle_id: str) -> dict:
        """
        Retrieves a raffle data.
        * https://docs.hyper.co/reference/retrieve-raffle

        Args:
            raffle_id: the raffle id.

        Returns:
            The raffle data.
        """

        return self._retrieve_raffle_request(raffle_id=raffle_id)

    def list_raffles(self, active: bool = True) -> dict:
        """
        Retrieves all the raffles.
        * https://docs.hyper.co/reference/list-raffles

        Returns:
            The raffles list and the pagination data.
        """

        params = {"active": "true" if active else "false"}

        return self._list_raffles_request(params=params)

    # ---- WAITLIST CLIENT ------------------------------------------------------------------------------ #

    def retrieve_waitlist_entry(self, entry_id: str) -> dict:
        """
        Retrieves a waitlist entry data.
        * https://docs.hyper.co/reference/retrieve-waitlist-entry

        Args:
            entry_id: the waitlist entry id.

        Returns:
            The waitlist entry data.
        """

        return self._retrieve_waitlist_entry_request(entry_id=entry_id)

    def list_waitlist_entries(self) -> dict:
        """
        Retrieves all the waitlist entries.
        * https://docs.hyper.co/reference/list-waitlist-entries

        Returns:
            The waitlist entries list and the pagination data.
        """

        return self._list_waitlist_entries_request()

    # ---- PAYMENTS CLIENT ------------------------------------------------------------------------------ #

    def retrieve_payment(self, payment_id: str) -> dict:
        """
        Retrieves a payment data.
        * https://docs.hyper.co/reference/retrieve-payment

        Args:
            payment_id: the payment id.

        Returns:
            The payment data.
        """

        return self._retrieve_payment_request(payment_id=payment_id)

    def refund_payment(self, payment: str) -> dict:
        """
        Refunds a payment.
        * https://docs.hyper.co/reference/refund-payment

        Args:
            payment: the payment id.

        Returns:
            "Accepted" if the payment was refunded successfuly.
        """

        return self._refund_payment_request(payment=payment)

    def list_payments(self) -> dict:
        """
        Retrieves all the payments.
        * https://docs.hyper.co/reference/list-payments

        Returns:
            The payments list and the pagination data.
        """

        return self._list_payments_request()

    # ---- COUPONS CLIENT ------------------------------------------------------------------------------ #

    def create_coupon(self, params: CreateCouponParams) -> dict:
        """
        Creates a coupon.
        * https://docs.hyper.co/reference/create-coupon

        Args:
            params: the create coupon params.

        Returns:
            The created coupon data.
        """

        payload = params._build_payload()

        return self._create_coupon_request(payload=payload)

    def retrieve_coupon(self, coupon_id: str) -> dict:
        """
        Retrieves a coupon data.
        * https://docs.hyper.co/reference/retrieve-coupon

        Args:
            coupon_id: the coupon id.

        Returns:
            The coupon data.
        """

        return self._retrieve_coupon_request(coupon_id=coupon_id)

    def list_coupons(self, active: bool = True) -> dict:
        """
        Retrieves all the coupons.
        * https://docs.hyper.co/reference/list-coupons

        Args:
            active: weather or not the retrieved coupons have to be active.

        Returns:
            The coupons list and the pagination data.
        """

        params = {"active": "true" if active else "false"}

        return self._list_coupons_request(params=params)

    # ---- AUTH CLIENT ----------------------------------------------------------------------------------- #

    def authorize(self, license_key: str) -> bool:
        """
        Authorizes a license using basic hardware id auth.
        * https://docs.hyper.co/recipes/python-cli-auth

        Args:
            license_key: the license key to auth.

        Returns:
            A boolean to indicate weather or not the license was authorized successfuly.
        """        
        
        license = self.retrieve_license(license_key=license_key)

        hardware_id = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

        if not license["metadata"]:
            
            params = UpdateLicenseParams(
                metadata={
                    "metadata": {
                        "hwid": hardware_id
                    }
                }
            )
            
            self.update_license(license_key=license_key, params=params)
            
            return True
        
        else:
            
            current_hwid = license["metadata"].get('hwid')
            
            if current_hwid == hardware_id:
                
                return True
            
            return False