if request.method == "POST":
    form = MyFormClass(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        # Without this next line the tags won't be saved.
        form.save_m2m()
