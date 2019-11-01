const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);

ref = admin.database().ref('/coordinates');

exports.getcoordinates = functions.https.onRequest((req, res) => {
    ref.once("value", function(snapshot) {
        console.log(snapshot.val());
        res.json(snapshot.val());
      }, function (errorObject) {
        console.log("The read failed: " + errorObject.code);
        res.send("Error");
      });
})