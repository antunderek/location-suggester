#! /usr/bin/env/python3

class Points:
    def __init__(self, business=0, adventure=0, family=0, casual=0):
        self.business = business
        self.adventure = adventure
        self.family = family
        self.casual = casual

    def update_points(self, points):
        self.business += points.business
        self.adventure += points.adventure
        self.family += points.family
        self.casual += points.casual
        self.limit_points()

    def limit_points(self):
        for item in self.__dict__:
            if self.__dict__[item] > 100:
                self.__dict__[item] = 100


class User(Points):
    # Ask user for information and update user points
    def set_user_information(self, questions):
        for question_index in questions:
            while True:
                print('\n')
                print(questions[question_index]['question'])
                for answer_index in questions[question_index]['answers']:
                    print('\t', answer_index, questions[question_index]['answers'][answer_index]['answer'])

                try:
                    user_choice = input(f"Type a number [1-{answer_index}]: ")
                    self.update_points(questions[question_index]['answers'][user_choice]['points'])
                    break
                except KeyError:
                    print('Not a valid number. Try again ...')

    def __str__(self):
        return f"Business: {self.business}, " \
               f"Adventure: {self.adventure}, " \
               f"Family: {self.family}, " \
               f"Casual: {self.casual} \n"


class LocationInterest:
    def __init__(self, location, user):
        self.location = location
        self.user = user

    # difference of user points and location points
    def optimal(self):
        business = abs(self.location.business - self.user.business)
        adventure = abs(self.location.adventure - self.user.adventure)
        family = abs(self.location.family - self.user.family)
        casual = abs(self.location.casual - self.user.casual)
        return business + adventure + family + casual

    # choose locations of interest
    @staticmethod
    def get_optimal_locations(locations, user):
        optimal_locations = []
        for location in locations:
            optimal_locations.append(LocationInterest(location, user))

        # calls __lt__() while sorting
        optimal_locations.sort()

        return optimal_locations[:5]

    @staticmethod
    def print_locations_of_interest(locations):
        for location in optimal_locations:
            print(location.location)
            print(f'User and location points difference: {location.optimal()}\n')

    def __lt__(self, other):
        return self.optimal() < other.optimal()


class Location:
    def __init__(self, name, business, adventure, family, casual):
        self.name = name
        self.business = business
        self.adventure = adventure
        self.family = family
        self.casual = casual

    def __str__(self):
        return f"Location: {self.name}\n" \
               f"\tBusiness: {self.business} \n" \
               f"\tAdventure: {self.adventure} \n" \
               f"\tFamily: {self.family} \n" \
               f"\tCasual: {self.casual}"


locations = [
    Location('zoo', 0, 37, 94, 15),
    Location('igraliste', 0, 15, 100, 50),

    Location('portanova', 0, 20, 80, 90),
    Location('kazaliste', 0, 10, 80, 90),
    Location('kino', 0, 10, 70, 100),
    Location('slasticarnica', 0, 0, 80, 100),

    Location('caffe', 20, 5, 60, 100),
    Location('bar', 0, 30, 0, 100),
    Location('nocni klub', 0, 50, 0, 100),
    Location('restoran', 20, 5, 60, 80),

    Location('paintball', 0, 100, 20, 40),
    Location('umjetne stijene za penjanje', 0, 90, 20, 40),
    Location('sport', 0, 80, 20, 40),
    Location('veslanje', 0, 100, 0, 60),

    Location('poslovni centar', 100, 0, 0, 0),
    Location('skola stranih jezika', 80, 5, 5, 10),
    Location('printaonica', 100, 0, 0, 0),
    Location('knjiznica', 70, 10, 10, 50),
]

questions = {
    '1': {
        'question': 'To which age group do you belong to?',
        'answers': {
            '1': {'answer': 'Youth [18-24]', 'points': Points(5, 20, 0, 10)},
            '2': {'answer': 'Adult [25-65]', 'points': Points(20, 15, 15, 20)},
            '3': {'answer': 'Senior [66-]', 'points': Points(5, 20, 5, 30)},
        }
    },
    '2': {
        'question': 'What would you rather do in your free time?',
        'answers': {
            '1': {'answer': 'Learn a new skills', 'points': Points(20, 10, 0, 0)},
            '2': {'answer': 'Try out new things', 'points': Points(0, 30, 0, 0)},
            '3': {'answer': 'Spend time with family', 'points': Points(0, 0, 30, 0)},
            '4': {'answer': 'Spend time with friends', 'points': Points(0, 5, 0, 25)},
        }
    },
    '3': {
        'question': 'Do you have children?',
        'answers': {
            '1': {'answer': 'Yes', 'points': Points(10, 0, 30, 0)},
            '2': {'answer': 'No', 'points': Points(0, 30, 0, 10)},
        }
    },
    '4': {
        'question': 'Would you rather watch a movie or a video course/tutorial?',
        'answers': {
            '1': {'answer': 'Video course/tutorial', 'points': Points(30, 0, 0, 0)},
            '2': {'answer': 'Movies', 'points': Points(0, 0, 0, 30)},
        }
    },
    '5': {
        'question': 'How are you feeling today?',
        'answers': {
            '1': {'answer': 'Serious', 'points': Points(30, 0, 0, 0)},
            '2': {'answer': 'Adventurous', 'points': Points(0, 30, 0, 0)},
            '3': {'answer': 'Familial', 'points': Points(0, 0, 30, 0)},
            '4': {'answer': 'Casual', 'points': Points(0, 0, 0, 30)},
        }
    },
}

user = User()
user.set_user_information(questions)
print("\n========================================================================\n"
      f"User information - {user}")
optimal_locations = LocationInterest.get_optimal_locations(locations, user)
LocationInterest.print_locations_of_interest(optimal_locations)
