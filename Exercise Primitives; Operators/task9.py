#name, age, city, favorite_color, and hobby.

print("Insert name:", end="");
name = input();
print("Insert age:", end="");
age = int(input());
print("Insert favorite color:", end="");
favorite_color = input();
print("Insert hobby:", end="");
hobby = input();

print("Your name is {name},\nyour age is {age},\n your favorite color is {favorite_color},\nyour hobby is {hobby}".format(name= name, age = age, favorite_color = favorite_color, hobby = hobby));