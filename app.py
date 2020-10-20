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
      encouragement_list.append("tomorrow will be a better day, cry if you have to it's okay to be vulnerable at times")
      counter += 1
    if each_word == "lost":
      feelings_list.append("lost")
      encouragement_list.append("i understand that you're going through a tough time now and it's okay to feel lost at times, maybe it's just time to take a rest and focus on yourself")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("you are stronger than you think think of how far you have come, why can't you go any furhter? jiayous! you are not alone please don't give up ")
      counter += 1
    if each_word == "alone":
      feelings_list.append("alone")
      encouragement_list.append("you are NOT facing this alone you have people who CARE about YOU we're in this TOGETHER!! remember that :) ")
      counter += 1
    if each_word == "frustrated":
      feelings_list.append("frustrated")
      encouragement_list.append("keep calm and don't give up! you can do it!")
      counter += 1
    if each_word == "stressed":
      feelings_list.append("stressed")
      encouragement_list.append("Take a deep breath. All will be fine! :)")
      counter += 1
      
  if counter == 0:
    
      output = "sorry I don't really understand. please use different words?"

  elif counter == 1:
    
      output = "and it is okay to feel this way " + feelings_list[0] + ". however, do remember that "+ encouragement_list[0] + "! you got this hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
