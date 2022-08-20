from .models import *

def scheduled_meetings(request):
    allmeetings= Meeting.objects.all()
    return {'meetings':allmeetings}

