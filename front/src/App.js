import React, { Component } from "react";
import "./App.css";
import Game from "./Game";
import WelcomePage from "./WelcomePage";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      page: "welcome_page",
      token: undefined
    };
  }

  saveToken = token => {
    this.setState({token});
  }

  handlePageChange(page_name) {
    let new_state = this.state;
    new_state.page = page_name;
    this.setState(new_state);
  }
  render() {
    if (this.state.page === "game") {
      return <Game token={this.state.token}/>;
    } else {
      return (
        <WelcomePage handlePageChange={() => this.handlePageChange("game")} saveToken={this.saveToken} token={this.state.token}/>
      );
    }
  }
}

export default App;
