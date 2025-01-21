from bintrees import BinaryTree

# Notice how we can use the same identifier to refer to
# two different variables (aka objects). Those objects
# have different types (but _their_ types never change)!
# It does _seem_ like the type of the variable changes,
# but it is really just referring to two different objects,
# each of which have a different type!

fir = "Buckeye Tree"
print(f"The type of `fir`: {type(fir)}")

fir = BinaryTree()
print(f"The type of `fir`: {type(fir)}")