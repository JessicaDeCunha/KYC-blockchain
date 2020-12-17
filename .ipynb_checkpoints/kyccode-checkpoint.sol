pragma solidity ^0.5.0;


contract KYC {

    struct Client {
        address userID;
        string email;
        string report_uri;
        bool used;
        //uint start_date;
        uint end_date;
    }
    
    
    // Stores userID => Client
    // Only permanent data that you would need to use within the smart contract later should be stored on-chain
    mapping (address => Client) public Clientdatabase;
    
    uint start_date = now;
    
    
    event NewClient(address userID, string report_uri);
    event ChangeClientInfo(address userID, string report_uri);
    
    function registerKYC(address userID, string memory email, string memory report_uri) public returns(bool) {
        
        require(!Clientdatabase[userID].used, "Account already Exists");
        
        emit NewClient(userID, report_uri);
       
       Clientdatabase[userID] = Client(userID, email, report_uri, true, now + 365 days);
       
       return Clientdatabase[userID].used;
  }
       
    
    function updateKYC(address userID, string memory newreport_uri) public returns(string memory) {
        Clientdatabase[userID].report_uri = newreport_uri;

        // Permanently associates the report_uri with the token_id on-chain via Events for a lower gas-cost than storing directly in the contract's storage.
        emit ChangeClientInfo(userID, newreport_uri);
        
        return Clientdatabase[userID].report_uri;
        

    }
    
     // check expiry date of a particular contract
    function checkvalidity(address userID) public view returns(string memory) {
        if (now > Clientdatabase[userID].end_date){
        return "Contract has Expired!";
    }
    
        else {
            
        return "Contract is Valid!";
        }
    } 
   
  // Create a list and loop through it to get expiring KYC reports
    address [] public clientList;

    event Logclientinfo(address client, uint clientend_date);

    function appendclientinfo(address client, uint clientend_date) public {
        clientList.push(client);
        Clientdatabase[client].end_date = clientend_date;
    }
    
    function getclientCount() public view returns(uint count) {
        return clientList.length;
    }
    
    function clientLoop() public {
        
        // WARN: This unbounded for loop is an anti-pattern
        
        for (uint i=0; i<clientList.length; i++) {
            emit Logclientinfo(clientList[i], Clientdatabase[clientList[i]].end_date);
            
            
        }
    }

}
 
      





