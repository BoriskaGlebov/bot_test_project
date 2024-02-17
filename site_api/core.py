from site_api.utils.site_api_func import SiteApiInterface

def_find_film = SiteApiInterface.film_finder()
def_top_100_film = SiteApiInterface.top_100_film()
def_find_film_param = SiteApiInterface.find_film_param()

from pprint import pprint

if __name__ == '__main__':
    para = [None, None, None, None, None]
    res = def_find_film_param(*para)
    pprint(res)
