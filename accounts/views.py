from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

@login_required
def profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    weight_logs = WeightLog.objects.filter(user=request.user).order_by('entry_date')
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def edit_profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST' and request.POST.get('form_type') == 'editProfile':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # This will now update both User and UserProfile
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')  # Redirect to the profile page after saving
        else:
            # Iterate over form errors and add them to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'form': form})

@login_required
def add_weight_log(request):
    if request.method == 'POST':
        form = WeightLogForm(request.POST)
        if form.is_valid():
            weight_log = form.save(commit=False)
            weight_log.user = request.user
            weight_log.weight = form.cleaned_data["weight"]
            weight_log.entry_date = timezone.now()
            weight_log.save()
            return redirect('profile')
        else:
            # Print form errors for debugging
            print(form.errors)
    else:
        form = WeightLogForm()
    return render(request, 'accounts/add_weight_log.html', {'form': form})

@login_required
def get_user_weight_logs(request):
    try:
        weight_logs = WeightLog.objects.filter(user=request.user).order_by('entry_date').values('weight', 'entry_date')
        weight_log_list = list(weight_logs)
        return JsonResponse(weight_log_list, safe=False)
        
    except WeightLog.DoesNotExist:
        return JsonResponse({"message": 'Weight log not found'}, status=404)
    


@login_required
def get_user_weight_logs_history(request):
    try:
        weight_logs = WeightLog.objects.filter(user=request.user).order_by('-entry_date').values('id', 'entry_date', 'weight')
        weight_logs_list = list(weight_logs)
        return JsonResponse(weight_logs_list, safe=False)
        
    except WeightLog.DoesNotExist:
        return JsonResponse({"message": 'Weight logs not found'}, status=404)
    

@login_required
def edit_weight_log(request, log_id):
    weight_log = get_object_or_404(WeightLog, id=log_id, user=request.user)

    if request.method == 'POST':
        form = WeightLogForm(request.POST, instance=weight_log)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = WeightLogForm(instance=weight_log)

    return render(request, 'accounts/edit_weight_log.html', {'form': form, 'weight_log': weight_log}) 


@login_required
def delete_weight_log(request, log_id):
    weight_log = get_object_or_404(WeightLog, id=log_id, user=request.user)

    if request.method == 'DELETE':
        weight_log.delete()
        return JsonResponse({'success': True})
    
    return JsonResponse({'success': False})

@login_required
def delete_user_profile(request):
    try:
        user = get_object_or_404(User, id=request.user.id)
        if user == request.user:
            # TODO: add a check before deletion for the user subscription. Issue #17
            user.delete()
            messages.success(request,
                                "Your account has been successfully deleted")
        else:
            messages.error(request, "You do not have permission"
                                    " to delete this user.")
    except User.DoesNotExist:
        messages.error(request, "The requested user does not exist.")
        return redirect('not_found')
    return redirect("home")

@login_required
def upload_progress_picture(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ProgressPictureForm(request.POST, request.FILES)
        if form.is_valid():
            progress_picture = form.save(commit=False)
            progress_picture.user = profile
            progress_picture.save()
            messages.success(request, 'Your Progress Picture has been uploaded successfully!')
            return redirect('profile')
    else:
        form = ProgressPictureForm()
    return render(request, 'profile.html', {'form': form})

@require_POST
def delete_progress_picture(request, picture_id):
    picture = get_object_or_404(ProgressPicture, id=picture_id)
    picture.delete()
    return redirect(reverse('profile'))