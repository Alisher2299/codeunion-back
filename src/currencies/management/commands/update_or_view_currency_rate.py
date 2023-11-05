from django.core.management.base import BaseCommand
from currencies.models import Currency


class Command(BaseCommand):
    help = 'Update or view currency rates'

    def add_arguments(self, parser):
        parser.add_argument('--update', action='store_true', help='Update currency rates')
        parser.add_argument('--view', action='store_true', help='View currency rates')
        parser.add_argument('--currency_id', type=int, help='Currency ID')
        parser.add_argument('--value', type=float, help='Currency value')

    def handle(self, *args, **options):
        if options['update']:
            self.update_currency_rate(options['currency_id'], options['value'])
        elif options['view']:
            self.view_currency_rates()
        else:
            self.stdout.write(self.style.WARNING('Please specify --update or --view'))

    def update_currency_rate(self, currency_id, value):
        try:
            currency = Currency.objects.get(pk=currency_id)
        except Currency.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Currency with ID {currency_id} does not exist'))
            return

        currency.rate = value
        currency.save()
        self.stdout.write(self.style.SUCCESS(f'Currency {currency.name} updated with rate {value}'))

    def view_currency_rates(self):
        currencies = Currency.objects.all()
        for currency in currencies:
            self.stdout.write(f'ID: {currency.id}, Name: {currency.name}, Rate: {currency.rate}')
