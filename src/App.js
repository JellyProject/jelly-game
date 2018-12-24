import React, { Component } from 'react';
import './App.css';
import MainGrid from './Elements';


class App extends Component {
  render() {
    return (
      <MainGrid/>
    );
  }

  resizeActions() {
    var actionsGrid = document.getElementById("actions");
    var actionsWidth = window.innerWidth / 10.4 * 0.8;
    var actionsGap = window.innerWidth / 11 * 0.2;
    actionsGrid.style.gridTemplateColumns = "repeat(10," + actionsWidth + "px)";
    actionsGrid.style.gridAutoRows = actionsWidth + "px";
    actionsGrid.style.gridColumnGap = actionsGap + "px";
    actionsGrid.style.height = "minmax(" + actionsWidth * 2 + ", auto)";
  }
}

export default App;
