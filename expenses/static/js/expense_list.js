'use strict';

console.log('start');

const stars = document.getElementsByClassName('star');
for (const star of stars) {
  star.addEventListener('click', function() {
    alert('!!!!');
  });
}

console.log('end');
