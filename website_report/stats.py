import requests
import html_to_json
import time
import warnings

# removes useless data from the url
def clean_url(url):

    url = url.replace('www.', '')
    url = url.replace('https://', '')
    url = url.replace('http://', '')
    url = url.split('/')[0]
    return url

def create_full_url(url):
    return f'https://nibbler.insites.com/en_US/reports/{clean_url(url)}'
def generate_report(website_url,
             step=5,
             max_time=60,
             debug=False,
             info=True):
    full_url = create_full_url(website_url)
    max_loop = max_time//step
    while True:
        resp = requests.get(full_url).text
        length = len(resp)
        
        # if the length is less than 15000, then the page is not ready yet

        if length < 15000:
            if debug:
                print(f'[DEBUG] : max time left {max_loop*step}s')
                print(f'[DEBUG] : sleeping for {step}s ')

            max_loop -= 1
            if max_loop < 0:
                if info:
                    print('[INFO] : max time reached')
                    print(f'[INFO] : check the report yourself {full_url}')

                return False
            time.sleep(step)
        else:
            # if the code reaches here, then we convert all html data in json
            jned = html_to_json.convert(resp)
            break
    returner = []
    try:
        for x in jned['html'][0]['body'][0]['div'][0]['div'][1]['div'][0]['div'][0]['div'][0]['div']:
            current = x['h3'][0]

            values = {
                'name': current['_value'],
                'rating': current['span'][0]['_attributes']['class'][1],
                'value': current['span'][0]['_value']
            }
            returner.append(values)

        for x in jned['html'][0]['body'][0]['div'][0]['div'][1]['div'][2]['div'][0]['div']:
            try:
                attribute = x['h2'][0]['_value']
                value = x['h2'][0]['span'][0]['_value']
                values = {
                    'name': attribute,
                    'value': value
                }
                returner.append(values)
            except Exception as e :
                # warnings.warn(e)
                pass
        return returner
    except Exception as e:
        print(e)
        warnings.warn(e)

