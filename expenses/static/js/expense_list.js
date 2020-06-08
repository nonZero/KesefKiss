'use strict';

console.log('start');

const stars = document.getElementsByClassName('star');

for (const star of stars) {
  star.addEventListener('click', function() {
    console.log(star);
    if (star.getAttribute('class').includes('loading')) {
      return;
    }
    star.setAttribute('class', 'star loading');
    const url = star.dataset.url;
    fetch(url).then(function(resp) {return resp.text();}).then(function(text) {
      console.log(text);
      star.setAttribute('class', text);
    });
  });
}

console.log('end');
