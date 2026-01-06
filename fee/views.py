from django.shortcuts import render

# Create your views here.
# fee/views.py
from django.shortcuts import render

def fee_index(request):
    context = {
        'student_name': 'Aadi',
        'fee_amount': 5000,
        'status': 'Unpaid'
    }
    return render(request, 'fee/fee_details.html', context)