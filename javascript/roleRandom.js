
// Retrieve file paths from champIcons.json 
fetchAndShuffle('helper/AWS-Cloudfront/aws_champIconsTop.json', 'Top', 'Top Name');
fetchAndShuffle('helper/AWS-Cloudfront/aws_champIconsJungle.json', 'Jungle', 'Jungle Name');
fetchAndShuffle('helper/AWS-Cloudfront/aws_champIconsMid.json', 'Mid', 'Mid Name');
fetchAndShuffle('helper/AWS-Cloudfront/aws_champIconsBot.json', 'Bot', 'Bot Name');
fetchAndShuffle('helper/AWS-Cloudfront/aws_champIconsSupport.json', 'Support', 'Support Name');


// When button is pressed, shuffle the array in the JSON file and pick a random name
function fetchAndShuffle(url, iconID, nameID) {
fetch(url)
    .then(response => response.json())  
    .then(array => { 
        document.getElementById('role-btn').addEventListener('click', () => { 
            shuffleArray(array);
            document.getElementById(iconID).src = array[0];
            document.getElementById(nameID).innerText = array[0].split('/').pop().replace('.png', '');
    });
});

}

//Shuffle array in JSON file using Fisher-Yates Algorithm
function shuffleArray(array) {
    for (let i = array.length -1; i > 0; i--) {
        let  j = Math.floor(Math.random() * (i+1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}





 
