from django.shortcuts import render, redirect
from .forms import StudentForm

def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Save data to browser session dictionary so the success view can access it
            request.session['submitted_data'] = form.cleaned_data
            return redirect('success_page')
    else:
        form = StudentForm()
        
    return render(request, "base.html", {'student_form': form})

def success_view(request):
    # Retrieve the saved dictionary data out of the browser session storage
    data = request.session.get('submitted_data', None)
    
    # Safety fallback: if someone navigates to /success directly without submitting data
    if not data:
        return redirect('index')
        
    return render(request, "success.html", {'data': data})
