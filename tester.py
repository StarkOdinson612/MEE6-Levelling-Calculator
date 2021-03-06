import asyncio
from mee6_py_api import API
import math
import os
import json

id_list = {
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
    "joosh" : 477148794861912084
}

async def api_fetch_details(ID):
    mee6API = API(377946908783673344)
    details = await mee6API.levels.get_user_details(ID)

    return details

def validate_id():
    id_to_add = input("Enter Discord User ID here (or enter N to cancel): ")

    if id_to_add.lower() == 'n':
        return 'CANCELLED'

    try: 
        details = api_fetch_details(id_to_add)

        return [id_to_add, details]
    except:
        print('Invalid ID, please try again.\n')
        validate_id()

def get_details():

    # os.system('cls' if os.name == 'nt' else 'clear')

    MY_ID = input("Enter ID here: ")

    try:
        details = asyncio.run(api_fetch_details(MY_ID))
    except:
        choice = input('Would you like to add this username to the database? (Y/N): ')

        if choice.lower() == 'y':
            x = validate_id()

            if (x == 'CANCELLED'):
                return
            else:
                user_id = x[0]
                details = x[1]

            with list_fo as open('id_list.json', 'r+'):
                list_dict = json.load(list_fo)
            list_dict.update({MY_ID : user_id})
            list_fo_write = open('id_list.json', "w+")
            json.dump(list_dict, list_fo_write, indent = 4)
            list_fo_write.close()
        else:
            print("Invalid ID, please try again.")
            print('\n\n')
            get_details()

    current_level = details['level']
    next_level = current_level + 1

    username = f"\n\nUsername: {details['username']}\nLevel: {current_level}"

    xp_r_lvl = details['detailed_xp'][1] - details['detailed_xp'][0]

    xp_r = details['detailed_xp'][0]

    next_level_str = '\n'.join(['Next Level Details: ',f'Current XP: {xp_r}', calculate_time_with_xp(xp_r_lvl, current_level, next_level)])
    
    next_rank_level = int(current_level + 5 - (current_level % 5))
    next_rank_level_xp = math.ceil(((5/3) * (next_rank_level ** 3)) + (22.5 * (next_rank_level ** 2)) + (75 + (5/6)) * next_rank_level)
    xp_r_rank = next_rank_level_xp - details['xp']

    next_rank_str = '\n'.join(['\nNext Rank Details:', f'Current XP: {xp_r}', calculate_time_with_xp(xp_r_rank, current_level, next_rank_level)])

    return '\n'.join([username, next_level_str, next_rank_str, ''])

    json_list = {
        "username" : details['username'],
        "current_level" : current_level
    }

    

    fin_input = check_retry()

    if fin_input:
        get_details()
    else:
        return


def check_retry():
    continue_again = input("Would you like to try again? (Y/N): ")

    if continue_again == 'Y' or continue_again == 'y':
        print('\n\n')
        os.system('clear')
        return True
    elif continue_again == 'N' or continue_again == 'n':
        os.system('clear')
        return False
    else:
        check_retry()

def calculate_time_with_xp(xp_r, lvl, n_lvl):
    n_lvl_str = f'Next Level: {n_lvl}'
    xp_str = f'XP Remaining: {xp_r}'
    min = f'Minimum: {t_format(math.ceil(xp_r/25))}'
    avg = f'Average: {t_format(math.ceil(xp_r/20))}' 
    max = f'Maximum: {t_format(math.ceil(xp_r/15))}'

    return '\n'.join([n_lvl_str, xp_str, min, avg, max])

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

def update_json_file():


# get_details()