import time
from turtle import degrees

def create_game_state(temperature=-60, usable_water=10, light=40, soil_pH=7.5):
    """Create the starting variables for the game as a dictionary."""

    game_state = {
        'plant_health': 50,
        'science_points': 0,
        'temperature': temperature,
        'usable_water': usable_water,
        'light': light,
        'soil_pH': soil_pH,
        'day': 1
    }

    return game_state


def display_stats(game_state):
    """Show all the game stats in a neat, easy-to-read format."""

    print("\n=== Mission Status ===")
    print(f"Day: {game_state['day']}")
    print(f"Plant Health: {game_state['plant_health']}")
    print(f"Science Points: {game_state['science_points']}")
    print(f"Temperature: {game_state['temperature']}°C")
    print(f"Usable Water: {game_state['usable_water']}")
    print(f"Light: {game_state['light']}%")
    print(f"Soil pH: {game_state['soil_pH']}")
    print("--------------------")


def get_mission_starting_values(mission_name):
    """Return the starting environmental values for each mission."""

    if mission_name == 'Europa':
        return {
            'temperature': -40,
            'usable_water': 12,
            'light': 50,
            'soil_pH': 6.8
        }
    elif mission_name == 'Titan':
        return {
            'temperature': -180,
            'usable_water': 14,
            'light': 45,
            'soil_pH': 7.0
        }

    return {
        'temperature': -60,
        'usable_water': 10,
        'light': 40,
        'soil_pH': 7.5
    }


def get_crop_requirements(chosen_crop1, mission_name):
    """Return the minimum environmental values each crop needs."""

    if mission_name == 'Mars':
        if chosen_crop1 == 'Potato':
            return {
                'temperature': -20,
                'usable_water': 15,
                'light': 35,
                'soil_pH': 6.0
            }
        elif chosen_crop1 == 'Wheat':
            return {
                'temperature': -10,
                'usable_water': 12,
                'light': 30,
                'soil_pH': 6.5
            }

    elif mission_name == 'Europa':
        if chosen_crop1 == 'Algae':
            return {
                'temperature': -30,
                'usable_water': 8,
                'light': 35,
                'soil_pH': 7.0
            }
        elif chosen_crop1 == 'Lettuce':
            return {
                'temperature': -10,
                'usable_water': 10,
                'light': 40,
                'soil_pH': 6.5
            }

    elif mission_name == 'Titan':
        if chosen_crop1 == 'Potato':
            return {
                'temperature': -120,
                'usable_water': 14,
                'light': 30,
                'soil_pH': 6.0
            }
        elif chosen_crop1 == 'Soybean':
            return {
                'temperature': -100,
                'usable_water': 13,
                'light': 32,
                'soil_pH': 6.5
            }

    return {
        'temperature': -10,
        'usable_water': 10,
        'light': 25,
        'soil_pH': 6.0
    }


def play_mission_gameplay(game_state, chosen_crop1, mission_name):
    """Run the two-day mission gameplay loop for any destination."""

    crop_requirements = get_crop_requirements(chosen_crop1, mission_name)

    while game_state['day'] <= 2:
        print(f"\n===== Day {game_state['day']} =====")
        display_stats(game_state)

        print(f"Mission objectives for {mission_name}:")
        print("- Keep the plant healthy.")
        print("- Keep the environment close to the crop's needs.")

        chosen_actions = []
        for action_number in range(1, 3):
            print(f"\nAction {action_number} of 2")
            print("1. Adjust Temperature")
            print("2. Add Water")
            print("3. Improve Soil Conditions")

            action_choice = input("Choose an action by entering a number: ")

            while action_choice not in ['1', '2', '3'] or action_choice in chosen_actions:
                print("Please choose a different valid action.")
                action_choice = input("Choose an action by entering a number: ")

            chosen_actions.append(action_choice)

            if action_choice == '1':
                game_state['temperature'] += 41
                print("You increased the heating.")
            elif action_choice == '2':
                game_state['usable_water'] += 8
                print("You watered the crop.")
            elif action_choice == '3':
                game_state['soil_pH'] -= 2
                print("You decreased the soil pH.")

        health_loss = 0

        if game_state['temperature'] < crop_requirements['temperature']:
            health_loss += 5
            print("The temperature is too cold. Cold stress slows photosynthesis and weakens the plant.")

        if game_state['usable_water'] < crop_requirements['usable_water']:
            health_loss += 5
            print("Water is too low. The plant cannot move nutrients properly without enough water.")

        if game_state['light'] < crop_requirements['light']:
            health_loss += 5
            print("Light is too low. The plant cannot make enough energy through photosynthesis.")

        if game_state['soil_pH'] < crop_requirements['soil_pH']:
            health_loss += 5
            print("Soil pH is too low. Acidic soil causes nutrient problems and weakens the plant.")

        if health_loss > 0:
            game_state['plant_health'] -= health_loss
            print(f"Plant health dropped by {health_loss} points.")
        else:
            print("The environment stayed close to the crop's needs. The plant kept its health.")

        game_state['plant_health'] = max(0, game_state['plant_health'])

        print("\nUpdated statistics:")
        display_stats(game_state)

        game_state['day'] += 1

    if game_state['plant_health'] >= 40 and game_state['day'] >= 2:
        print(f"\n{mission_name} mission complete. Your two-day challenge is finished.")
        return True

    print(f"\n{mission_name} mission complete. Unfortunately, your plant did not survive the harsh conditions.")
    restart = input("Do you want to try again? (Enter 'yes' to try again or any other key to continue): ")
    if restart == 'yes':
        fresh_state = create_game_state(**get_mission_starting_values(mission_name))
        return play_mission_gameplay(fresh_state, chosen_crop1, mission_name)

    return False


def choose_crop_for_mission(mission_name):
    """Let the player choose a crop for the current mission."""

    print(f'{mission_name} crop selection:')

    if mission_name == 'Mars':
        print('1. Potato')
        print('2. Wheat')
        crop_choice = input('Choose a crop by entering 1 or 2: ')

        if crop_choice == '1':
            print('You chose Potato.')
            return 'Potato'
        elif crop_choice == '2':
            print('You chose Wheat.')
            return 'Wheat'

    elif mission_name == 'Europa':
        print('1. 🟢 Algae')
        print('2. 🥬 Lettuce')
        crop_choice = input('Choose a crop by entering 1 or 2: ')

        if crop_choice == '1':
            print('You chose Algae.')
            return 'Algae'
        elif crop_choice == '2':
            print('You chose Lettuce.')
            return 'Lettuce'

    elif mission_name == 'Titan':
        print('1. Potato')
        print('2. Soybean')
        crop_choice = input('Choose a crop by entering 1 or 2: ')

        if crop_choice == '1':
            print('You chose Potato.')
            return 'Potato'
        elif crop_choice == '2':
            print('You chose Soybean.')
            return 'Soybean'

    print('Invalid choice. Please enter 1 or 2.')
    return choose_crop_for_mission(mission_name)


print('Welcome to Seeds Among the Stars')
playerName = input('What is your name? ')

print(f'Hello, {playerName}, choose one of the following options by entering the corresponding number:')

print('1. Start game')
time.sleep(3)
print('2. View game instructions')
print('3. Exit')

playerChoice = int(input('Enter your choice: '))

while playerChoice > 0 and playerChoice < 4:
    if playerChoice == 1:
        print('Starting the game...')
        time.sleep(2)

        missions = [
            (
                'Mars',
                'Welcome to Mars, the first destination of the Seeds Beyond Earth Initiative. Although Mars contains frozen water and an atmosphere rich in carbon dioxide, its freezing temperatures, poor soil quality and intense radiation make farming extremely difficult.'
            ),
            (
                'Europa',
                'Welcome to Europa, a frozen moon with a hidden ocean beneath its icy shell. The challenge here is to grow crops in a cold, low-light world where every drop of water matters.'
            ),
            (
                'Titan',
                'Welcome to Titan, the largest moon of Saturn. Its thick atmosphere, cryogenic temperatures and unusual chemistry make farming difficult, but the surface may still support hardy crops.'
            )
        ]

        for mission_number, (mission_name, mission_intro) in enumerate(missions, start=1):
            print(f'\nMission {mission_number}: {mission_name}')
            time.sleep(1)
            print(mission_intro)
            time.sleep(3)

            print(f'Your mission is to plant seeds and grow a crop on {mission_name}. You will need to carefully manage resources, protect your plants from harsh conditions, and make strategic decisions to ensure the survival of your garden.')
            time.sleep(3)

            chosen_crop = choose_crop_for_mission(mission_name)
            print(f'Your selected crop for Mission {mission_number} is: {chosen_crop}')

            game_state = create_game_state(**get_mission_starting_values(mission_name))
            print(f'Mission {mission_number} has begun! Here are your starting stats:')
            display_stats(game_state)

            play_mission_gameplay(game_state, chosen_crop, mission_name)

            if mission_name != 'Titan':
                print(f'\nThe {mission_name} mission is over. Your crew prepares for the next destination...')
                time.sleep(2)

        print('\nYour journey through the solar system has begun. The Seeds Among the Stars mission continues!')
        break
    elif playerChoice == 2:
        print('Game instructions:')
        time.sleep(3)
        print('- Choose a number to make choices')
        print('- Explore the galaxy and plant seeds')
        print('- Try to survive and grow your garden in space')
    elif playerChoice == 3:
        print('Goodbye! Thanks for playing.')
        break

else:
    print('Invalid choice. Please run the game again and choose 1, 2, or 3.')
