let karty = [
        {
            src: "https://placecats.com/neo/300/200"
        },
        {
            src: "https://placecats.com/millie/300/200"
        },
        {
             src: "https://placecats.com/bella/300/200"
        },
]

let pole = [0,2,1,2,0,1]
let el = document.getElementById('pexeso')
pole.forEach((prvek) => {
    el.textContent += pole[prvek].src + '<br>'
    const newEl = document.createElement('img')
    el.src = karty[prvek].src
    el.appendChild(newEl)
})

function show(){
    
}