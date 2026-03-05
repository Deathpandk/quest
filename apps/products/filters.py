import django_filters as filters


class ProductFilterSet(filters.FilterSet):
    keywords = filters.CharFilter(field_name="keywords", lookup_expr="icontains")
