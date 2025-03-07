def main():
   ted1 = input("Please enter your favorite movie: ")
   ted2= input("Please enter the of your favorite movie: ")
   ted3= input("where did the star of your favorite movie live: ")
   ted4= int(input("how many times did your watch your favorite movie: "))

   print(f"your favorite movie is {ted1}, staring {ted2}. ")
   print(f"{ted2} live in {ted3}")
   print(f"the next time that you watch{ted1},you will have watched it {ted4 + 1} times.")



if __name__ == '__main__':
    main()
