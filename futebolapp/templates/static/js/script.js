(function(win,doc){
  'use strict'

  doc.querySelector('#times').addEventListener('change',async(event)=>{
    event.preventDefault();
    let req = await fetch('http://127.0.0.1:8000/timesFilter/',{
      method:'POST',
      headers:{
        'Accept':'application/json',
        'Content-Type':'application/json',
        'X-CSRFToken':doc.querySelectorAll('input')[0].value
      },
      body:JSON.stringify({
        'times':doc.querySelector('#times').value
      })
    });
    let res = await req.json()
    doc.querySelector('.result').innerHTML=res.data;
  },false);

})(window,document)