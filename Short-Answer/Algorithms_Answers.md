#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n): This is also a linear complexity as there is one while loop, and it will run longer as n increases.


b) O(n^2): There is a for loop running through n, with a while loop that also is comparing each and every n. As n get's higher, the runtime will take longer as it has two n's to calculate everytime.


c) O(n): This is a linear complexity as there is one for loop that is looking through n and equal to the size of n, as well as adding a count each time. 

## Exercise II

Building stories = n
egg = e
floor = f

<!-- Pseudocode below, Assuming someone would have to decide if it broke, or we had calculations for how much pressure and egg could take in relation to the force off the egg hitting the group from a particular floor. In a sense, for every floor (f) in the (n)-story building you would drop the egg (e). You would start at the first floor as that is that absolute minimum force the egg would recieve when dropped. If the egg is not broken, continue moving up. Else, record and return the current floor that the egg broke on. This way, only one egg would break before you discover which floor it can not be dropped from. This would be a linear complexity, O(n) because the for loop will continue as many times as there are floors in nth-story building. -->

<!-- Start at first floor and move up -->
for f in range(0, n, 1):
    <!-- Egg broken ? -->
    if e is True:
        return f





