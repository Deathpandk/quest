from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPagination(PageNumberPagination):
    """
    Pagination Class
    """

    page_size = 40
    page_size_query_param = "per_page"

    def get_paginated_response(self, data):
        return Response(
            {
                "page": self.page.number,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )
