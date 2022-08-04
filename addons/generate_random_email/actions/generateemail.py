"""This module contains the GenerateEmail proxy action class."""
from src.testproject.classes import ProxyDescriptor
from src.testproject.sdk.addons import ActionProxy


class GenerateEmail(ActionProxy):
    def __init__(self, emailTag: str, domain: str = "gmail.com"):
        super().__init__()
        self.proxydescriptor = ProxyDescriptor(
            guid="9u79u5Uk4U-vi_Cc3S-c3g",
            classname="main.addon.GenerateEmail"
        )
        self.emailTag = emailTag
        self.domain = domain
        self.generatedEmail = None
