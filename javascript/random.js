
// Retrieve file paths from champIcons.json 
fetch('helper/AWS-Cloudfront/aws_champIconsAll.json')
    .then((response) => response.json())  
    .then(array => { 
        document.getElementById('random-btn').addEventListener('click', () => shuffleChamps(array));
    });


//Shuffle array in JSON file using Fisher-Yates Algorithm
function shuffleChamps(array) {
    for (let i = array.length -1; i > 0; i--) {
        let  j = Math.floor(Math.random() * (i+1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    //Assign the first 5 elements to a role
    document.getElementById("Top").src = array[0];
    document.getElementById("Top Name").innerText = array[0].split('/').pop().replace('.png', '');
    document.getElementById("Jungle").src = array[1];
    document.getElementById("Jungle Name").innerText = array[1].split('/').pop().replace('.png', '');
    document.getElementById("Mid").src = array[2];
    document.getElementById("Mid Name").innerText = array[2].split('/').pop().replace('.png', '');
    document.getElementById("Bot").src = array[3];
    document.getElementById("Bot Name").innerText = array[3].split('/').pop().replace('.png', '');
    document.getElementById("Support").src = array[4];
    document.getElementById("Support Name").innerText = array[4].split('/').pop().replace('.png', '');
}

