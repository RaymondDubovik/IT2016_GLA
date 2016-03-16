from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from pitchify.forms import *
from pitchify.models import Company, Investor, Offer
from pitchify.populate import Population

USER_TYPE_COMPANY = 'C'
USER_TYPE_INVESTOR = 'I'

MAX_DESCRIPTION_LENGTH = 100


def get_user_type(request, user_id = 0):
    if user_id == 0:
        user_id = request.user.id

    type = ''
    try:
        u = User.objects.get(id=user_id)
        try:
            Company.objects.get(user=u)
            type = USER_TYPE_COMPANY
        except:
            pass
        try:
            Investor.objects.get(user=u)
            type = USER_TYPE_INVESTOR
        except:
            pass
    except:
        pass
    return type


def index(request):
        # Render and return the rendered response back to the user.
    user_type = get_user_type(request)

    context = {'type': user_type}
    if request.user.is_authenticated():
        if user_type == USER_TYPE_COMPANY:
            company = Company.objects.get(user=request.user)
            top_five_selling_pitches = Pitch.objects.filter(company=company).order_by('-sold_stocks')
            context['my_pitches'] = top_five_selling_pitches
            context['ext_template'] = 'pitchify/index.html'
            return render(request, 'pitchify/my_pitches_child.html', context)

        if user_type == USER_TYPE_INVESTOR:
            return render(request,
                          'pitchify/index.html',
                          context )
    else:
        # A boolean value for telling the template whether the registration was successful.
        # Set to False initially. Code changes value to True when registration succeeds.

        user_form = UserForm()
        # profile_form = UserProfileForm()
        company_form = CompanyForm()
        investor_form = InvestorForm()

        context['user_form'] = user_form
        context['company_form'] = company_form
        context['investor_form'] = investor_form

        # Render the template depending on the context.
        return render(request,
                      'pitchify/index.html',
                      context)


def populate(request):
    context = {}

    # print('populate')
    population = Population()
    population.populate(True)

    return render(request, 'pitchify/populate.html', context)


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

            # Save the user's form data to the database.
            if user_type == USER_TYPE_COMPANY and company_form.is_valid():
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
            elif user_type == USER_TYPE_INVESTOR and investor_form.is_valid():
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

            if registered:
                user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
                login(request, user)
                return HttpResponseRedirect("/pitchify/")


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
    context = {}
    context['user_form'] = user_form
    context['company_form'] = company_form
    context['investor_form'] = investor_form
    return render(request,
                  'pitchify/index.html',
                  context)


def user_login(request):
    errors = ''
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
                return HttpResponseRedirect('/pitchify/')
            else:
                # An inactive account was used - no logging in!
                errors = "Your pitchify account is disabled."
                return render(request, 'pitchify/login.html', {"errors": errors})
        else:
            # Bad login details were provided. So we can't log the user in.
            errors = "Invalid login details"
            return render(request, 'pitchify/login.html', {"errors": errors})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'pitchify/login.html', {})


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/pitchify/')


@login_required
def create_pitch(request):
    # getting user type
    user_type = get_user_type(request)

    context = {}
    context['type'] = user_type

    if request.method == 'POST':
        pitch_form = PitchForm(data=request.POST)
        # print pitch_form
        # pitch_form.data['company_id'] = request.user.id
        if pitch_form.is_valid():
            company = Company.objects.get(user=request.user)
            pitch = pitch_form.save(commit=False)
            pitch.company = company
            pitch.save()
        else:
            print pitch_form.errors
            context['pitch_form'] = pitch_form
            return render(request, 'pitchify/create_pitch.html', context)
        return HttpResponseRedirect('/pitchify/my_pitches')

    pitch_form = PitchForm()
    context['pitch_form'] = pitch_form
    return render(request, 'pitchify/create_pitch.html', context)


# @user_passes_test(lambda u: u.is_superuser)
@login_required
def my_pitches(request):
    context = {}

    user_type = get_user_type(request)

    context['type'] = user_type

    company = Company.objects.get(user=request.user)
    # pages = Page.objects.filter(category=category).order_by('-views')
    pitches_for_company = Pitch.objects.filter(company=company)

    context['my_pitches'] = pitches_for_company
    context['ext_template'] = 'pitchify/my_pitches.html'

    return render(request, 'pitchify/my_pitches_child.html', context)


@login_required
def investor_pitches(request):
    context = {}
    user_type = get_user_type(request)
    context['type'] = user_type

    pitches = Pitch.objects.order_by('-created')
    for pitch in pitches: # loop through all pitches the pitches
        # if description is too long, truncate it and append 3 dots at the end
        if len(pitch.description) > MAX_DESCRIPTION_LENGTH:
            pitch.description = pitch.description[:MAX_DESCRIPTION_LENGTH] + '...'

    context['pitches'] = pitches

    return render(request, 'pitchify/investor_pitches.html', context)


@login_required
def investor_offers(request):
    context = {}
    user_type = get_user_type(request)
    context['type'] = user_type

    user = request.user
    investor = Investor.objects.get(user=user)
    offers = Offer.objects.filter(investor=investor).order_by('status')

    context['offers'] = offers
    context['ext_template'] = 'pitchify/investor_offers.html'
    context['hide'] = False

    return render(request, 'pitchify/investor_offers_child.html', context)


@login_required
def pitch(request, pitch_id):
    context = {}
    user_type = get_user_type(request)
    context['type'] = user_type

    try:
        pitch = Pitch.objects.get(id=pitch_id)
    except: # pitch does not exist
        return render(request, 'pitchify/error.html',
                      {'error_message': "Could not find a pitch!",
                       'return_message': 'Browse pitches',
                       'return_url': 'pitchify:investor_pitches',})

    context['pitch'] = pitch
    context['pitch_id'] = pitch_id
    context['Offer'] = Offer
    context['ext_template'] = 'pitchify/investor_pitch.html'
    context['hide'] = True
    context['percentage_claimed'] = pitch.sold_stocks * 100 / pitch.total_stocks
    context['top_pitches'] = Pitch.objects.order_by("-sold_stocks")[:10]  # retrieve only top 10 pitches

    user = request.user
    if user_type == USER_TYPE_INVESTOR:
        investor = Investor.objects.get(user=user)
        offers = Offer.objects.filter(investor=investor, pitch=pitch).order_by('status')
        context['offers'] = offers
        return render(request, 'pitchify/investor_offers_child.html', context)

    company = Company.objects.get(user=user)
    if company != pitch.company: # verifies, that the company owns the pitch
        # TODO: company not allowed to view this pitch
        return render(request, 'pitchify/error.html',
                      {'error_message': "Sorry it is not your pitch!",
                       'return_message': 'Browse your pitches',
                       'return_url': 'pitchify:my_pitches',})

    offers = Offer.objects.filter(pitch=pitch).order_by('status')
    context['offers'] = offers
    return render(request, 'pitchify/company_offers_child.html', context)


@login_required
def investor_remove_offer(request, offer_id):
    try:
        offer = Offer.objects.get(id=offer_id)
    except:
        return JsonResponse({'success': False})

    user = request.user
    investor = Investor.objects.get(user=user)
    if offer.investor != investor or offer.status != Offer.PENDING:
        return JsonResponse({'success': False, 'message': "You can not remove this offer"})

    offer.delete()
    return JsonResponse({'success': True})


@login_required
def investor_add_offer(request, pitch_id, offer_stock_count, offer_stock_price, offer_message):
    if get_user_type(request) != USER_TYPE_INVESTOR:
        return JsonResponse({'success': False, 'message': "You can not add an offer"})

    try:
        pitch = Pitch.objects.get(id=pitch_id)
    except:
        return JsonResponse({'success': False, 'message': "Pitch does not exist"})

    offer_stock_count = int(offer_stock_count)
    offer_stock_price = int(offer_stock_price)

    if pitch.stocks_left < offer_stock_count:
        return JsonResponse({'success': False, 'message': "Sorry, there are only " + str(pitch.stocks_left) +
                                                          " stocks left"})

    if offer_stock_price <= 0:
        return JsonResponse({'success': False, 'message': "Invalid stock count"})

    user = request.user
    investor = Investor.objects.get(user=user)

    offer, created = Offer.objects.get_or_create(
            pitch=pitch,
            investor=investor,
            stock_count=offer_stock_count,
            price=offer_stock_price,
            message=offer_message,)

    return JsonResponse({'success': True, 'id': offer.id})


@login_required
def profile(request, user_id):
    context = {}

    user_type = get_user_type(request)

    context['type'] = user_type

    type = get_user_type(request, user_id)
    if type == USER_TYPE_COMPANY:
        company = Company.objects.get(user_id=user_id)
        context['description'] = company.description
    elif type == USER_TYPE_INVESTOR:
        investor = Investor.objects.get(user_id=user_id)
        context['website'] = investor.website

    return render(request, 'pitchify/profile.html', context)


@login_required
def company_accept_offer(request, offer_id, accept, offer_answer):
    try:
        offer = Offer.objects.get(id=offer_id)
    except:
        return JsonResponse({'success': False, 'message': "Offer does not exist!"})

    user = request.user
    company = Company.objects.get(user=user)
    if company != offer.pitch.company:  # verifies, that the company owns the offer
        return JsonResponse({'success': False, 'message': "Offer is not for your pitch!"})

    if accept == "true":
        new_stock_count = offer.pitch.sold_stocks + offer.stock_count
        if new_stock_count > offer.pitch.total_stocks:
            message = 'You can\'t accept this offer. You have only ' + str(offer.pitch.sold_stocks) + ' stocks left!'
            return JsonResponse({'success': False, 'message': message})

        offer.pitch.sold_stocks = new_stock_count
        offer.pitch.save()
        offer.status = Offer.ACCEPTED
    else:
        offer.status = Offer.DECLINED

    offer.answer = offer_answer
    offer.save()

    return JsonResponse({'success': True, 'soldStocks': offer.pitch.sold_stocks, 'invested': offer.pitch.invested})


@login_required
def edit_pitch(request, pitch_id, youtube, description):
    pitch = Pitch.objects.get(id=pitch_id)

    user = request.user
    company = Company.objects.get(user=user)
    if company != pitch.company:  # verifies, that the company owns the pitch
        return JsonResponse({'success': False, 'message': "This is not your pitch!"})

    if youtube and 'youtube' in youtube:
        # regex for the YouTube ID: "^[^v]+v=(.{11}).*"
        result = re.match('^[^v]+v=(.{11}).*', youtube)
        youtube = result.group(1)

    pitch.youtube_video_id = youtube
    pitch.description = description
    pitch.save()

    return JsonResponse({'success': True, 'youtubeId': youtube})