import json

folder_path = 'metacritic_data_json_game'


def get_uniq_data() -> dict:
    uniq_data = {}
    platforms = []
    genres = []
    developers = []
    for page in range(0, 203):
        try:
            with open(f'{folder_path}/games_from_page{page}.json', 'r') as file:
                data = json.loads(file.read())
                for i in data:
                    match i['platforms']:
                        case val if isinstance(val, str):
                            if val not in platforms:
                                platforms.append(val)
                        case lst if isinstance(lst, list):
                            for k in lst:
                                if k not in platforms:
                                    platforms.append(k)

                    match i['genres']:
                        case val if isinstance(val, str):
                            if val not in genres:
                                genres.append(val)
                        case lst if isinstance(lst, list):
                            for k in lst:
                                if k not in genres:
                                    genres.append(k)

                    match i['developers']:
                        case val if isinstance(val, str):
                            if val not in genres:
                                developers.append(val)
                        case lst if isinstance(lst, list):
                            for k in lst:
                                if k not in genres:
                                    developers.append(k)
        except Exception as error:
            print(f'In loading file {page} get error {error}')

    uniq_data['developers'] = developers
    uniq_data['genres'] = genres
    uniq_data['platforms'] = platforms
    return uniq_data


def write_uniq_date_json():
    with open(f'{folder_path}/uniq_data.json', 'a') as file:
        data = get_uniq_data()
        json.dump(data, file)


def main():
    write_uniq_date_json()


if __name__ == '__main__':
    main()
