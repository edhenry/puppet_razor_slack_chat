__author__ = 'edhenry'

import httplib
import json
import sys

class razor_api():

    def __init__(self, razor_server):
        self.razor_server = razor_server
        self.all_razor_nodes()
        self.razor_single_node()

    def all_razor_nodes(self):
        # open HTTP connection to razor API
        self.conn = httplib.HTTPConnection(self.razor_server)
        # Issues HTTP GET for nodes endpoint in API
        self.conn.request("GET", "/api/collections/nodes")
        # Collects HTTP GET response from the razor server
        self.resp = self.conn.getresponse()
        # Reads the HTTP GET response from the razor server
        self.body = self.resp.read()

        # Converts razor server HTTP GET response to JSON object
        return json.loads(self.body)

    def razor_single_node(self, node_name=None):
        # open HTTP connection to razor API
        self.conn = httplib.HTTPConnection('172.15.1.12:8080')
        # Issues HTTP GET for nodes endpoint in API along with command line argument
        #TODO command line argument collected from slack string entered in chat window
        self.conn.request("GET", "/api/collections/nodes/%s" % node_name)
        # Collects HTTP GET response from the razor server
        self.resp = self.conn.getresponse()
        # Reads the HTTP GET response from the razor server
        self.body = self.resp.read()
        # Converts razor server HTTP GET response to JSON object
        return json.loads(self.body)

    def razor_all_tags(self):
        # open HTTP connection to razor API
        self.conn = httplib.HTTPConnection(self.razor_server)
        # Issues HTTP GET for nodes endpoint in API
        self.conn.request("GET", "/api/collections/tags")
        # Collects HTTP GET response from the razor server
        self.resp = self.conn.getresponse()
        # Reads the HTTP GET response from the razor server
        self.body = self.resp.read()

        # Converts razor server HTTP GET response to JSON object
        return json.loads(self.body)

    def razor_single_tag(self, tag_name=None):
        # open HTTP connection to razor API
        self.conn = httplib.HTTPConnection('172.15.1.12:8080')
        # Issues HTTP GET for nodes endpoint in API along with command line argument
        #TODO command line argument collected from slack string entered in chat window
        self.conn.request("GET", "/api/collections/tags/%s" % tag_name)
        # Collects HTTP GET response from the razor server
        self.resp = self.conn.getresponse()
        # Reads the HTTP GET response from the razor server
        self.body = self.resp.read()
        # Converts razor server HTTP GET response to JSON object
        return json.loads(self.body)

    def razor_all_policies(self):
        # open HTTP connection to razor API
        self.conn = httplib.HTTPConnection(self.razor_server)
        # Issues HTTP GET for nodes endpoint in API
        self.conn.request("GET", "/api/collections/policies")
        # Collects HTTP GET response from the razor server
        self.resp = self.conn.getresponse()
        # Reads the HTTP GET response from the razor server
        self.body = self.resp.read()

        # Converts razor server HTTP GET response to JSON object
        return json.loads(self.body)

    def razor_single_policy(self, policy_name=None):
        # open HTTP connection to razor API
        self.conn = httplib.HTTPConnection('172.15.1.12:8080')
        # Issues HTTP GET for nodes endpoint in API along with command line argument
        #TODO command line argument collected from slack string entered in chat window
        self.conn.request("GET", "/api/collections/policies/%s" % policy_name)
        # Collects HTTP GET response from the razor server
        self.resp = self.conn.getresponse()
        # Reads the HTTP GET response from the razor server
        self.body = self.resp.read()
        # Converts razor server HTTP GET response to JSON object
        return json.loads(self.body)

    def razor_all_tasks(self):
        # open HTTP connection to razor API
        self.conn = httplib.HTTPConnection(self.razor_server)
        # Issues HTTP GET for nodes endpoint in API
        self.conn.request("GET", "/api/collections/tasks")
        # Collects HTTP GET response from the razor server
        self.resp = self.conn.getresponse()
        # Reads the HTTP GET response from the razor server
        self.body = self.resp.read()

        # Converts razor server HTTP GET response to JSON object
        return json.loads(self.body)

    def razor_single_task(self, task_name=None):
        # open HTTP connection to razor API
        self.conn = httplib.HTTPConnection('172.15.1.12:8080')
        # Issues HTTP GET for nodes endpoint in API along with command line argument
        #TODO command line argument collected from slack string entered in chat window
        self.conn.request("GET", "/api/collections/tasks/%s" % task_name)
        # Collects HTTP GET response from the razor server
        self.resp = self.conn.getresponse()
        # Reads the HTTP GET response from the razor server
        self.body = self.resp.read()
        # Converts razor server HTTP GET response to JSON object
        return json.loads(self.body)

    def razor_all_brokers(self):
        # open HTTP connection to razor API
        self.conn = httplib.HTTPConnection(self.razor_server)
        # Issues HTTP GET for nodes endpoint in API
        self.conn.request("GET", "/api/collections/tasks")
        # Collects HTTP GET response from the razor server
        self.resp = self.conn.getresponse()
        # Reads the HTTP GET response from the razor server
        self.body = self.resp.read()

        # Converts razor server HTTP GET response to JSON object
        return json.loads(self.body)

    def razor_single_broker(self, broker_name=None):
        # open HTTP connection to razor API
        self.conn = httplib.HTTPConnection('172.15.1.12:8080')
        # Issues HTTP GET for nodes endpoint in API along with command line argument
        #TODO command line argument collected from slack string entered in chat window
        self.conn.request("GET", "/api/collections/tasks/%s" % broker_name)
        # Collects HTTP GET response from the razor server
        self.resp = self.conn.getresponse()
        # Reads the HTTP GET response from the razor server
        self.body = self.resp.read()
        # Converts razor server HTTP GET response to JSON object
        return json.loads(self.body)