var firebaseConfig = {
    apiKey: "AIzaSyCO09JciLlqV3N4K7hV90qK_8XBvGBaCLI",
    authDomain: "fifabot-e4c0b.firebaseapp.com",
    databaseURL: "https://fifabot-e4c0b.firebaseio.com",
    projectId: "fifabot-e4c0b",
    storageBucket: "fifabot-e4c0b.appspot.com",
    messagingSenderId: "694276584575",
    appId: "1:694276584575:web:f21f5e813c58849ab8fb4a",
    measurementId: "G-55C2C3Y9HH"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
var db = firebase.database();
//   firebase.analytics();


d3.select("#btnDetener").on("click", detener);
d3.select("#btnSS").on("click", screenshot);
d3.select("#btnIniciar").on("click", iniciar);


function detener() {
    db.ref().set({
        comando: "0"
    });

    db.ref().set({
        comando: "DETENER"
    });


}

function screenshot() {
    db.ref().set({
        comando: "0"
    });


    db.ref().set({
        comando: "SCREENSHOT"
    });


}

function iniciar() {

    db.ref().set({
        comando: "0"
    });
    db.ref().set({
        comando: "INICIAR"
    });


}