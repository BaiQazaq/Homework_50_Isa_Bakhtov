import random


class Cat:
    state = ["Awake", "Sleeping"]
    name = None
    age = None
    sleep = state[0]
    feeling = 0
    feeding = 0


    def get_name(self, name):
        Cat.name = name

    def get_age(self):
        age = random.randint(1, 18)
        Cat.age = age

    def var_image(self):
        if Cat.feeling < 30 and Cat.feeling >= 0:
            img_cat = 'image/cat_level_low.jpeg'
        elif Cat.feeling < 70 and Cat.feeling >= 30:
            img_cat = 'image/cat_level_midle.jpeg'
        elif Cat.feeling >= 70:
            img_cat = 'image/cat_level_high.jpeg'
        return img_cat

    def action_by_cat(self, action):
        action = action
        self.change_sleep(action)
        self.change_feeling(action)
        self.change_feeding(action)

    def change_sleep(self, action):
        if action == 'sleep':
            Cat.sleep = Cat.state[1]

    def change_feeling(self, action):
        if Cat.sleep == Cat.state[1] and action == 'play':
            Cat.feeling -= 5
            Cat.sleep = Cat.state[0]
        elif Cat.sleep == Cat.state[0] and action == 'play':
            angry = random.randint(1, 3)
            if angry == 3:
                Cat.feeling = 0
            else:
                Cat.feeling += 15
        elif action == 'feed' and Cat.sleep == Cat.state[0]:
            if Cat.feeding < 100:
                Cat.feeling += 5
            else:
                Cat.feeling -= 30

    def change_feeding(self, action):
        if Cat.sleep == Cat.state[0] and action == 'feed':
            Cat.feeding += 15
        elif Cat.sleep == Cat.state[0] and action == 'play':
            Cat.feeding -= 10
