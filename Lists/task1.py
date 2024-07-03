my_list = ["apple", "peach", "watermelon"];

print(my_list[1]);

my_list[2] = "grape";

my_list.append("strawberry");

more_fruits = ["kiwi", "pineapple"];

#my_list += more_fruits това попринцип е по-бързо
my_list.extend(more_fruits);

print(my_list)
sliced_list = my_list[1:3:1]
print(sliced_list)

print(len(my_list))

my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)