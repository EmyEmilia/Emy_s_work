lucky_number = "One"
guess_number = ""
guess_count= 0
guess_limit= 3
out_of_guesses= False
while guess_number != lucky_number and not(out_of_guesses):
      if guess_count<guess_limit:
            guess_number = input("Choose lucky number: ")
            guess_count+=1
      else:
            out_of_guesses= True
            print("Out of guesses")

      if guess_number=="one":
            print("You win!")