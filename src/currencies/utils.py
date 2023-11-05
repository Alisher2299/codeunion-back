import requests
from lxml import etree
from django.conf import settings

from currencies.models import Currency

URL = settings.CURRENCY_URL


def update_currency_rates():
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching XML data: {e}")
        return

    xml_data = response.content

    try:
        root = etree.fromstring(xml_data)
    except etree.XMLSyntaxError as e:
        print(f"Error parsing XML data: {e}")
        return

    for item in root.findall(".//item"):
        currency_code = item.find("title").text
        rate = float(item.find("description").text)
        try:
            currency = Currency.objects.get(name=currency_code)
            currency.rate = rate
            currency.save()
        except Currency.DoesNotExist:
            print(f"Currency {currency_code} not found in the database.")
            Currency.objects.create(name=currency_code, rate=rate)

    print("Currency rates updated successfully.")
