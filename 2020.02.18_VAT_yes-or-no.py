# VAT in the EUROPEAN UNION. One country must be from the EU for this program to have proper functionality.
# More complex functions can be added, like invoicing of goods, where the invoice from and ship from countries differ.

country_list_eu = [
    'bulgaria',
    'croatia',
    'cyprus',
    'czech republic',
    'denmark',
    'estonia',
    'finland',
    'france',
    'germany',
    'greece',
    'hungary',
    'ireland',
    'italy',
    'latvia',
    'lithuania',
    'luxembourg',
    'malta',
    'netherlands',
    'poland',
    'portugal',
    'romania',
    'slovakia',
    'slovenia',
    'spain',
    'sweden',

]

invoicing_from = input('Where are you invoicing from? Enter EU Country: ').lower()
invoicing_to = input('Where are you invoicing to?(customer). Enter Country: ').lower()
eu_validvatnr = ''

if invoicing_from in country_list_eu and invoicing_to not in country_list_eu:
    print('No VAT applies, keep export declaration.')

if invoicing_from == invoicing_to:
    print(invoicing_from.upper() + ' VAT applies.')

if invoicing_from in country_list_eu and invoicing_to in country_list_eu:
    eu_validvatnr = input('Does the customer have a valid EU VAT number?(enter yes or no): ').lower()
    if eu_validvatnr == 'yes':
        print('No VAT applies.')
    else:
        print(invoicing_from.upper() + ' VAT applies.')

if invoicing_from and invoicing_to not in country_list_eu:
    print('This program requires for at least one item to be an EU Country.')
