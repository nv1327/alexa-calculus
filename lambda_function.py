import main
def lambda_handler(event, context):
    #print(event)
    print(main.main(event['request']['intent']['slots']['function']['value']))
