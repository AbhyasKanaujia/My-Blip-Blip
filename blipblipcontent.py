from blipbliptime import formattedTime, formattedTimeNow, getFormattedTime, getLastBlipTime, getNextBlipTimeAfter
from datetime import datetime

################## SUBTITLE TABLE ##################


def getSubtitleTable(date) -> str:
    """get subtitle section contents

    Args:
        date (datetime object): date time object

    Returns:
        str: formatted content for subtitle
    """
    return """| Start of the day | Weeks until NIMCET |
| ---------------- | -----------------: |
| {time} | {weeks} weeks |""".format(time=formattedTimeNow(), weeks=round((datetime(2021, 5, 21) - date).days/7, 1))
# s = "This is an {example} with {vars}".format(vars="variables", example="example")

################## TARGET TABLE ##################


def getTargets(targets) -> str:
    """Provide list of targets to generate formatted targets section

    Args:
        targets (string): list of targets extracted from previous file

    Returns:
        str: formatted table with heading and table for target section
    """
    return"""## Target
|  |Category|      |Task| Estimated Time | Actual Time |
| - | -: | - | - | - | - |
{previousTargets}""".format(previousTargets=targets)


def extractTargets(file) -> str:
    """Extract incomplete targets from a given blip blip file

    Args:
        file (file path): file from wich to extract

    Returns:
        str: formatted and numbered table of incompltetd target in a string
    """
    file = open(file, 'r', encoding='utf8')
    previousTargets = file.readlines()
    file.close()
    # HARDCODE: line after ## Target = 10
    line = 10
    targets = ""
    number = 1
    while previousTargets[line].strip() != "":
        if isIncomplete(previousTargets[line]):
            previousTargets[line] = addTargetNumber(
                previousTargets[line], number)
            targets += previousTargets[line]
            number += 1
        line += 1
    if number == 1:
        targets = "|||||||"
    return targets


def isIncomplete(target) -> bool:
    """check if a given target is complete or not by searching for ✅ in 3rd column

    Args:
        target (str): target row

    Returns:
        bool:
    """
    targetPropeties = target.split("|")
    if '✅' in targetPropeties[3]:
        return False
    return True


def addTargetNumber(target, number) -> str:
    """add given number to 1st column of target row

    Args:
        target (str): target row with/without number
        number (int): number to be assigned

    Returns:
        str: formatted and numbered row of target in a string
    """
    targetPropeties = target.split("|")
    targetPropeties[1] = str(number)
    return " | ".join(targetPropeties)

################## BLIP BLIP TABLE ##################


def generateBlipBlip(date) -> str:
    """generate blip blip table at 15 minutes inteval

    Args:
        date (datetime): date and time object of now

    Returns:
        str: formatted table for blip blip
    """
    table = """## Blip Blip

| |Time|Progress| Achievement   | |
| - | - | - | - |
"""
    time = getLastBlipTime()
    number = 1
    while time.date().day == datetime.now().date().day:
        row = "| " + str(number) + " | " + \
            getFormattedTime(time) + " | | |"
        time = getNextBlipTimeAfter(time)
        number += 1
        table += row + "\n"
    return table
