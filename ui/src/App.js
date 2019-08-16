import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [request, setRequest] = useState('');
  const [calculations, setCalculations] = useState([]);

  const handleOnChange = event => {
    setRequest(event.target.value);
  }

  const handleSubmit = event => {
    if (request) {
      fetch('/api/v1/calc/difference?n=' + request).then(response => {
        setCalculations(calculations.then(result => result.unshift(response.json)));
      });
    }

    setRequest('');
    event.preventDefault();
  };

  useEffect(() => {
    fetch('/api/v1/calc/difference').then(response => setCalculations(response.json()));
  }, []);

  return (
    <div className="App container pt-5">
      <form className="form-inline" onSubmit={handleSubmit}>
        <div className="form-group mx-sm-3 mb-2">
          <input type="text" className="form-control" value={request}
            onChange={handleOnChange}
            placeholder="Enter the value"/>
        </div>
        <button type="submit" className="btn btn-primary mb-2">Calculate</button>
      </form>
      <div className="p-3">
        <table className="table">
          <thead>
            <tr>
              <th scope="col">Date</th>
              <th scope="col">Number</th>
              <th scope="col">Solution</th>
              <th scope="col">Times</th>
            </tr>
          </thead>
          <tbody>
            {calculations.map && calculations.map(calculation => (
              <tr key={calculation.id}>
                <th scope="row">{calculation.datetime}</th>
                <td>{calculation.number}</td>
                <td>{calculation.solution}</td>
                <td>{calculation.occurrences}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
