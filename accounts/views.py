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
from checkout.models import *

# Create your views here.


@login_required
def profile_view(request):
    """
    View to display the user's profile page.

    Retrieves the user's profile and weight logs,
    then renders the profile page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    weight_logs = WeightLog.objects.filter(user=request.user).order_by(
        'entry_date'
    )
    return render(request, 'accounts/profile.html', {'profile': profile})


@login_required
def user_order_history(request):
    """
    View to display the user's order history.

    Retrieves the user's order history, including related training plans, and
    renders the order history page.
    """
    order_history = Order.objects.filter(
        user=request.user).select_related('training_plan').order_by(
        '-created_at'
    )
    return render(
        request,
        'accounts/user_order_history.html',
        {'order_history': order_history}
    )


@login_required
def edit_profile_view(request):
    """
    View to edit the user's profile information.

    Handles the form submission for updating the user's profile and displays
    success or error messages as appropriate.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if (
        request.method == 'POST' and
        request.POST.get('form_type') == 'editProfile'
    ):
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()  # This will now update both User and UserProfile
            messages.success(request, "Profile updated successfully.")
            return redirect('profile')  # Redirect to the profile page
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
    """
    View to add a new weight log entry.

    Handles form submission for adding a new weight log, validates the data,
    and provides feedback messages on success or failure.
    """
    if request.method == 'POST':
        form = WeightLogForm(request.POST)
        if form.is_valid():
            weight_log = form.save(commit=False)
            weight_log.user = request.user
            weight_log.weight = form.cleaned_data["weight"]
            weight_log.entry_date = timezone.now()
            weight_log.save()
            messages.success(
                request,
                "Your weight log was successfully saved."
            )
            return redirect('profile')
        else:
            # Iterate over form errors and add them to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = WeightLogForm()
    return render(request, 'accounts/add_weight_log.html', {'form': form})


@login_required
def get_user_weight_logs(request):
    """
    API view to retrieve the user's weight logs for chart display.

    Returns a JSON response with the user's weight logs ordered by entry date.
    """
    try:
        weight_logs = WeightLog.objects.filter(
            user=request.user
        ).order_by('entry_date').values('weight', 'entry_date')
        weight_log_list = list(weight_logs)
        return JsonResponse(weight_log_list, safe=False)
    except WeightLog.DoesNotExist:
        return JsonResponse({"message": 'Weight log not found'}, status=404)


@login_required
def get_user_weight_logs_history(request):
    """
    API view to retrieve the user's weight logs history.

    Returns a JSON response with the user's weight logs ordered by entry date.
    """
    try:
        weight_logs = WeightLog.objects.filter(
            user=request.user
        ).order_by('-entry_date').values('id', 'entry_date', 'weight')
        weight_logs_list = list(weight_logs)
        return JsonResponse(weight_logs_list, safe=False)
    except WeightLog.DoesNotExist:
        return JsonResponse({"message": 'Weight logs not found'}, status=404)


@login_required
def edit_weight_log(request, log_id):
    """
    View to edit a specific weight log entry by its ID.

    Handles form submission for editing a weight log, validates the data,
    and provides feedback messages on success or failure.
    """
    weight_log = get_object_or_404(WeightLog, id=log_id, user=request.user)

    if request.method == 'POST':
        form = WeightLogForm(request.POST, instance=weight_log)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your weight log was successfully updated."
            )
            return redirect('profile')
        else:
            # Iterate over form errors and add them to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = WeightLogForm(instance=weight_log)

    return render(
        request,
        'accounts/edit_weight_log.html',
        {'form': form, 'weight_log': weight_log}
    )


@login_required
def delete_weight_log(request, log_id):
    """
    View to delete a specific weight log entry by its ID.

    Handles the deletion of the weight log and provides feedback messages
    on success or failure.
    """
    weight_log = get_object_or_404(WeightLog, id=log_id, user=request.user)

    if request.method == 'DELETE':
        weight_log.delete()
        messages.success(request, "Your weight log was successfully deleted.")
        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


@login_required
def delete_user_profile(request):
    """
    View to delete the user's profile and account.

    Handles the deletion of the user's account, providing confirmation messages
    and redirecting to the home page.
    """
    try:
        user = get_object_or_404(User, id=request.user.id)
        if user == request.user:
            # TODO: add a check before deletion for the user subscription. Issue #17 # noqa
            user.delete()
            messages.success(
                request,
                "Your account has been successfully deleted"
            )
        else:
            messages.error(
                request, "You do not have permission to delete this user."
            )
    except User.DoesNotExist:
        messages.error(request, "The requested user does not exist.")
        return redirect('not_found')
    return redirect("home")


@login_required
def upload_progress_picture(request):
    """
    View to upload a progress picture for the user's profile.

    Handles form submission for uploading a progress picture and provides
    feedback messages on success or failure.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ProgressPictureForm(request.POST, request.FILES)
        if form.is_valid():
            progress_picture = form.save(commit=False)
            progress_picture.user = profile
            progress_picture.save()
            messages.success(
                request,
                'Your Progress Picture has been uploaded successfully!'
            )
            return redirect('profile')
        else:
            # Iterate over form errors and add them to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = ProgressPictureForm()
    return render(request, 'profile.html', {'form': form})


@require_POST
def delete_progress_picture(request, picture_id):
    """
    View to delete a specific progress picture by its ID.

    Handles the deletion of the progress picture
    and redirects to the profile page.
    """
    picture = get_object_or_404(ProgressPicture, id=picture_id)
    picture.delete()
    messages.success(
                request,
                'Your Progress Picture has been deleted successfully!'
            )
    return redirect(reverse('profile'))

