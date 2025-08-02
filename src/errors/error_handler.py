from src.main.http_types.http_response import HttpResponse
from .types.http_not_found import HttpNotFoundError
from .types.http_unprocessable_entity import HttpUnprocessableEntityError

def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpUnprocessableEntityError)):
        #enviar para um logger
        return HttpResponse(
            status_code=error.status_code,
            body={
                "error": [{
                    "title": error.name,
                    "detail": error.message
                }]
                }
        )
    return HttpResponse(
        status_code=500,
        body={
            "error": [{
                "title": "InternalServerError",
                "detail": str(error)
            }]
        }
    )