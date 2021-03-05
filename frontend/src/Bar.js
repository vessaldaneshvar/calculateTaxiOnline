import React, { useEffect, useState } from 'react';
import {Line} from 'react-chartjs-2';

function App() {
  const [price, setPrice] = useState([])
  const [label, setLabel] = useState([])
  let data = {
      labels: label,
      datasets: [
        {
          label: 'قیمت تاکسی در طول زمان',
          fill: true,
          lineTension: 0.1,
          backgroundColor: 'rgba(75,192,192,0.4)',
          borderColor: 'rgba(75,192,192,1)',
          borderCapStyle: 'butt',
          borderDash: [],
          borderDashOffset: 0.0,
          borderJoinStyle: 'miter',
          pointBorderColor: 'rgba(75,192,192,1)',
          pointBackgroundColor: '#fff',
          pointBorderWidth: 1,
          pointHoverRadius: 5,
          pointHoverBackgroundColor: 'rgba(75,192,192,1)',
          pointHoverBorderColor: 'rgba(220,220,220,1)',
          pointHoverBorderWidth: 2,
          pointRadius: 1,
          pointHitRadius: 10,
          data: price
        }
      ]
    }
  const get_data = () => {
    fetch("http://127.0.0.1:8000/prices/", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
    .then((response) => {
      if (!response.ok) {
        throw response;
      }
      return response.json();
    })
    .then((response) => {
      setLabel(response.map((item) => item.created_at))
      setPrice(response.map((item) => item.price))
    })
  }
  useEffect(() => {
    get_data();
  }, []);
  return (
    <div>
        <h2>Area Chart</h2>
        <h2>Price of Taxi duration Time</h2>
        <Line
          data={data}
        />
    </div>
  );
}
export default App;