from pygal.maps.world import COUNTRIES
#import warnings
#warnings.filterwarnings("ignore")
def get_country_code(country_name):
    for code,name in COUNTRIES.items():

        if name==country_name:      #不满足if语句，然后不执行
            return code             #在循环中return返回值，然后退出循环
    return None


