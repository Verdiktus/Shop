from django.shortcuts import render
from django.views.generic import DetailView
from .models import Notebook, Smartphone


def test_view(request):
    return render(request, 'base.html', {})


class ProductDetailView(DetailView):
    CT_MODEL_MODEL_CLASS = {
        'notebook': Notebook,
        'smartphone': Smartphone
    }

    def dispatch(self, request, *args, **kwargs):
        ct_model = kwargs.get('ct_model')

    # model = Modeml
    # queryset = Model.objects.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'
