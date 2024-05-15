import requests
import generated.edge_nodes.edge_nodes_pb2 as en
import generated.error.error_pb2 as error
import generated.user_devices.user_devices_pb2 as ud
import pyfzf
import base64

BASE_URL = 'https://mca.utils.dev/v1/api/'
GET_ACTIVE_NODES_URL = 'edge_nodes/active/'
CONNECT_DEVICE_URL = 'user_devices/connect/'
ACCESS_TOKEN = "ADD_YOUR_ACCESS_TOKEN"



def post_req(url, message, response_handler):
    response = requests.post(url,data=message.SerializeToString())
    if response.status_code == 200:
        response_handler(response)
    else:
        errMessage = error.APIError()
        errMessage.ParseFromString(response.content)
        return errMessage


def handle_connect_device_response(response):
    resMessage = ud.ConnectDeviceResponse()
    resMessage.ParseFromString(response.content)
    serverPublicKey = base64.b64encode(eval(str(resMessage.serverPublicKey))).decode('utf-8')
    clientSecretKey = base64.b64encode(eval(str(resMessage.clientSecretKey))).decode('utf-8')
    clientIPbytes = resMessage.clientIP.ip
    clientIP = '.'.join([str(i) for i in clientIPbytes])
    cidr = resMessage.clientIP.cidr
    endpoint = resMessage.serverEndpoint
    out = f'[Interface]\nAddress = {clientIP}/{cidr}\nPrivateKey = {clientSecretKey}\n\n[Peer]\nPublicKey = {serverPublicKey}\nAllowedIPs = 0.0.0.0/0, ::/0\nEndpoint = {endpoint}'
    print(out)


def handle_active_nodes_response(response):
    resMessage = en.GetActiveNodesResponse()
    resMessage.ParseFromString(response.content)

    nodeList = (list(resMessage.nodes))

    fzfPrompt = pyfzf.FzfPrompt()
    choice = fzfPrompt.prompt([(node.id, node.label) for node in nodeList] + ['Exit'], fzf_options='--reverse --header="Select a server location"')
    if choice[0] == 'Exit':
        exit(1)
    choice = eval(choice[0])

    udConnectMessage = ud.ConnectDeviceRequest()
    udConnectMessage.edgeNodeID = choice[0]
    udConnectMessage.accessToken = ACCESS_TOKEN

    post_req(BASE_URL + CONNECT_DEVICE_URL, udConnectMessage, handle_connect_device_response)



if __name__ == '__main__':
    edge_nodes_message = en.GetActiveNodesRequest()
    edge_nodes_message.accessToken = ACCESS_TOKEN
    post_req(BASE_URL+ GET_ACTIVE_NODES_URL, edge_nodes_message, handle_active_nodes_response)






















# response = requests.post(base_url+get_active_nodes_url,data=edge_nodes_message.SerializeToString())
# if response.status_code == 200:

#     res_message = en.GetActiveNodesResponse()
#     res_message.ParseFromString(response.content)

#     node_list = (list(res_message.nodes))


#     fzf = pyfzf.FzfPrompt()
#     choice = fzf.prompt([(node.id, node.label) for node in node_list])
#     choice = eval(choice[0])

# else:
#     err_message = error.APIError()
#     err_message.ParseFromString(response.content)
#     print(err_message)


# ud_connect_message = ud.ConnectDeviceRequest()
# ud_connect_message.edgeNodeID = choice[0]
# ud_connect_message.accessToken = edge_nodes_message.accessToken

# response = requests.post(base_url + connect_device_url,data=ud_connect_message.SerializeToString())

# if response.status_code == 200:
#     res_message = ud.ConnectDeviceResponse()
#     res_message.ParseFromString(response.content)
#     print(res_message)

# else:
#     err_message = error.APIError()
#     err_message.ParseFromString(response.content)
#     print(err_message)

