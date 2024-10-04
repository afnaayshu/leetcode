'''
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.
Note that you do not have any change in hand at first.
Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
'''
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0  # Counter for $5 bills
        ten = 0   # Counter for $10 bills

        for bill in bills:
            if bill == 5:
                five += 1  # Simply collect $5, no change needed
                
            elif bill == 10:
                if five > 0:  # We need to give one $5 as change
                    five -= 1
                    ten += 1  # Collect the $10 bill
                else:
                    return False  # No $5 to give as change
                
            elif bill == 20:
                # Prefer to give one $10 and one $5 as change if possible
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                elif five >= 3:  # Otherwise, give three $5 bills as change
                    five -= 3
                else:
                    return False  # Not enough change to give back $15

        return True  # If we successfully provided change for all customers
