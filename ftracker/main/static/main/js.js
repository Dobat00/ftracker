// 'api/chartdata?format=json'
// '/api/chartdata?format=api'
// '/api/chartdata'
console.log("ASDIONIEHFUIEHU")
var endpoint = '/api/chartdata'
var gastos = []
var gastos_nome = []
$.ajax({
  method:"GET",
  url:endpoint,
  success: function(data){
    // console.log(data)
    // console.log(data[0])
    // console.log(data[0].valor)
    $.each(data, function(index, value){
      console.log(index)
      console.log(value.valor)
      gastos.push(value.valor)
      gastos_nome.push(value.nome)
    })
    console.log(gastos)
      const ctx = document.getElementById('myChart');

  new Chart(ctx, {
    type: 'pie',
    data: {
      labels: gastos_nome,
      datasets: [{
        label: 'valor gasto',
        data: gastos,
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

  },
  error:function(error_data){
    console.log("error")
  }
})

