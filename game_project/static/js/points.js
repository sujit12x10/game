const row1 = document.getElementById('row-1')
const row2 = document.getElementById('row-2')
const row3 = document.getElementById('row-3')
const row4 = document.getElementById('row-4')
const playbtn = document.getElementById('play')
const matchTable = document.getElementById('match-table')

const season = playbtn.getAttribute('data-season')
const team1 = row1.getAttribute('data-name')
const team2 = row2.getAttribute('data-name')
const team3 = row3.getAttribute('data-name')
const team4 = row4.getAttribute('data-name')

//click on playoffs button

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

playbtn.addEventListener('click', () => {
    const csrfToken  = getCookie('csrftoken');
    fetch(`http://127.0.0.1:8000/season/${season}/playoffs/`, {
        method: 'POST',
        body: JSON.stringify({
            season: season,
            team1: team1,
            team2: team2,
            team3: team3,
            team4: team4,
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
            'X-CSRFToken': csrfToken
        },
        credentials: 'same-origin'
    })
    .then(response => response.json())
    .then(data => { console.log('hlo');
        window.location = `http://127.0.0.1:8000/season/${season}/playoffs-play/`
    })  
})

const fn = (el) => {
    const team1 = el.getAttribute('data-team1');
    const team2 = el.getAttribute('data-team2');
    const description = el.getAttribute('data-desc');
    fetch(`http://127.0.0.1:8000/season/${season}/playoffs-play/`, {
        method: 'POST',
        body: JSON.stringify({
            season: season,
            team1: team1,
            team2: team2,
            desc: description,
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    })
    .then((response) => response.json())
    .then((data) => {
        winner = data['winner']
        winner = data['loser']
    })
}


