from site_api.utils.site_api_func import SiteApiInterface

def_find_film = SiteApiInterface.film_finder()

if __name__ == '__main__':
    res = def_find_film('1+1')
    print(res)
