from enum import Enum


class AppRoute(str, Enum):
    REGISTRATION = "./register"
    LOGIN = "./login"
    PROJECTS = "./projects"
    PROFILE = "./profile"
    