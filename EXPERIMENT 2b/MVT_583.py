def main():
    ms = int(input("Enter the total memory available (in Bytes) -- "))
    temp = ms  # Temporary variable to keep track of available memory

    mp = []  # List to store memory required for each process
    n = 0    # Number of processes
    ch = 'y' # Variable to control the loop

    while ch == 'y':
        n += 1
        memory_required = int(input(f"\nEnter memory required for process {n} (in Bytes) -- "))
        if memory_required <= temp:
            print(f"\nMemory is allocated for Process {n}")
            mp.append(memory_required)
            temp -= memory_required  # Update remaining memory
        else:
            print("\nMemory is Full")
            break
        ch = input("\nDo you want to continue(y/n) -- ").lower()

    print(f"\n\nTotal Memory Available -- {ms}")
    print("\n\tPROCESS\t\tMEMORY ALLOCATED")
    for i in range(n):
        print(f"\t{i+1}\t\t{mp[i]}")

    print(f"\nTotal Memory Allocated is {ms - temp}")
    print(f"Total External Fragmentation is {temp}")

if __name__ == "__main__":
    main()
