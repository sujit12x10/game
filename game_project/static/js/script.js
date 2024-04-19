const playButtons = [...document.getElementsByClassName('play-btn')];
const playOffButtons = [...document.getElementsByClassName('playoff-btn')];

playButtons.forEach((btns) => {
    btns.addEventListener('click', () => {
    matchId = btns.getAttribute('data-id');
    fetch(`http://127.0.0.1:8000/play/${matchId}/`)
    .then((response) => response.json())
    .then((data) => {
        const div = document.getElementById(`match-${matchId}`)
        const matchNumber = btns.getAttribute('data-match-number')

        const winner = data.winner;
        const loser = data.loser;
        div.innerHTML = `<td>${matchNumber} <b style="color: #3FFF00; font-style: italic;">${winner}</b> beat <b style="color: #cc0000; font-style: italic;">${loser}</b></td><td></td>`
    })
    })
})


playOffButtons.forEach((btns) => {
    btns.addEventListener('click', () => {
    matchId = btns.getAttribute('data-id');
    console.log(matchId);
    fetch(`http://127.0.0.1:8000/play/${matchId}/`)
    .then((response) => response.json())
    .then((data) => {
        const div = document.getElementById(`match-${matchId}`)
        const matchDesc = btns.getAttribute('data-match-desc')
        const winner = data.winner;
        const loser = data.loser;
        div.innerHTML = `<td><b>${matchDesc} </b></td><td><b style="color: #3FFF00; font-style: italic;">${winner}</b> beat <b style="color: #cc0000; font-style: italic;">${loser}</b></td><td></td>`
        if (matchDesc === 'Qualifier-1'){
            document.getElementById('Final1').innerText = `${winner}`; 
            console.log(document.getElementById('Final1').innerText)
            document.getElementById('Qualifier-21').innerText = `${loser}`;
        }
        if (matchDesc === 'Eliminator'){
            document.getElementById('Qualifier-22').innerText = `${winner}`;
        }
        if (matchDesc === 'Qualifier-2'){
            document.getElementById('Final2').innerText = `${winner}`;
        }
        if (matchDesc === 'Final'){
            document.getElementById('main').innerHTML = `<h2><b style="color: #3FFF00;">${winner}</b> are the new Champions!</h2>`
            console.log('hurray');
        }
    })
    })
})

    

