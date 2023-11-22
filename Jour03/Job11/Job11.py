def time_to_text(minute):
    heures = minute // 60

    minute = minute % 60

    print(heures,"Heures et ", minute,"Minutes")
    
 
time_to_text(125) 

time_to_text(120)

time_to_text(60)

time_to_text(30)


time_to_text(3600)