from django.shortcuts import render
from datetime import date

def home(request):
    # Add your memories here!
    memories = [
        {
            'date': date(2023, 2, 14),
            'title': 'Our First Date',
            'description': 'We went to that Italian place and talked for hours.',
            'image': 'timeline/firstDate.jpeg'  # Make sure this filename matches your static folder!
        },
        {
            'date': date(2023, 6, 20),
            'title': 'Summer Trip',
            'description': 'Our first trip to the beach.',
            'image': 'timeline/firstUI.jpeg'
        },
        # Copy and paste the block above to add more memories
    ]
    
    return render(request, 'timeline/home.html', {'memories': memories})
