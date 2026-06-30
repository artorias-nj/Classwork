import os

#collecting inputs and variables
fn=input("Please enter your first name: ")
ln=input("please enter your last name: ")
street=input("Please enter the street you live on: ")
city=input("Please enter the city you live in: ")
state=input("Please enter the state you live in: ")
zipc=input("Please enter your zip code: ")
smr=input("Please enter the start meter reading: ")
emr=input("Please enter the end meter reading: ")
try:
    smr=int(smr)
    emr=int(emr)
except:
    print("Please use digits for the meter reaings")
    quit()
ppkwh=.1125
fmdf=23.05
frc=11.9
st=.065

#calculations

mec=emr-smr
dec=mec/30
ope=mec*0.20
mpe=mec*.45
epe=mec*0.8
dope=ope/24
dmpe=mpe/24
depe=epe/24
opec=(ope*0.17)
mpec=(mpe*0.11)
epec=(epe*.08)
dopec=(dope*0.17)
dmpec=(dmpe*0.11)
depec=(depe*.08)
mecp=opec+mpec+epec
dmecp=dopec+dmpec+depec
bb4t=mecp+frc+fmdf
bill=bb4t*(1+st)
tax=bill-bb4t

#Presentation

os.system("cls")
print("                     Name: Noah Jones")
print("                     College Name: Adrian College")
print("")

#Bill

print("                     Electricity Bill")
print("Name:     "+fn+(" ")+ln)
print("Adress:   "+street)
print("          "+city+(", ")+state+(", ")+zipc)
print("Start Meter Reading: "+str(smr))
print("End Meter Reading: "+str(emr))
print("Monthly Electricity consumption:  "+str(mec)+(" KWh"))
print("Daily Electricity consumption:    "+str('%.2f'%dec)+(" KWh"))
print("")
print("Monthly electricity consumption price:                   $"+str('%.2f'%mecp))
print("Fixed delivery fee:                                      $"+str(fmdf))
print("Regulatory Charge:                                       $"+str(frc))
print("Toatal electricity price:                                $"+str('%.2f'%bb4t))
print("Tax (6.5%):                                              $"+str('%.2f'%tax))
print("Total Actual Electricity Charges:                        $"+str('%.2f'%bill))

#detailed monthly consumption

print("                     Detailed Monthly electricity consumption")
print("On peak:     07:00 AM - 12:00 PM- consumption = "+str('%.2f'%ope)+":     $"+str('%.2f'%opec))
print("Mid Peak:    12:01 PM - 07:00 PM- consumption = "+str('%.2f'%mpe)+":     $"+str('%.2f'%mpec))
print("Off Peak:    07:01 PM - 06:59 AM- consumption = "+str('%.2f'%epe)+":     $"+str('%.2f'%epec))
print("Average Monthly Consumption                                 $"+str('%.2f'%mecp))
print("")

#average daily consumption

print("                     Average Daily Electricity Consumption")
print("On peak:     07:00 AM - 12:00 PM- consumption = "+str('%.2f'%dope)+":     $"+str('%.2f'%dopec))
print("Mid Peak:    12:01 PM - 07:00 PM- consumption = "+str('%.2f'%dmpe)+":     $"+str('%.2f'%dmpec))
print("Off Peak:    07:01 PM - 06:59 AM- consumption = "+str('%.2f'%depe)+":     $"+str('%.2f'%depec))
print("Average Daily Consumption                                  $"+str('%.2f'%dmecp))

