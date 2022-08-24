from django.shortcuts import render, redirect
from .btctestnet import *
from .forms import AddressForm
from .models import Address, Transaction


def index(request):
    form = AddressForm(request.POST or None)
    txs = Transaction.objects.all()
    result = None
    if form.is_valid():
        address = Address.objects.get_or_create(address=form.cleaned_data['address'])
        try:
            result = send_tx(address[0].address)
        except Exception as error:
            error_html = 'Неизвестная ошибка'
            if str(error) == 'Transaction blocked':
                error_html = 'Все кошельки ожидают подтверждения транзакций, пожалуйста подождите'
            return render(request, 'index.html', {'txs': txs, 'error': error_html})
        Transaction.objects.create(hash_str=result, address=address[0])
        result = 'Транзакция проведена успешна'
    return render(request, 'index.html', {'txs': txs, 'result': result})


def tx_view(request, tx_id):
    tx = Transaction.objects.get(pk=tx_id)
    return render(request, 'tx.html', {'tx': tx})
