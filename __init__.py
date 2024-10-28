from sqlalchemy.schema import CreateTable
from app.models.user import User
from app.models.task import Task
from sqlalchemy.schema import CreateTable


print(CreateTable(User.__table__).compile(compile_kwargs={"literal_binds": True}))


print(CreateTable(Task.__table__).compile(compile_kwargs={"literal_binds": True}))
