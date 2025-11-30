from django.shortcuts import render
from datetime import date

def home(request):
    # Improved content with all uploaded photos
    memories = [
        {
            'date': date(2024, 3, 11),
            'title': 'The Beginning',
            'description': 'Waktu aku selesai main basket, aku nanya nih ke doi lagi dimana. Terus dia bilang lagi beli jajan bareng temennya. Yaudah aku ajak fotbar aja sekalian heheheh',
            'image': 'timeline/firstPhoto.jpeg' 
        },
        {
            'date': date(2024, 6, 23),
            'title': 'First Study Date',
            'description': 'Dia pengen minta diajarin Biologi katanya buat OSM waktu itu (Tapi tetep dikalahin anak Alba dong anjay slebew)',
            'image': 'timeline/firstStudy.jpeg'
        },
        {
            'date': date(2024, 4, 16),
            'title': 'First Official Date',
            'description': 'FIRST DATEEEE!!!! Asli dia cantik banget seperti biasa. Waktu awal ketemu dua-duanya malu-malu kucing :D',
            'image': 'timeline/firstDate.jpeg'
        },
        {
            'date': date(2025, 9, 21),
            'title': 'Campus Memories',
            'description': 'Disini kita pengen photobooth pake almet masing-masing (Meskipun rada telat sih WKWKKW)',
            'image': 'timeline/firstAlmet.jpeg'
        },
        {
            'date': date(2025, 9, 14),
            'title': 'First Photobooth',
            'description': 'Karena ini pertama kali, jadi bingung posenya gimana huft...',
            'image': 'timeline/firstPhotobooth.jpeg'
        },
        {
            'date': date(2025, 8, 24),
            'title': 'Adventures at UI',
            'description': 'Akhirnyaaa tidak LDR!!!',
            'image': 'timeline/firstUI.jpeg'
        },
    ]
    
    # Sort memories by date (newest first or oldest first, your choice)
    # This sorts them oldest to newest
    memories.sort(key=lambda x: x['date'])
    
    # LIST BARU: Foto-foto Flashback (Sesuai nama file di screenshot kamu)
    flashback_photos = [
        'timeline/random1.jpeg', 'timeline/random2.jpeg', 'timeline/random3.jpeg',
        'timeline/random4.jpeg', 'timeline/random5.jpeg', 'timeline/random6.jpeg',
        'timeline/random7.jpeg', 'timeline/random8.jpeg', 'timeline/random9.jpeg',
        'timeline/random10.jpeg', 'timeline/random11.jpeg', 'timeline/random12.jpeg',
        'timeline/firstFlower.jpeg', 'timeline/flower2.jpeg'
    ]
    

    return render(request, 'timeline/home.html', {
        'memories': memories,
        'flashback_photos': flashback_photos
    })