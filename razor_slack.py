__author__ = 'edhenry'

from Razor import razor_channel
from Slack import slack_channel
import json
import sys
import ast

#Webhook URL assigned when creating an integration in the slack web portal
slack_url = ''

def all_nodes():

    #Instantiates the razor_api object
    n = razor_channel.razor_api(razor_server='172.15.1.12:8080')

    #Instantiates the razor api object
    nodes = n.all_razor_nodes()

    #Instantiate list to populate with list of nodes from Razor
    node_list = []

    #Parse dictionary and append results to list
    for n in nodes['items']:
        node_list.append(str(n['name']))

    #Variable definition for message to post to slack
    message = "Nodes currently being managed by Puppet Razor: " + str(node_list)

    #Instantiate post object and pass in proper arguments for posting to slack channel
    return slack_channel.post_to_slack(channel='ed-integration-tests', username='integration-bot', icon='',
                                             message=message, url=slack_url)

def single_node():

    #Instantiates the razor_api object
    n = razor_channel.razor_api(razor_server='172.15.1.12:8080')

    #Instantiates the razor api object
    node = n.razor_single_node(node_name=sys.argv[1])

    #converts razor api_call to python object
    node_list = json.dumps(node['facts'])

    # Converts node_list str to dictionary
    node_facts = ast.literal_eval(node_list)

    fact_dict = {}

    #Parse node_facts dictionary and write results to fact_dict dictionary
    for k, v in node_facts.iteritems():
        fact_dict[k] = v

    #Variable definition for message to post to slack
    message = "Facts about %s: " % sys.argv[1] + str(fact_dict)

    #Instantiate post object and pass in proper arguments for posting to slack channel
    return slack_channel.post_to_slack(channel='ed-integration-tests', username='integration-bot', icon='',
                                             message=message, url=slack_url)

#all_nodes()
single_node()

