document.addEventListener('DOMContentLoaded', function() {

// Use buttons to toggle between views
    document.querySelector('#searchBtn').addEventListener('click', () => searchCard());
    document.querySelector('#statsBtn').addEventListener('click', () => getStats());
});

// When back arrow is clicked, show previous section
window.onpopstate = function(event) {
    console.log(event.state.section);
    showStats(event.state.section);
}


// Show card info on button click
function searchCard() {
    const cardNum = document.querySelector('#cardInput').value;
    fetch(`/api_1/${cardNum}`, {
          method: 'POST'})
    .then(response => response.json())
    .then(data => {
        console.log(data['scheme']);
        document.querySelector('#content').innerHTML = '';
        createPara = `<h4>Card Info:</h4>
                        <ul>
                           <li>Scheme: ${data['scheme']}</li>
                           <li>Scheme: ${data['type']}</li>
                           <li>Scheme: ${data['bank']}</li>
                        </ul>`
        document.querySelector('#content').innerHTML = createPara;
    })
}

// Show stats data on button click
function getStats() {
    document.querySelector('#content').innerHTML = '';
    fetch(`/api_2`)
    .then(response => response.json())
    .then(data => {
        console.log(typeof(data));
        data_obj = Object.keys(data)
        console.log(data[data_obj][0]);
        for (let d of Object.keys(data[data_obj])) {

            for (let c of Object.keys(data[data_obj][d])) {
                document.querySelector('#content').innerHTML += `<p><b>Card Number:</b> ${c},
                                                                <b>Hits:</b> ${data[data_obj][d][c][0]},
                                                                <b>Latest Timestamp:</b> ${data[data_obj][d][c][2]},
                                                                <b>Oldest Timestamp:</b> ${data[data_obj][d][c][2]}
                                                                </p>`;
                console.log(c, data[data_obj][d][c][0], data[data_obj][d][c][1], data[data_obj][d][c][2])
            }
        }


    });
}

