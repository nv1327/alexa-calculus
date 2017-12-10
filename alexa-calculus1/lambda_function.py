import main
import json
def lambda_handler(event, context):
    print(event)

    
    #event_parsed = json.loads(event)
    #print(main.main(event_parsed['request']['intent']['slots']['function']['value']))
    #json_data = json.loads(event)
    #print(main.main(event['value']))

#we need to put the key ['value'] into main.main() but parse for a different json key as output
