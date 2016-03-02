from Pitchify.forms import UserForm, CompanyForm, InvestorForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from Pitchify.models import Company, Investor
from Pitchify.populate import Population


def index(request):
    # Render and return the rendered response back to the user.
    context = {'type': ''}
    try:
        u = User.objects.get(username=request.user.username)
        try:
            Company.objects.get(user=u)
            context['type'] = 'C'
            print context,'here'
        except:
            pass
        try:
            Investor.objects.get(user=u)
            context['type'] = 'I'
            print context
        except:
            pass
    except:
        pass

        # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileForm(data=request.POST)
        company_form = CompanyForm(data=request.POST)

        investor_form = InvestorForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            user_type = user_form.cleaned_data['type']
            print user_type
            # Save the user's form data to the database.
            if user_type == 'C' and company_form.is_valid():
                user = user_form.save()

                # Now we hash the password with the set_password method.
                # Once hashed, we can update the user object.
                user.set_password(user.password)
                user.save()

                # Now sort out the UserProfile instance.
                # Since we need to set the user attribute ourselves, we set commit=False.
                # This delays saving the model until we're ready to avoid integrity problems.
                company = company_form.save(commit=False)
                company.user = user

                # Now we save the UserProfile model instance.
                #
                # g = Group.objects.get_or_create(name='Company')
                # user.groups.add(g)
                company.save()

                # Update our variable to tell the template registration was successful.
                registered = True
            elif user_type == 'I' and investor_form.is_valid():
                user = user_form.save()

                # Now we hash the password with the set_password method.
                # Once hashed, we can update the user object.
                user.set_password(user.password)
                user.save()

                # Now sort out the UserProfile instance.
                # Since we need to set the user attribute ourselves, we set commit=False.
                # This delays saving the model until we're ready to avoid integrity problems.
                investor = investor_form.save(commit=False)
                investor.user = user

                # Did the user provide a profile picture?
                # If so, we need to get it from the input form and put it in the UserProfile model.
                if 'picture' in request.FILES:
                    investor.picture = request.FILES['picture']

                # # Now we save the UserProfile model instance.
                # g = Group.objects.get_or_create(name='Investor')
                # user.groups.add(g)
                investor.save()

                # Update our variable to tell the template registration was successful.
                registered = True


        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, investor_form.errors, company_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        # profile_form = UserProfileForm()
        company_form = CompanyForm()
        investor_form = InvestorForm()

    # Render the template depending on the context.
    return render(request,
                  'Pitchify/index.html',
                  {'user_form': user_form, 'company_form': company_form,
                   'investor_form': investor_form, 'registered': registered, 'context': context})


    # return render(request, 'Pitchify/index.html', context)


def populate(request):
    context = {}

    # print('populate')
    population = Population()
    population.populate(True)

    return render(request, 'Pitchify/populate.html', context)


def register(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        # profile_form = UserProfileForm(data=request.POST)
        company_form = CompanyForm(data=request.POST)

        investor_form = InvestorForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            user_type = user_form.cleaned_data['type']
            print user_type
            # Save the user's form data to the database.
            if user_type == 'C' and company_form.is_valid():
                user = user_form.save()

                # Now we hash the password with the set_password method.
                # Once hashed, we can update the user object.
                user.set_password(user.password)
                user.save()

                # Now sort out the UserProfile instance.
                # Since we need to set the user attribute ourselves, we set commit=False.
                # This delays saving the model until we're ready to avoid integrity problems.
                company = company_form.save(commit=False)
                company.user = user

                # Now we save the UserProfile model instance.
                #
                # g = Group.objects.get_or_create(name='Company')
                # user.groups.add(g)
                company.save()

                # Update our variable to tell the template registration was successful.
                registered = True
            elif user_type == 'I' and investor_form.is_valid():
                user = user_form.save()

                # Now we hash the password with the set_password method.
                # Once hashed, we can update the user object.
                user.set_password(user.password)
                user.save()

                # Now sort out the UserProfile instance.
                # Since we need to set the user attribute ourselves, we set commit=False.
                # This delays saving the model until we're ready to avoid integrity problems.
                investor = investor_form.save(commit=False)
                investor.user = user

                # Did the user provide a profile picture?
                # If so, we need to get it from the input form and put it in the UserProfile model.
                if 'picture' in request.FILES:
                    investor.picture = request.FILES['picture']

                # # Now we save the UserProfile model instance.
                # g = Group.objects.get_or_create(name='Investor')
                # user.groups.add(g)
                investor.save()

                # Update our variable to tell the template registration was successful.
                registered = True


        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, investor_form.errors, company_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        # profile_form = UserProfileForm()
        company_form = CompanyForm()
        investor_form = InvestorForm()

    # Render the template depending on the context.
    return render(request,
                  'Pitchify/register.html',
                  {'user_form': user_form, 'company_form': company_form,
                   'investor_form': investor_form, 'registered': registered})


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
        # because the request.POST.get('<variable>') returns None, if the value does not exist,
        # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/Pitchify/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Pitchify account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'Pitchify/login.html', {})


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/Pitchify/')
