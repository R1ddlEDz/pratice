full_dot = '●'
empty_dot = '○'
def create_character(name,strength,intelligence,charisma):
    if not isinstance(name,str):
        return 'The character name should be a string'
    if name == "":
        return 'The character should have a name'
    if len(name) >10:
        return 'The character name is too long'
    if " " in name:
        return 'The character name should not contain spaces'
    if not all(isinstance(stat, int) for stat in (strength, intelligence, charisma)):
        return 'All stats should be integers'
    if not all(stat >=1 for stat in(strength,intelligence,charisma)):
        return 'All stats should be no less than 1'
    if not all(stat <=4 for stat in(strength,intelligence,charisma)):
        return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    def stat_line(value):
        return f"{'●' * value}{'○' * (10 - value)}"
    return f'''{name}
STR {stat_line(strength)}
INT {stat_line(intelligence)}
CHA {stat_line(charisma)}'''

        
print(create_character("ren",4,2,1))
