#!/usr/bin/python

__author__ = 'edhenry'

from Razor.razor_channel import razor_api
from Slack.slack_channel import slack_api
import json
import sys
import ast

#Webhook URL assigned when creating an integration in the slack web portal
slack_url = 'ENTER SLACK URL HERE'

def all_nodes(ip, port):

    #Create the Razor server address
    server = str(ip) + ':' + str(port)

    #Instantiates the razor_api object
    razor_channel = razor_api(razor_server=server)

    #Pull all the nodes from Razor
    nodes = razor_channel.all_razor_nodes()
    
    #Instantiate list to populate with list of nodes from Razor
    node_list = []

    #Parse dictionary and append results to list
    for n in nodes['items']:
        node_list.append(str(n['name']))

    #Variable definition for message to post to slack
    message = "Nodes currently being managed by Puppet Razor: " + str(node_list)

    #Define the slack channel to send the message out on
    slack_channel = slack_api(channel='ed-integration-tests', username='integration-bot-ed', icon='', url=slack_url)

    #Post your message to the slack channel
    return slack_channel.post_to_slack(message)

def single_node(ip, port):

    #Create the Razor server address
    server = str(ip) + ':' + str(port)

    #Instantiates the razor_api object
    razor_channel = razor_api(razor_server=server)

    #Pull a single node from Razor
    node = razor_channel.razor_single_node(node_name=sys.argv[1])

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

    #Define the slack channel to send the message out on
    slack_channel = slack_api(channel='ed-integration-tests', username='integration-bot-ed', icon='', url=slack_url)

    #Post your message to the slack channel
    return slack_channel.post_to_slack(message)

def all_tags(ip, port):

    #Create the Razor server address
    server = str(ip) + ':' + str(port)

    #Instantiates the razor_api object
    razor_channel = razor_api(razor_server=server)

    #Pull all the nodes from Razor
    tags = razor_channel.razor_all_tags()

    #Instantiate list to populate with list of nodes from Razor
    tag_list = []

    #Parse dictionary and append results to list
    for t in tags['items']:
        tag_list.append(str(t['name']))

    #Variable definition for message to post to slack
    message = "Tags currently configured within Puppet Razor:" + str(tag_list)

    #Define the slack channel to send the message out on
    slack_channel = slack_api(channel='ed-integration-tests', username='integration-bot-ed', icon='', url=slack_url)

    #Post your message to the slack channel
    return slack_channel.post_to_slack(message)

def single_tag(ip, port):

    #Create the Razor server address
    server = str(ip) + ':' + str(port)

    #Instantiates the razor_api object
    razor_channel = razor_api(razor_server=server)

    #Pull all the nodes from Razor
    tag = razor_channel.razor_single_tag(tag_name=sys.argv[1])

    #Instantiate list to populate with list of rules for tag from Razor
    rule_list = []

    #Parse dictionary and append results to list
    for t in tag['rule']:
        rule_list.append(t)

    #Create node_list to store list of nodes tag is applied to
    node_list = []

    #Iterate over tag dict and store nodes result in node list
    for t in tag['nodes'].iteritems():
        print t

    #TODO Split the list for formatting when delivering message to slack
    #Variable definition for message to post to slack
    message = "The tag *%s* " % sys.argv[1] + "currently has the following rules configured : \n"\
              "\n"\
              + str(rule_list)

    #Define the slack channel to send the message out on
    slack_channel = slack_api(channel='ed-integration-tests', username='integration-bot-ed', icon='', url=slack_url)

    #Post your message to the slack channel
    return slack_channel.post_to_slack(message)

def all_policies(ip, port):

    #Create the Razor server address
    server = str(ip) + ':' + str(port)

    #Instantiates the razor_api object
    razor_channel = razor_api(razor_server=server)

    #Pull all the nodes from Razor
    policies = razor_channel.razor_all_policies()

    #Instantiate list to populate with list of nodes from Razor
    tag_list = []

    #Parse dictionary and append results to list
    for p in policies['items']:
        tag_list.append(str(p['name']))

    #TODO Formatting of message for posting to Slack
    #Variable definition for message to post to slack
    message = "Policies currently configured within Puppet Razor : \n" \
               + str(tag_list)

    #Define the slack channel to send the message out on
    slack_channel = slack_api(channel='ed-integration-tests', username='integration-bot-ed', icon='', url=slack_url)

    #Post your message to the slack channel
    return slack_channel.post_to_slack(message)

def single_policy(ip, port):

    #Create the Razor server address
    server = str(ip) + ':' + str(port)

    #Instantiates the razor_api object
    razor_channel = razor_api(razor_server=server)

    #Pull all the nodes from Razor
    policy = razor_channel.razor_single_policy(policy_name=sys.argv[1])

    #Instantiate list to populate with list of rules for tag from Razor
    policy_list = []

    #Parse dictionary and append results to list
    for p in policy['rule']:
        policy_list.append(p)

        print p

    #TODO Split the list for formatting when delivering message to slack
    #Variable definition for message to post to slack
    message = "The tag *%s* " % sys.argv[1] + "currently has the following rules configured : \n"\
              "\n"\
              + str(policy_list)

    #Define the slack channel to send the message out on
    slack_channel = slack_api(channel='ed-integration-tests', username='integration-bot-ed', icon='', url=slack_url)

    #Post your message to the slack channel
    return slack_channel.post_to_slack(message)


#all_nodes('RAZOR SERVER', 'RAZOR SERVER PORT')
#single_node('RAZOR SERVER', 'RAZOR SERVER PORT')
#all_tags('RAZOR SERVER', 'RAZOR SERVER PORT')
#single_tag('RAZOR SERVER', 'RAZOR SERVER PORT')
#all_policies('RAZOR SERVER', 'RAZOR SERVER PORT')
#single_policy('RAZOR SERVER', 'RAZOR SERVER PORT')

