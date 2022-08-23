################################################################################
## Create "screens.rpy"
################################################################################

init -1500 python:
    #Code for python get current directory:
    #importing the os module
    import os

    #to get the current working directory
    directory = config.gamedir # Don't know what to do to get the directory of THIS file

    #to get the DDLC directory
    gameDir = config.gamedir

    #to get tl folders
    pathTl = os.path.join(gameDir,"tl")

    if os.path.exists(pathTl) == False:
        os.mkdir(pathTl)

    tlFolders = []
    for nameTl in os.listdir(pathTl):
        tlFolders.append(nameTl)

    # Start to create the output file "switch_tl_screens.rpy"
    fileScreens = os.path.join(directory,"switch_tl_screens.rpy")
    if directory == config.gamedir:
        fileScreens = os.path.join(gameDir,"submods","switch_tl","switch_tl_screens.rpy")

    fS = open(fileScreens, "w")
    fS.write("################################################################################\n")
    fS.write("## Initialization\n")
    fS.write("################################################################################\n\n")


    fS.write("init offset = -1\n\n")


    fS.write("################################################################################\n")
    fS.write("## Screen Languages\n")
    fS.write("################################################################################\n\n")


    fS.write("screen switch_tl_screen():\n")

    fS.write("    vbox:\n\n")

    fS.write("        hbox:\n")
    fS.write("            box_wrap True\n\n")

    fS.write("#begin language_picker\n")
    fS.write("            ## Additional vboxes of type \"radio_pref\" or \"check_pref\" can be\n")
    fS.write("            ## added here, to add additional creator-defined preferences.\n\n")

    fS.write("            vbox:\n")
    fS.write("                style_prefix \"radio\"\n")
    fS.write("                label _(\"Language\")\n\n")

    fS.write("                textbutton \"English\" text_font \"DejaVuSans.ttf\" action Language(None)\n")

    # For each translation found, create the choice to switch language.
    for tlf in tlFolders:
        trans = tlf
        tf = "DejaVuSans.ttf"
        pathTlA = os.path.join(pathTl,tlf)
        fileInfo = os.path.join(pathTlA,"tl.txt")
        if os.path.exists(fileInfo) == True:
            FITl = open(fileInfo, 'r')
            toRead = FITl.readlines()
            FITl.close()
            toRead = toRead[1].split(";")
            trans = toRead[0]
            tf = toRead[1]
        else:
            toWrite = ["#translation;text_font# # Don't delete this line\n", trans + ";" + tf]
            FITl = open(fileInfo, 'w')
            FITl.writelines(toWrite)
            FITl.close()
        fS.write("                textbutton \"{}\" text_font \"{}\" action Language(\"{}\")\n".format(trans,tf,tlf))

    fS.write("#end language_picker")
    fS.close()
