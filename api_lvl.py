import asyncio
from mee6_py_api import API
import math
import json
import os

idl = {
    "jelly" : 298294667219435521,
    "stark" : 550694373537611776,
    "coo" : 688754047955501241,
    "sen" : 692894461117857815,
    "hyper" : 692524907044667392,
    "turtle" : 199006852707647488,
    "fawry" : 164041317968642058,
    "moon" : 697485467288862810,
    "cez" : 356864811436605444,
    "forgetful" : 565079240500838412,
    "sean" : 509436503802249216,
    "wezo" : 727531759834759219,
    "felox" : 387259938977742849,
    "joosh" : 477148794861912084,
    "phoe" : 396612195926147072,
    "nex" : 863460357477367838,
    "noman" : 640769129183182849,
    "fired": 550694373537611776,
    "nacho": 624554736317759497
}

async def api_fetch_details(ID):
    mee6API = API(377946908783673344)
    details = await mee6API.levels.get_user_details(ID)

    return details

### DEPRECATED ###
def get_details_old():

    with open('dict.json', 'r') as fo:
        id_list = json.load(fo)

    print('Currently Stored Users:')
    print('\n'.join([i for i in id_list]))
    print('\n')

    MY_ID = input("Enter username here: ")

    if MY_ID in id_list:
        details = asyncio.run(api_fetch_details(id_list[MY_ID]))
    else:
        this_id = input("Enter your Discord User ID here: ")

        try:
            details = asyncio.run(api_fetch_details(this_id))
        except:
            print("Invalid ID, please retry.")
            return

        if this_id not in id_list.values():
            input_t = input(f"Would you likse to save your ID under the username {MY_ID}? (Y/N)  ")


            is_correct_username = input_t.lower() == 'y'

            if is_correct_username:
                id_list.update({str(MY_ID): int(this_id)})
                with open('dict.json', 'w+') as fo:
                    json.dump(id_list, fo, indent=2)
            else:
                correct_username = input("Enter your username here: ")

                id_list.update({str(correct_username): int(this_id)})
                with open('dict.json', 'w+') as fo:
                    json.dump(id_list, fo, indent=2)
        else:
            print(f"{this_id} is already registered under the username {[i for i, j in id_list.items() if j == this_id][0]}")

    username = f"\n\nUsername: {details['username']}\n"

    xp_r_lvl = details['detailed_xp'][1] - details['detailed_xp'][0]

    current_level = details['level']
    next_level = current_level + 1

    xp_r = details['detailed_xp'][0]

    nlxpt = '\n'.join(calculate_time_with_xp(xp_r_lvl, current_level, next_level))

    next_level_str = '\n'.join(['Next Level Details: ',f'Current XP: {xp_r}', f"Current Level: {current_level}", nlxpt])
    
    next_rank_level = int(current_level + 5 - (current_level % 5))
    next_rank_level_xp = math.ceil(((5/3) * (next_rank_level ** 3)) + (22.5 * (next_rank_level ** 2)) + (75 + (5/6)) * next_rank_level)
    xp_r_rank = next_rank_level_xp - details['xp']

    nrxpt = '\n'.join(calculate_time_with_xp(xp_r_rank, current_level, next_rank_level))

    next_rank_str = '\n'.join(['\nNext Rank Details:', f'Current XP: {xp_r}', f"Current Level: {current_level}", nrxpt])

    print('\n'.join([username, next_level_str, next_rank_str, '']))

    json_list = {
        "username": details['username'],
        "current_xp": xp_r,
        "current_level": current_level,
        "next_level": next_level,
        "next_level_xp": xp_r_lvl,
        "time_remaining_level": {
            "min": nlxpt[2],
            "avg": nlxpt[3],
            "max": nlxpt[4]
        },
        "next_rank_xp": xp_r_rank,
        "next_rank": next_rank_level,
        "time_remaining_rank": {
            "min": nrxpt[2],
            "avg": nrxpt[3],
            "max": nrxpt[4]
        }
    }

    fin_json_obj = json.dumps(json_list, indent=4)

def get_details(USER_ID):
    try:
        details = asyncio.run(api_fetch_details(USER_ID))
    except:
        raise InvalidID

    username = f"\n\nUsername: {details['username']}\n"

    xp_r_lvl = details['detailed_xp'][1] - details['detailed_xp'][0]

    current_level = details['level']
    next_level = current_level + 1

    xp_r = details['detailed_xp'][0]

    nlxpt = '\n'.join(calculate_time_with_xp(xp_r_lvl, current_level, next_level))

    next_level_str = '\n'.join(['Next Level Details: ',f'Current XP: {xp_r}', f"Current Level: {current_level}", nlxpt])
    
    next_rank_level = int(current_level + 5 - (current_level % 5))
    next_rank_level_xp = math.ceil(((5/3) * (next_rank_level ** 3)) + (22.5 * (next_rank_level ** 2)) + (75 + (5/6)) * next_rank_level)
    xp_r_rank = next_rank_level_xp - details['xp']

    nrxpt = '\n'.join(calculate_time_with_xp(xp_r_rank, current_level, next_rank_level))

    next_rank_str = '\n'.join(['\nNext Rank Details:', f'Current XP: {xp_r}', f"Current Level: {current_level}", nrxpt])

    fin_str_returnable = '\n'.join([username, next_level_str, next_rank_str, ''])

    json_list = {
        "username": details['username'],
        "current_xp": xp_r,
        "current_level": current_level,
        "next_level": next_level,
        "next_level_xp": xp_r_lvl,
        "time_remaining_level": {
            "min": nlxpt[2],
            "avg": nlxpt[3],
            "max": nlxpt[4]
        },
        "next_rank_xp": xp_r_rank,
        "next_rank": next_rank_level,
        "time_remaining_rank": {
            "min": nrxpt[2],
            "avg": nrxpt[3],
            "max": nrxpt[4]
        }
    }

    fin_json_obj = json.dumps(json_list, indent=4)

    return [fin_json_obj, fin_str_returnable]


def calculate_time_with_xp(xp_r, lvl, n_lvl):
    n_lvl_str = f'Next Level: {n_lvl}'
    xp_str = f'XP Remaining: {xp_r}'
    min = f'Minimum: {t_format(math.ceil(xp_r/25))}'
    avg = f'Average: {t_format(math.ceil(xp_r/20))}' 
    max = f'Maximum: {t_format(math.ceil(xp_r/15))}'

    return [n_lvl_str, xp_str, min, avg, max]

def t_format(min):

    o_min = min

    if (min < 60):
        return f'{min}m ({o_min} messages)'
    
    hours = math.floor(min/60)
    min = min % 60

    if (hours < 24):
        return f'{hours}h {min}m ({o_min} messages)'
    
    days = math.floor(hours/24)
    hours = hours % 24

    if (days < 7):
        return f'{days}d {hours}h {min}m ({o_min} messages)'
    
    weeks = math.floor(days/7)
    days = days % 7

    return f'{weeks}w {days}d {hours}h {min}m ({o_min} messages)'

def validate_id(ID):
    try:
        asyncio.run(api_fetch_details(ID))
        return
    except:
        raise InvalidID

def update_json_file(username, user_id):
    with open('dict.json', 'r') as fo:
        id_list = json.load(fo)
        id_list.update({str(username): int(user_id)})

        with open('dict.json', 'w+') as fo:
            json.dump(id_list, fo, indent=2)
    
class InvalidID(Exception):
    def __init__(self, message="Invalid ID, user does not exist"):
        self.message = message
        super().__init__(self.message)


# get_details()