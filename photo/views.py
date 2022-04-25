from django.shortcuts import render, redirect
from .models import Photo
#from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos': photos})

def photo_detail(request):
    login_required()
    get_user = request.user
    if get_user.is_authenticated:
        user = UserWarning.objects.get(get_user=request.user)

        return render(request, "photo/detail.html", {'user':user})
    else:
        return redirect('registration/login.html')






class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'photo/update.html'

#class PhotoListView(ListView):
 #   model = Photo
  #  fields = ['photo', 'text']
   # template_name = 'photo/list.html'


