import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# sphinx_gallery_thumbnail_number = 2

vegetables = ["LPo94 Yr 7", "LPo94 Yr 8", "KS-3 Yr 7", "KS-3 Yr 8", "MYP3", "MYP4", "MPY5",
              "Lpf94 A/GY11 1bc", "Lpf94 B/GY11 2bc", "Lpf94 C/GY11 3bc", "Lpf94 D/GY11 4", "Lpf94 E/GY11 5","IGCSE", "IBST","IBSL", "IBHL/AAHL"]
farmers = ["IEST", "IEGS", "ISSR", "SSHL", "BISS"]

harvest = np.array([[2, 0, 0, 0, 0], #LPo94 Yr 7
                    [2, 0, 0, 0, 0], #LPo94 Yr 8
                    [0, 0, 0, 0, 1], #KS-3 Yr 7
                    [0, 0, 0, 0, 1], #KS-3 Yr 8
                    [0, 0, 2, 0, 0], #MYP3
                    [0, 0, 2, 0, 0], #MYP4
                    [0, 0, 2, 1, 0], #MYP5
                    [0, 6, 1, 2, 0], #Lpf94 A/GY11 1bc
                    [0, 6, 2, 2, 0], #Lpf94 B/GY11 2bc
                    [0, 5, 0, 3, 0], #Lpf94 C/GY11 3bc
                    [0, 5, 0, 0, 0], #Lpf94 D/GY11 4
                    [0, 3, 0, 0, 0], #Lpf94 E/GY11 5
                    [0, 0, 0, 0, 1], #IGCSE
                    [0, 0, 0, 1, 0], #IBST
                    [0, 0, 2, 2, 0], #IBSL
                    [0, 0, 1, 2, 1]]) #IBHL/AAHL


fig, ax = plt.subplots()
im = ax.imshow(harvest, cmap="bone_r")

# We want to show all ticks...
ax.set_xticks(np.arange(len(farmers)))
ax.set_yticks(np.arange(len(vegetables)))
# ... and label them with the respective list entries
ax.set_xticklabels(farmers)
ax.set_yticklabels(vegetables)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Courses Taught (years experience )")
#fig.tight_layout()
#plt.show()

plt.savefig('cv-CoursesTaught.pdf',bbox_inches='tight')