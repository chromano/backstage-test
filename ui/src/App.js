import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App container pt-5">
      <form className="form-inline">
        <div className="form-group mx-sm-3 mb-2">
          <input type="text" className="form-control" value="Enter the value"/>
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
            <tr>
              <th scope="row">1</th>
              <td>Mark</td>
              <td>Otto</td>
              <td>@mdo</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
