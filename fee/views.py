from django.shortcuts import render

# Create your views here.
# fee/views.py
from django.shortcuts import render

# fee/views.py
def fee_index(request):
    # Simulated data - in a real app, this would come from a database Model
    context = {
        'student_name': 'Aadi',
        'fee_amount': '5,000.00',
        'status': 'Unpaid' # Set this to 'Paid' to see the green badge
    }
    
    if request.method == 'POST':
        # Handle logic for saving the file here...
        context['status'] = 'Pending Verification'
        context['message'] = "Receipt submitted successfully!"
        
    return render(request, 'fee/fee_details.html', context)