class GoogleApi:

    def __init__(self):

        self.resp_dict = {
            'nodejs' : ['node_link1','node_link2','node_link3','node_link4','node_link5','node_link6'],
            'game' : ['game_link1','game_link2','game_link3','game_link4','game_link5','game_link6'],
            'got' : ['got_link1','got_link2','got_link3','got_link4','got_link5','got_link6'],
            'query1' : ['query1_link1','query1_link2','query1_link3','query1_link4','query1_link5','query1_link6'],
            'query2' : ['query2_link1','query2_link2','query2_link3','query2_link4','query2_link5','query2_link6']
        }

    def get_resp(self,query):
        resp = None
        if query in self.resp_dict.keys():
            resp = self.resp_dict[query]
            # get top 5
            resp = resp[:5]
        else:
            resp = ['random_resp1','random_resp2','random_resp3','random_resp4','random_resp5']
        return resp