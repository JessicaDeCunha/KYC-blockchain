import sys
from kyc import convertDataToJSON, pinJSONtoIPFS, initContract, w3

from pprint import pprint

kyccontract = initContract()


def createkycReport():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    dob = input("Date of birth mm/dd/yyyy: ")
    email = input("Email: ")
    nationality = input("Nationality: ")
    occupation = input("Occupation: ")
    annual_income =input("Annual Income:  ")
    user_id = input("User ID: ")
    image = input("Driv Lic image_uri:  ")
    
    json_data = convertDataToJSON(first_name, last_name, dob, email, nationality, occupation, annual_income, image)
    report_uri = pinJSONtoIPFS(json_data)

    return user_id, report_uri


def kycreport(user_id, report_uri):
    tx_hash = kyccontract.functions.registerKYC(user_id, report_uri).transact(
        {"from": user_id}
    )
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt

def kycupdate(user_id, report_uri):
    tx_hash = kyccontract.functions.updateKYC(user_id, report_uri).transact(
        {"from": user_id}
    )
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return receipt



# sys.argv is the list of arguments passed from the command line
# sys.argv[0] is always the name of the script
# sys.argv[1] is the first argument, and so on
# For example:
#        sys.argv[0]        sys.argv[1]    
# python kycreport.py        report
# python kycreport.py        update            
def main():
    if sys.argv[1] == "report":
        user_id, report_uri = createkycReport()

        receipt = kycreport(user_id, report_uri)

        pprint(receipt)
        print("Report IPFS Hash:", report_uri)


    if sys.argv[1] == "update":
        user_id,  report_uri = createkycReport()

        receipt = kycupdate(user_id, report_uri)

        pprint(receipt)
        print("Report IPFS Hash:", report_uri)
   



main()
