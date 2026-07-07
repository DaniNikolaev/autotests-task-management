from enum import Enum


class APIRoutes(str, Enum):
    AUTHENTICATION = "/api/v1/authentication"
    USERS = "/api/v1/users"
    PROJECTS = "/api/v1/projects"
    TASKS = "/api/v1/tasks"
    ATTACHMENTS = "/api/v1/attachments"
    COMMENTS = "/api/v1/comments"

    def __str__(self):
        return self.value
