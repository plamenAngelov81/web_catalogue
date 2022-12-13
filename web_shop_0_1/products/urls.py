from django.urls import path, include

from web_shop_0_1.products.views import show_all_products, show_paint, ProductDetailsView, ShowMaterialView, ShowToolsView, \
    ShowMetalElementsView, show_bricks, show_tiles, show_insulation, show_mixtures, dry_construction, show_hand_tools, \
    show_power_tools, show_nuts, show_bolts, show_washers, show_nails, show_metal_profile

urlpatterns = [
    path('product/', include([
        path('details/<int:pk>', ProductDetailsView.as_view(), name='product details'),
        path('paint/', show_paint, name='paint'),
        path('tools/', include([
            path('', ShowToolsView.as_view(), name='tool'),
            path('hand-tools', show_hand_tools, name='hand tool'),
            path('power-tools', show_power_tools, name='power tool'),
        ])),

        path('materials/', include([
            path('',  ShowMaterialView.as_view(), name='materials'),
            path('bricks', show_bricks, name='bricks'),
            path('tiles', show_tiles, name='tiles'),
            path('insulation', show_insulation, name='insulation'),
            path('mixtures/', show_mixtures, name='mixtures'),
            path('dry-construction/', dry_construction, name='dry const'),
        ])),
        path('metal-elements/', include([
            path('', ShowMetalElementsView.as_view(), name='metal elements'),
            path('nuts/', show_nuts, name='nuts'),
            path('bolts/', show_bolts, name='bolts'),
            path('washers/', show_washers, name='washers'),
            path('nails/', show_nails, name='nails'),
            path('metal-components/', show_metal_profile, name='metal components'),
        ])),
        path('product-filter/', show_all_products, name='product filter')
    ])),
]
