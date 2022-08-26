# title: 
# author: 
# description: 

from earsketch import *

setTempo(120)

# Add Sounds
fitMedia(RD_UK_HOUSE_MAINBEAT_8, 1, 1, 5)
fitMedia(RD_POP_SYNTHBASS_6, 2, 1, 9)
fitMedia(YG_RNB_TAMBOURINE_1, 4, 1, 9)
fitMedia(YG_FUNK_CONGAS_3, 5, 1, 5)
fitMedia(YG_FUNK_HIHAT_2, 6, 5, 9)
fitMedia(RD_POP_TB303LEAD_3, 7, 5, 9)

# Effects fade in
setEffect(2, VOLUME,GAIN, -20, 1, 6, 5)

# Fills
fillA = "0---0-0-00--0000"
fillB = "0--0--0--0--0-0-"
fillC = "--000-00-00-0-00"
makeBeat(OS_SNARE03, 3, 4, fillA)
makeBeat(COMMON_LOVE_DRUMBEAT_1, 3, 8, fillB)
