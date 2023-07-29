"""A class representing a StopWatch.

This module defines the StopWatch ADT, which stores information and supports 
operations relevant to logic starting and stopping a stopwatch.

Typical usage example:

  stopwatch = StopWatch()
  stopwatch.start()
  stopwatch.stop()
"""

from datetime import datetime


class StopWatch:
    def __init__(self) -> None:
        self.__started : bool = False
        "Whether the StopWatch has started."
        self.__stopped : bool = False
        "Whether the StopWatch has stopped."
        self.__start_time : datetime = None
        "The start date and time of the StopWatch"
        self.__stop_time : datetime = None
        "The stop date and time of the StopWatch"
        return

    def start(self) -> None:
        """Starts the StopWatch."""
        if self.__started:
            print("Error: StopWatch has already been started.")
            return

        self.__started = True
        self.__start_time = datetime.now()
        return

    def stop(self) -> None:
        """Stops the StopWatch."""
        if not self.__started:
            print("Error: Cannot stop StopWatch that has not been started.")
            return
        if self.__stopped:
            print("Error: StopWatch has already been stopped.")
            return

        self.__stopped = True
        self.__stop_time = datetime.now()
        return

    def __str__(self) -> str:
        if self.__started and self.__stopped:
            return f"{self.__stop_time - self.__start_time}"
        if self.__started:
            return f"{datetime.now() - self.__start_time}"
        return "StopWatch has not yet been started."


def main() -> None:
    stopwatch = StopWatch()
    print(stopwatch)
    stopwatch.start()
    print(stopwatch)
    stopwatch.stop()
    print(stopwatch)
    return


if __name__ == "__main__":
    main()
