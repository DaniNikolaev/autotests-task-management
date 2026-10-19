from enum import Enum

from faker import Faker


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

    def __str__(self):
        return self.value


class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    def __str__(self):
        return self.value


class Fake:

    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        return self.faker.text()

    def uuid4(self) -> str:
        return self.faker.uuid4()

    def email(self) -> str:
        return self.faker.email()

    def sentence(self) -> str:
        return self.faker.sentence()

    def password(self) -> str:
        return self.faker.password()

    def last_name(self) -> str:
        return self.faker.last_name()

    def first_name(self) -> str:
        return self.faker.first_name()

    def estimated_time(self) -> str:
        return f"{self.integer(1, 30)} hours"

    def integer(self, start: int = 1, end: int = 1000) -> int:
        return self.faker.random_int(start, end)

    def task_status(self) -> str:
        return self.faker.random_element(list(TaskStatus)).value

    def task_priority(self) -> str:
        return self.faker.random_element(list(TaskPriority)).value

    def registration_form(self) -> dict:
        return {"email": self.faker.email(),
                "password": self.faker.password(),
                "first_name": self.faker.first_name(),
                "last_name": self.faker.last_name()}

    def project_form(self) -> dict:
        return {"title": self.faker.sentence(),
                "description": self.faker.text()
                }


fake = Fake(faker=Faker())
