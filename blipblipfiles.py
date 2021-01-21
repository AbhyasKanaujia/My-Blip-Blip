from datetime import datetime
from shutil import copyfile
import blipbliptime
import os
import blipblipcontent


def archiveREADME():
    """Move README.md to new file with proper name and leave current README with todays date. Assuming the file exists.
    """
    file = open('README.md', 'rt', encoding='utf8')
    # should get # Monday 18th Jan 2021
    fileDate = blipbliptime.parseFormattedDate(file.readline().strip())
    file.close()
    archiveFileName = blipbliptime.dateToFileName(fileDate) + ".md"
    copyfile('README.md', archiveFileName)
    createREADME(datetime.now(),
                 blipblipcontent.extractTargets(archiveFileName))


def createREADME(date, targets="| | | | | | |"):
    """Create new blank README with formatted date provided

    Args:
        formattedToday (date): date object
    """
    file = open("README.md", "wt", encoding='utf8')
    READMEcontent = blipbliptime.dateToFormattedDate(date) + "\n\n"
    READMEcontent += blipblipcontent.getSubtitleTable(date) + "\n\n"
    READMEcontent += blipblipcontent.getTargets(targets) + "\n\n"
    READMEcontent += blipblipcontent.generateBlipBlip(date) + "\n"
    file.write(READMEcontent)
    file.close()


def setupREADME():
    """if README if not exist or not in right format then create. if readme exists and not current then archive.
    """
    if os.path.exists("README.md"):  # README exists
        file = open('README.md', 'rt', encoding='utf8')
        readmeDate = file.readline().strip()
        file.close()
        if not blipbliptime.isFormattedDate(readmeDate):  # wrong README exists
            createREADME(datetime.now())
        elif readmeDate != blipbliptime.formattedToday():  # old README exists
            archiveREADME()
    else:  # README does not exists
        createREADME(datetime.now())
