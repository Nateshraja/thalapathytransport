from email.mime import message
from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip, MyCompany
from .forms import TripForm
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required, user_passes_test
#import pywhatkit as kit
import os
from django.conf import settings
from pdf2image import convert_from_path

# ✅ Helper: Staff check
def is_staff_user(user):
    return user.groups.filter(name='TripStaff').exists()

# ✅ Helper: Generate PDF and return file path
def generate_trip_pdf_file(trip):
    # Ensure media folder exists
    media_path = os.path.join(settings.BASE_DIR, 'media')
    os.makedirs(media_path, exist_ok=True)

    # PDF file path
    file_path = os.path.join(media_path, f"trip_{trip.id}.pdf")
    
    # Generate PDF
    template = get_template('trip_receipt.html')
    html = template.render({'trip': trip})
    with open(file_path, 'wb') as f:
        pisa.CreatePDF(html, dest=f)

    return file_path

# ✅ Trip Entry View
@login_required
@user_passes_test(is_staff_user)
def trip_entry_view(request):
    form = TripForm(request.POST or None)
    if form.is_valid():
        trip = form.save(commit=False)
        trip.created_by = request.user
        trip.save()
        return redirect('trip_list')
    return render(request, 'trip_form.html', {'form': form})

# ✅ Trip List View
@login_required
def trip_list(request):
    if is_staff_user(request.user):
        trips = Trip.objects.filter(created_by=request.user).order_by('-date')
    else:
        trips = Trip.objects.all().order_by('-date')
    return render(request, 'trip_list.html', {'trips': trips})

# ✅ Trip PDF View
@login_required
def trip_pdf(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    file_path = generate_trip_pdf_file(trip)
    if not file_path:
        return HttpResponse("PDF generation failed")

    with open(file_path, 'rb') as pdf_file:
        response = HttpResponse(pdf_file.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="trip_{trip.id}.pdf"'
        return response

# ✅ WhatsApp Send View
#@login_required
def send_whatsapp(request, pk):
    trip = get_object_or_404(Trip, pk=pk)
    phone_number = f"+91{trip.company.phone_number}"  # Format: +91XXXXXXXXXX
    invoice_url = f"http://127.0.0.1:8000/trips/{trip.id}/pdf/"
    print(f"Sending WhatsApp message to {phone_number} for trip {trip.id}")
    print(invoice_url)
    message = (
        f"Hello {trip.company.name},\n"
        f"Your trip invoice dated {trip.date} is ready.\n"
        f"Download Invoice: {invoice_url}\n"
        f"Pay via UPI: thalapathi@upi\n"
        f"Thank you - Thalapathi Transport"
    )
    print(f"WhatsApp message: {message}")
    try:
        message = "Here is your invoice link"
        phone = "+919566907059"
        wa_url = f"https://wa.me/{phone}?text={message}"
        return redirect(wa_url)
    except Exception as e:
        return HttpResponse(f"Error sending WhatsApp message: {e}")