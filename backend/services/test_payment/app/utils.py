import stripe

# import json
# from bson.objectid import ObjectId

# class MongoEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, ObjectId):
#             return str(obj)
#         return super().default(obj)

stripe_keys = {
    "secret_key": 'sk_test_51OrbjMC8yRcQdEl0w13nANLCRoKyTFoKWDmZWiZvUXtQKlmjvLBb46tpDSCHY0PHJzf58no91ZJs8ODKcjbf8DNg00mBFVAaJQ',
    "publishable_key": 'pk_test_51OrbjMC8yRcQdEl0iyEcmAtTVmPb7U7YVUPrtYyLd0fIAZvm4mtj5EwoQftTKCLcfryyiYTP1ioU4tcpTrhGjk21008zPpEqso'
}

stripe.api_key = stripe_keys['secret_key']