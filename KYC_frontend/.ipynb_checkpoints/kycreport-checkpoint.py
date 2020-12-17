import sys
from kyc import convertDataToJSON, pinJSONtoIPFS, initContract, w3

from pprint import pprint

kycwithtime = initContract()


def createkycReport():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    gender = input("Gender: ")    
    dob = input("Date of birth: ")
    email = input("Email: ")
    nationality = input("Nationality: ")
    user_id = input("User ID: ")
    
    json_data = convertDataToJSON(first_name, last_name, gender, dob, email, nationality)
    report_uri = pinJSONtoIPFS(json_data)

    return user_id, email, report_uri


def kycreport(user_id, email, report_uri):
    tx_hash = kycwithtime.functions.registerKYC(user_id, email, report_uri).transact(
        {"from": w3.eth.accounts[0]}
    )
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt

def kycupdate(user_id, report_uri):
    tx_hash = kycwithtime.functions.updateKYC(user_id, report_uri).transact(
        {"from": w3.eth.accounts[0]}
    )
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt


# def getkycReports(user_id):
#     kyc_filter = kycwithtime.events.NewClient.createFilter(
#         fromBlock="0x0", argument_filters={"user_id": user_id}
#     )
#     return kyc_filter.get_all_entries()


# sys.argv is the list of arguments passed from the command line
# sys.argv[0] is always the name of the script
# sys.argv[1] is the first argument, and so on
# For example:
#        sys.argv[0]        sys.argv[1]    sys.argv[2]
# python kycreport.py        report
# python kycreport.py        get            1
def main():
    if sys.argv[1] == "report":
        user_id, email, report_uri = createkycReport()

        receipt = kycreport(user_id, email, report_uri)

        pprint(receipt)
        print("Report IPFS Hash:", report_uri)

#     if sys.argv[1] == "get":
#         user_id = sys.argv[2]

#         Client = kycwithtime.functions.Clientdatabase(user_id).call()
#         reports = getkycReports(user_id)

#         pprint(reports)
#         print("KYC", Client[0], "has been registered.")

    if sys.argv[1] == "update":
        user_id, email, report_uri = createkycReport()

        receipt = kycupdate(user_id, report_uri)

        pprint(receipt)
        print("Report IPFS Hash:", report_uri)
   



main()
