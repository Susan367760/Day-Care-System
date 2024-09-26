from django.shortcuts import render, redirect
from .models import Parent, Child, CheckIn  # Ensure to import your models

def home(request):
    return render(request, 'home.html')

def register_child(request):
    if request.method == 'POST':
        # Save parent data
        parent_first_name = request.POST['parent_first_name']
        parent_last_name = request.POST['parent_last_name']
        parent_email = request.POST['parent_email']
        parent_phone_number = request.POST['parent_phone_number']
        next_of_kin_name = request.POST['next_of_kin_name']
        next_of_kin_email = request.POST['next_of_kin_email']
        next_of_kin_phone = request.POST['next_of_kin_phone']

        parent = Parent(  # Remove quotes around Parent
            first_name=parent_first_name,
            last_name=parent_last_name,
            email=parent_email,
            phone_number=parent_phone_number,
            next_of_kin_name=next_of_kin_name,
            next_of_kin_email=next_of_kin_email,
            next_of_kin_phone=next_of_kin_phone
        )
        parent.save()  # Save parent instance to the database

        # Now save the child data
        child_first_name = request.POST['child_first_name']
        child_last_name = request.POST['child_last_name']
        child_year_of_birth = int(request.POST['child_year_of_birth'])  # Ensure it's an integer

        child = Child(  # Remove quotes around Child
            parent=parent,  # Associate child with the saved parent
            first_name=child_first_name,
            last_name=child_last_name,
            year_of_birth=child_year_of_birth
        )
        child.save()  # Save child instance to the database

        return redirect('check_in_child')  # Redirect to the check-in page

    return render(request, 'register_child.html')

def check_in_child(request):
    success_message = None
    if request.method == 'POST':
        # Handle check-in logic
        child_first_name = request.POST['child_first_name']  # Assuming you get this from the form
        child_last_name = request.POST['child_last_name']    # Assuming you get this from the form
        date = request.POST['date']  # Get the date from the form

        # Retrieve the child instance based on first name and last name
        try:
            child = Child.objects.get(first_name=child_first_name, last_name=child_last_name)
            check_in = CheckIn(child=child, date=date)  # Create a CheckIn instance
            check_in.save()  # Save check-in information to the database
            success_message = 'You have successfully checked in your child!'
        except Child.DoesNotExist:
            success_message = 'Child not found! Please check the names entered.'

        return render(request, 'check_in_child.html', {'success': success_message})

    return render(request, 'check_in_child.html')
