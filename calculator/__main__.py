from add import add
from sub import sub

print("For adding type 1")
print("For subtracting type 2")

choice = int(input("Choose 1 and 2 :"))
if choice == 1:
    add()

elif choice == 2:
    sub()

else:
    print("Invalid choice!")