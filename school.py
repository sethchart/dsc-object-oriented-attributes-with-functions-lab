class School:

    def __init__(self, name, roster=dict()):
        self.name = name
        self.roster = roster

    def add_student(self, fullName, gradeLevel):
        student_list = self.roster.get(gradeLevel, [])
        student_list.append(fullName)
        self.roster[gradeLevel] = student_list

    def grade(self, gradeLevel):
        return self.roster[gradeLevel]

    def sort_roster(self):
        sorted_roster = { key: sorted(self.roster[key]) for key in
                         sorted(self.roster.keys())}
        return sorted_roster
