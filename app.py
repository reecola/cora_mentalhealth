print("Title of program: mental health bot")
print()
while True:
  description = input("how are you feeling today?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "just miserable":
      feelings_list.append("sad")
      encouragement_list.append("tomorrow will be a better day, cry if you have to it's okay to be vulnerable at times!")
      counter += 1
    if each_word == "lost":
      feelings_list.append("lost")
      encouragement_list.append("that i understand you're going through a tough time now and it's okay to feel lost at times, maybe it's just time to take a rest and focus on yourself!")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think. Think of how far you have come, why can't you go any further? jiayous! You are not alone please don't give up")
      counter += 1
    if each_word == "alone":
      feelings_list.append("alone")
      encouragement_list.append("that you are NOT facing this alone you have people who CARE about YOU we're in this TOGETHER!! Remember that :)")
      counter += 1
    if each_word == "frustrated":
      feelings_list.append("frustrated")
      encouragement_list.append("to keep calm and don't give up! you can do it!")
      counter += 1
    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("to take a deep breath. All will be fine! :)")
      counter += 1
    if each_word == "devastated":
      feelings_list.append("devasted")
      encouragement_list.append("bad times would pass!")
      counter += 1
    if each_word == "useless":
      feelings_list.append("useless")
      encouragement_list.append("don't give up! it is always darkest before dawn!")
      counter += 1
    if each_word == "scared":
      feelings_list.append("scared")
      encouragement_list.append("Im sending you a virtual hug, know you arent alone")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling!")
      counter -= 1
    if each_word == "worried":
      feelings_list.append("worried")
      encouragement_list.append("to chillax for a bit and keep calm!")
      counter += 1
    if each_word == "crazy":
      feelings_list.append("crazy")
      encouragement_list.append("to rest your mind for a while and calm down.")
      counter += 1
    if each_word == "sick":
      feelings_list.append("sick")
      encouragement_list.append("to rest well and you'll soon recover!")
      counter += 1    
      
  if counter == 0:
    
      output = "sorry I don't really understand. please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember "+ encouragement_list[0] + " Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += " " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += " " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + " Hope you feel better :)"

  print()
  print(output)
  print()
