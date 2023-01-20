'''
Project Name: Yondu Udonta
Author: Dawson Allen
Due Date: 01/20/2023
Course: CS1400-001

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
'''

def main():
    '''
    Program starts here.
    '''
    try:
        # (1) replace pass with your code
        reavers = int(input("How many Reavers:\n"))
        units = int(input("How many units:\n"))
    except ValueError:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 1 or units < 1:
        print("Enter positive integers for reavers and units.")
        return

    if reavers < 3:
        print("Not enough crew.")
        return

    if units <= 3 * reavers:
        print("Not enough units.")
        return

    # (2) replace pass with your code
    shore_leave = 3 * (reavers - 2)
    units_2 = units - shore_leave

    share_yondu = int(units_2 * 0.13)
    units_3 = units_2 - share_yondu
    share_peter = int(units_3 * 0.11)
    units_4 = units_3 - share_peter

    share_crew = units_4 // reavers
    share_rbf = units_4 - (share_crew * reavers)

    print(f"Yondu's share: {share_yondu + share_crew}")
    print(f"Peter's share: {share_peter + share_crew}")
    print(f"Crew: {share_crew}")
    print(f"RBF: {share_rbf}")

if __name__ == "__main__":
    main()
