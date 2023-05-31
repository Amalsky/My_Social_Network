from .register import Register, Pic_Update, User_Update
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Post


def register(request):
    if request.method == 'POST':
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {user} please login !')
            return redirect('login')
    else:
        form = Register()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = Pic_Update(request.POST, request.FILES, instance=request.user.profile)
        u_form = User_Update(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, "Your profile has been successfully updated!")
            return redirect('profile')
    else:
        u_form = User_Update(instance=request.user)
        p_form = Pic_Update(instance=request.user.profile)
        context = {'p_form': p_form, 'u_form': u_form}
    return render(request, 'user/profile.html', context)


@login_required
def favourite_add(request, id):
    post = get_object_or_404(Post, id=id)
    if post.favourites.filter(id=request.user.id).exists():
        post.favourites.remove(request.user)
    else:
        post.favourites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def favourite_list(request):
    new = Post.objects.filter(favourites=request.user)
    return render(request, 'user/favourites.html', {'new': new})
