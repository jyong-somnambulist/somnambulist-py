import urllib
import datetime
import os
import requests

def downloadErrorFile(wgj_url, output_url):
    try:
        urllib.urlretrieve(wgj_url, output_url)
        return True
    except Exception, e:
        print e.message
        return False


if __name__ == '__main__':
    dt = datetime.datetime.now().strftime('%Y-%m-%d')
    wgj_url = 'http://localhost:8080/test_data.zip'
    output_url = 'D:\\data\\' + dt + '.zip'
    print output_url
    bool = downloadErrorFile(wgj_url, output_url)

    url = 'http://localhost:8080/test_data'
    # get_dir('http://localhost:8080/test_data', "./")
    content = requests.get(url).text
    sub_url = re.findall('href="(.*?)"', content)
