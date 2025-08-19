from django.shortcuts import render, redirect
from django.contrib import messages
from tracker.models import Transaction
from django.db.models import Sum

def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        print(description,amount)
        if not description and not amount:
            messages.warning(request, "Please fill the description or amount fields.")
            return redirect('/')

        try:
            amount = float(amount)
        except Exception as e:
            messages.warning(request, "Please input only digits in amount.")
            return redirect('/')

        Transaction.objects.create(description=description, amount=amount)

        return redirect('/')
    context = {
    'transactions':Transaction.objects.all(),
    'balance':Transaction.objects.all().aggregate(total_balance = Sum('amount'))['total_balance'] or 0,
    'income':Transaction.objects.filter(amount__gte=0).aggregate(income = Sum('amount'))['income'] or 0,
    'expense':Transaction.objects.filter(amount__lte=0).aggregate(expense = Sum('amount'))['expense'] or 0,
    }
    return render(request, 'index.html', context)

def deleteTransaction(request,uuid):
    Transaction.objects.get(uuid=uuid).delete()
    return redirect('/')
