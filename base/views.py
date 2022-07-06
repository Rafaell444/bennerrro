from .models import slider
from django.shortcuts import render
from .models import slider, category, about, product, advantage


def home(request):
    slid_img = slider.objects.all()
    cat_img = category.objects.all()
    ab_img = about.objects.all()
    prod_img = product.objects.all()
    adv_img = advantage.objects.all()

    return render(request, template_name="base/index.html", context={
        "cat_image": cat_img,
        "slid_img": slid_img,
        "ab_img": ab_img,
        "prod_img": prod_img,
        "adv_img": adv_img
    })
