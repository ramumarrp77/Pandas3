


# Problem 1 : Calculate Special Bonus

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'].where( (employees['employee_id']%2 == 1) & ~(employees['name'].str.startswith('M')), other=0)
    return employees[['employee_id','bonus']].sort_values(by=['employee_id'])
	
	
# Problem 2 : Fix Names in a Table


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    def formatting(name):
        f = name[0].upper()
        r = name[1:].lower()
        return f+r
    users['name']= users['name'].apply(formatting)
    return users.sort_values(by='user_id')
	



# Problem 3 : Patients with a Condition  


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[(patients['conditions'].str.startswith('DIAB1')) |
                    (patients['conditions'].str.contains(' DIAB1'))]