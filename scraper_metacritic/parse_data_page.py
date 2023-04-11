def get_soup_general_data(soup) -> dict:
    """
    This function gets a game's soup and returns a dictionary containing general data about the game
    """
    data_dict = {}

    name = soup.find(class_='product_title')
    if name:
        data_dict['name'] = name.h1.text

    details_link = soup.find(class_='product_title').a['href']
    if details_link:
        data_dict['details_link'] = f'https://www.metacritic.com{details_link}'

    publisher = soup.find('li', class_='summary_detail publisher')
    if publisher:
        publisher = publisher.find('span', class_='data')

        data_dict['publisher'] = publisher.a.text.strip()

    release_date = soup.find('li', class_='summary_detail release_data')
    if release_date:
        release_date = release_date.find('span', class_='data')
        if release_date:
            release_date = release_date.text.strip().replace(',', '')
            data_dict['release_date'] = release_date
            # data_dict['release_date'] = datetime.datetime.strptime(release_date, "%b-%d-%Y").date()

    developers = soup.find('li', class_='summary_detail developer')
    if developers:
        developers = developers.find_all('span', class_='data')
        developers = [developer.text.strip().split(', ') for developer in developers]
        for developer in developers:
            data_dict['developers'] = developer

    platforms = soup.find('li', class_='summary_detail product_platforms')
    if platforms:
        main_platform = soup.find('span', class_='platform')
        main_platform = main_platform.text.strip()
        platforms = platforms.find_all('span', class_='data')
        platforms = [platform.text.strip().replace('  ', '').split(',') for platform in platforms]
        platforms[0].append(main_platform)
        for platform in platforms:
            data_dict['platforms'] = platform
    else:
        platform = soup.find(class_='product_title')
        data_dict['platforms'] = platform.span.text.strip()

    num_players = soup.find('li', class_='summary_detail product_players')
    if num_players:
        data_dict['num_players'] = num_players.find(class_='data').text

    genres = soup.find('li', class_='summary_detail product_genre')
    if genres:
        genres = genres.find_all('span', class_='data')
        data_dict['genres'] = [genre.text for genre in genres]

    meta_score = soup.find('span', itemprop='ratingValue')
    if meta_score:
        data_dict['meta_score'] = int(meta_score.text)
    else:
        data_dict['meta_score'] = 0

    users_score_pos = soup.find('div', class_='metascore_w user large game positive')
    users_score_mix = soup.find('div', class_='metascore_w user large game mixed')
    users_score_neg = soup.find('div', class_='metascore_w user large game negative')

    if users_score_pos:
        data_dict['users_score'] = float(users_score_pos.text)
    elif users_score_mix:
        data_dict['users_score'] = float(users_score_mix.text)
    elif users_score_neg:
        data_dict['users_score'] = float(users_score_neg.text)
    else:
        data_dict['users_score'] = 0.0

    image = soup.find('img', class_='product_image large_image')['src']
    if image:
        data_dict['image'] = image

    try:
        descriptions = soup.find('li', class_='summary_detail product_summary').text.replace('Summary:', '').strip()
    except Exception as error:
        print(error)
        data_dict['descriptions'] = None
    else:
        data_dict['descriptions'] = descriptions

    details_link = soup.find(class_='product_title').a['href']
    if details_link:
        data_dict['details_link'] = f'https://www.metacritic.com{details_link}'

    return data_dict
