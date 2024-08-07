from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, WeightLogForm
from .models import UserProfile, WeightLog

# Create your views here.

@login_required
def profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    weight_logs = WeightLog.objects.filter(user=request.user).order_by('entry_date')
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def edit_profile_view(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
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
