    let currentTemp = document.querySelector('.currentTemp')
    let dataTemp = document.querySelector('.data')
    let maxTemp = document.querySelector('.maxTemp')
    let minTemp = document.querySelector('.minTemp')
    let icon = document.querySelector('.icon')

document.addEventListener('DOMContentLoaded', function() {
    fetch('https://api.weatherapi.com/v1/forecast.json?key=df409a4dd5564e069f5230424221206&q=Lisbon&days=3&aqi=no&alerts=no')
    .then(response => response.json())
    .then(data => {
            currentTemp.innerHTML = data.current.temp_c + ' º';
            dataTemp.innerHTML = data.location.name;
            maxTemp.innerHTML =  data.forecast.forecastday[0].day.maxtemp_c + ' º';
            minTemp.innerHTML =  data.forecast.forecastday[0].day.mintemp_c + ' º';
            icon.src = data.current.condition.icon;
    });
});