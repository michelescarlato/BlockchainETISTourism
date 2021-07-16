const driver = require('bigchaindb-driver')
const fs = require('fs');

const sleepNow = (delay) => new Promise((resolve) => setTimeout(resolve, delay))


fs.readFile('js/fullData.json', (err,data) => {
        if (err) throw err;
        dataIteration(eval(data.toString()));
});


async function dataIteration (jsonData){
    console.log("Inside data iteration")

    //console.log(jsonData.length);
    let len = jsonData.length;
    for(let i=40;i<80; i++){
        console.log('Taking a break...');
        await sleepNow(5000);
        //await new Promise(done => setTimeout(() => done(), 5000));
        console.log('5 seconds later...');
        // Accessing elements
        console.log(jsonData[i]);
        assetdata=jsonData[i]

        console.log(jsonData[i])
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
      const alice = new driver.Ed25519Keypair()
      let createTxId
      const metadata = {"Survey Type": ""+assetdata['SurveyType']+""}
      // Construct a transaction payload
      const txCreateAliceSimple = driver.Transaction.makeCreateTransaction(
              assetdata,
              metadata,
              // A transaction needs an output
              [ driver.Transaction.makeOutput(
                              driver.Transaction.makeEd25519Condition(alice.publicKey))
              ],
              alice.publicKey
      )

      // Sign the transaction with private keys of Alice to fulfill it
      const txCreateAliceSimpleSigned = driver.Transaction.signTransaction(txCreateAliceSimple, alice.privateKey)
      // Send the transaction off to BigchainDB
      let conn = new driver.Connection(API_PATH)
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
