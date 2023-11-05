import pytest

from currencies.models import Currency


@pytest.mark.django_db
def test_create_currency():
    currency = Currency.objects.create(name='USD', rate=470.00)
    get_currency = Currency.objects.get(pk=currency.pk)

    assert get_currency.name == 'USD'
    assert get_currency.rate == 470.00
