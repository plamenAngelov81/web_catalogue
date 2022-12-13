from django.core.paginator import Paginator
from django.shortcuts import render
# from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from web_shop_0_1.products.models import Products

from .filters import ProductFilter

from help_core.core import HelpCore


class ProductDetailsView(generic.DetailView):
    model = Products
    template_name = 'products/product_details.html'


# class SearchView(generic.ListView):
#     model = Products
#     template_name = 'products/search_results.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         object_list = Products.objects.filter(Q(product_type__type_name__icontains=query))
#         return object_list


class ShowMaterialView(generic.TemplateView):
    template_name = 'products/materials.html'


class ShowToolsView(generic.TemplateView):
    template_name = 'products/tools.html'


class ShowMetalElementsView(generic.TemplateView):
    template_name = 'products/metal.html'


class ShowMixturesView(generic.ListView):
    model = Products.objects.filter(product_type__type_name='Mixture')
    template_name = 'products/mixtures.html'


def show_tiles(request):
    title = 'Tile'
    context = HelpCore.get_context(title)
    return render(request, 'products/reusable_material.html', context)


def show_bricks(request):
    title = 'Brick'
    context = HelpCore.get_context(title)
    return render(request, 'products/reusable_material.html', context)


def show_insulation(request):
    title = 'Insulation'
    context = HelpCore.get_context(title)
    return render(request, 'products/reusable_material.html', context)


def show_paint(request):
    title = 'Paint'
    context = HelpCore.get_context(title)
    return render(request, 'products/reusable_material.html', context)


def show_mixtures(request):
    title = 'Mixture'
    context = HelpCore.get_context(title)
    return render(request, 'products/reusable_material.html', context)


def dry_construction(request):
    title = 'Dry Construction'
    context = HelpCore.get_context(title)
    return render(request, 'products/reusable_material.html', context)


def show_hand_tools(request):
    title = 'Hand Tool'
    context = HelpCore.get_context(title)
    return render(request, 'products/reusable_material.html', context)


def show_power_tools(request):
    title = 'Power Tool'
    context = HelpCore.get_context(title)
    return render(request, 'products/reusable_material.html', context)


def show_bolts(request):
    ordinary_bolts = Products.objects.filter(product_type__type_name='Ordinary Bolt')
    socket_bolts = Products.objects.filter(product_type__type_name='Socket Bolt')
    context = {
        'ordinary_bolts': ordinary_bolts,
        'socket_bolts': socket_bolts,
    }
    return render(request, 'products/bolts.html', context)


def show_nuts(request):
    hex_nuts = Products.objects.filter(product_type__type_name='Hex Nut')
    lock_nuts = Products.objects.filter(product_type__type_name='Lock Nut')
    context = {
        'hex_nuts': hex_nuts,
        'lock_nuts': lock_nuts
    }
    return render(request, 'products/nuts.html', context)


def show_washers(request):
    ordinary_washers = Products.objects.filter(product_type__type_name='Washer Ordinary')
    spiral_washers = Products.objects.filter(product_type__type_name='Washer Spiral')
    context = {
        'ordinary_washers': ordinary_washers,
        'spiral_washers': spiral_washers
    }
    return render(request, 'products/washers.html', context)


def show_nails(request):
    nails = Products.objects.filter(product_type__type_name='Nail')
    context = {
        'nails': nails
    }
    return render(request, 'products/nails.html', context)


def show_metal_profile(request):
    shape = Products.objects.filter(product_type__type_name='Shape')
    armatures = Products.objects.filter(product_type__type_name='Armature')
    context = {
        'shape': shape,
        'armatures': armatures
    }
    return render(request, 'products/metal_components.html', context)


def show_all_products(request):
    all_products = Products.objects.all()
    product_filter = ProductFilter(request.GET, queryset=all_products)
    all_products = product_filter.qs
    paginator = Paginator(all_products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        # 'all_products': all_products,
        'page_obj': page_obj,
        'product_filter': product_filter
    }
    return render(request, 'products/products.html', context)
