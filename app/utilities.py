import os
import requests
from provider import get_db, get_cache, get_notification_service
from notification import Notification
from cache import Cache
from schemas import Product
from bs4 import BeautifulSoup

def download_image(url, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    image_name = os.path.join(folder, url.split("/")[-1])
    with open(image_name, 'wb') as file:
        response = requests.get(url)
        file.write(response.content)
    return image_name

def write_to_database(products, db = get_db()) -> None:
    db.save(products)

def notify_user(
        records_inserted: int, 
        records_updated: int, 
        records_skipped: int, 
        notification: Notification = get_notification_service()
        ) -> None:
    
    message = f"""
    No of Products inserted in the database: {records_inserted}, 
    No of Products updated in the database: {records_updated}, 
    No of Products skipped due to no change: {records_skipped}
    """
    notification.notify(message)
    
def reset_cache(cache: Cache = get_cache()) -> None:
    cache.set(Cache.RECORDS_INSERTED, int(0))
    cache.set(Cache.RECORDS_UPDATED, int(0))
    cache.set(Cache.RECORDS_SKIPPED, int(0))

def parse_web_page(soup: BeautifulSoup, cache: Cache = get_cache()) -> list[dict]:
    products = []
    for product in soup.find_all('div', class_='product-inner'): 
            product_name = product.find('h2', class_='woo-loop-product__title').get_text()
            product_price = product.find('span', class_='woocommerce-Price-amount amount').get_text()
            product_price = float(product_price.replace('₹', ''))
            
            if cache.get(product_name) is None:
                cache.set(product_name, product_price)
                cache.set(Cache.RECORDS_INSERTED, int(cache.get(Cache.RECORDS_INSERTED)) + 1)
                product_image = get_product_image(product)
                products.append(
                    Product(
                        name = product_name,
                        price = product_price,
                        image = product_image
                    ).model_dump()
                )
            else:
                if float(cache.get(product_name)) == product_price:
                    cache.set(Cache.RECORDS_SKIPPED, int(cache.get(Cache.RECORDS_SKIPPED)) + 1)   
                else:
                    cache.set(product_name, product_price)
                    cache.set(Cache.RECORDS_UPDATED, int(cache.get(Cache.RECORDS_UPDATED)) + 1)
                    product_image = get_product_image(product)
                    products.append(
                        Product(
                            name = product_name,
                            price = product_price,
                            image = product_image
                        ).model_dump()
                    )
    
    return products

def get_product_image(product: BeautifulSoup) -> str:
    product_image = product.find('img', class_='attachment-woocommerce_thumbnail size-woocommerce_thumbnail')['data-lazy-src'].replace('-300x300', '')
    return download_image(product_image, 'images')