/*
    # Same as my app to display random quotes on the CLI
    # This app displays random quotes from $dataHome file
    # at the Notification center in MacOS
*/
var app = Application.currentApplication()

app.includeStandardAdditions = true

let nowTime= app.currentDate() //current date and time
var monty=["Jan","Feb","Mar","Apr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dec"];

/*var monty = nowTime.getMonth()+1; //0~11
let dia = ["日","月","火","水","木","金","土"];
var heute = monty + "月" + nowTime.getDate() + "日" + "(" + dia[nowTime.getDay()] + ")";*/
var heute = monty[nowTime.getMonth()] + " " + nowTime.getDate();

const dataHome = "data/goodreads_quotes_short.json"

function readDataFile(fileName){
	try{
		var pathStr = fileName.toString()
		return app.read(Path(pathStr))
	}catch(error){
		displayError("There's NO such data on system. Would you like to try another?", ["Cancel", "OK"])
	}
}

function displayError(errorMessage, buttons) {
    app.displayDialog(errorMessage, {
        buttons: buttons
    })
}

var myData=readDataFile(dataHome);

//Read JSON
var quotesObj = JSON.parse(myData); 

var numbQuotes= quotesObj["quotes"].length
//tags=idx+"/"+total+"--"+myData["quotes"][idx]["tags"]

var idx = Math.floor(Math.random() * numbQuotes);
var thisQuote = quotesObj["quotes"][idx]["quote"]
var author = quotesObj["quotes"][idx]["author"];
/*
if (thisQuote.length < 65){
    dispQuote=thisQuote;
    author= quotesObj["quotes"][idx]["author"];
}*/

//Display quote
app.displayNotification(author,{
	withTitle: "Quote of the day " + heute ,
	subtitle: thisQuote,
	soundName: "Frog"
})
