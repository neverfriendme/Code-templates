List1 = "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"
List2 = "blooded", "banana", "dolphin", "breath", "stream","facade","Norses","Nurses","engineer","feared","happiness","growth","solar_system","lunatic","cooled","chilled","filled","Batman","Superman","Shovel"
List3 = "!", "@", ",", ".", "#", "/", "*","-", "—", "~", "|","?", ":", ";","%", "^", "$", "&","`","+","=","_"

generatelist1 = random.choice(List1)
generatelist2 = random.choice(List2)
generatelist3 = random.choice(List3)

print(f"{generatelist1}{generatelist2}{generatelist3}")
