from abc import ABC, abstractmethod
from typing import TypeVar, List, Generic

T = TypeVar('T')
R = TypeVar('R')


class ResponseBuilder(ABC, Generic[R]):

    @abstractmethod
    def then_return(self, result: R) -> None:
        """
        Sets the behaviour of the mock to return the given response.

        Args:
            result:

        """


class MemberType:
    ARG: str = "arg"
    ATTRIBUTE: str = "attribute"
    RETURN: str = "return"


class MissingHint:

    def __init__(self, path: List[str], member_type: str):
        self.path = path
        self.member_type = member_type

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.member_type == other.member_type and self.path == other.path

    def __repr__(self):
        return "MissingHint(path={path}, member_type={member_type})".format(
            path=self.path,
            member_type=self.member_type
        )


class MissingTypeHintsError(Exception):
    pass


class MockTypeSafetyError(Exception):
    pass


class NoBehaviourSpecifiedError(Exception):
    pass
