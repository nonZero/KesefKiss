'use strict';

console.log('start');

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const stars = document.getElementsByClassName('star');

for (const star of stars) {
  star.addEventListener('click', function() {
    console.log(star);
    if (star.getAttribute('class').includes('loading')) {
      return;
    }
    star.setAttribute('class', 'star loading');
    const url = star.dataset.url;
    const csrftoken = getCookie('csrftoken');

    fetch(url, {
      method: 'POST',
      headers: {
        "X-CSRFToken": csrftoken,
      },
    }).then(function(resp) {return resp.json();}).then(function(data) {
      console.log(data);
      const cls = "star " + (data.star ? "star-on" : "star-off")
      star.setAttribute('class', cls);
    });
  });
}

console.log('end');
