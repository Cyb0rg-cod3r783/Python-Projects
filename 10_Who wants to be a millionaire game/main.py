# Add some random questions you which want to ask. You can add as many as you want
questions = [
["Who is Shah Rukh Khan ?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 2],
["Who is the Prime Minister of India?", "Pandit Jawaharlal Nehru", "Baba Saheb Ambedkar", "Narendra Modi", "Harshad Mehta", 3],
["Who was the first person to step on the moon?", "Neil Armstrong", "Sunita Williams", "Steve Jobs", "Bill Gates",1],
["Where is Taj Mahal located?", "Delhi", "Mumbai", "Banglore", "Karnataka", 1],
["In which country is the Silicon Valley located", "America", "Germany", "China", "France", 1],
["Where is the fastest land animal?", "Fox", "Wolf", "Tiger", "Cheetha",4],
["Which is the largest country in the world?", "America", "China", "India", "Russia",4],
["Which is the country with the highes population in the world?", "America", "India", "China", "Russia",2 ]
]


sum = 0 
i = 0

# Use loop  for iterating through all the questions.
for question in questions:
    print(question[0])
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # check whether the answer is correct or not

    prizes = [10000, 20000, 40000, 80000, 200000, 1000000, 3000000, 6000000]
    
    ans = int(input("Enter 1 if you want to select 'a'\nEnter 2 if you want to select 'b'\nEnter 3 if you want to select 'c'\nEnter 4 if you want to select 'd'\nEnter your answer: "))
    
    # Condition Statement : Check whether the answer selected by the player is equal to the actual answer or not.
    if(question[5] == ans):
        print("Your entered the correct answer\n\n")
        sum = sum + prizes[i]
        print(f"You won $ {prizes[i]}")
        print(f"Total amount you won : $ {sum}") # adds the prize to the total amount won.

        choice = input("Do you want to continue? : ").lower()
        if(choice == 'yes'):
            continue
        elif(choice == "no"):
            print(f"Congratulations!, You won $ {sum}")
    else:
        print(f"You entered the wrong answer, the correct answer was {question[5]}\n\n")
        break
    i += 1 # for adding the prize to the total amount won.

