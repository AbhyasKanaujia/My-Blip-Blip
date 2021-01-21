import datetime
from math import floor
from time import strftime
import blipbliphelper


def formattedToday() -> str:
    """get formatted date string for today

    Returns:
        str: "# Wednesday 20<sup>th</sup> January 2021" if today's date
    """
    date = datetime.datetime.now()
    return "# " + date.strftime('%A') + " " + blipbliphelper.getOrdinal(
        int(date.strftime("%d"))) + " " + date.strftime("%B %Y")


def dateToFormattedDate(date) -> str:
    """convert date object to formatted date string

    Args:
        date (datetime): datetime.datetime(2021, 20, 1)

    Returns:
        str: "# Wednesday 20<sup>th</sup> January 2021"
    """
    return "# " + date.strftime('%A') + " " + blipbliphelper.getOrdinal(
        int(date.strftime("%d"))) + " " + date.strftime("%B %Y")


def parseFormattedDate(formattedDate) -> datetime:
    """Convert application specific date to date object

    Args:
        formattedDate (str): '# Wednesday 20<sup>th</sup> January 2021'

    Returns:
        datetime: datetime.datetime(2021, 20, 1)
    """
    formattedDate = formattedDate.replace("<sup>st</sup>", "")
    formattedDate = formattedDate.replace("<sup>nd</sup>", "")
    formattedDate = formattedDate.replace("<sup>rd</sup>", "")
    formattedDate = formattedDate.replace("<sup>th</sup>", "")
    return datetime.datetime.strptime(formattedDate, '# %A %d %B %Y')


def dateToFileName(date) -> str:
    """convert date object to formatted date string for file name

    Args:
        date (datetime): datetime.datetime(2021, 20, 1)

    Returns:
        str: "Blip Blip 20 January 2021"
    """
    return "Blip Blip " + date.strftime("%d %B %Y")


def isFormattedDate(string) -> bool:
    """Check if a string is/not the application stle formatted date. don't forget to strip before checking.

    Args:
        string (str): # Wednesday 20<sup>th</sup> January 2021

    Returns:
        bool: ture or false
    """
    try:
        parseFormattedDate(string)
    except:
        return False
    return True


def formattedTime(date) -> str:
    """formatted time

    Args:
        date (datetime): datetime object to be formatted

    Returns:
        str: 10:54 PM
    """
    return date.strftime('%I:%M %p')


def formattedTimeNow() -> str:
    """formatted current time

    Args:
        date (datetime): datetime object to be formatted

    Returns:
        str: 10:54 PM
    """
    return datetime.datetime.now().strftime('%I:%M %p')


def getLastBlipTime() -> datetime:
    currentTime = datetime.datetime.now()
    return currentTime.replace(minute=floor(currentTime.minute/15)*15)


def getBlipTimeBefore(date) -> datetime:
    return date.replace(minute=floor(date.minute/15)*15)


def getNextBlipTimeAfter(date) -> datetime:
    fifteenPlus = datetime.timedelta(minutes=15)
    date = date + fifteenPlus
    return getBlipTimeBefore(date)


def getFormattedTime(date) -> str:
    return date.strftime('%I:%M %p')
