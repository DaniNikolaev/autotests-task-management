import allure
from httpx import Client, Response

from api.clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from api.clients.projects.projects_schema import CreateProjectRequestSchema, UpdateProjectRequestSchema, \
    CreateProjectResponseSchema
from api.clients.tasks.tasks_schema import CreateTaskRequestSchema, CreateTaskResponseSchema
from tools.api.routes import APIRoutes


class ProjectsClient:
    def __init__(self, client: Client):
        self.client = client

    @allure.step("Get projects")
    def get_projects_api(self) -> Response:
        return self.client.get(APIRoutes.PROJECTS)

    @allure.step("Create project")
    def create_project_api(self, request: CreateProjectRequestSchema) -> Response:
        return self.client.post(APIRoutes.PROJECTS, json=request.model_dump(by_alias=True))

    def create_project(self, request: CreateProjectRequestSchema) -> CreateProjectResponseSchema:
        response = self.create_project_api(request)
        return CreateProjectResponseSchema.model_validate_json(response.text)

    @allure.step("Get project by id {project_id}")
    def get_project_api(self, project_id: str) -> Response:
        return self.client.get(f"{APIRoutes.PROJECTS}/{project_id}")

    @allure.step("Update project by id {project_id}")
    def update_project_api(self, project_id: str, request: UpdateProjectRequestSchema) -> Response:
        return self.client.patch(f"{APIRoutes.PROJECTS}/{project_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete project by id {project_id}")
    def delete_project_api(self, project_id: str) -> Response:
        return self.client.delete(f"{APIRoutes.PROJECTS}/{project_id}")

    @allure.step("Get project tasks")
    def get_project_tasks_api(self, project_id: str,
                              status: str | None = None,
                              priority: str | None = None) -> Response:
        params = {}
        if status:
            params["status"] = status
        if priority:
            params["priority"] = priority
        return self.client.get(f"{APIRoutes.PROJECTS}/{project_id}/tasks", params=params)

    @allure.step("Create project task")
    def create_project_task_api(self, project_id: str,
                                request: CreateTaskRequestSchema) -> Response:
        return self.client.post(f"{APIRoutes.PROJECTS}/{project_id}/tasks", json=request.model_dump(by_alias=True))

    def create_project_task(self, project_id: str,
                            request: CreateTaskRequestSchema) -> CreateTaskResponseSchema:
        response = self.create_project_task_api(project_id, request)
        return CreateTaskResponseSchema.model_validate_json(response.text)


def get_projects_client(authentication_user: AuthenticationUserSchema):
    return ProjectsClient(client=get_private_http_client(authentication_user))
