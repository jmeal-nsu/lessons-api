from .crud import BaseCRUD
from ..models.teacher import Teacher

teachers_crud = BaseCRUD(Teacher)
