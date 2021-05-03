#!/usr/bin/env python3

import simplejson as json

test_text = 'src/test.txt'
test_json = 'src/test.json'
polygon_queries = 'src/Polygon_queries.txt'
polygon_queries_json = 'src/Polygon_queries.json'



with open(polygon_queries_json, encoding="utf8") as json_file:
    data = json.load(json_file)
    #print(data['guild'])
    default_count = total = 0
    for default in data['messages']:
        total += 1
        if default['type'] != "":
            default_count += 1
            print("Questions :")
            print('id: ' + default['id'])
            print('type: ' + default['type'])
            print('Content: ' + default['content'])
            for reply in data['messages']:
                if "reference" in reply and default['id'] == reply['reference']['messageId']:
                    print('Answers :')
                    print('id: ' + reply['id'])
                    print('type: ' + reply['type'])
                    print('Content: ' + reply['content'])
                    print(reply['reference']['messageId'])
            print("======")
    print('\n==== Summary ====')
    print('Total count: ' + str(total))
    print('Default messages count: ' + str(default_count))
    print('Reply messages count: ' + str(total-default_count))
    print('Non answered messages: ' + str(default_count-(total-default_count)))






