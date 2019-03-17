########### BLOCK: Pupils BAD ##############################################################
alex = [3, 5, 2, 4, 4]
philipp = [4, 5, 3, 3, 4]
matthew = [3, 5, 2, 2, 2]

print(f'Alex GPA: {sum(alex) / len(alex)}')
print(f'Philipp GPA: {sum(philipp) / len(philipp)}')
print(f'Matthew GPA: {sum(matthew) / len(matthew)}')
############ END OF: Pupils #############################################################

########### BLOCK: Pupils - BETTER ##############################################################
pupils = [{'name': 'Alex', 'grades': [3, 5, 2, 4, 4]},
          {'name': 'Philipp', 'grades': [4, 5, 3, 3, 4]},
          {'name': 'Matthew', 'grades': [3, 5, 2, 2, 2]}, ]

for i in pupils:
    print(f'{i["name"]} GPA: {sum(i["grades"]) / len(i["grades"])}')


############ END OF: Pupils - BETTER #############################################################
########### BLOCK: EVEN BETTER ##############################################################
class Pupil:
    def __init__(self, name: str, grades: list):
        self.name = name
        self.grades = grades

    def get_GPA(self):
        return f'{self.name} GPA: {sum(self.grades) / len(self.grades)}'


pupils = [Pupil('Alex', [3, 5, 2, 4, 4]),
          Pupil('Philipp', [4, 5, 3, 3, 4]),
          Pupil('Matthew', [3, 5, 2, 2, 2]),
          ]

for p in pupils:
    print(p.get_GPA())
############ END OF: EVEN BETTER #############################################################
