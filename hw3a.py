# Your name: J. Wilton
# Your student id: 78299051
# Your email:wilton@umich.edu  
# List who you have worked with on this homework: No one
# import the random module for use in this program
import random
# Create the class Animal_Fact_Generator
class Animal_Fact_Generator:
    
    def __init__(self, fact_list, animal_list, fact_history_list=[]):
        self.fact_list = fact_history_list
        self.animal_list = animal_list
        self.fact_history_list=fact_history_list

    def __str__(self, animal_list):
        return(str(self.animal_list))

    def get_fact_for_animal(self, animal_name):
        if animal_name in self.animal_list:
            return self.animal_list.index(animal_name)
        else:
            return("Sorry! I do not have any facts for" + animal_name)

    def random_fact(self):
            lenlist = len(self.fact_list)
            index= random.randint(0, lenlist-1)
            self.fact_history_list.append(index)
            return(self.fact_list[index]+ " - "+ self.animal_list[index]     

    def get_fact_for_animal(self, animal_name):
        if animal_name in self.animal_list:
            return self.animal_list.index(animal_name)
        else:
            return("Sorry! I do not have any facts for" + animal_name)

    def print_history(self):
        for item in fact_history_list:
            print(fact_list[fact_history_list] +" - "+ animal[fact_history_list])


    # EXTRA POINTS
    # create the generate_n_facts method
    # it takes as input:
    #    a number, n. Ex: 200
    # it generates a random fact n times
    # then returns the index and length of the longest consecutive run for an animal index
    # A run is a repetition of the same number consecutively in a list.
    # Ex: If 10 facts generated are [1,5,6,3,2,4,1,4,4,4] then three 4's is the longest run
    # hence the function should return "longest run was length of 3 for index 4"
    #def generate_n_facts(self, num):
    #    for n in range (num):
    #        random_fact()
    #    longeststreak = 0
    #    longeststreaker = 0
    #    for factnum in fact_history_list:
    #        if factnum == fact_history_list[factnum+1]:
    #            longeststreak +=1
    #            longeststreaker=factnum




def main():
    # You are welcome to replace the facts and names with your favorite facts and animals
     fact_list = ["These animals are the only animals that can't jump.", \
     "This animal's tail contains nearly 10 percent of all the bones in its body.", \
     "This animal can go for more than a week without eating.", \
     "This animal's heart weighs about 25 pounds.", \
     "This animal eats half the day.", \
     "These animals are the only big cats that can't roar."]

     animal_list = ["elephant", "cat", "wolf", "giraffe", "panda", "tiger"]

     print("Testing the first animal_fact_generator:")
     fact_bot = Animal_Fact_Generator(fact_list, animal_list)
     print("\nGenerating a random fact")
     print("\nfact : " + fact_bot.random_fact())
     print("\nTesting __str__ method")
     print(fact_bot.__str__())
     print("\nTesting that it can get fact for given animal : panda")
     print(fact_bot.get_fact_for_animal("panda"))
     print("\nPrinting the full history:")
     fact_bot.print_history()

     print("\n===================================================================================================\n")

    #Create another fact-generator
     print("Testing the second animal_fact_generator:")
     fact_bot2 = Animal_Fact_Generator(fact_list, animal_list)

     print("\nTesting when no facts have been generated yet")
     print(fact_bot2.print_history())

     print("\nGetting a cat fact")
     print("\nfact : " + fact_bot.get_fact_for_animal("cat"))

     print("\nGetting a dog fact")
     print("\nfact : " + fact_bot.get_fact_for_animal("dog"))

     print("\nGenerating five facts randomly")
     for x in range(5):
         print("fact : " + fact_bot2.random_fact())
     print("\nPrinting the full history:")
     fact_bot2.print_history()

    #EXTRA POINTS
    #Uncomment the lines below if you attempt the extra credit!
     print("\nTesting generate_n_facts method with 200 facts")
     print(fact_bot2.generate_n_facts(200))


# only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    main()