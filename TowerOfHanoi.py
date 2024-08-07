def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from Rod",source,"to Rod",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from Rod",source,"to Rod",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         
# Driver code
n = 4
TowerOfHanoi(n,'A','B','C')
