from infrastructure.repository.unit_of_work import UnitOfWork
from typing import TypeVar, Any
from domain.entities.base_class import BaseEntity
from infrastructure.repository.base_repo import BaseRepo

E = TypeVar('E', bound=BaseEntity)
T = TypeVar('T', bound=BaseRepo[Any])


class BaseService:

    def add(self, entity: E, repo: T) -> E | None:
        with UnitOfWork(repo) as uow:
            result = uow.repo.insert(entity, uow.session)
            return result

    def get_all(self, repo: T) -> list[E]:
        with UnitOfWork(repo) as uow:
            students = uow.repo.get_all(uow.session)
        return students

    def get_by_id(self, id: int, repo: T) -> E | None:
        with UnitOfWork(repo) as uow:
            student_entity = uow.repo.get(id, uow.session)
        return student_entity

    def update(self, id: int, entity: E, repo: T) -> bool:
        with UnitOfWork(repo) as uow:
            subject = uow.repo.get(id, uow.session)
            if subject is None:
                return False
            else:
                subject = entity
            uow.repo.update(subject, id, uow.session)
            return True

    def delete(self, id: int, repo: T) -> bool:
        with UnitOfWork(repo) as uow:
            result = uow.repo.delete(id, uow.session)
            return result
