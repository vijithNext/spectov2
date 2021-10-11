ADMIN_PATH = 'v1/web/'
STUDENT_PATH = 'v1/web/'

PASSWORD_LENGTH = 6
CODE_LENGTH = 15

#Pagination:
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class LabourListPagination(PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_counts': self.page.paginator.count,
            'count_per_page':self.page_size,
            'total_pages': self.page.paginator.num_pages,
            'status': 200,
            'results': data
        })

class TaskListPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'total_counts': self.page.paginator.count,
            'count_per_page':self.page_size,
            'total_pages': self.page.paginator.num_pages,
            'status': 200,
            'results': data
        })

MODE_KEY = "rzp_test_HaGgMxK8sECTDp"
SECRET_KEY = "pC5q92wsgnKZ3ickuv6Gs67b"