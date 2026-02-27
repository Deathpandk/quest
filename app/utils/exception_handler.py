from pydantic import ValidationError as PydanticValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, PydanticValidationError):
        errors = exc.errors()

        drf_errors = {}
        for error in errors:
            loc = error["loc"][0] if error["loc"] else "non_field_errors"
            msg = error["msg"]
            if loc not in drf_errors:
                drf_errors[loc] = []
            drf_errors[loc].append(msg)

        return Response(drf_errors, status=status.HTTP_400_BAD_REQUEST)

    return response
