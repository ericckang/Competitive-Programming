
#Author: Eric Kang
#It is not ok to share my code anonymously for educational purposes
def BankQueue(n, t, people):
    #create a list of all people along with their departure times
    people_list = []
    for time, money_list in people.items():
        for money in money_list:
            people_list.append([money, time])

    #sort the list
    for i in range(len(people_list)):
        for j in range(i + 1, len(people_list)):
            # If the money of j-th person is greater than i-th person, swap them
            if people_list[j][0] > people_list[i][0]:
                people_list[i], people_list[j] = people_list[j], people_list[i]

    #create a list to track the time slots that have been used
    used_time_slots = [False] * t

    total_money = 0

    #loop through each person in the sorted list
    for money, time in people_list:
        #find the latest available time slot before the person's departure time
        for i in range(time, -1, -1):
            if not used_time_slots[i]:
                used_time_slots[i] = True
                total_money += money
                break

    return total_money

def main():
    expr = input().split()
    map = {}
    n = int (expr[0])
    t = int (expr[1])

    for i in range(0,n):
        expr = input().split()
        if int(expr[1]) in map:
            map[int (expr[1])].append(int (expr[0]))
        else:
            map[int (expr[1])] = [int(expr[0])]

    output = BankQueue(n,t,map)
    print(output)


if __name__ == "__main__":
    main()
