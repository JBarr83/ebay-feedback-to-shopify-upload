# sunshine-hut-admin

## Installation
Using pip run the following command 
```bash
pip install -r requirements.txt
```

## Summary
A simple Python app to retrieve eBay feedback and join to a Shopify store's products using the product titles (product IDs  don't match.)

This project uses the [Ebaysdk](https://github.com/timotheus/ebaysdk-python#welcome-to-the-python-ebaysdk) and the [Shopify API](https://github.com/Shopify/shopify_python_api#shopify-api)

To run this you will need to join both eBay and Shopify developers portals and generate credentials to populate a `/resources/credentials.yml` file like the following:

```yml
sunshine_hut:
  shopify:
    shop_url: https://111-1.myshopify.com
    admin_token:
  ebay:
    app_id:
    dev_id:
    cert_id:
    user_id: ebay-user-to-get-feedback-for
    token:
```
