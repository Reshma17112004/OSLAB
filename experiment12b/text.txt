def main():

Window

ms = int(input ("Enter the total memory available (in Bytes): "))

temp = ms

mp = []

n = 0

ch = 'y'

while ch.lower() = 'y':

n += 1

mem_req = int(input(f"\nEnter memory required for process (n) (in Bytes): ")) mp.append(mem_req)

if mem_req <= temp:

print(f"\nMemory is allocated for Process (n)")

temp mem_req

else:

print("\nMemory is Full")

n = 1

break

ch = input("\nDo you want to continue (y/n): ")

print("\n\nTotal Memory Available:", ms)

("\nPROCESS\t\tMEMORY ALLOCATED")

for i in range(n):

print (f"[i+1}\t\t{mp[i]}")

print("\n\nTotal Memory Allocated is", ms temp)

print("Total External Fragmentation is", temp)

if name main() main":