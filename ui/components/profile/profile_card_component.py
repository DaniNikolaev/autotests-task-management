from playwright.sync_api import Page

from ui.components.base_component import BaseComponent
from ui.elements.Text import Text


class ProfileCardComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.avatar = Text(page, "profile-avatar",
                               "Profile card avatar")
        self.name = Text(page, "profile-name",
                            "Profile card name")
        self.email = Text(page, "profile-email",
                            "Profile card email")
        self.user_id_label = Text(page, "profile-user-id-label",
                                 "Profile card user id label")
        self.user_id = Text(page, "profile-user-id",
                            "Profile card user id")
        self.status = Text(page, "profile-status",
                           "Profile card status")
        self.status_label = Text(page, "profile-status-label",
                                "Profile card status label")
        self.created_at = Text(page, "profile-created",
                               "Profile card created at")
        self.created_label = Text(page, "profile-created-label",
                                 "Profile card created label")
        self.updated_at = Text(page, "profile-updated",
                               "Profile card updated at")
        self.updated_label = Text(page, "profile-updated-label",
                                 "Profile card updated label")

    def check_avatar(self, first_name: str, last_name: str):
        self.avatar.check_visible()
        self.avatar.check_have_text(f"{first_name[0]}{last_name[0]}")

    def check_name(self, first_name: str, last_name: str):
        self.name.check_visible()
        self.name.check_have_text(f"{first_name} {last_name}")

    def check_email(self, email: str):
        self.email.check_visible()
        self.email.check_have_text(email)

    def check_user_id(self, user_id: str):
        self.user_id.check_visible()
        self.user_id_label.check_visible()
        self.user_id.check_have_text(user_id)
        self.user_id_label.check_have_text("ID пользователя")

    def check_status(self, status: str):
        self.status.check_visible()
        self.status_label.check_visible()
        self.status.check_have_text(status)
        self.status_label.check_have_text("Статус аккаунта")

    def check_created_at(self, created_date: str):
        self.created_at.check_visible()
        self.created_label.check_visible()
        self.created_at.check_have_text(created_date)
        self.created_label.check_have_text("Дата регистрации")

    def check_updated_at(self, updated_date: str):
        self.updated_at.check_visible()
        self.updated_label.check_visible()
        self.updated_at.check_have_text(updated_date)
        self.updated_label.check_have_text("Последнее обновление")
