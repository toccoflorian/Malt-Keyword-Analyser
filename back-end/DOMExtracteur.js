

// extract nodes

const divElements = document.querySelectorAll(".keywords__row");
const nodes = []
divElements.forEach(node => {
    nodes.push(node.querySelectorAll("span"))
    for (let i in node.querySelectorAll("span")) {
        // console.log(i);
    }
})


// extract nettoie et formate les données
const data = {};
nodes.map((spans, index) => {

    const value1 = spans[0].innerHTML
    const value2 = spans[1].innerHTML
    const value3 = spans[2].innerHTML

    data[index] = {
        "keyWord": value1.replace("\n", "").replace("   ", " ").replace("              ", " "),
        "nombre": value2.replace("\n", ""),
        "position": value3.replace("\n", ""),
    }

})
console.log(data);

const r = fetch("http://127.0.0.1:5000/js_to_py/", {
    method: "POST",
    headers: {
        "content-type": "application/json",

    },
    body: JSON.stringify(data),
    mode: "no-cors"

})

