visit_list=['surat','bengaluru','manali','ladakh','kedarnath','meghalaya','chennai','rameshwaram']

print("Original list: ",visit_list,"\n")

#using sorted()
print("Temporarily ascending order",sorted(visit_list),"\n")
print("The list has not changed: ",visit_list,"\n")

#using sorted(reverse)
print("Temporarily in descending order",sorted(visit_list,reverse=True),"\n")
print("The list has not changed: ",visit_list,"\n")

#using reverse
visit_list.reverse()
print("Changing order of the list",visit_list,"\n")
print("The list has changed: ",visit_list,"\n")

#using reverse again
visit_list.reverse()
print("Changing order of the list",visit_list,"\n")
print("The list has changed: ",visit_list,"\n")

#using sort() for alphabetical ascending
visit_list.sort()
print("Order in alphabetical ascending: ",visit_list,"\n")
print("The list has changed",visit_list,"\n")

#using sort() for alphabetical descending
visit_list.sort(reverse=True)
print("Order in alphabetical descending: ",visit_list,"\n")
print("The list has changed",visit_list,"\n")
