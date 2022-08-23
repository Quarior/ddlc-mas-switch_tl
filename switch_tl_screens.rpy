################################################################################
## Initialization
################################################################################

init offset = -1

################################################################################
## Screen Languages
################################################################################

screen switch_tl_screen():
    vbox:

        hbox:
            box_wrap True

#begin language_picker
            ## Additional vboxes of type "radio_pref" or "check_pref" can be
            ## added here, to add additional creator-defined preferences.

            vbox:
                style_prefix "radio"
                label _("Language")

                textbutton "English" text_font "DejaVuSans.ttf" action Language(None)
                textbutton "Français" text_font "DejaVuSans.ttf" action Language("french")
#end language_picker