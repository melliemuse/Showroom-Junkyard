# Create an empty set named showroom.
showroom = set()
print(showroom)
# Add four of your favorite car model names to the set.
showroom.update(["Camaro", "Spyder", "Vintage", "Tesla"])
# print(showroom)
# Print the length of your set.
# print(len(showroom))
# Pick one of the items in your show room and add it to the set again.
showroom.add("Tesla")
# Print your showroom. Notice how there's still only one instance of that model in there.
# print(showroom)
# Using update(), add two more car models to your showroom with another set.
fanciful = {"flying car", "delorean"}
showroom.update(fanciful)
# print(showroom)
# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard('Camaro')
print(showroom)

# Acquiring more cars
# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.
junkyard = {"old Prius", "Vintage", "rustbucket", "clunker", "Spyder"}
# Use the intersection method to see which cars exist in both the showroom and that junkyard.
overlap = junkyard.intersection(showroom)
# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.