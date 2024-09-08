import os

def auction():
    data = {}
    while True:
        print("Welcome to the secret auction.")
        name = input("What is your name?: ")
        
        while True:
            bid = input("What is your bid?: $")
            
            try:
                bid = float(bid)
            except:
                print("Invalid bid. Must be a number greater than zero.")
            
            if not bid > 0:
                print("Invalid bid. Must be a number greater than zero.")
            else: break
        
        data[name] = bid
        
        while True:
            continueBidding = input("Are there any other bidders? Type 'yes' or 'no'.: ")
            
            if(continueBidding not in ['yes', 'no']):
                print("Invalid choice. Must be 'yes' or 'no'.")
            else: break
        
        if continueBidding == 'no':
            max = -1
            for bidder, bid in data.items():
                if bid > max:
                    max = bid
                    winner = bidder
            print(f"{bidder} won with bid {max}!")
            
            while True:
                isNextAuction = input("Want to do another auction? Type 'yes' or 'no'.")
                
                if(isNextAuction not in ['yes', 'no']):
                    print("Invalid choice. Must be 'yes' or 'no'.")
                else: break
                
            if isNextAuction == 'no':
                break
        
        else:
            os.system('cls')
            
        
auction()
            
        