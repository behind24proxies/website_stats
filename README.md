# website_report

## _generate website reports_

[![Build Status](https://wangchujiang.com/sb/status/stable.svg)](https://github.com/behind24proxies/web-stats)  [![Build Status](https://wangchujiang.com/sb/license/mit.svg)](https://en.wikipedia.org/wiki/MIT_License) [![Build Status](https://wangchujiang.com/sb/github/green.svg)](https://github.com/behind24proxies/web-stats)

website_report is a simple library that allows you to generate website reports in less than 60 seconds , by scraping data from _insites.com_

- only _10_ requests/ip are allowed
- you will have to use proxies
- only *60 seconds* to generate a report

## Requirements

```sh
pip install html_to_json
```

## Installation

```sh
pip install website_report
```

## Usage

```py
from website_report import generate_report 
generate_report('https://www.dafk.net/what/')
```

## Optional Parameters

```py
generate_report(website_url,
             step=5, # time between requests
             max_time=60,# maximum wait time 
             debug=False,# debug option, it prints out some extra information on each iteration
             info=True) # this option is useful only if the website does not exist/ is offline 
```


## Output example

```sh
[{'name': 'Overall', 'rating': 'good', 'value': '6.7'}, {'name': 'Accessibility', 'rating': 'better', 'value': '8.3'}, {'name': 'Experience', 'rating': 'good', 'value': '5.2'}, {'name': 'Marketing', 'rating': 'good', 'value': '5.1'}, {'name': 'Technology', 'rating': 'better', 'value': '8.1'}, {'name': 'Twitter', 'value': '0.0'}, {'name': 'Analytics', 'value': '0.0'}, {'name': 'Printability', 'value': '0.0'}, {'name': 'Freshness', 'value': '0.0'}, {'name': 'Meta tags', 'value': '1.0'}, {'name': 'Mobile', 'value': '3.0'}, {'name': 'Popularity', 'value': '5.6'}, {'name': 'Amount of content', 'value': '7.8'}, {'name': 'Server behavior', 'value': '10.0'}, {'name': 'Page titles', 'value': '10.0'}, {'name': 'Headings', 'value': '10.0'}, {'name': 'Incoming links', 'value': '10.0'}, {'name': 'Images', 'value': '10.0'}, {'name': 'Internal links', 'value': '10.0'}, {'name': 'URL format', 'value': '10.0'}, {'name': 'Domain age', 'value': 'i'}]
```

## License

MIT

**free stuff , hell yeah !**
