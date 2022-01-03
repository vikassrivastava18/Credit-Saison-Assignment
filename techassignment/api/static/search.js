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

// Show stats data on button click
function getStats() {
    fetch(`/api_2`)
    .then(response => {
        console.log(response);
        document.querySelector('#content').innerHTML = '';
        document.querySelector('#content').innerHTML = response;
    });
}

// Show card info on button click
function searchCard() {
    const cardNum = document.querySelector('#cardInput').value;
    fetch(`/api_1/${cardNum}`)
    .then(response => {
        console.log(response);
        document.querySelector('#content').innerHTML = '';
        document.querySelector('#content').innerHTML = response;
    });
}
