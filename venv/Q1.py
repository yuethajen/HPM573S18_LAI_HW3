
class Patient:   # master class
    def __init__(self, name):
        self.name = name

    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        print(self.name, "got hospitalized and was discharged.")

class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        print(self.name, "visited the emergency department and was discharged.")

class Hospital:

    list_ER_patient = []
    list_HP_patient = []

    def __init__(self, name, admit_type):
        self.name = name
        self.admit_type = admit_type
        self.cost = 0

    def admit(self, name, admit_type):
        if admit_type == 1:
            self.list_ER_patient.append(name)
            print(name, 'is admitted to emergency department.')
        if admit_type == 2:
            self.list_HP_patient.append(name)
            print(name, 'is hospitalized.')

    def discharge_all(self, name):
        for name in name:
            if name in self.list_ER_patient:
                p = EmergencyPatient(name)
                p.discharge()
                self.cost += 1000
            else:
                q = HospitalizedPatient(name)
                q.discharge()
                self.cost += 2000

    def get_total_cost(self):
        return self.cost

P1 = Hospital('Lai',1) # Emergency Department: admit_type =1
P2 = Hospital('Li',1)
P3 = Hospital('Lu',2)  # Hospitalized: admit_type = 2
P4 = Hospital('Lau',2)
P5 = Hospital('Lee',2)

P1.admit('Lai',1)
P2.admit('Li',1)
P3.admit('Lu',2)
P4.admit('Lau',2)
P5.admit('Lee',2)

All = Hospital(['Lai','Li','Lu','Lau','Lee'],[1,1,2,2,2])

All.discharge_all(['Lai','Li','Lu','Lau','Lee'])

print('The total operation cost of this day: ',All.get_total_cost())

