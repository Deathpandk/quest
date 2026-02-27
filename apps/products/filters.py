import django_filters as filters


class ProductFilterSet(filters.FilterSet):
    name = filters.BooleanFilter(field_name="name")
