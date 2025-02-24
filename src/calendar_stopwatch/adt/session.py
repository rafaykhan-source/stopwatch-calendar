"""A class representing a Session.

This module defines the Session ADT, which stores information and supports
operations relevant to logic associated utilizing a StopWatch and information
of why a client needs the use the stopwatch.

Typical usage example:

  session = Session()
  session.begin()
  session.end()
"""

import logging
import time
from datetime import datetime

from adt.stopwatch import StopWatch

logger = logging.getLogger("ADTs")


class Session:
    """This class wraps information pertaining to a stopwatch session.

    Attributes:
        title (str): Name of the session.
        description (str): Additional details of the session.
    """

    def __init__(self, title: str, description: str) -> None:
        """Instantiates the session.

        Args:
            title (str): Name of the session.
            description (str): Additional details of the session.
        """
        self.title: str = title
        "A general title for the timed session."
        self.description: str = description
        "A description for the session."
        self.__stopwatch: StopWatch = StopWatch()
        "A stopwatch for the session."
        self.__began: bool = False
        "Whether the session has begun."
        self.__ended: bool = False
        "Whether the session has ended."

    def begin(self) -> None:
        """Begins the Session."""
        if self.__began:
            logger.error("Error: Cannot begin session that has already begun.")
            return
        self.__began = True
        self.__stopwatch.start()
        logger.info("Session has begun.")
        return

    def end(self) -> None:
        """Ends the session."""
        if not self.__began:
            logger.error("Error: Cannot end session that has not yet begun.")
            return
        if self.__ended:
            logger.error("Error: Cannot end session that has already ended.")
            return
        self.__ended = True
        self.__stopwatch.stop()
        logger.info("Session has ended.")
        return

    def get_duration(self) -> str:
        """Returns the duration of the session.

        Returns:
            str: duration of the session
        """
        return str(self.__stopwatch)

    def is_complete(self) -> bool:
        """Returns whether session is complete.

        Returns:
            bool: Whether session is completed.
        """
        return self.__began and self.__ended

    def get_time_range(self) -> tuple[datetime | None, datetime | None]:
        """Returns the start and end datetimes if complete.

        Returns None if session is incomplete.

        Returns:
            tuple[datetime]: start and end datetimes
        """
        if not self.is_complete():
            logger.error("Error: Session is incomplete.")
            return (None, None)
        return (self.__stopwatch.start_time, self.__stopwatch.stop_time)

    def __str__(self) -> str:
        """Returns a string representation of the session.

        Returns:
            str: Session's information.
        """
        return f"""
Title: {self.title}
Description: {self.description}
Duration: {self.__stopwatch}
"""


def main() -> None:
    """Unit Testing."""
    session = Session(
        title="Marshmallow Development",
        description="Doing Intensive Refactoring",
    )
    session.end()
    print(session)
    session.begin()
    print(session)
    time.sleep(5)
    session.end()
    print(session)
    session.begin()
    session.end()
    print(str(session.get_time_range()) + ": " + session.get_duration())


if __name__ == "__main__":
    main()
