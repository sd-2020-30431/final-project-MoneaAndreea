from django.contrib.auth.decorators import login_required
from users.forms import profileUpdateForm, userUpdateForm
from users.models import Profile as Pro, Requests
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect



@login_required
def Profile(request):
    if request.method == 'POST':
        u_form = userUpdateForm(request.POST,instance=request.user)
        p_form = profileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been successfully updated!')
            return redirect('users:profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile)

    context= {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'profile/profile.html',context)


def reqts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('e-mail')
        nb_tel = request.POST.get('phone')
        prof = request.user.profile
        req = Requests(prof, name, email, nb_tel)
        req.save()
        prof_id = prof.id
        Pro.objects.filter(id=prof_id).update(is_teacher=True)

        messages.info(request, f'The request has been succsefully processed for teacher account')
        return redirect('courses:home')


