from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Music_Embed, Local_List


# Create your views here.
# class HomePage(TemplateView):
#     """
#     """
#     template_name = 'jukebox/index.html'


@login_required
def add_to_local_list(request, embed_id):
    # Get the song (Music_Embed) by its ID
    song = get_object_or_404(Music_Embed, id=embed_id)

    # Check if the song is already in the user's local list
    if Local_List.objects.filter(embed_id=song, user_id=request.user).exists():
        messages.warning(request, "This song is already in your local list.")
    else:
        # Add the song to the local list
        Local_List.objects.create(embed_id=song, user_id=request.user)
        messages.success(request, "Song added to your local list!")

    # Redirect back to the index page
    return redirect('index')  # Replace 'index' with the name of your indexview


# def index(request):
#     # Get all songs from the Music_Embed model
#     songs = Music_Embed.objects.all()
#     local_list = Local_List.objects.filter(user_id=request.user)
#     context = {
#         'songs': songs,
#         'local_list': local_list,
#     }
#     return render(request, 'jukebox/index.html', context)

def index(request):
    # Get the search query from the URL
    query = request.GET.get('q', "")  # Get the search query, default to an empty string
    if query:
        # Filter songs based on the search query (case-insensitive)
        songs = Music_Embed.objects.filter(song_name__icontains=query)
    else:
        # If no query, show no songs
        songs = Music_Embed.objects.none()

    # Get the user's local list
    print("current user: ", request.user)
    if request.user.is_authenticated:
        local_list = Local_List.objects.filter(user_id=request.user)
    else:
        local_list = Local_List.objects.none()

    # Pass the songs and the local list to the template
    context = {
        'songs': songs,
        'local_list': local_list,
        'query': query,  # Pass the query back to the template to display in the search bar
    }
    return render(request, 'jukebox/index.html', context)


def search(request):
    query = request.GET.get('q', "")
    if query:
        # Filter songs based on the search query (case-insensitive search)
        songs = Music_Embed.objects.filter(song_name__icontains=query)
    else:
        songs = Music_Embed.objects.all()
        messages.error(request, "No songs found matching your search.")

    return render(
        request, 'jukebox/index.html', {'songs': songs, 'query': query})


# def search(request, query=None):
#     """"
#     """
#     # Get the search query from the URL
#     print("Request is: ", request)
#     for item in request.GET.items():
#         print("Item is: ", item)

#     if query:
#         # Filter songs based on the search query (case-insensitive search)
#         songs = Music_Embed.objects.filter(song_name__icontains=query)
#     else:
#         songs = Music_Embed.objects.all()

#     if songs.count() == 0:
#         # If no songs match the query, show a message
#         messages.info(request, "No songs found matching your search.")
#         # If no query, show all songs
#         songs = Music_Embed.objects.all()

#     # Pass the songs and the query back to the template
#     return render(request, 'jukebox/index.html', {'songs': songs})
