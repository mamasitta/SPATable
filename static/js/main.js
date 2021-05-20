function Filter (e) {
    e.preventDefault();
    var user_input = document.getElementById('user_input').value;
    var column = document.getElementById('column').value;
    var condition = document.getElementById('condition').value;
    console.log(user_input, column, condition)

    const Url = 'http://127.0.0.1:5000/api/filter?user_input=' + user_input + '&column=' + column + '&condition=' + condition
    fetch(Url)
    .then(response =>
        response.json().then(data => ({
            data: data,
            status: response.status
        })
    ).then(res => {

    if (res.status === 200){
            var elements = document.getElementsByClassName('trow')
            while(elements.length > 0){
                elements[0].parentNode.removeChild(elements[0]);
            }
            var response_list = res.data.data

            for (i = 0; i < response_list.length; i++){
                var dateobj = new Date(response_list[i].date)
                var newRow = document.createElement("tr");
                newRow.setAttribute("class", 'trow')
                var newCellTitle = document.createElement("td");
                newCellTitle.innerHTML = response_list[i].title;
                var newCellDate = document.createElement("td");
                newCellDate.innerHTML = dateobj.toISOString().slice(0,10);
                var newCellAmount = document.createElement("td");
                newCellAmount.innerHTML = response_list[i].amount;
                var newCellDistance = document.createElement("td");
                newCellDistance.innerHTML = response_list[i].distance;
                newRow.append(newCellTitle, newCellDate, newCellAmount, newCellDistance)
                document.getElementById("tbody").appendChild(newRow);
            }


        }else {
            console.log('HI')
            document.getElementById('user_input').innerHTML = "Invalid filter parameters";
        }
    }));
    }

function removeElementsByClass(className){
    const elements = document.getElementsByClassName(className);
    while(elements.length > 0){
        elements[0].parentNode.removeChild(elements[0]);
    }
}