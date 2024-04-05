from .endpoints.lessons import router as lessons_router
from .endpoints.places import router as places_router
from .endpoints.teachers import router as teachers_router

routers = [lessons_router, places_router, teachers_router]
