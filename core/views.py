from django import UserPlayList
from .models import UserPlayList
from .forms import PlayListForm

# Create your views here.
def homepage(request):
    # return HttpResponse("hello world")
    return render(request, "home.html")

def about_view(request):
    return render(request, 'about.html')
def playlist_info(request, id):
    playlist_object = UserPlayList.objects.get(id=id)
    context = {"playlist_object": playlist_object}
    return render(request, "playlist_info.html", context)

def playlist_add(request):
    if request.method == "POST":
        name = request.POST["playlist_name"]
        description = request.POST["description"]
        playlist_object = UserPlayList.objects.create(
            name=name,
            description=description,
        )
        return redirect(playlist_info, id=playlist_object.id)
    return render(request, "playlist_add.html")

def playlist_df_add(request):
    if request.method == "POST":
        playlist_form = PlayListForm(request.POST)
        if playlist_form.is_valid()
        playlist_form = PlayListForm.save()
        return redirect(playlist_info, id=playlist_object.id)
    
    playlist_form = PlayListForm()
    context["playlist_form"] = playlist_form
    return render(request, "play_df_add.html", context)