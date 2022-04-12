from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Watch_2_watch.accounts.decorators import user_required
from Watch_2_watch.accounts.models import UserProfile
from Watch_2_watch.common.forms import CommentForm
from Watch_2_watch.watches.forms import WatchForm, EditWatchForm, CreateWatchForm
from Watch_2_watch.watches.models import Watch, Comment
from django.contrib.auth.models import User


def list_watches(request):
    context = {
        'watches': Watch.objects.all()
    }

    return render(request, 'watches/watches_list.html', context)


@login_required
def watch_details(request, pk):
    watch = Watch.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'watch': watch,
            'form': CommentForm(),
            'can_edit_delete': request.user == watch.user.user,
            'can_comment': request.user,
        }

        return render(request, 'watches/watch_details.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.watch = watch
            comment.user = request.user.userprofile
            comment.save()
            return redirect('list watches')
        context = {
            'watch': watch,
            'form': form,
        }

        return render(request, 'watches/watch_details.html', context)


@login_required
def comment_watch(request, pk):
    watch = Watch.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'watch': watch,
            'form': CommentForm(),
            'can_delete': request.user == watch.user.user,
            'can_edit': request.user == watch.user.user,
        }

        return render(request, 'watches/watch_details.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                text=form.cleaned_data['text'],
            )
            comment.watch = watch
            comment.user = request.user.userprofile
            comment.save()

            return redirect('watch details', pk)
        context = {
            'watch': watch,
            'form': form,
        }

        return render(request, 'watches/watch_details.html', context)


@user_required(Watch)
def edit_watch(request, pk):
    watch = Watch.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditWatchForm(instance=watch)

        context = {
            'form': form,
            'watch': watch,
        }

        return render(request, 'watches/watches_edit.html', context)
    else:
        form = EditWatchForm(
            request.POST,
            request.FILES,
            instance=watch
        )
        if form.is_valid():
            form.save()
            return redirect('watch details', watch.pk)

        context = {
            'form': form,
            'watch': watch,
        }

        return render(request, 'watches/watches_edit.html', context)


def create_watch(request, pk=None, user=None):
    # def get_user_name(request):
    #     username = None
    #     if request.user.is_authenticated():
    #         username = request.user.username
    #         return username
    #

    if request.method == 'GET':
        watch_owner = request.user.username
        form = CreateWatchForm(initial = {'user': watch_owner})
        context = {
            'form': form,
            'watch_owner': watch_owner,
        }

        return render(request, 'watches/watches_create.html', context)
    else:
        watch_owner = request.user.username
        form = CreateWatchForm(
            request.POST,
            request.FILES,
        )
        if form.is_valid():
            watch = form.save()
            watch.save()
            return redirect('list watches')

        context = {
            'form': form,
            'watch_owner': watch_owner,
        }

        return render(request, 'watches/watches_create.html', context)


@login_required
def delete_watch(request, pk):
    watch = Watch.objects.get(pk=pk)
    if request.method == "POST":
        watch.delete()
        return redirect('list watches')
    else:
        context = {
            'watch': watch,
        }

        return render(request, 'watches/watch_delete.html', context)
