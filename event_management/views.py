from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from datetime import datetime

from event_management.models import EventTag, EventType, Location, Event, LikedEvents, FileLink, FileLinkType, ReportEvent
from .forms import CreateUserForm, LoginForm, ProfileCompletionForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .filters import EventFilter

def homepage(request):

    return render(request, 'index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_login')
    context = {'registerform' : form}
    return render(request, 'register.html', context = context)

def my_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    else:
        form = LoginForm()
    context = {'loginform': form}
    return render(request, 'my_login.html', context=context)

@login_required(login_url="my_login")
def dashboard(request):
    events = Event.objects.order_by('start_date').prefetch_related('file_links').all()
    myFilter = EventFilter(request.GET, queryset = events)
    events = myFilter.qs
    return render(request, 'dashboard.html', {'events': events, 'myFilter' : myFilter})


def search(request):
    return render(request, 'search.html')

@login_required(login_url="my_login")
def profile(request):
    events = Event.objects.filter(created_by_id=request.user).order_by('start_date')
    return render(request, 'profile.html', {'events': events})

@login_required(login_url="my_login")
def edit_profile(request):
    if request.method == 'POST':
        print(request.POST)
        profile_form = ProfileCompletionForm(request.POST, user=request.user)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile') 
    else:
        profile_form = ProfileCompletionForm(user=request.user)
    
    return render(request, 'edit_profile.html', {'profile_form': profile_form})

def user_logout(request):
    auth.logout(request)
    return redirect("")

@login_required(login_url="my_login")
def event_list(request):
    events = Event.objects.order_by('start_date')
    return render(request, 'events.html', {'events': events})

@login_required(login_url="my_login")
def event_delete(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('profile')

@login_required(login_url="my_login")
def like_event(request, event_id):
    print(event_id)
    event = Event.objects.get(id=event_id)
    try:
        likedEvent = LikedEvents.objects.get(event_id=event_id, owner_id=request.user)
        likedEvent.delete()
        event.likes_count -= 1
        event.save()
    except LikedEvents.DoesNotExist:
        likedEvent = LikedEvents.objects.create(event_id=event, owner_id=request.user, liked_on=timezone.now())
        event.likes_count +=10
        event.save()
    return redirect('dashboard')

@login_required(login_url="my_login")
def report_event(request, event_id):
    print(event_id)
    event = Event.objects.get(id=event_id)
    try:
        report_event = ReportEvent.objects.get(event_id=event_id, owner_id=request.user)
        report_event.delete()
        event.reports_count -= 1
        event.save()
    except ReportEvent.DoesNotExist:
        report_event = ReportEvent.objects.create(event_id=event, owner_id=request.user, reported_on=timezone.now())
        event.reports_count += 1
        event.save()
    return redirect('dashboard')

def event_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location_id = request.POST.get('location_id')
        type_id = request.POST.get('type_id')
        tag_id = request.POST.get('tag_id')
        link = request.POST.get('link')
        start_date = request.POST.get('start_date') 
        end_date = request.POST.get('end_date')
        likes_count = 0
        created_by_id = request.user

        modified_by_id = created_by_id

        created_on = timezone.now()
        modified_on = created_on

        # Create the event object
        event = Event.objects.create(
            title=title,
            description=description,
            location_id=location_id,
            type_id=type_id,
            tag_id=tag_id,
            link=link,
            start_date=start_date,
            end_date=end_date,
            likes_count=likes_count,
            created_by_id=created_by_id,
            modified_by_id=modified_by_id,
            created_on=created_on,
            modified_on=modified_on
        )

        image  = request.FILES.get('image')
        if image:
            FileLink.objects.create(
                file_link=image,
                link_type=FileLinkType.EVENT,
                event=event,
                owner=request.user,
            )
            
        # Redirect to the event list page
        return redirect('profile')
    # Fetch data for the dropdowns
    locations = Location.objects.all()
    event_types = EventType.objects.all()
    event_tags = EventTag.objects.all()

    context = {
        'locations': locations,
        'event_types': event_types,
        'event_tags': event_tags,
        'action': 'Create'
    }

    return render(request, 'event_form.html', context)

@login_required(login_url="my_login")
def event_edit(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location_id = request.POST.get('location_id')
        type_id = request.POST.get('type_id')
        tag_id = request.POST.get('tag_id')
        link = request.POST.get('link')
        start_date = request.POST.get('start_date') 
        end_date = request.POST.get('end_date')

        # Convert likes_count to an integer
        likes_count = int(request.POST.get('likes_count', 0))  # Default value is 0 if not provided

        start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M') if start_date else None
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M') if end_date else None

        try:
            image  = request.FILES.get('image')
            if image:
                FileLink.objects.filter(event=event).delete()
                FileLink.objects.create(
                    file_link=image,
                    link_type=FileLinkType.EVENT,
                    event=event,
                    owner=request.user,
                )
        except Exception as e:
            print(e)
        
        print(start_date)
        print(end_date)

        modified_by_id = request.user
        modified_on = timezone.now()

        event.title = title
        event.description = description
        event.location_id = location_id
        event.type_id = type_id
        event.tag_id = tag_id
        event.link = link
        event.start_date = start_date
        event.end_date = end_date
        event.likes_count = likes_count
        event.modified_by_id = modified_by_id
        event.modified_on = modified_on

        event.save()

        return redirect('dashboard')
    # Fetch data for the dropdowns
    locations = Location.objects.all()
    event_types = EventType.objects.all()
    event_tags = EventTag.objects.all()

    context = {
        'event': event,
        'locations': locations,
        'event_types': event_types,
        'event_tags': event_tags,
        'action': 'Edit'
    }

    return render(request, 'event_form.html', context)

@login_required(login_url="my_login")
def event_form(request):
    locations = Location.objects.all()
    event_types = EventType.objects.all()
    event_tags = EventTag.objects.all()

    context = {
        'locations': locations,
        'event_types': event_types,
        'event_tags': event_tags
    }
    print(context)
    # Rendering the template with the data
    return render(request, 'event_form.html', context)

def reports(request):
    if not request.user.is_staff:
        return redirect('dashboard')
    report_counts = (
        ReportEvent.objects
        .values('event_id')
        .annotate(report_count=Count('id'))
        .order_by('-report_count')
    )

    reported_events = [
        {
            'event_id': report['event_id'],
            'title': Event.objects.get(id=report['event_id']).title,
            'report_count': report['report_count'],
        }
        for report in report_counts
    ]

    return render(request, 'reports.html', {'reported_events': reported_events})