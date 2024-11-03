def main():
ms = int (input ("Enter the total memory available (in Bytes): "))
bs = int (input ("Enter the block size (in Bytes): "))
nob
S
ms // bs
ef
m.S
nob Ac
bs
n = int (input ("Enter the number of processes: "))
mp
for i in range (n) :
mem req = int (input (f"Enter memory required for process (i t 1) (in Bytes)
mp.append (mem_req)
print ("InNo. of Blocks available in memory:", nob)
print ("InPROCESS\tMEMORY REQUIRED\tALLOCATED\tINTERNAL FRAGMENTATION")
tif =
p=0
for i in range (n)
print (f"fi + 1)\t\t(mp[i])", end="")
if mp[i] > bs:
print ("It\tNO\t\t-
else:
print (f"It\tYES\t\t[bs - mp[il)")
tif += bs - mp[i]
p +=1
if p>= nob:
break
if i <n
1:
-
print ("InMemory is Full, Remaining Processes cannot ba accommodated")
print ("InTotal Internal Fragmentation is", tif)
print ("Total External Fragmentation is", e£)|
if
name
main
main ()


">