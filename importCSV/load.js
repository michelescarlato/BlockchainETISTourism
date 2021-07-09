const driver = require('bigchaindb-driver')
const fetch = require('node-fetch');
console.log("Before fetch")
fetch("js/fullData.json")
    .then(response => response.json())
    .then(json => dataIteration(json)); //console.log(json));


async function dataIteration (jsonData){
    //console.log(jsonData.length);
    let len = jsonData.length;
    for(let i=0;i<len; i++){
        //TODO: manage async calls
        // Add code here

        // demo:
        // Accessing elements
        console.log(jsonData[i]);
        assetdata=jsonData[i]
        sendTransactionToBigChainDB (assetdata)
        // Accessing a single field of the i-th element
        //console.log(jsonData[i]['Postcode']);
        // await sendTransactionToBigChainDB(jsonData[i]);

    }

}


function sendTransactionToBigChainDB (assetdata){
      // BigchainDB server instance or testnetwork (e.g. https://example.com/api/v1/)
      //const API_PATH = 'http://192.168.100.120:9984/api/v1/'
      const API_PATH = 'http://59.0.198.238:9984/api/v1/'
      // Create a new keypair for Alice and Bob
      const alice = new BigchainDB.Ed25519Keypair()
      let createTxId
      const metadata = {"Survey Type": ""+SurveyType+""}
      // Construct a transaction payload
      const txCreateAliceSimple = BigchainDB.Transaction.makeCreateTransaction(
              assetdata,
              metadata,
              // A transaction needs an output
              [ BigchainDB.Transaction.makeOutput(
                              BigchainDB.Transaction.makeEd25519Condition(alice.publicKey))
              ],
              alice.publicKey
      )

      // Sign the transaction with private keys of Alice to fulfill it
      const txCreateAliceSimpleSigned = BigchainDB.Transaction.signTransaction(txCreateAliceSimple, alice.privateKey)
      // Send the transaction off to BigchainDB
      let conn = new BigchainDB.Connection(API_PATH)
      conn.postTransactionCommit(txCreateAliceSimpleSigned)
      .then(res => {
            createTxId = res.id
            document.body.innerHTML ='<h3>Transaction created</h3>';
            document.body.innerHTML+=API_PATH
            document.body.innerHTML+='transactions/'
            document.body.innerHTML+=txCreateAliceSimpleSigned.id
            document.body.innerhtml.href = API_PATH + 'transactions/' + txCreateAliceSimpleSigned.id

        })
      return;
}
