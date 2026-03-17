import threading
import time

def cook_dish(dish_name, cook_time):
    print(f" Chef started cooking: {dish_name}")
    time.sleep(cook_time)  
    print(f" {dish_name} is READY!")

t1 = threading.Thread(target=cook_dish, args=("Pasta", 3))
t2 = threading.Thread(target=cook_dish, args=("Garlic Bread", 2))

t1.start()
t2.start()

t1.join()
t2.join()

print("️ All dishes served! Enjoy your meal.")
