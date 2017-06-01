function lotteryDraw() {
	
	//Storing all the values from the form into variables.
	var amount = parseInt(document.lottery.amount.value);
	//document.lottery.amount.value = '';
	
	var lotteryMin = parseInt(document.lottery.rangeMin.value);
	//document.lottery.rangeMin.value = '';
	
	var lotteryMax = parseInt(document.lottery.rangeMax.value);
	//document.lottery.rangeMax.value = '';
			
	var range = lotteryMax - lotteryMin;
	
	//Checking to see if there needs to be a "Mega" number drawn.
	if(document.lottery.mega[0].checked) {
		
		var megaNumber = 1;
		
		var megaMin = parseInt(document.lottery.megaMin.value);
		var megaMax = parseInt(document.lottery.megaMax.value);
		//document.lottery.rangeMin.value = '';
		//document.lottery.rangeMax.value = '';
		
		//document.lottery.mega[0].checked = false;
		
	} else {
		var megaNumber = 0;
		//document.lottery.rangeMin.value = '';
		//document.lottery.rangeMax.value = '';
		//document.lottery.mega[1].checked = false;
	}
	
	var lottoList = createList(lotteryMin, lotteryMax);
	var lotteryNumbers = draw(amount, lottoList);
	
	///////////////////////////
	/*
	for(var i=0; i<amount; i++){
		lotteryNumbers[i] = Math.floor(Math.random()*(range + 1)) + lotteryMin;
		
		//Check for repeats
		for(var j=0; j<i; j++){
		
			//If there's a repeated number, it will change itself 
			//and then go back to the beginning of the list (j=0) to check again.
			while(lotteryNumbers[i] === lotteryNumbers[j]){
				lotteryNumbers[i] = Math.floor(Math.random()*(range + 1)) + lotteryMin;
				j = 0;
			}
		}
	}
	*/
	///////////////////////////
	
	lotteryNumbers = sort(lotteryNumbers);
	document.getElementById("output").innerHTML = '<div class="lottoResults">The numbers are: </div>';
	display(lotteryNumbers);
	
	if(megaNumber === 1) {
		var mega = Math.floor(Math.random()*((megaMax - megaMin) + 1)) + megaMin;
		var megaType = typeof(mega);
		if(megaType !== 'number') {
			document.getElementById("output").innerHTML += '<br /><div class="lottoResults">Sorry, you did not provide the correct information for the Mega Number.';
		} else {
			document.getElementById("output").innerHTML += '<br /><div class="lottoResults">Your Mega Number is: ' + mega + '</div>';
		}
	}
	
}

function sort(list1) {
	var tempList = [];
	var listLength = list1.length;
	
	for(var i = 0; i < listLength; i++) {
		var tempNumber = list1[0];
		
		for(var j = 1; j < list1.length; j++) {
			if(list1[j] < tempNumber) {
				tempNumber = list1[j];
			}
		}
		
		tempList[i] = list1.splice(list1.indexOf(tempNumber),1);
	}
	
	return tempList;
}

function display(list) {
	for(var i = 0; i < list.length; i++) {
		document.getElementById("output").innerHTML += '<div class="lottoResults">' + list[i] + '</div>';
		if(i < list.length - 1) {
			document.getElementById("output").innerHTML += '<div class="lottoResults">, ';
		}
	}
}

function createList(low, high) {
  var list = [];
  var place = 0;
  
  for(var i = low; i <= high; i++) {
	list[place] = parseInt(i);
	place++;
  }
  
  return list;
}

function draw(quantity, list) {
  var selections = [];
  
  for(var i = 0; i < quantity; i++){
	selections[i] = parseInt(list.splice(Math.floor(Math.random()*list.length),1));
  }
  
  return selections;
}