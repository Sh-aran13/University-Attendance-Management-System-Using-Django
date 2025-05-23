from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods

def stviewreport(request):
    if not request.session.get('authenticated'):
        return redirect('login')
    
    # Empty context since we're not using any data
    return render(request, 'myapp/stviewreport.html')

def home_view(request):
    if not request.session.get('authenticated'):
        return redirect('login')
    return render(request, 'myapp/home.html')

def student_dashboard(request):
    if not request.session.get('authenticated'):
        return redirect('login')
    return render(request, 'myapp/studentdash.html')

def faculty_dashboard(request):
    if not request.session.get('authenticated'):
        return redirect('login')
    return render(request, 'myapp/facultydash.html')

@require_http_methods(["GET", "POST"])
def faculty_mark(request):
    if not request.session.get('authenticated'):
        return redirect('login')
    
    if request.method == 'POST':
        # Just validate that fields exist without storing anything
        required_fields = ['faculty_name', 'date', 'attendance_status']
        if not all(field in request.POST for field in required_fields):
            messages.error(request, 'All fields are required!')
        else:
            messages.success(request, 'Attendance would be marked here in a real implementation')
            return redirect('faculty_dashboard')
            
    return render(request, 'myapp/facultymarkatt.html')

@require_http_methods(["GET", "POST"])
def mark_attendence(request):
    if not request.session.get('authenticated'):
        return redirect('login')
    
    if request.method == 'POST':
        if 'date' not in request.POST:
            messages.error(request, 'Date is required')
        else:
            messages.success(request, 'Attendance would be marked here in a real implementation')
            return redirect('student_dashboard')
    
    return render(request, 'myapp/markattendence.html')

@require_http_methods(["GET", "POST"])
def login_view(request):
    if request.method == 'POST':
        # Basic validation - just check that fields exist
        if 'username' not in request.POST or 'password' not in request.POST:
            messages.error(request, 'Username and password are required')
        else:
            # Simple authentication - any non-empty credentials will work
            request.session['authenticated'] = True
            request.session['username'] = request.POST['username']
            
            # Redirect to appropriate dashboard based on URL pattern
            if 'student' in request.POST['username'].lower():
                return redirect('student_dashboard')
            elif 'faculty' in request.POST['username'].lower():
                return redirect('faculty_dashboard')
            else:
                return redirect('home')
    
    return render(request, 'myapp/login.html')

@require_http_methods(["GET", "POST"])
def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if not name or not email or not password or not confirm_password:
            messages.error(request, 'All fields are required.')
        elif password != confirm_password:
            messages.error(request, 'Passwords do not match.')
        else:
            messages.success(request, 'Successfully signed up! You can now log in.')
    return redirect('login')
        # If there are errors, fall through to render the signup page again

    return render(request, 'myapp/signup.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')