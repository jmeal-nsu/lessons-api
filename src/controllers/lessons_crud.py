from .crud import BaseCRUD
from ..models.lesssons_with_places_and_teachers import LessonsWithPlacesAndTeachers
from ..models.lesson import Lesson

lessons_crud = BaseCRUD(LessonsWithPlacesAndTeachers)
raw_lessons_crud = BaseCRUD(Lesson)
