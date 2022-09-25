fetch('"http://127.0.0.1:8000/api/v1/articlesapi/', {
      method: 'post',
      headers: {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Authorization':'Token ed73db9bf18f3c3067be926d5ab64cec9bcb9c5e'
      },
      body: JSON.stringify({data: "your data"})
    }).then(res=>res.json())
      .then(res => console.log(res));