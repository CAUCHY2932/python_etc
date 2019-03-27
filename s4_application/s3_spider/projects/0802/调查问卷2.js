<script type="text/javascript">
var length = "${fn:length(typelist)}";
var questionLength = "${fn:length(questionList)}";
var optionLength = "${fn:length(optionList)}";
var tempradio = new Array();
function showChild(checkedRadio, index) {
for ( var i = 0; i < length; i++) {
if (index == i) {
var subQuestion = "type" + i;
if (tempradio[i] == checkedRadio) {
checkedRadio.checked = false;
document.getElementById(subQuestion).style.display = "none";
tempradio[i] = null;

} else {
document.getElementById(subQuestion).style.display = "block";
tempradio[i] = checkedRadio;
}
}
}
}

function change(answerId) {
var questionId = "answer" + answerId;
var v = document.getElementById(questionId).getElementsByTagName("input");
for ( var i = 0; i < v.length; i++) {
if (v.item(i).checked) {
var inputID = v.item(i).id;
var tableId = "table" + inputID.substring(2, 3);
var writeTable = document.getElementById(tableId);
if (writeTable != null) {
writeTable.style.display = "block";

}
for ( var j = 0; j < v.length; j++) {
if (i != j) {
var inputID = v.item(j).id;
var writeId = "write" + inputID.substring(2, 3);
var writeText = document.getElementById(writeId);
if (writeText != null) {
writeText.value = "";
}
}
}
} else {
var inputID = v.item(i).id;
var tableId = "table" + inputID.substring(2, 3);

var writeTable = document.getElementById(tableId);

if (writeTable != null) {
writeTable.style.display = "none";
}
}
}


}
function check() {
var sum = 0;
for (var i = 0; i < optionLength; i++) {
var questionId = "op" + i;
var v = document.getElementById(questionId);
if(v.checked) {
sum+=1;
}

}
if (sum > 0) {
return true;
} else {
return false;
}

}