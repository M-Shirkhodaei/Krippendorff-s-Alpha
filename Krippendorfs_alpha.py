import krippendorff
import numpy as np
#Matrix = [[0,0,1,1,1,2,1,1,1,0,0,0,2,1,2,1,3,2,0,0,3,1,1,2,0,0,1,2,0,2],[0,0,1,1,1,2,1,1,1,0,0,1,2,1,2,1,2,2,0,0,3,1,1,2,0,0,1,2,1,3]]
#Matrix is intercoder matrix
Matrix = eval(input("add your intercoder matrix:"))
DT = input('add your level of measurement(nominal, ordinal, interval or ratio)')
if DT =="nominal":
    alpha = krippendorff.alpha(reliability_data=Matrix,level_of_measurement="nominal")
elif DT == "ordinal":
    alpha = krippendorff.alpha(reliability_data=Matrix,level_of_measurement="ordinal")
elif DT == "interval":
    alpha = krippendorff.alpha(reliability_data=Matrix,level_of_measurement="interval")
elif DT == "ratio":
    alpha = krippendorff.alpha(reliability_data=Matrix,level_of_measurement="ratio")
print(alpha)
if alpha >= 0.8:
    print("you can rely on this variables (Krippendorff, 2004:241).")
elif alpha >= 0.667 and alpha < 0.8:
    print("Consider this variables only for drawingtentative conclusions (Krippendorff, 2004:241).")
elif alpha < 0.667:
    print("you can't rely on this variables (Krippendorff, 2004).")
input("say any thing to close:")
