from .actions import GenerateEmail


class GenerateRandomEmail:
    @staticmethod
    def generateemail(emailTag: str, domain: str) -> GenerateEmail:
        """Run Random Email Generator."""
        return GenerateEmail(emailTag, domain)
