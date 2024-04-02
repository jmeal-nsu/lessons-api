from .crud import BaseCRUD
from ..models.lesssons_with_places_and_teachers import LessonsWithPlacesAndTeachers

lessons_crud = BaseCRUD(LessonsWithPlacesAndTeachers)
